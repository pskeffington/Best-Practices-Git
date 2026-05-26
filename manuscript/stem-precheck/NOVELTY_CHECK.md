# Novelty Check: Claim Auditability Target

## Core target

The manuscript should target **auditability of manuscript claims**.

The central contribution is not generic peer-review automation, manuscript grading, plagiarism detection, reference checking, or reporting-checklist completion. The target is a pre-review audit trail that makes each major scientific claim inspectable by authors, editors, reviewers, and publishers.

## Claim-audit object

```text
Claim
  -> claim level
  -> manuscript location
  -> evidence artifact
  -> method support
  -> validation or justification
  -> boundary language
  -> reproducibility support
  -> reviewer finding
  -> editorial status
```

## Adjacent work identified

### Peerispect

Peerispect focuses on claim verification in scientific peer reviews. It extracts check-worthy claims from peer-review text, retrieves evidence from the manuscript, and verifies whether reviewer statements are grounded in the paper.

**Difference:** Peerispect audits claims made by reviewers. Our framework audits claims made by manuscript authors before peer review.

### FactReview

FactReview is an evidence-grounded reviewing system for machine-learning papers. It extracts major claims and reported results, performs literature positioning, and can execute released code to test empirical claims when code is available.

**Difference:** FactReview focuses on AI-assisted review generation and ML claim verification. Our framework is a discipline-aware STEM pre-check artifact for authors, editors, reviewers, and publishers, with the claim audit trail as the submission object.

### WarrantScore

WarrantScore evaluates whether claims in peer-review comments are substantiated by evidence and whether the logical warrant between claim and evidence is strong.

**Difference:** WarrantScore evaluates peer-review comments. Our framework evaluates manuscript claims and publisher submission readiness.

### OpenNovelty

OpenNovelty evaluates scholarly novelty by extracting task and contribution claims, retrieving related work, and producing evidence-backed novelty reports.

**Difference:** OpenNovelty focuses on novelty assessment. Our framework focuses on claim auditability, evidence mapping, methodological support, boundary language, and editorial pre-check status.

### Reporting checklists and transparency policies

PRISMA, TOP-style transparency guidance, reproducibility checklists, and publisher reporting policies improve disclosure and transparency.

**Difference:** These usually specify what should be disclosed. Our framework organizes disclosures around the claim as the audit unit.

## Novelty position

The strongest defensible novelty claim is:

> Existing systems increasingly verify reviewer comments, automate review support, assess novelty, or check reporting guideline adherence. This framework instead proposes a claim-to-evidence audit trail for STEM manuscripts as an author/editor-facing pre-review artifact. Its unit of analysis is the manuscript claim, and its purpose is claim auditability before peer review.

## Revised manuscript target language

Use this phrase consistently:

> claim auditability

Recommended title refinement:

> Claim Auditability in STEM Manuscripts: A Claim-to-Evidence Audit Trail for Pre-Review Validation

## Contribution boundary

Do not claim:

- no one has worked on claim verification,
- no one has built AI review tools,
- no one has proposed reporting checklists,
- no one has studied evidence support in peer review.

Do claim:

- the manuscript contributes a claim-audit artifact for author/editor pre-review validation,
- the framework centers manuscript claims rather than reviewer comments,
- the framework links claims to evidence, methods, validation, boundary language, and reproducibility support,
- the framework is designed as a reviewer-readable and publisher-ingestible submission artifact.

## Publishability implication

The paper is strongest when framed as a metascience and publishing-infrastructure contribution:

> a structured pre-review artifact for making scientific claims auditable before reviewers are asked to evaluate them.
