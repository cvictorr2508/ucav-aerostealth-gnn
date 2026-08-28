# UCAV Aero-Stealth GNN

Multifidelity Graph Neural Networks with Geometric Algebra and physics-informed learning for accelerated aero-stealth optimization of low-observable UCAV configurations.

> **Terminology:** UCAV denotes a functional class of unmanned combat aircraft/air vehicles; it is not synonymous with a flying-wing aerodynamic configuration. Flying-wing, tailless, blended-wing-body, or other layouts may be considered as specific design families.

## Objective

This project investigates Graph Neural Networks (GNNs) as multifidelity surrogate models to accelerate multidisciplinary aero-stealth optimization involving:

- Radar Cross Section (RCS);
- subsonic aerodynamic performance;
- geometric representations informed by Geometric Algebra;
- physics-informed learning based on Maxwell and Euler equations;
- uncertainty-aware multifidelity learning and active learning;
- multiobjective optimization with high-fidelity revalidation.

## Research architecture

```text
Geometry / OpenVSP
        ↓
Mesh and graph representation
        ↓
Low- and high-fidelity physics solvers
        ↓
Multifidelity physics-informed GNNs
        ↓
Fast surrogate models
        ↓
Aero-stealth multidisciplinary optimization
        ↓
High-fidelity validation
```

The principal computational contribution is the use of multifidelity GNNs to reduce the cost of repeated electromagnetic and aerodynamic evaluations inside the optimization loop. Geometric Algebra is investigated as a representation and physics-regularization layer, not assumed a priori to provide computational speed-up.

## Documentation

The technical documentation and research eBook are written in [Quarto](https://quarto.org/) and rendered to HTML and PDF from the same source.

## Development workflow

- `main`: stable, reviewed content;
- `develop`: integration branch for the next milestone;
- feature branches: optional branches for isolated experiments or substantial changes.

Changes from `develop` to `main` should be reviewed through pull requests.

## Repository status

Research and development in progress. M1 expands the UCAV engineering context, literature gap, objectives, hypotheses, and evaluation criteria before implementation milestones begin.

## License

Software in this repository is currently distributed under the MIT License. Licensing for the eBook and other research content will be specified separately before public release of substantive content.
