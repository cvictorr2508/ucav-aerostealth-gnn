"""Prepare ordered 2D contour CSVs for Chapter 5 experiments."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import tomllib

from ucav_aerostealth.data.io import graphs_from_contour_csv, write_graph_dataset
from ucav_aerostealth.data.schema import ContourCSVSchema
from ucav_aerostealth.data.split import DEFAULT_SEED, split_configuration_ids, write_split_manifest


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate a 2D contour CSV, build graph files, and create a geometry-level split."
    )
    parser.add_argument("--config", required=True, help="TOML job configuration.")
    parser.add_argument("--input-csv", help="Override input.csv from the TOML file.")
    parser.add_argument("--output-dir", help="Override input.output_dir.")
    parser.add_argument("--seed", type=int, help="Override split.seed.")
    parser.add_argument("--train-ratio", type=float, help="Override split.train.")
    parser.add_argument(
        "--validation-ratio", type=float, help="Override split.validation."
    )
    parser.add_argument("--test-ratio", type=float, help="Override split.test.")
    return parser


def _optional_string(value: object) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text or None


def main(argv: list[str] | None = None) -> None:
    args = _parser().parse_args(argv)
    config_path = Path(args.config)
    config = tomllib.loads(config_path.read_text(encoding="utf-8"))

    input_cfg = config.get("input", {})
    columns_cfg = config.get("columns", {})
    split_cfg = config.get("split", {})

    input_csv = Path(args.input_csv or input_cfg.get("csv", ""))
    output_dir = Path(args.output_dir or input_cfg.get("output_dir", ""))
    if not str(input_csv):
        raise ValueError("An input CSV path is required.")
    if not str(output_dir):
        raise ValueError("An output directory is required.")

    schema = ContourCSVSchema(
        configuration_id=str(columns_cfg.get("configuration_id", "configuration_id")),
        node_id=str(columns_cfg.get("node_id", "node_id")),
        x=str(columns_cfg.get("x", "x")),
        y=str(columns_cfg.get("y", "y")),
        order=_optional_string(columns_cfg.get("order")),
        target_columns=tuple(str(x) for x in columns_cfg.get("targets", [])),
        global_columns=tuple(str(x) for x in columns_cfg.get("globals", [])),
    )

    seed = args.seed if args.seed is not None else int(split_cfg.get("seed", DEFAULT_SEED))
    train_ratio = (
        args.train_ratio
        if args.train_ratio is not None
        else float(split_cfg.get("train", 0.70))
    )
    validation_ratio = (
        args.validation_ratio
        if args.validation_ratio is not None
        else float(split_cfg.get("validation", 0.15))
    )
    test_ratio = (
        args.test_ratio
        if args.test_ratio is not None
        else float(split_cfg.get("test", 0.15))
    )

    graphs = graphs_from_contour_csv(input_csv, schema)
    output_dir.mkdir(parents=True, exist_ok=True)
    dataset_manifest = write_graph_dataset(
        graphs,
        output_dir,
        source_csv=input_csv,
    )
    split = split_configuration_ids(
        [graph.configuration_id for graph in graphs],
        train=train_ratio,
        validation=validation_ratio,
        test=test_ratio,
        seed=seed,
    )
    split_manifest = write_split_manifest(split, output_dir / "split_manifest.json")

    summary = {
        "seed": seed,
        "num_configurations": len(graphs),
        "dataset_manifest": str(dataset_manifest),
        "split_manifest": str(split_manifest),
        "split_sizes": {
            "train": len(split.train),
            "validation": len(split.validation),
            "test": len(split.test),
        },
    }
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
