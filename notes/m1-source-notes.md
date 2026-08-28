# M1 source-grounding notes

This project note records the source basis used to construct and revise `chapters/01_problem.qmd`.

## Existing project corpus

- João Pedro Rocha Silva (2026), TCC on theoretical and experimental RCS characterization: used for the CEM/experimental baseline, RCS context, scattering mechanisms, method comparison, and continuity from characterization to optimization.
- `GNNs no framework de otimização de assinatura RCS para um UCAV flying-wing`: used as an exploratory project synthesis for mesh/graph representation, multifidelity GNN surrogates, RCS-specific outputs, and reference-model re-evaluation. Recommendations from this report are not automatically promoted to mandatory methodology.
- Tensor/differential-forms course: reserved primarily for later Geometric Algebra and physics chapters.

## UCAV and MDO literature

The revised chapter separates UCAV as a functional vehicle class from flying-wing, tailless, blended-wing-body and other aerodynamic configurations. Sources include:

- Department of the Air Force AFI 16-401 for formal UAV/UCAV terminology;
- Sepulveda & Smith (2017) for stealth-UCAV technology challenges;
- Hu & Yu (2009), Nguyen et al. (2013), Papageorgiou et al. (2018), Sepulveda et al. (2019), and Liersch et al. (2020) for UCAV multidisciplinary design;
- Aleisa et al. (2023) and Nikbay et al. (2026) for configuration-specific UCAV studies;
- Martins & Lambe (2013) and Leng et al. (2025) for MDO architectures and current aircraft-MDO context;
- Shi et al. (2021) for metamodel-based MDO and the computational-resource motivation for surrogate models.

## Deterministic mathematical optimization

The revised chapter explicitly introduces deterministic mathematical optimization within MDO:

- Li et al. (2019) and Thoulon et al. (2024) for gradient-based aero-stealth optimization;
- Lee & Leyffer (2012) and Belotti et al. (2013) for MINLP foundations;
- Roy et al. (2017) for a mixed-integer aircraft allocation/mission/design application.

The final formulation is NLP when all decision variables are continuous and MINLP only when discrete decisions are present.

## GNN and multifidelity literature

- Pfaff et al. (2021), Chen et al. (2021), Peng et al. (2024) and Li et al. (2023) support mesh/graph modeling in physics and CFD;
- Shan et al. (2024) and Kong et al. (2024) support geometry-native learned models in computational electromagnetics;
- Black & Najafi (2022) and Taghizadeh et al. (2025) support explicit multifidelity graph-learning architectures;
- Li et al. (2026), `Multi-task diffusion graph model for aero-electromagnetic analysis of blended-wing-body configurations`, is the closest current direct benchmark for joint aero-EM graph modeling.

## Revised research gap

The research gap is expressed affirmatively as the integration of:

1. UCAV aero-stealth MDO;
2. mesh-native GNN surrogate modeling;
3. explicit multifidelity learning in aerodynamics and electromagnetics;
4. angular and polarized RCS prediction;
5. deterministic mathematical optimization with NLP/MINLP compatibility;
6. Geometric Algebra as the common mathematical formalism;
7. end-to-end evaluation of time and computational-resource demand;
8. reference-model re-evaluation of optimization solutions.

UQ and active learning are supporting strategies that may be evaluated if they improve the selection of additional resource-intensive simulations; they are not part of the core gap by default.

## Geometric Algebra discipline

Geometric Algebra is a committed methodological pillar. The chapter states its role in geometric/physical representation and optimization algebra. Claims of linearization are constrained by mathematical rigor: Maxwell equations in linear media are already linear in the fields, while Euler equations retain intrinsic nonlinearities. The project seeks compact multivector formulations and linear representations only where mathematically admissible.

The former H4 that treated GA adoption as a comparative hypothesis has been removed.
