# Best Practices Git

A publishable-manuscript workflow repository for using machine learning responsibly, reproducibly, and transparently from research query to publication.

**Maintainer:** Paul Skeffington, MS, MPH  
**Repository status:** active best-practices scaffold and reusable documentation standard for science-based Git repositories.  
**Last documentation refresh:** 2026-05-25

## Purpose

This repository is organized around a full scholarly production pipeline:

1. Frame a research query that is specific, testable, and literature-grounded.
2. Convert the query into a reproducible machine-learning or quantitative study design.
3. Document data provenance, preprocessing, model development, validation, and limitations.
4. Produce a publication-ready manuscript with transparent methods and review checklists.
5. Preserve all artifacts required for peer review, replication, audit, and future extension.

## Scope

This repo is not only a manuscript workspace. It is the reusable standards repository for research projects that need clear documentation, reproducible code, source verification, and defensible publication workflows.

It is especially suited for:

- Public health and epidemiology projects.
- Environmental-health and GIS workflows.
- Health-services and policy analyses.
- Machine-learning manuscripts.
- Open-data science projects.
- Research repositories that require peer-review-ready audit trails.

## Repository map

```text
.
├── manuscript/              # LaTeX manuscript source
│   ├── main.tex
│   └── sections/
├── docs/                    # Workflow guidance and editorial standards
├── checklists/              # Query-to-publication review gates
├── templates/               # Reusable manuscript and reporting templates
├── src/best_practices_git/  # Object-oriented workflow helpers
├── tests/                   # Lightweight validation tests
├── references/              # Bibliography and source notes
└── artifacts/               # Generated manuscript outputs; not committed by default
```

## Recommended branch workflow

Create a branch for each manuscript or documentation stage:

```bash
git checkout -b query/research-question
git checkout -b methods/ml-protocol
git checkout -b data/source-registry
git checkout -b manuscript/full-draft
git checkout -b review/revision-cycle-1
```

Each merge should pass the relevant checklist in `checklists/query-to-publish.md` or the nearest project-specific review gate.

## Documentation standard for science repositories

A science-based repository should make the following objects explicit before results are treated as manuscript-ready:

- Research question, estimand or analytic target, and intended contribution.
- Data-source registry with access route, retrieval date, geography, years, variables, and license or redistribution constraints.
- Reproducible environment instructions.
- Raw-data exclusion policy and `.gitignore` coverage.
- Analysis workflow map from source extraction to tables, figures, diagnostics, and manuscript claims.
- Citation-verification log with DOI, source URL, version, retrieval date, and manuscript role.
- Validation checks for derived variables, denominators, model inputs, and reported outputs.
- Clear status language distinguishing scaffold, exploratory analysis, validated outputs, and publication-ready findings.

## Manuscript thesis

Working title:

> From Query to Publication: Best Practices for Publishable Machine-Learning Manuscripts

The manuscript is designed as a best-practices article for researchers using machine learning in empirical, policy, public health, social science, intelligence, or operational research settings.

## Practical review gates

Before a project leaves scaffold status, confirm that:

- The README states the research purpose, data boundaries, and current status.
- Source files and derived outputs are separated.
- No restricted, sensitive, or unclear-license raw data are committed.
- The project has a reproducible execution path or a documented reason why automation is not yet possible.
- Manuscript claims are traceable to code, tables, source files, or verified citations.
- Limitations are documented before drafting conclusions.

## Next execution steps

1. Expand `checklists/query-to-publish.md` into modular review gates for query, methods, data, modeling, manuscript, and submission stages.
2. Add reusable README templates for public-health, GIS, machine-learning, and manuscript-only repositories.
3. Add a citation-verification template and source-registry template.
4. Add lightweight tests for repository structure, required documentation files, and raw-data exclusion rules.
5. Convert the manuscript outline into LaTeX sections with verified references.

## Status

Documentation refreshed on 2026-05-25. The repository now serves as the best-practices standard for current science and manuscript repositories while the article scaffold continues to develop.
