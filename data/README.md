# Data

This directory documents datasets used by the project.

Public, redistributable, or synthetic datasets may be versioned in the repository when their size and license permit it. Large, proprietary, sensitive, export-controlled, or otherwise restricted solver/experimental data must not be committed here.

For each dataset added later, document at least:

- source and provenance;
- license and redistribution status;
- geometry/operating-condition definition;
- fidelity level;
- schema and units;
- procedure or script required to regenerate derived data.

## Chapter 5 — initial 2D data contract

The first executable pipeline targets ordered closed 2D contours. The raw CSV
is expected to contain one row per contour node and a persistent geometry
identifier.

Canonical core columns are:

- `configuration_id`: geometry identifier used for leakage-free splitting;
- `node_id`: node identifier unique inside one configuration;
- `x`, `y`: planar coordinates;
- optional explicit point-order column when `node_id` does not define contour order.

Global responses such as `CL`, `CD`, and the electromagnetic target may be
repeated on every row of a configuration; the loader verifies that they are
constant within that configuration. Operating conditions may be handled in the
same way.

The electromagnetic target name must reflect the solver definition. A strictly
2D scattering-width quantity must not be relabeled as 3D RCS.

No project dataset is committed by this change. The example configuration under
`configs/2d/` documents column mapping and paths without fabricating solver
results.
