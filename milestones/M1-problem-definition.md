# M1 — Problem Definition

## Status

Construction authorized and completed. Merge into `develop` is pending owner review and explicit Gate B authorization.

## Purpose

Transform `chapters/01_problem.qmd` from an editorial outline into the first substantive scientific chapter of the eBook, establishing the engineering problem, research question, hypotheses, objectives, scope, and evaluation criteria before expanding the mathematical and computational chapters.

## Scientific hierarchy preserved

1. Engineering problem: multidisciplinary aero-stealth optimization of a UCAV flying-wing.
2. Main computational contribution: acceleration of the optimization process using multifidelity Graph Neural Networks (GNNs).
3. Supporting mathematical contribution: Geometric Algebra as a candidate representation and physics-regularization layer for the GNNs.
4. Physical foundations: electromagnetic scattering/RCS and subsonic inviscid aerodynamics.
5. Decision layer: multiobjective surrogate-assisted optimization with high-fidelity revalidation.

M1 does not present Geometric Algebra as the principal contribution and does not assume a priori that it reduces computational cost.

## Source corpus used

M1 was constructed from the material already consolidated for this project:

- João Pedro Rocha Silva's 2026 TCC on theoretical and experimental RCS characterization;
- the report on GNNs for RCS optimization of a UCAV flying-wing;
- the verified repository bibliography and bibliographic checks for references needed by M1;
- methodological decisions consolidated during project planning.

The tensor/differential-forms material remains primarily reserved for later Geometric Algebra and physics chapters.

## Content completed

`chapters/01_problem.qmd` now covers the engineering context, RCS and aerodynamic responses, preliminary multidisciplinary formulation, computational bottleneck, central role of GNN acceleration, multifidelity and active learning, the supporting role of Geometric Algebra, the research question, objectives, hypotheses, scope, evaluation metrics, ablation strategy, and contribution hierarchy.

## Files changed

- `chapters/01_problem.qmd`
- `references.bib`
- `notes/m1-source-notes.md`
- `milestones/M1-problem-definition.md`

No Python implementation is introduced in M1.

## Acceptance criteria

The content-oriented criteria are complete. Before merge, the remaining requirements are:

- successful Quarto HTML/PDF build in CI;
- review of the completed PR diff;
- explicit owner authorization to merge into `develop`.

## Authorization gates

### Gate A — construction

AUTHORIZED by the repository owner before substantive construction.

### Gate B — merge

PENDING. The PR must remain open until CI succeeds and the repository owner explicitly authorizes merge into `develop`.

Promotion from `develop` to `main` remains a separate reviewed PR so the public GitHub Pages content represents approved material only.
