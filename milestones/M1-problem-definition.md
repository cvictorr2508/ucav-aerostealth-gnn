# M1 — Problem Definition

## Status

Construction authorized and completed. The chapter has been revised after owner feedback to strengthen academic rigor, terminology, the explanation of fidelity/multifidelity, deterministic mathematical optimization, and the role of Geometric Algebra. Merge into `develop` remains pending owner review and explicit Gate B authorization.

## Purpose

Transform `chapters/01_problem.qmd` into a self-contained scientific introduction that establishes the UCAV engineering context, literature review, justification, research gap, mathematical-optimization interest, research question, objectives, hypotheses, scope, and evaluation criteria.

## Scientific hierarchy

1. **Engineering problem:** multidisciplinary aero-stealth optimization of low-observable UCAV configurations.
2. **Main computational contribution:** acceleration of the optimization process using multifidelity Graph Neural Networks (GNNs).
3. **Structuring mathematical formalism:** Geometric Algebra (GA) for geometry, physics, learning, and optimization operations.
4. **Physical foundations:** electromagnetic scattering/RCS and subsonic aerodynamics.
5. **Decision layer:** deterministic mathematical optimization within MDO, using NLP for continuous formulations and MINLP when discrete decisions are present.

UCAV is treated as a functional class of unmanned combat air/aerial vehicle, not as a synonym for a flying-wing aerodynamic configuration.

## Editorial/scientific conventions

The conventions requested during the review are recorded in `notes/editorial-scientific-guidelines.md` and apply to subsequent milestones. Key points include:

- public text is written for external specialized readers and contains no milestone/developer language;
- acronyms are expanded at first occurrence;
- computational burden is expressed in terms of time, CPU/GPU, memory, storage and solver evaluations rather than “cheap/expensive” computation;
- fidelity and multifidelity are explicitly defined;
- research gaps are stated affirmatively;
- UQ and active learning are supporting strategies to be justified empirically, not mandatory components;
- Geometric Algebra is a committed methodological pillar;
- the former H4 comparing GA with conventional representations is removed;
- claims of linearization must preserve intrinsic physical nonlinearities.

## Literature positioning

M1 uses:

- João Pedro Rocha Silva's 2026 TCC on theoretical and experimental RCS characterization;
- verified UCAV literature on technology challenges, MDO, multifidelity design and SACCON/MULDICON;
- recent aero-stealth optimization literature, including deterministic gradient-based methods;
- recent mesh-based GNN work for aerodynamics, electromagnetics and coupled aero-electromagnetic analysis;
- mathematical optimization references on MDO architectures, NLP/MINLP and mixed-integer aerospace design.

The 2026 work by Li et al. on a multitask diffusion graph model for aero-electromagnetic analysis is treated as a direct benchmark. The research gap is expressed positively as the integration of UCAV MDO, multifidelity mesh-GNN surrogates, angular/polarized RCS, deterministic mathematical optimization, Geometric Algebra, and reference-model re-evaluation.

## Content completed

`chapters/01_problem.qmd` now includes:

- UCAV concept and terminology;
- UCAV as a multidisciplinary engineering problem;
- continuity from João Pedro Rocha Silva's RCS characterization work;
- explicit definitions of fidelity and multifidelity;
- RCS as an angular and polarization-dependent response;
- subsonic aerodynamic scope;
- state of the art in aero-stealth UCAV optimization;
- deterministic MDO, NLP and MINLP context;
- current GNN aero-EM literature;
- affirmative research gap and justification;
- Geometric Algebra as a structuring formalism;
- initial multidisciplinary mathematical formulation;
- GNN/multifidelity role;
- justified but optional UQ/active-learning section;
- research question;
- general and specific objectives;
- descriptive, falsifiable research hypotheses without the former GA-adoption H4;
- evaluation metrics based on prediction quality, computational-resource demand, processing time and re-evaluated Pareto quality;
- ablation plan and study delimitation.

## Files changed

- `chapters/01_problem.qmd`
- `references.bib`
- `index.qmd`
- `README.md`
- `notes/editorial-scientific-guidelines.md`
- `notes/m1-source-notes.md`
- `notes/m1-review-checklist.md`
- `milestones/M1-problem-definition.md`

No Python implementation is introduced in M1.

## Acceptance criteria

M1 is ready for Gate B review when:

- public prose is academically self-contained and free of internal planning language;
- all relevant acronyms are expanded at first occurrence;
- fidelity/multifidelity and computational-resource demand are explained clearly;
- UCAV is not conflated with a specific aerodynamic configuration;
- deterministic mathematical optimization, NLP and MINLP are introduced in the MDO context;
- the literature gap is affirmative and supported by current references;
- Geometric Algebra is presented as a committed formalism with mathematically rigorous statements about compactification/linearization;
- UQ/active learning are presented only as optional, justified supporting strategies;
- the former comparative H4 for Geometric Algebra is absent;
- `quarto render` succeeds for HTML and PDF;
- the completed PR diff is reviewed;
- the repository owner explicitly authorizes merge into `develop`.

## Authorization gates

### Gate A — construction

AUTHORIZED and completed.

### Gate B — merge

PENDING. The PR must remain open until the repository owner explicitly authorizes merge into `develop`.

Promotion from `develop` to `main` remains a separate reviewed PR so the public GitHub Pages content represents approved material only.
