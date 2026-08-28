# M1 — Problem Definition

## Status

Construction authorized and completed. The chapter has been revised after owner feedback to strengthen the UCAV engineering context and update the literature review through 2026. Merge into `develop` remains pending owner review and explicit Gate B authorization.

## Purpose

Transform `chapters/01_problem.qmd` from an editorial outline into the first substantive scientific chapter of the eBook, establishing the UCAV engineering context, justification, literature gap, research question, objectives, hypotheses, scope, and evaluation criteria before expanding the mathematical and computational chapters.

## Scientific hierarchy preserved

1. **Engineering problem:** multidisciplinary aero-stealth optimization of a low-observable UCAV configuration.
2. **Main computational contribution:** acceleration of the optimization process using multifidelity Graph Neural Networks (GNNs).
3. **Supporting mathematical contribution:** Geometric Algebra as a candidate representation and physics-regularization layer for the GNNs.
4. **Physical foundations:** electromagnetic scattering/RCS and subsonic aerodynamics.
5. **Decision layer:** multiobjective surrogate-assisted optimization with high-fidelity revalidation.

UCAV is treated as a functional class of unmanned combat air/aerial vehicle, **not as a synonym for a flying-wing aerodynamic configuration**. Flying-wing, tailless, blended-wing-body, lambda-wing, or other layouts are specific design families.

## Source corpus used

M1 was constructed and revised from:

- João Pedro Rocha Silva's 2026 TCC on theoretical and experimental RCS characterization;
- the project report on GNNs for RCS optimization;
- verified literature on UCAV technology challenges, multidisciplinary design, multifidelity UCAV design, NATO SACCON/MULDICON research, recent aero-stealth optimization, and GNN-based aero-electromagnetic surrogate modeling;
- methodological decisions consolidated during project planning.

The tensor/differential-forms material remains primarily reserved for later Geometric Algebra and physics chapters.

## Revised state-of-the-art positioning

The 2026 literature update identified Li et al., *Multi-task diffusion graph model for aero-electromagnetic analysis of blended-wing-body configurations*, which directly demonstrates a mesh-based multitask GNN for joint aerodynamic and electromagnetic aircraft analysis. Therefore M1 does not claim that integrated aero-EM GNN analysis is absent.

The research gap is positioned instead at the intersection of:

1. UCAV aero-stealth multidisciplinary optimization;
2. mesh-native GNN surrogate modeling;
3. explicit LF→HF multifidelity learning in aerodynamics and electromagnetics;
4. angular/polarized RCS prediction rather than mean-RCS only;
5. uncertainty-aware active learning oriented to Pareto-relevant regions;
6. end-to-end optimization speed-up accounting;
7. selective high-fidelity and, when feasible, experimental revalidation;
8. controlled testing of Geometric Algebra as a representation/regularization layer.

## Content completed

`chapters/01_problem.qmd` now includes:

- UCAV concept, terminology, and distinction from aerodynamic configuration;
- UCAV as a multidisciplinary engineering problem;
- continuity from the previous RCS characterization work;
- RCS as an angular and polarization-dependent design response;
- subsonic aerodynamic scope;
- state of the art in UCAV aero-stealth MDO;
- current GNN aero-EM literature and the refined research gap;
- explicit justification;
- preliminary multiobjective mathematical formulation;
- role of GNNs and multifidelity;
- research question;
- general and specific objectives;
- falsifiable hypotheses H1--H5;
- evaluation metrics, ablation plan, scope, and exclusions.

## Files changed

- `chapters/01_problem.qmd`
- `references.bib`
- `index.qmd`
- `README.md`
- `notes/m1-source-notes.md`
- `notes/m1-review-checklist.md`
- `milestones/M1-problem-definition.md`

No Python implementation is introduced in M1.

## Acceptance criteria

M1 is ready for Gate B review when:

- UCAV terminology is technically correct and not conflated with flying wing;
- the engineering context and state of the art include current literature through 2026;
- the direct 2026 aero-EM GNN antecedent is explicitly acknowledged;
- justification, literature gap, research question, general objective, and specific objectives are explicit;
- central claims are supported by citations;
- GNN acceleration is clearly the principal computational contribution;
- Geometric Algebra is framed as a representation/regularization hypothesis, not an assumed speed-up mechanism;
- `quarto render` succeeds for HTML and PDF;
- the completed PR diff is reviewed;
- the repository owner explicitly authorizes merge into `develop`.

## Authorization gates

### Gate A — construction

AUTHORIZED and completed.

### Gate B — merge

PENDING. The PR must remain open until the repository owner explicitly authorizes merge into `develop`.

Promotion from `develop` to `main` remains a separate reviewed PR so the public GitHub Pages content represents approved material only.
