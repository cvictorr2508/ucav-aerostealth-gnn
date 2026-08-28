# M1 — Problem Definition

## Purpose

Transform `chapters/01_problem.qmd` from an editorial outline into the first substantive scientific chapter of the eBook, establishing the engineering problem, research question, hypotheses, objectives, scope, and evaluation criteria before expanding the mathematical and computational chapters.

## Scientific hierarchy to preserve

1. **Engineering problem:** multidisciplinary aero-stealth optimization of a UCAV flying-wing.
2. **Main computational contribution:** acceleration of the optimization process using multifidelity Graph Neural Networks (GNNs).
3. **Supporting mathematical contribution:** Geometric Algebra as a candidate representation and physics-regularization layer for the GNNs.
4. **Physical foundations:** electromagnetic scattering/RCS and subsonic inviscid aerodynamics.
5. **Decision layer:** multiobjective surrogate-assisted optimization with high-fidelity revalidation.

M1 must not present Geometric Algebra as the principal contribution and must not assume a priori that it reduces computational cost.

## Source corpus for M1

M1 will initially use only the material already consolidated for this project:

- João Pedro Rocha Silva's TCC on theoretical and experimental RCS characterization;
- the report on GNNs for RCS optimization of a UCAV flying-wing;
- the tensor/differential-forms course as supporting mathematical context where directly relevant;
- the verified initial references already present in `references.bib`;
- methodological decisions consolidated in the project planning discussion.

Additional references will be incorporated in later milestones or only when a specific M1 claim cannot be adequately supported by the current corpus.

## Planned content for `chapters/01_problem.qmd`

### 1. UCAV flying-wing and aero-stealth design

- engineering context of a flying-wing UCAV;
- geometric coupling between aerodynamic performance and electromagnetic signature;
- why simultaneous treatment is required.

### 2. Radar Cross Section as an optimization response

- operational meaning of RCS;
- dependence on geometry, frequency, incidence, polarization, and scattering mechanisms;
- distinction between scalar summaries and angular/polarization-dependent RCS responses.

### 3. Subsonic aerodynamic performance

- scope restricted to the aerodynamic quantities required for the optimization problem;
- expected responses such as lift, drag, moment, and lift-to-drag ratio;
- explicit separation between the inviscid Euler model used as one fidelity level and higher-fidelity CFD when required.

### 4. Multidisciplinary trade-off

- geometric variables affect both electromagnetic and aerodynamic responses;
- preliminary multiobjective formulation;
- continuous and potentially discrete design variables;
- constraints to be refined later.

### 5. Computational bottleneck

- repeated CEM and CFD evaluations make direct optimization expensive;
- distinguish cost per solver evaluation from cost of the complete optimization process;
- motivate surrogate-assisted optimization.

### 6. Why GNNs are central

- mesh/graph correspondence;
- geometry-aware surrogate modeling;
- prediction of electromagnetic and aerodynamic responses;
- main acceleration mechanism: replace most expensive solver calls inside the optimization loop with fast GNN inference, while preserving selective high-fidelity calls.

### 7. Why multifidelity is central

- high-fidelity data are expensive;
- combine broad low-fidelity coverage with sparse high-fidelity correction;
- connect multifidelity learning to active learning and Pareto-oriented sampling.

### 8. Role of Geometric Algebra

- candidate representation for oriented geometric and physical quantities;
- candidate basis for physics-informed regularization;
- explicit research hypothesis rather than assumed performance advantage.

### 9. Research question

Proposed form:

> To what extent can multifidelity Graph Neural Networks, enriched by geometric representations and physics-informed constraints formulated with Geometric Algebra, reduce the computational cost of aero-stealth optimization of a UCAV flying-wing while preserving sufficient accuracy relative to reference electromagnetic and aerodynamic solvers?

### 10. General objective

Proposed form:

> Develop and validate multifidelity, physics-informed Graph Neural Network surrogate models, with geometric representations informed by Geometric Algebra, to accelerate multidisciplinary optimization of Radar Cross Section and aerodynamic performance of a UCAV flying-wing.

### 11. Research hypotheses

At minimum:

- graph representation versus parameter-only baseline;
- multifidelity versus high-fidelity-only learning under a fixed computational budget;
- physics-informed versus purely data-driven learning;
- Geometric-Algebra-informed versus conventional Cartesian/geometric representation;
- GNN-assisted optimization versus direct solver-based optimization.

### 12. Evaluation metrics

M1 will define the metric families, leaving numerical targets for later experimental milestones:

- surrogate prediction error;
- uncertainty calibration;
- evaluation speed-up;
- end-to-end optimization speed-up including dataset generation and training;
- Pareto-front quality after high-fidelity revalidation;
- ablation-based attribution of gains.

## Files expected to change during construction

Required:

- `chapters/01_problem.qmd`
- `references.bib` only when a citation used in M1 is missing or needs correction

Optional, only if necessary for consistency:

- `index.qmd`
- `_quarto.yml`

No Python implementation is planned for M1.

## Acceptance criteria

M1 will be considered ready for merge when:

- `chapters/01_problem.qmd` is a coherent scientific chapter rather than an outline;
- central claims are supported by citations from the available corpus;
- source-derived statements are distinguishable from project hypotheses and methodological choices;
- GNN acceleration is clearly identified as the principal computational contribution;
- Geometric Algebra is framed as a representation/regularization hypothesis, not an assumed speed-up mechanism;
- the multidisciplinary problem, research question, objective, hypotheses, and evaluation criteria are explicit;
- `quarto render` succeeds for HTML and PDF;
- the PR diff is reviewed before merge.

## Authorization gates

### Gate A — authorization to construct M1

No substantive M1 chapter expansion should begin until the repository owner explicitly authorizes construction in this PR or in the associated project discussion.

### Gate B — authorization to merge M1

After construction, citation review, and successful Quarto build, the PR should remain open until the repository owner explicitly authorizes the merge into `develop`.

After M1 is integrated and validated in `develop`, promotion from `develop` to `main` should occur through a separate reviewed PR so that the public GitHub Pages content continues to represent approved material.
