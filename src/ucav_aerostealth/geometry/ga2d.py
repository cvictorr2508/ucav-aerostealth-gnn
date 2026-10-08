"""Minimal, explicit Cl(2,0) implementation for Chapter 5.

The first implementation intentionally keeps the algebra transparent instead
of depending on a large external GA package. This makes the identities used
to build graph features directly unit-testable.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


def _blade_product(left_mask: int, right_mask: int) -> tuple[float, int]:
    """Return sign and basis mask for a Cl(2,0) basis-blade product."""

    sign = 1.0
    for basis_index in range(2):
        if left_mask & (1 << basis_index):
            lower_right_bits = right_mask & ((1 << basis_index) - 1)
            if lower_right_bits.bit_count() % 2:
                sign *= -1.0
    return sign, left_mask ^ right_mask


@dataclass(frozen=True)
class Multivector2D:
    """Multivector a + b e1 + c e2 + d e12 in Cl(2,0)."""

    scalar: float = 0.0
    e1: float = 0.0
    e2: float = 0.0
    e12: float = 0.0

    def as_array(self) -> np.ndarray:
        return np.asarray([self.scalar, self.e1, self.e2, self.e12], dtype=float)

    @classmethod
    def from_array(cls, values: np.ndarray) -> "Multivector2D":
        array = np.asarray(values, dtype=float)
        if array.shape != (4,):
            raise ValueError("A Cl(2,0) multivector requires four components.")
        return cls(*array.tolist())

    @classmethod
    def vector(cls, x: float, y: float) -> "Multivector2D":
        return cls(e1=float(x), e2=float(y))

    @classmethod
    def bivector(cls, coefficient: float) -> "Multivector2D":
        return cls(e12=float(coefficient))

    def geometric_product(self, other: "Multivector2D") -> "Multivector2D":
        left = self.as_array()
        right = other.as_array()
        result = np.zeros(4, dtype=float)

        for left_mask, left_value in enumerate(left):
            if left_value == 0.0:
                continue
            for right_mask, right_value in enumerate(right):
                if right_value == 0.0:
                    continue
                sign, output_mask = _blade_product(left_mask, right_mask)
                result[output_mask] += sign * left_value * right_value

        return Multivector2D.from_array(result)

    def reverse(self) -> "Multivector2D":
        return Multivector2D(
            scalar=self.scalar,
            e1=self.e1,
            e2=self.e2,
            e12=-self.e12,
        )

    def right_dual(self) -> "Multivector2D":
        """Right dual A I^{-1}; in Cl(2,0), I^{-1} = -I."""

        return self.geometric_product(Multivector2D(e12=-1.0))


@dataclass(frozen=True)
class ContourGeometry2D:
    """Geometric quantities reconstructed from one oriented closed contour."""

    points: np.ndarray
    signed_area: float
    orientation: int
    edge_vectors: np.ndarray
    edge_lengths: np.ndarray
    edge_tangents: np.ndarray
    edge_outward_normals: np.ndarray
    node_tangents: np.ndarray
    node_outward_normals: np.ndarray
    turn_dot: np.ndarray
    turn_bivector_e12: np.ndarray


def _as_open_polygon(points: np.ndarray) -> np.ndarray:
    array = np.asarray(points, dtype=float)
    if array.ndim != 2 or array.shape[1] != 2:
        raise ValueError("Contour points must have shape (n, 2).")
    if len(array) < 3:
        raise ValueError("A closed contour requires at least three points.")
    if np.allclose(array[0], array[-1]):
        array = array[:-1]
    if len(array) < 3:
        raise ValueError("A closed contour requires at least three distinct points.")
    if not np.isfinite(array).all():
        raise ValueError("Contour coordinates must be finite.")
    return array


def signed_polygon_area(points: np.ndarray) -> float:
    """Shoelace signed area; positive means counter-clockwise ordering."""

    polygon = _as_open_polygon(points)
    x = polygon[:, 0]
    y = polygon[:, 1]
    x_next = np.roll(x, -1)
    y_next = np.roll(y, -1)
    return 0.5 * float(np.sum(x * y_next - x_next * y))


def _normalize_rows(vectors: np.ndarray, *, atol: float = 1e-14) -> np.ndarray:
    lengths = np.linalg.norm(vectors, axis=1)
    if np.any(lengths <= atol):
        raise ValueError("Zero-length geometric direction encountered.")
    return vectors / lengths[:, None]


def oriented_contour_geometry(points: np.ndarray) -> ContourGeometry2D:
    """Reconstruct Cl(2,0)-compatible descriptors of a closed contour."""

    polygon = _as_open_polygon(points)
    area = signed_polygon_area(polygon)
    if np.isclose(area, 0.0, atol=1e-14):
        raise ValueError("Contour has zero or numerically degenerate signed area.")

    orientation = 1 if area > 0.0 else -1
    edge_vectors = np.roll(polygon, -1, axis=0) - polygon
    edge_lengths = np.linalg.norm(edge_vectors, axis=1)
    if np.any(edge_lengths <= 1e-14):
        raise ValueError("Consecutive contour points must be distinct.")

    edge_tangents = edge_vectors / edge_lengths[:, None]
    right_duals = np.column_stack(
        [edge_tangents[:, 1], -edge_tangents[:, 0]]
    )
    edge_normals = orientation * right_duals

    previous_tangent = np.roll(edge_tangents, 1, axis=0)
    node_tangent_raw = previous_tangent + edge_tangents
    raw_lengths = np.linalg.norm(node_tangent_raw, axis=1)

    node_tangents = np.empty_like(node_tangent_raw)
    regular = raw_lengths > 1e-14
    node_tangents[regular] = (
        node_tangent_raw[regular] / raw_lengths[regular, None]
    )
    node_tangents[~regular] = edge_tangents[~regular]

    node_right_duals = np.column_stack(
        [node_tangents[:, 1], -node_tangents[:, 0]]
    )
    node_normals = orientation * node_right_duals

    turn_dot = np.sum(previous_tangent * edge_tangents, axis=1)
    turn_bivector = (
        previous_tangent[:, 0] * edge_tangents[:, 1]
        - previous_tangent[:, 1] * edge_tangents[:, 0]
    )

    return ContourGeometry2D(
        points=polygon,
        signed_area=area,
        orientation=orientation,
        edge_vectors=edge_vectors,
        edge_lengths=edge_lengths,
        edge_tangents=edge_tangents,
        edge_outward_normals=edge_normals,
        node_tangents=node_tangents,
        node_outward_normals=node_normals,
        turn_dot=turn_dot,
        turn_bivector_e12=turn_bivector,
    )
