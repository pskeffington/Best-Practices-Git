# Grant Writing Standard

_Last updated: 2026-10-07_

This standard governs grant drafting in Best-Practices-Git. It is intentionally stricter than a generic prose generator.

## 1. Authority hierarchy

When instructions conflict, use the most specific current source:

1. current law/policy notices and sponsor-wide notices;
2. the live funding opportunity / solicitation;
3. current sponsor application guide;
4. institutional sponsored-research requirements;
5. Best-Practices sponsor profile;
6. generated scaffold.

The compiler never overrides a live opportunity.

## 2. Before drafting

A proposal may enter drafting only when the following are known:

- authoritative opportunity URL;
- sponsor and mechanism;
- applicant route and eligibility;
- deadline or confirmed rolling status;
- award period and budget frame;
- required partners or prime/subaward structure;
- project thesis and current evidence package;
- unresolved hard gates.

For high-value research proposals, also create:

- literature/evidence matrix;
- competing/funded-project landscape where available;
- aims/objectives architecture;
- claims-aims-evidence-risk matrix;
- preliminary budget-to-work map.

## 3. Aims and objectives

For NIH-style research proposals, the Specific Aims page should establish:

1. **Problem** — the important scientific, clinical, service, implementation, or technical problem.
2. **Gap** — what is not known or not working and why that gap blocks progress.
3. **Overall objective** — what the project will accomplish within the award period.
4. **Central hypothesis or premise** — the proposition that organizes the work.
5. **Aims** — usually two to four bounded objectives, scaled to the mechanism.
6. **Expected outcomes** — what new knowledge, capability, evidence, or system improvement will exist.
7. **Impact** — why those outcomes matter after the project ends.

### Aim quality rules

Each aim should:

- begin with an action-oriented objective;
- have a measurable endpoint or acceptance criterion;
- produce a useful result even if the preferred hypothesis or implementation path fails;
- avoid total dependence on success of the prior aim;
- map to methods, personnel, timeline, budget, risk, and deliverable;
- avoid being merely a list of experiments.

## 4. Significance / need

A strong significance section moves in this order:

`important problem -> current evidence -> precise gap -> consequence of gap -> proposed contribution -> likely impact`

Rules:

- quantify need only with verified evidence;
- distinguish prevalence/burden from evidence that the proposed intervention works;
- explain why the gap matters to the sponsor's mission;
- do not use generic statements such as "this is a major problem" without an evidence anchor.

## 5. Innovation

Innovation may be:

- conceptual;
- methodological;
- technical;
- implementation/workflow;
- integration of existing methods in a new context.

Routine software development is not automatically innovation.

State:

1. what current practice does;
2. what this proposal changes;
3. why that difference matters for the expected result.

## 6. Approach

Organize the approach around aims/objectives or sponsor-required workstreams.

For each:

- rationale;
- design/activity;
- population/data/source;
- variables/endpoints;
- analysis/evaluation;
- responsible roles;
- milestones;
- feasibility evidence;
- major risks;
- alternative strategies;
- expected result;
- interpretation;
- deliverable.

### Feasibility rule

Every material promise should have at least one feasibility anchor:

- preliminary data;
- prior implementation;
- published evidence;
- partner capability;
- validated technical component;
- bounded scope;
- explicit pilot milestone.

## 7. Reviewer-first drafting

Draft for the actual review criteria.

Create a crosswalk before final prose:

| Criterion | Proposal location | Evidence | Weakness/gap | Status |
|---|---|---|---|---|

For point-scored opportunities, mirror the sponsor's scoring order unless there is a strong reason not to.

### NIH research project grants under the Simplified Review Framework

Primary review logic:

- **Factor 1 — Importance of the Research:** Significance + Innovation.
- **Factor 2 — Rigor and Feasibility:** Approach.
- **Factor 3 — Expertise and Resources:** sufficiency of investigators/environment for the proposed work.

Do not use an obsolete five-independent-score mental model for an SRF-covered application.

### NSF

Explicitly cover:

- Intellectual Merit;
- Broader Impacts.

Broader Impacts should identify actual activities, beneficiaries/participants, responsible roles, milestones, and evaluation rather than a generic societal-benefit paragraph.

### SAMHSA and other point-scored NOFOs

Use the exact current NOFO headings and make every scored criterion easy to locate.

## 8. Budget-to-work consistency

Every significant budget line should answer:

- what work does it support?
- who owns that work?
- when is it needed?
- what output does it enable?

Every significant work package should answer:

- which budget category supports it?
- what level of effort is required?
- does a partner/subaward own part of it?
- is the cost allowable under the current opportunity?

The compiler should flag orphaned work and orphaned budget lines.

## 9. Citation and evidence controls

Never invent references.

Every substantive factual claim should resolve to one of:

- a verified literature citation;
- a sponsor policy/instruction source;
- a project dataset;
- a documented preliminary result;
- a partner-provided fact with provenance.

Maintain retrieval/review dates for sponsor requirements and time-sensitive program facts.

## 10. Plain language and readability

Use:

- topic sentences;
- short paragraphs;
- active voice;
- consistent terminology;
- acronyms expanded on first use in each standalone attachment;
- headings that let reviewers find required information quickly.

Technical precision belongs in the Research Strategy/Project Description. Titles, abstracts, public-health relevance statements, and executive summaries should remain understandable to an educated non-specialist audience.

## 11. Multi-pass review

Run separate passes rather than one undifferentiated review:

1. eligibility/compliance;
2. aims/objectives architecture;
3. literature and significance;
4. innovation;
5. rigor/methods/feasibility;
6. citations and claim verification;
7. budget/timeline/team consistency;
8. readability and terminology;
9. final panel-style review.

Each finding should contain:

- evidence anchor;
- problem;
- likely reviewer impact;
- recommended revision;
- verification method;
- severity.

## 12. Submission boundary

Generated text is never submission-ready by default.

Before submission:

- re-open the live opportunity;
- verify current forms and page limits;
- verify eligibility and registrations;
- resolve all placeholders;
- verify citations;
- verify partner commitments and letters;
- verify budget and institutional approvals;
- run the deterministic linter;
- run reviewer-criteria review;
- obtain human approval.

## 13. Funded-project handoff

At award activation:

`proposal aims -> final protocol -> data provenance -> analysis/evaluation -> validation -> limitations -> manuscript -> dissemination`

The grant should become the first controlled artifact in the manuscript audit trail, not a document that is discarded after funding.
