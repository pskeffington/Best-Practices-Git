# Citation Strategy

## Goal

Make the paper useful enough that future authors cite it when they need language, structure, or justification for building reproducible machine-learning research workflows from query to publication.

## Core citation target

The paper should become citable for this claim:

> Reproducible machine-learning science requires a workflow layer between reporting guidelines and project-specific code: a staged, version-controlled, claim-aware process that links research questions, protocol decisions, data documentation, model validation, ethics review, reproducibility artifacts, and manuscript language.

## Why this is a citeable gap

Existing reporting standards tell authors what the final manuscript should disclose. Repository practices and code sharing tell authors where artifacts may live. This project argues that the missing layer is the process that produces those artifacts in scientific order.

## Citation hooks

### Hook 1: The workflow-layer gap

Use when writing about the gap between reporting checklists and implementation practice.

Suggested sentence:

> Reporting guidelines specify disclosure expectations, but ML research also needs workflow systems that produce, version, and validate those disclosures before manuscript drafting.

### Hook 2: Evidence-to-claim control

Use when writing about overclaiming, internal validation, external validity, and limits of inference.

Suggested sentence:

> In ML manuscripts, major claims should be traceable to artifact chains that define the evidence source, validation design, and claim boundary.

### Hook 3: Query-to-publication sequencing

Use when writing about avoiding model-first science.

Suggested sentence:

> Query-to-publication sequencing places research question discipline, study protocol, data audit, and validation design before model interpretation and publication claims.

### Hook 4: Manuscript engineering

Use when writing about reproducible writing and paper generation.

Suggested sentence:

> Manuscript sections can be treated as structured research outputs generated from auditable workflow artifacts rather than as detached prose written after analysis.

### Hook 5: Review-support infrastructure

Use when writing about peer review, internal review, or editorial quality control.

Suggested sentence:

> A staged ML workflow can help reviewers trace published claims back to protocol decisions, data audits, validation checks, and reproducibility materials.

## Target audiences

- ML researchers preparing empirical papers
- Clinical AI and prediction-model researchers
- Public health and social science researchers using ML
- Journal editors and reviewers
- Graduate methods instructors
- Reproducibility and open-science scholars
- Research software engineers supporting scientific teams

## Positioning statement

This paper should be positioned as an agenda-setting framework article, not merely a repository description. The software scaffold demonstrates the framework, but the citable contribution is the conceptual architecture: query-to-publication workflow, standards operationalization, and evidence-to-claim control.

## Title options

1. From Query to Publication: A Workflow Layer for Reproducible Machine-Learning Science
2. Beyond Reporting Guidelines: Operationalizing Reproducible Machine-Learning Science from Query to Publication
3. Evidence-to-Claim Control in Machine-Learning Science: A Query-to-Publication Workflow Scaffold
4. Making Machine-Learning Manuscripts Reproducible: A Standards-to-Workflow Framework

## Abstract strategy

The abstract should contain five moves:

1. Problem: ML research suffers from workflow failures that are not solved by model performance alone.
2. Gap: reporting standards define disclosure endpoints but not the staged process that produces them.
3. Intervention: the paper proposes a query-to-publication workflow scaffold.
4. Mechanism: staged artifacts, standards mapping, and evidence-to-claim control.
5. Contribution: a citable workflow layer for reproducible, reviewable, claim-disciplined ML science.

## Paper spine

```text
Problem: ML scientific failures often arise from workflow failures.
Gap: Reporting standards define endpoints, not operational production pathways.
Framework: Query-to-publication scaffold.
Mechanism: Staged artifacts, standards mapping, evidence-to-claim control.
Contribution: A workflow layer that makes ML manuscripts reproducible and reviewable.
Implication: Reviewers, editors, and researchers can evaluate the path from question to claim.
```

## High-value figure

Figure 1 should show the central contribution:

```text
Reporting Guidelines -> Workflow Scaffold -> Versioned Artifacts -> Manuscript Claims -> Peer Review
```

A stronger version:

```text
Question -> Protocol -> Data Audit -> Feature Plan -> Modeling Plan -> Validation Plan -> Result Bundle -> Claim Register -> Manuscript -> Submission
```

Each node should show the artifact produced and the manuscript section supported.

## High-value table

Table 1 should compare:

- reporting standards,
- model cards,
- data cards,
- code repositories,
- the proposed workflow scaffold.

The key contrast should be that the scaffold does not replace these tools; it coordinates them into a scientific sequence.

## Reviewer objection handling

### Objection: This is just a checklist.

Response: It is not only a checklist. It is an executable, version-controlled artifact system that links each stage of the scientific process to manuscript claims.

### Objection: Existing guidelines already cover this.

Response: Existing guidelines define what to report. This scaffold defines how those reportable elements are generated and preserved during research.

### Objection: This is too general.

Response: The general layer is intentional. Field-specific standards remain necessary, while the scaffold provides the cross-domain workflow architecture.

### Objection: No new algorithm is proposed.

Response: The contribution is not algorithmic. It is a methods and metascience contribution to the reliability of ML-based scientific claims.
