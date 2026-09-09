# Bibliographic audit — Chapters 1–3

Scope: `chapters/01_problem.qmd`, `chapters/02_geometric_algebra.qmd`, `chapters/03_physics.qmd`, `references.bib`, and project-level citation configuration.

## Global convention

The eBook adopts IEEE-style numeric engineering citations. `_quarto.yml` points to `ieee.csl`; citations should therefore render as numbered references in order of appearance. Source QMD files should attach citations directly to claims using Pandoc citation syntax, while author names used narratively must be written as normal prose rather than exposing a raw citation key as the grammatical subject.

## Chapter 1 — Context and problem definition

The citation keys used in Chapter 1 resolve to entries in `references.bib`. The chapter uses references with appropriate evidentiary roles: official terminology for UCAV classification; peer-reviewed literature for UCAV design, MDO, aero-stealth optimization, multifidelity modeling and GNN applications; foundational books for RCS and optimization; and the Rocha Silva thesis for the project-specific experimental/computational RCS antecedent.

No orphan citation key was identified in the audited source. Narrative attributions already use author names in prose followed by citations, so no systematic source-level citation rewrite is required in this chapter.

## Chapter 2 — Geometric Algebra

The chapter relies appropriately on foundational GA books for algebraic definitions and on specialized sources for tensor analysis, fluid-mechanics interpretations and GA-based graph learning. All audited citation keys resolve in `references.bib`.

Source-level narrative citation forms requiring normalization were identified in sentences whose grammatical subject is a raw citation key. These should be rewritten as normal author prose followed by the IEEE citation: `@vanbladel2007`, `@sen2023`, `@parameswaran2024` and `@zhong2025` in narrative positions. Parenthetical/claim-attached uses such as `[@hestenes1984; @doran2003]` are already appropriate.

## Chapter 3 — Physics

The chapter uses Knott for RCS/scattering foundations; Yee and Rao–Wilton–Glisson for foundational numerical CEM methods; Dressel and Doran for spacetime algebra; and Sen and Parameswaran et al. for the fluid/GA analogies. These evidentiary roles are appropriate and the citation keys resolve in `references.bib`.

Narrative citation forms requiring source normalization were identified for `@yee1966`, `@rao1982`, `@dressel2015`, `@sen2023` and `@parameswaran2024` when the raw key is used as part of the grammatical sentence. Claim-attached citations already enclosed in brackets are appropriate.

The audit also confirms the need to preserve the distinction between the cited GA fluid analogies and the conservative compressible Euler system: the Sen and Parameswaran references support geometric/Maxwell-like reformulations, not a claim that the full Euler equations become linear.

## Bibliographic metadata corrected

The following metadata were strengthened during the audit:

- Hestenes and Sobczyk: DOI, ISBN and publication place;
- Bronstein et al.: arXiv DOI;
- Pfaff et al.: stable OpenReview URL for the ICLR 2021 conference paper;
- Taghizadeh et al.: issue number;
- Li et al. (GINO): proceedings page range;
- Air Force Instruction 16-401: report number;
- Knott et al.: ISBN;
- Yee: DOI `10.1109/TAP.1966.1138693`;
- Rao, Wilton and Glisson: DOI `10.1109/TAP.1982.1142818`;
- Rocha Silva: normalized as a bachelor's thesis entry;
- Van Bladel: publisher, series and ISBN.

## Verification notes

Publisher/DOI checks were performed against authoritative or publisher-linked records where available. In particular, the IEEE records confirm the Yee and Rao–Wilton–Glisson DOIs; Wiley confirms the second edition and publisher metadata for Van Bladel; Springer/Reidel records confirm the Hestenes–Sobczyk DOI; NeurIPS records confirm the GINO proceedings metadata; and the AIP/Wiley publisher records confirm the current Li et al. and Taghizadeh et al. entries.

## Remaining source-normalization work in this branch

Before this audit PR is marked ready for review, the raw author-in-text citation-key usages identified in Chapters 2 and 3 should be rewritten to normal author prose with claim-attached IEEE citations. No scientific content change is required for those sentences; the change is editorial and bibliographic only.
