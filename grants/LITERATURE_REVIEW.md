# Literature and Open-Source Review: Grant Compilers and Grant-Writing Systems

_Last reviewed: 2026-10-07_

## Purpose

This review defines the design principles for the Best-Practices-Git grant compiler. It combines:

1. current sponsor instructions and review frameworks;
2. published grantsmanship literature;
3. open-source grant/proposal tooling patterns on GitHub.

The objective is not to copy another grant-writing project. The objective is to identify durable workflow patterns that can be encoded as transparent, testable proposal-generation rules.

## Executive synthesis

The strongest pattern across official guidance, published grantsmanship literature, and open-source systems is that grant generation should be **structured around review logic rather than around free-form prose generation**.

A useful compiler therefore needs to do more than produce narrative text. It should preserve:

- the funding opportunity and instruction hierarchy;
- a project-specific evidence base;
- a clear problem/gap/solution/impact chain;
- aims or objectives that control the rest of the proposal;
- a requirement-to-section crosswalk;
- review-criterion coverage;
- budget-to-work alignment;
- milestone and risk logic;
- citation provenance;
- draft version history;
- human review before submission.

## Open-source GitHub review

### 1. UABPeriopAI/Grant_Guide

Repository: https://github.com/UABPeriopAI/Grant_Guide

Relevant pattern:

- combines NIH RePORTER search/comparison with an NIH-oriented Specific Aims drafting workflow;
- uses funded-project retrieval to position the proposed work against existing awards;
- explicitly treats generated content as a draft requiring investigator validation.

Best-Practices adoption:

- add a funded-project landscape stage before high-value NIH drafting;
- preserve a boundary between literature/award retrieval and proposal claims;
- never treat model-generated prose as verified scientific content.

### 2. camorford/grantsmith-ai

Repository: https://github.com/camorford/grantsmith-ai

Relevant architecture:

- separates organization profile, grant record, prompt construction, LLM service, and generated draft;
- maintains distinct draft types such as Letter of Intent, narrative, and budget justification;
- versions generated drafts rather than overwriting the prior draft;
- records the prompt used and generation state.

Best-Practices adoption:

- keep project facts separate from funder facts;
- generate proposal sections from typed templates;
- preserve revision lineage;
- make the exact source inputs and compiler profile visible in generated artifacts.

### 3. anlijuncn/AIGrant

Repository: https://github.com/anlijuncn/AIGrant

Relevant pattern:

- modular proposal sections;
- multiple specialist reviewer passes for language, citations, state of the art, innovation, hypothesis, methodology, research foundation, significance, and final critical review;
- consistent reviewer issue format with evidence anchor, problem, impact, revision, and verification.

Best-Practices adoption:

- do not use one monolithic "review grant" step;
- separate scientific-positioning, methods, citation, feasibility, significance, and final panel review;
- every automated critique should point to an evidence anchor and propose a verification step.

### 4. OpenGHz/academic-human-in-the-loop grant workflow

Repository: https://github.com/OpenGHz/academic-human-in-the-loop

Relevant pattern:

- literature review and novelty checking occur before proposal drafting;
- proposal architecture is designed before full prose;
- uses a claims-aims-evidence matrix;
- emphasizes independently useful aims, risk assessment, milestones, and human checkpoints;
- distinguishes the narrative arc of a grant from the narrative arc of a completed paper.

Best-Practices adoption:

- add a pre-draft architecture gate;
- create an aims/evidence/risk matrix;
- use explicit stop conditions when evidence, eligibility, or sponsor requirements are unresolved;
- connect funded work forward into the manuscript pipeline.

### 5. corybrunson/NIH-proposal-template

Repository: https://github.com/corybrunson/NIH-proposal-template

Relevant pattern:

- Markdown as the editable source format;
- Pandoc as a portable conversion layer;
- separate proposal attachments represented as top-level document sections;
- bibliography kept machine-readable.

Best-Practices adoption:

- retain Markdown as the canonical compiler output;
- keep document rendering downstream from scientific/content validation;
- preserve bibliography and citation data separately from narrative text.

### 6. Noble-Lab/nih-latex

Repository: https://github.com/Noble-Lab/nih-latex

Relevant pattern:

- proposal can be authored as one logical source while ultimately producing sponsor-specific attachment PDFs;
- proposal instructions can be kept close to the writing during drafting and excluded from final output.

Best-Practices adoption:

- support a "guidance visible" drafting mode and a clean submission mode;
- compile attachment-sized units rather than a single undifferentiated proposal.

### 7. noise-lab/nsf-template

Repository: https://github.com/noise-lab/nsf-template

Relevant pattern:

- separate source files for Project Summary, Project Description, Results from Prior NSF Support, Broader Impacts, management/timeline, data management, mentoring, facilities, and personnel;
- explicit pre-submission compliance checklist;
- current-template warning that the PAPPG and solicitation remain authoritative.

Best-Practices adoption:

- make NSF proposal components distinct compiler artifacts;
- treat Broader Impacts as a concrete workstream;
- validate required components and page-limit metadata before submission packaging.

## Published grantsmanship literature

### Specific Aims as controlling architecture

Santen et al. describe the Specific Aims page as the central summary of the scientific premise, gap, hypotheses, methods, expected outcomes, and impact. The paper emphasizes that reviewer impressions often form at this stage.

Reference:
- Santen RJ, et al. *The Jewel in the Crown: Specific Aims Section of Investigator-Initiated Grant Proposals.* Journal of the Endocrine Society. 2017. doi:10.1210/js.2017-00318.

Best-Practices rule:
- the compiler should not produce a full NIH research strategy until the aims architecture passes a structural review.

### Problem -> gap -> solution -> impact

Robertson et al. describe the Specific Aims page as a compact combination of scientific argument and persuasive framing: establish the problem, define the knowledge gap, propose a defensible solution, state aims, and show impact.

Reference:
- Robertson C, et al. *Introduction to the Specific Aims Page of a Grant Proposal.* Academic Emergency Medicine. 2018. PMID: 29608233.

Best-Practices rule:
- every aims page should expose these elements explicitly enough for a deterministic linter to find them.

### Algorithmic aims construction

A 2020 surgical grantsmanship article argues for an algorithmic approach in which the aims page previews the core review dimensions, especially the gap, central hypothesis/premise, aims, and expected impact.

Reference:
- *An algorithmic approach to an impactful specific aims page.* Surgery. 2020. PMID: 32709487.

Best-Practices rule:
- proposal generation should begin from structured fields and matrices, not from an unconstrained request to "write a grant."

## Current official sponsor guidance

### NIH

NIH advises drafting Specific Aims early, usually limiting the attachment to one page, focusing aims on goals, anticipated outcomes, and overall impact rather than merely listing experiments.

NIH's current Simplified Review Framework applies to most research project grants with due dates on or after January 25, 2025. The framework organizes review into:

1. **Importance of the Research** — Significance and Innovation;
2. **Rigor and Feasibility** — Approach;
3. **Expertise and Resources** — investigator/environment sufficiency.

The framework changes review logic more than application structure. The compiler should therefore retain conventional Significance/Innovation/Approach organization while also generating a reviewer crosswalk against the three current factors.

Authoritative sources:
- https://grants.nih.gov/grants-process/write-application/advice-on-application-sections
- https://grants.nih.gov/grants-process/write-application/general-grant-writing-tips
- https://www.grants.nih.gov/policy-and-compliance/policy-topics/peer-review/simplifying-review/framework
- https://grants.nih.gov/grants-process/write-application/how-to-apply-application-guide

### NSF

As of this review, NSF identifies PAPPG 24-1 as the current base guide, with 2026 supplements. NSF general guidance requires the proposal to communicate what will be done, why it matters, how it will be done, how success will be determined, and what benefits may result. Common research proposals include a one-page Project Summary and a Project Description typically limited to 15 pages, but the live solicitation controls.

Authoritative sources:
- https://www.nsf.gov/policies/pappg
- https://www.nsf.gov/funding/preparing-proposal
- https://www.nsf.gov/policies/pappg/24-1/ch-2-proposal-preparation

### SAMHSA

SAMHSA requires applicants to follow the current NOFO and Grants.gov forms. Its application resources emphasize complete required forms and a detailed budget/narrative aligned to SF-424A object classes for non-construction awards.

Authoritative source:
- https://www.samhsa.gov/grants/how-to-apply/forms-and-resources

## Compiler design requirements derived from the review

### A. Funder profile before prose

Every generated proposal must bind to a sponsor profile before drafting.

A profile contains:

- section order;
- required sections;
- expected signals within each section;
- current review dimensions;
- page-rule metadata;
- submission warnings;
- authoritative sources.

Implementation:
- `grants/sponsor-profiles.json`

### B. Aims-first architecture

For NIH-style research proposals:

1. problem;
2. knowledge/practice gap;
3. long-term goal or overall objective;
4. central hypothesis or premise;
5. bounded aims;
6. expected outcomes;
7. overall impact.

The aims architecture should then control:

- approach subsections;
- milestones;
- budget;
- team roles;
- risks;
- evaluation;
- eventual manuscript analysis sections.

### C. Claims-Aims-Evidence-Risk matrix

Before full proposal prose, create a matrix:

| Aim/objective | Claim or premise | Existing evidence | Proposed test/work | Risk | Alternative | Deliverable | Budget owner |
|---|---|---|---|---|---|---|---|

No high-risk aim should enter a final draft without an alternative path or explicit reason why the risk is acceptable.

### D. Criteria crosswalk

Every application should have a machine-readable crosswalk:

| Review criterion | Where answered | Evidence anchor | Status |
|---|---|---|---|
| Importance / significance | section | source or preliminary evidence | pass/gap |
| Innovation | section | comparison or technical rationale | pass/gap |
| Rigor / feasibility | section | methods, power, pilot, milestones | pass/gap |
| Expertise/resources | section | role/resource mapping | pass/gap |

For point-scored NOFOs, each scoring criterion should map to a proposal heading in the same order where practical.

### E. Budget-work consistency

The compiler should flag:

- personnel named in the approach but absent from the budget frame;
- major work packages without an identified budget category;
- budget categories with no narrative purpose;
- effort/timeline mismatches;
- partner/subaward work without an explicit scope.

### F. Multi-pass review

Use distinct review stages:

1. **eligibility/compliance**;
2. **specific aims / objectives architecture**;
3. **significance and literature positioning**;
4. **innovation**;
5. **methods, rigor, and feasibility**;
6. **citation and evidence audit**;
7. **budget and milestone consistency**;
8. **plain-language/readability**;
9. **panel-style final review**.

### G. Human-controlled submission boundary

Automation may:

- assemble verified facts;
- create section scaffolds;
- map evidence;
- draft language;
- run deterministic checks;
- produce mock-review findings.

Automation must not silently:

- invent preliminary data;
- invent partner commitments;
- invent citations;
- infer regulatory status;
- assert applicant eligibility without verification;
- alter budget numbers to make a narrative fit;
- submit an application.

## Engineering conclusion

The Best-Practices grant compiler should be treated as a **proposal build system**, not a text generator.

Its core objects are:

`opportunity -> sponsor profile -> evidence manifest -> aims/objectives matrix -> section drafts -> deterministic lint -> specialist review -> submission packet -> funded protocol -> manuscript pipeline`

This architecture preserves the strongest open-source patterns while keeping authoritative sponsor instructions and evidence provenance above model-generated prose.
