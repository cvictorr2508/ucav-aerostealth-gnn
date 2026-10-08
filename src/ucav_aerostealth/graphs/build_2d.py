"""Convert ordered 2D contours into serializable graph objects."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Mapping

import numpy as np

from ucav_aerostealth.geometry.ga2d import oriented_contour_geometry


NODE_FEATURE_NAMES = (
    "x",
    "y",
    "tangent_x",
    "tangent_y",
    "normal_x",
    "normal_y",
    "turn_dot",
    "turn_bivector_e12",
)

EDGE_FEATURE_NAMES = (
    "dx",
    "dy",
    "length",
    "unit_dx",
    "unit_dy",
)


@dataclass(frozen=True)
class Graph2D:
    """Framework-neutral graph representation for one 2D configuration."""

    configuration_id: str
    node_ids: np.ndarray
    node_features: np.ndarray
    edge_index: np.ndarray
    edge_features: np.ndarray
    signed_area: float
    orientation: int
    targets: dict[str, float]
    global_features: dict[str, object]

    @property
    def num_nodes(self) -> int:
        return int(self.node_features.shape[0])

    @property
    def num_edges(self) -> int:
        return int(self.edge_index.shape[1])


def _normalize_ids(node_ids: np.ndarray | None, original_n: int, final_n: int) -> np.ndarray:
    if node_ids is None:
        return np.asarray([str(i) for i in range(final_n)], dtype=str)

    ids = np.asarray(node_ids).astype(str)
    if ids.shape != (original_n,):
        raise ValueError("node_ids must have one entry per supplied point.")
    if original_n != final_n:
        ids = ids[:-1]
    if len(set(ids.tolist())) != len(ids):
        raise ValueError("node_ids must be unique within a configuration.")
    return ids


def build_contour_graph(
    points: np.ndarray,
    *,
    configuration_id: object,
    node_ids: np.ndarray | None = None,
    targets: Mapping[str, float] | None = None,
    global_features: Mapping[str, object] | None = None,
) -> Graph2D:
    """Build a bidirectional vertex graph from an ordered closed contour."""

    raw_points = np.asarray(points, dtype=float)
    original_n = len(raw_points)
    geometry = oriented_contour_geometry(raw_points)
    polygon = geometry.points
    n_nodes = len(polygon)
    ids = _normalize_ids(node_ids, original_n, n_nodes)

    node_features = np.column_stack(
        [
            polygon[:, 0],
            polygon[:, 1],
            geometry.node_tangents[:, 0],
            geometry.node_tangents[:, 1],
            geometry.node_outward_normals[:, 0],
            geometry.node_outward_normals[:, 1],
            geometry.turn_dot,
            geometry.turn_bivector_e12,
        ]
    )

    forward_source = np.arange(n_nodes, dtype=np.int64)
    forward_target = np.roll(forward_source, -1)
    source = np.concatenate([forward_source, forward_target])
    target = np.concatenate([forward_target, forward_source])
    edge_index = np.vstack([source, target])

    deltas = polygon[target] - polygon[source]
    lengths = np.linalg.norm(deltas, axis=1)
    if np.any(lengths <= 1e-14):
        raise ValueError("Graph contains a zero-length contour edge.")
    directions = deltas / lengths[:, None]
    edge_features = np.column_stack(
        [
            deltas[:, 0],
            deltas[:, 1],
            lengths,
            directions[:, 0],
            directions[:, 1],
        ]
    )

    target_dict = {str(key): float(value) for key, value in (targets or {}).items()}
    global_dict = {str(key): value for key, value in (global_features or {}).items()}

    return Graph2D(
        configuration_id=str(configuration_id),
        node_ids=ids,
        node_features=np.asarray(node_features, dtype=float),
        edge_index=edge_index,
        edge_features=np.asarray(edge_features, dtype=float),
        signed_area=float(geometry.signed_area),
        orientation=int(geometry.orientation),
        targets=target_dict,
        global_features=global_dict,
    )


def save_graph_npz(graph: Graph2D, path: str | Path) -> Path:
    """Store one graph without framework-specific serialization."""

    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        output,
        configuration_id=np.asarray(graph.configuration_id),
        node_ids=graph.node_ids.astype(str),
        node_features=graph.node_features,
        edge_index=graph.edge_index,
        edge_features=graph.edge_features,
        signed_area=np.asarray(graph.signed_area),
        orientation=np.asarray(graph.orientation),
        node_feature_names=np.asarray(NODE_FEATURE_NAMES),
        edge_feature_names=np.asarray(EDGE_FEATURE_NAMES),
        targets_json=np.asarray(json.dumps(graph.targets, sort_keys=True)),
        global_features_json=np.asarray(
            json.dumps(graph.global_features, sort_keys=True, default=str)
        ),
    )
    return output


def load_graph_npz(path: str | Path) -> Graph2D:
    """Load a graph written by :func:`save_graph_npz`."""

    with np.load(Path(path), allow_pickle=False) as data:
        return Graph2D(
            configuration_id=str(data["configuration_id"].item()),
            node_ids=data["node_ids"].astype(str),
            node_features=np.asarray(data["node_features"], dtype=float),
            edge_index=np.asarray(data["edge_index"], dtype=np.int64),
            edge_features=np.asarray(data["edge_features"], dtype=float),
            signed_area=float(data["signed_area"].item()),
            orientation=int(data["orientation"].item()),
            targets={
                str(key): float(value)
                for key, value in json.loads(data["targets_json"].item()).items()
            },
            global_features=json.loads(data["global_features_json"].item()),
        )
