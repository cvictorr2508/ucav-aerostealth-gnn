from pathlib import Path

import pandas as pd

from ucav_aerostealth.data.io import graphs_from_contour_csv
from ucav_aerostealth.data.schema import ContourCSVSchema


def test_csv_loader_creates_one_graph_per_configuration(tmp_path: Path):
    rows = []
    square = [(0, 0), (1, 0), (1, 1), (0, 1)]
    for config_id, cl_value in [("A", 0.4), ("B", 0.6)]:
        for node_id, (x, y) in enumerate(square):
            rows.append(
                {
                    "configuration_id": config_id,
                    "node_id": node_id,
                    "x": x,
                    "y": y,
                    "CL": cl_value,
                    "CD": 0.02,
                    "mach": 0.3,
                }
            )

    csv_path = tmp_path / "contours.csv"
    pd.DataFrame(rows).to_csv(csv_path, index=False)

    schema = ContourCSVSchema(
        target_columns=("CL", "CD"),
        global_columns=("mach",),
    )
    graphs = graphs_from_contour_csv(csv_path, schema)

    assert [graph.configuration_id for graph in graphs] == ["A", "B"]
    assert graphs[0].targets["CL"] == 0.4
    assert graphs[1].targets["CL"] == 0.6
    assert graphs[0].global_features["mach"] == 0.3
