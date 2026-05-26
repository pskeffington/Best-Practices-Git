# Auto Pipeline Verification

## Purpose

The repository includes an automated verification layer for users who are producing machine-learning manuscripts through the query-to-publication scaffold.

The goal is to give users immediate feedback on whether their project has the minimum artifact trail needed to support a publishable manuscript.

## What the verification layer checks

### 1. Pipeline completeness

The verifier checks whether every required workflow stage exists and whether required fields are complete.

Core stages:

- Research Query
- Study Protocol
- Data Audit
- Modeling Plan
- Validation Plan
- Manuscript Package

### 2. Standards mapping

The verifier checks whether scaffold stages are mapped to reporting functions and relevant standards or documentation practices.

This supports the manuscript's standards-operationalization claim.

### 3. Claim readiness

The verifier checks whether manuscript claims have:

- claim text,
- claim level,
- valid evidence source,
- boundary note.

A claim without evidence or a boundary note is not publication-ready.

### 4. Artifact generation

The CLI can generate the expected artifact templates so the user starts with a complete scaffold.

Command:

```bash
bpg-workflow init-artifacts --root .
```

### 5. CI verification

The GitHub Actions workflow runs tests on push and pull requests to `main`. The CI currently checks:

- package installation,
- Python tests,
- workflow CLI status command,
- artifact template generation.

## User-facing value

Auto pipeline verification gives users a practical quality-control system before manuscript submission. It helps answer:

- Is the research query documented?
- Is the validation plan present?
- Are standards mapped to workflow stages?
- Are manuscript claims supported by evidence?
- Are claim boundaries stated clearly?
- Can artifact templates be generated automatically?

## Scientific contribution

This verification layer strengthens the framework's contribution by showing that the scaffold is not only conceptual. It is executable and testable.

The paper can therefore argue that reproducible machine-learning science requires automated workflow verification in addition to code availability and final-stage reporting checklists.
