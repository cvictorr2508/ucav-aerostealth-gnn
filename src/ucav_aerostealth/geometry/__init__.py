"""Geometric Algebra utilities used by the research pipeline."""

from .ga2d import (
    ContourGeometry2D,
    Multivector2D,
    oriented_contour_geometry,
    signed_polygon_area,
)

__all__ = [
    "ContourGeometry2D",
    "Multivector2D",
    "oriented_contour_geometry",
    "signed_polygon_area",
]
