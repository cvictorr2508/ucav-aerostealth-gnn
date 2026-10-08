from pathlib import Path

import numpy as np

from ucav_aerostealth.graphs.build_2d import (
    build_contour_graph,
    load_graph_npz,
    save_graph_npz,
)


def test_square_graph_is_bidirectional_and_serializable(tmp_path: Path):
    points = np.asarray(
        [[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0]]
    )
    graph = build_contour_graph(
        points,
        configuration_id="square",
        node_ids=np.asarray(["a", "b", "c", "d"]),
        targets={"CL": 0.5, "CD": 0.02},
        global_features={"mach": 0.3},
    )

    assert graph.num_nodes == 4
    assert graph.num_edges == 8
    assert graph.node_features.shape == (4, 8)
    assert graph.edge_features.shape == (8, 5)

    path = save_graph_npz(graph, tmp_path / "square.npz")
    loaded = load_graph_npz(path)

    assert loaded.configuration_id == graph.configuration_id
    assert loaded.targets == graph.targets
    assert loaded.global_features == graph.global_features
    np.testing.assert_allclose(loaded.node_features, graph.node_features)
    np.testing.assert_array_equal(loaded.edge_index, graph.edge_index)
