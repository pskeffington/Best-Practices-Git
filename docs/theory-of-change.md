# Theory of Change

## Purpose

This document explains how the query-to-publication scaffold is expected to improve machine-learning research in the scientific process.

## Problem

Machine-learning studies can fail scientifically even when their code runs and their models produce strong metrics. Common failures include:

- research questions defined after model experimentation,
- unclear population or target definition,
- undocumented data provenance,
- feature construction that creates leakage,
- weak or missing baseline comparison,
- validation designs that do not support the final claim,
- incomplete ethics and use-boundary review,
- reproducibility materials assembled only after manuscript drafting,
- publication claims that exceed the evidence chain.

These problems are workflow failures as much as technical failures.

## Intervention

The scaffold introduces a staged, version-controlled workflow:

```text
Query -> Protocol -> Data audit -> Feature plan -> Modeling plan -> Validation plan -> Result bundle -> Ethics review -> Reproducibility package -> Manuscript -> Submission
```

Each stage produces an artifact that can be reviewed before the next stage proceeds.

## Mechanism

The scaffold improves ML scientific practice through five mechanisms.

### 1. Sequencing

The workflow forces researchers to frame the question and protocol before model selection dominates the project.

### 2. Visibility

Research decisions become visible artifacts rather than hidden assumptions inside code, notebooks, or memory.

### 3. Traceability

Manuscript claims are linked back to evidence sources, validation checks, and claim boundaries.

### 4. Reviewability

Collaborators and reviewers can inspect the chain from design to claim rather than only reading the final manuscript.

### 5. Reproducibility

The repository preserves the environment, data documentation, artifact manifest, and manuscript source needed for future inspection.

## Expected outputs

The scaffold should produce:

- clearer research questions,
- better documented protocols,
- earlier detection of leakage risks,
- stronger baseline comparisons,
- validation designs aligned with claims,
- more precise limitation language,
- reproducibility packages built during research rather than after submission,
- manuscripts that are easier to review and revise.

## Expected scholarly contribution

The theory of change supports the manuscript's main claim: reproducible machine-learning science requires a workflow layer that links scientific reasoning, technical execution, reporting standards, and manuscript production.

## Boundary conditions

The scaffold is most useful for ML studies that aim to produce publishable empirical research. It is less useful for purely exploratory notebooks, production-only engineering systems, or theoretical ML papers where the primary contribution is mathematical or algorithmic.
