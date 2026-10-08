"""Schema definitions for the first 2D contour datasets."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class ContourCSVSchema:
    """Column mapping for an ordered closed-contour CSV.

    The initial Chapter 5 implementation deliberately targets ordered 2D
    contours. Connectivity for arbitrary 2D cell meshes will be added only
    after the actual solver CSV schema is inspected.
    """

    configuration_id: str = "configuration_id"
    node_id: str = "node_id"
    x: str = "x"
    y: str = "y"
    order: str | None = None
    target_columns: tuple[str, ...] = field(default_factory=tuple)
    global_columns: tuple[str, ...] = field(default_factory=tuple)

    @property
    def required_columns(self) -> tuple[str, ...]:
        columns = [
            self.configuration_id,
            self.node_id,
            self.x,
            self.y,
            *self.target_columns,
            *self.global_columns,
        ]
        if self.order:
            columns.append(self.order)
        return tuple(dict.fromkeys(columns))
