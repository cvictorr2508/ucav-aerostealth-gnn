# M1 source-grounding notes

This project note records the source basis used to construct and revise `chapters/01_problem.qmd`.

## Existing project corpus

- João Pedro Rocha Silva (2026), TCC on theoretical and experimental RCS characterization: used for the existing CEM/experimental baseline, RCS context, high-frequency scattering regime, and continuity from characterization to optimization.
- `GNNs no framework de otimização de assinatura RCS para um UCAV flying-wing`: used as the project-level synthesis that motivated mesh/graph representation, multifidelity GNN surrogates, active learning, uncertainty quantification, RCS-specific metrics, and selective HF revalidation.
- Tensor/differential-forms course: not used as a technical source for M1 derivations; its role remains deferred to the Geometric Algebra and physics chapters.

## Literature update triggered by M1 review

The first M1 draft used the expression `UCAV flying-wing` too broadly. The revised chapter explicitly separates **UCAV as a functional vehicle class** from **flying-wing/tailless/blended-wing configurations as aerodynamic design choices**.

The literature review was extended with:

- Department of the Air Force AFI 16-401 for a formal UCAV/UAV terminology reference;
- Sepulveda & Smith (2017) on technology challenges of stealth UCAVs;
- Hu & Yu (2009), Nguyen et al. (2013), Papageorgiou et al. (2018), Sepulveda et al. (2019), and Liersch et al. (2020) for the progression of UCAV MDO and multidisciplinary design;
- Aleisa et al. (2023) as a configuration-specific flying-wing UCAV study;
- Nikbay et al. (2026) as an up-to-date UCAV aero-stealth MDO study using classical surrogate/global optimization;
- Li et al. (2026), `Multi-task diffusion graph model for aero-electromagnetic analysis of blended-wing-body configurations`, as the closest direct current antecedent to an integrated aero-EM GNN surrogate;
- Taghizadeh et al. (2025) for a recent multifidelity mesh-GNN methodology.

## Revised gap discipline

After the 2026 literature update, M1 must **not** claim that GNNs have not been used for joint aerodynamic/electromagnetic aircraft analysis. Li et al. (2026) directly demonstrates such a model.

The project gap is instead positioned at the intersection of:

1. UCAV aero-stealth multidisciplinary optimization;
2. mesh-native GNN surrogate modeling;
3. explicit LF→HF multifidelity learning in aero and EM;
4. angular/polarized RCS prediction rather than mean-RCS only;
5. uncertainty-aware active learning oriented to Pareto-relevant regions;
6. end-to-end optimization speed-up accounting;
7. selective HF/experimental revalidation;
8. controlled testing of Geometric Algebra as a representation/regularization layer.

## Claim discipline

M1 distinguishes among established/source-supported theory and prior work, methodological choices adopted by this project, and hypotheses that must be tested experimentally. In particular, the chapter does not assume that Geometric Algebra reduces computational cost and does not treat a learned surrogate as a replacement for high-fidelity validation.
