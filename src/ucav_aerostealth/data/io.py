"""CSV ingestion and graph-dataset materialization for ordered 2D contours."""

from __future__ import annotations

import json
from pathlib import Path
import re
from typing import Iterable

import numpy as np
import pandas as pd

from ucav_aerostealth.data.schema import ContourCSVSchema
from ucav_aerostealth.graphs.build_2d import Graph2D, build_contour_graph, save_graph_npz


def read_contour_csv(path: str | Path, schema: ContourCSVSchema) -> pd.DataFrame:
    """Read and validate the columns required by the configured schema."""

    source = Path(path)
    frame = pd.read_csv(source)
    missing = [column for column in schema.required_columns if column not in frame.columns]
    if missing:
        raise ValueError(
            "CSV is missing required columns: " + ", ".join(sorted(missing))
        )

    coordinates = frame[[schema.x, schema.y]].to_numpy(dtype=float)
    if not np.isfinite(coordinates).all():
        raise ValueError("CSV coordinates contain NaN or infinite values.")
    if frame[schema.configuration_id].isna().any():
        raise ValueError("configuration_id values must not be missing.")
    if frame[schema.node_id].isna().any():
        raise ValueError("node_id values must not be missing.")

    return frame


def _constant_value(series: pd.Series, *, column: str) -> object:
    non_null = series.dropna()
    if non_null.empty:
        raise ValueError(f"Column '{column}' has no value for one configuration.")

    if pd.api.types.is_numeric_dtype(non_null):
        values = non_null.to_numpy(dtype=float)
        if not np.allclose(values, values[0], rtol=1e-10, atol=1e-12):
            raise ValueError(
                f"Column '{column}' must be constant within each configuration."
            )
        return float(values[0])

    values = non_null.astype(str).unique()
    if len(values) != 1:
        raise ValueError(
            f"Column '{column}' must be constant within each configuration."
        )
    return str(values[0])


def graphs_from_contour_csv(
    path: str | Path,
    schema: ContourCSVSchema,
) -> list[Graph2D]:
    """Create one graph per configuration in an ordered-contour CSV."""

    frame = read_contour_csv(path, schema)
    graphs: list[Graph2D] = []

    grouped = frame.groupby(schema.configuration_id, sort=True, dropna=False)
    for configuration_id, group in grouped:
        sort_column = schema.order or schema.node_id
        ordered = group.sort_values(sort_column, kind="stable")

        if ordered[schema.node_id].duplicated().any():
            raise ValueError(
                f"Duplicate node_id detected in configuration {configuration_id!r}."
            )

        points = ordered[[schema.x, schema.y]].to_numpy(dtype=float)
        node_ids = ordered[schema.node_id].astype(str).to_numpy()

        targets = {
            column: float(_constant_value(ordered[column], column=column))
            for column in schema.target_columns
        }
        global_features = {
            column: _constant_value(ordered[column], column=column)
            for column in schema.global_columns
        }

        graphs.append(
            build_contour_graph(
                points,
                configuration_id=configuration_id,
                node_ids=node_ids,
                targets=targets,
                global_features=global_features,
            )
        )

    if not graphs:
        raise ValueError("No configurations were found in the CSV.")
    return graphs


def _safe_file_stem(configuration_id: str, index: int) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9_.-]+", "_", configuration_id).strip("._")
    if not cleaned:
        cleaned = "configuration"
    return f"{index:04d}_{cleaned}"


def write_graph_dataset(
    graphs: Iterable[Graph2D],
    output_dir: str | Path,
    *,
    source_csv: str | Path | None = None,
) -> Path:
    """Write framework-neutral graph files plus a dataset index."""

    output = Path(output_dir)
    graph_dir = output / "graphs"
    graph_dir.mkdir(parents=True, exist_ok=True)

    entries: list[dict[str, object]] = []
    for index, graph in enumerate(graphs):
        filename = _safe_file_stem(graph.configuration_id, index) + ".npz"
        save_graph_npz(graph, graph_dir / filename)
        entries.append(
            {
                "configuration_id": graph.configuration_id,
                "graph_file": str(Path("graphs") / filename),
                "num_nodes": graph.num_nodes,
                "num_edges": graph.num_edges,
                "signed_area": graph.signed_area,
                "orientation": graph.orientation,
                "targets": graph.targets,
                "global_features": graph.global_features,
            }
        )

    manifest = {
        "source_csv": str(source_csv) if source_csv is not None else None,
        "num_configurations": len(entries),
        "configurations": entries,
    }
    manifest_path = output / "dataset_manifest.json"
    manifest_path.write_text(
        json.dumps(manifest, indent=2, sort_keys=True, default=str) + "\n",
        encoding="utf-8",
    )
    return manifest_path
