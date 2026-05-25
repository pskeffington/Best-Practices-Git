# Best Practices Git

A publishable-manuscript workflow repository for using machine learning responsibly, reproducibly, and transparently from research query to publication.

## Purpose

This repository is organized around a full scholarly production pipeline:

1. Frame a research query that is specific, testable, and literature-grounded.
2. Convert the query into a reproducible machine-learning study design.
3. Document data provenance, preprocessing, model development, validation, and limitations.
4. Produce a publication-ready manuscript with transparent methods and review checklists.
5. Preserve all artifacts required for peer review, replication, and future extension.

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

## Recommended workflow

Create a branch for each manuscript stage:

```bash
git checkout -b query/research-question
git checkout -b methods/ml-protocol
git checkout -b manuscript/full-draft
git checkout -b review/revision-cycle-1
```

Each merge should pass the relevant checklist in `checklists/query-to-publish.md`.

## Manuscript thesis

Working title:

> From Query to Publication: Best Practices for Publishable Machine-Learning Manuscripts

The manuscript is designed as a best-practices article for researchers using machine learning in empirical, policy, public health, social science, intelligence, or operational research settings.

## Status

Initial scaffold. The next milestone is to expand the manuscript sections and populate the bibliography with verified sources.