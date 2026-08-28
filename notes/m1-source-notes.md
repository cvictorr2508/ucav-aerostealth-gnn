# M1 source-grounding notes

This internal project note records the source basis used to construct `chapters/01_problem.qmd`.

## Existing project corpus

- João Pedro Rocha Silva (2026), TCC on theoretical and experimental RCS characterization: used for the existing CEM/experimental baseline, RCS context, high-frequency scattering regime, and prior GFF/AIM-120 work.
- `GNNs no framework de otimização de assinatura RCS para um UCAV flying-wing`: used as the project-level synthesis that motivated mesh/graph representation, multifidelity GNN surrogates, active learning, uncertainty quantification, RCS-specific metrics, and selective HF revalidation.
- Tensor/differential-forms course: not used as a technical source for M1 derivations; its role remains deferred to the Geometric Algebra and physics chapters.

## External bibliographic verification performed for M1

The repository bibliography was expanded only with references needed to support the M1 framing, including Black & Najafi (MFGNN), Chen et al. (mesh-based CFD GNN), Shan et al. (physics-informed graph residual learning for 3-D EM), Kong et al. (3-D PEC far-field prediction), Peng et al. (physics-informed GCN for flow), and Li et al. (GINO).

## Claim discipline

M1 distinguishes among:

1. established/source-supported theory and prior work;
2. methodological choices adopted by this project;
3. hypotheses that must be tested experimentally.

In particular, the chapter does not assume that Geometric Algebra reduces computational cost and does not treat a learned surrogate as a replacement for high-fidelity validation.
