import numpy as np

from ucav_aerostealth.geometry.ga2d import (
    Multivector2D,
    oriented_contour_geometry,
    signed_polygon_area,
)


def test_cl20_basis_products():
    e1 = Multivector2D.vector(1.0, 0.0)
    e2 = Multivector2D.vector(0.0, 1.0)
    i = Multivector2D.bivector(1.0)

    np.testing.assert_allclose(e1.geometric_product(e1).as_array(), [1, 0, 0, 0])
    np.testing.assert_allclose(e2.geometric_product(e2).as_array(), [1, 0, 0, 0])
    np.testing.assert_allclose(e1.geometric_product(e2).as_array(), [0, 0, 0, 1])
    np.testing.assert_allclose(e2.geometric_product(e1).as_array(), [0, 0, 0, -1])
    np.testing.assert_allclose(i.geometric_product(i).as_array(), [-1, 0, 0, 0])


def test_right_dual_rotates_e1_clockwise():
    e1 = Multivector2D.vector(1.0, 0.0)
    np.testing.assert_allclose(e1.right_dual().as_array(), [0, 0, -1, 0])


def test_ccw_square_has_positive_area_and_outward_normals():
    points = np.asarray(
        [[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0]]
    )
    geometry = oriented_contour_geometry(points)

    assert signed_polygon_area(points) == 1.0
    assert geometry.orientation == 1
    np.testing.assert_allclose(geometry.edge_lengths, np.ones(4))
    np.testing.assert_allclose(geometry.edge_outward_normals[0], [0.0, -1.0])
    assert np.all(geometry.turn_bivector_e12 > 0.0)


def test_clockwise_square_preserves_outward_direction():
    points = np.asarray(
        [[0.0, 0.0], [0.0, 1.0], [1.0, 1.0], [1.0, 0.0]]
    )
    geometry = oriented_contour_geometry(points)

    assert geometry.orientation == -1
    np.testing.assert_allclose(geometry.edge_outward_normals[0], [-1.0, 0.0])
