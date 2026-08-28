# UCAV Aero-Stealth GNN

Multifidelity Graph Neural Networks with Geometric Algebra for accelerated multidisciplinary aero-stealth optimization of low-observable UCAV configurations.

> **Terminology:** UCAV denotes a functional class of unmanned combat aircraft/air vehicles; it is not synonymous with a flying-wing aerodynamic configuration. Flying-wing, tailless, blended-wing-body, or other layouts may be considered as specific design families.

## Objective

This project develops a multidisciplinary aero-stealth optimization framework that combines:

- Radar Cross Section (RCS) modeling;
- subsonic aerodynamic performance;
- Geometric Algebra as a common mathematical representation for geometry and physics;
- mesh-based Graph Neural Networks (GNNs);
- multifidelity learning across models with different physical/numerical detail and computational-resource requirements;
- deterministic mathematical optimization, including NLP and MINLP formulations when appropriate;
- high-fidelity re-evaluation of selected optimization solutions.

## Research architecture

```text
Geometry / OpenVSP
        ↓
Mesh and graph representation
        ↓
Physics models at different fidelity levels
        ↓
Multifidelity physics-informed GNNs
        ↓
Fast surrogate evaluations
        ↓
Deterministic multidisciplinary aero-stealth optimization
        ↓
Reference-model re-evaluation
```

The principal computational contribution is the use of multifidelity GNNs to reduce the number of resource-intensive electromagnetic and aerodynamic evaluations required inside the optimization loop. Geometric Algebra is adopted as a structuring mathematical formalism for geometric representation, physical relations, and optimization operators.

Uncertainty quantification and active learning are considered supporting strategies that may be evaluated when they demonstrably improve the selection of additional high-fidelity simulations; they are not assumed as mandatory components of the framework.

## Documentation

The technical documentation and research eBook are written in [Quarto](https://quarto.org/) and rendered to HTML and PDF from the same source.

## Development workflow

- `main`: stable, reviewed content;
- `develop`: integration branch for the next milestone;
- feature branches: optional branches for isolated experiments or substantial changes.

Changes from `develop` to `main` should be reviewed through pull requests.

## Repository status

Research and development in progress.

## License

Software in this repository is currently distributed under the MIT License. Licensing for the eBook and other research content will be specified separately before public release of substantive content.
