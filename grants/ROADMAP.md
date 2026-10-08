# Automated Grant Drafting — Gated Milestone Roadmap

_Last updated: 2026-10-07_

## Operating rule

Automated grant drafting advances by **evidence-backed gates**, not by the amount of prose generated.

A gate advances only when:

1. required artifacts exist;
2. source and sponsor instructions are current;
3. deterministic checks pass;
4. unresolved eligibility, evidence, regulatory, partner, or budget constraints are explicit;
5. the next gate does not require the system to invent facts, commitments, citations, or scientific evidence.

A polished draft alone never satisfies a gate.

## Current system status

**Overall:** **G8 IN PROGRESS / G8.3 NEXT**

Current automated path:

`opportunity registry -> freshness gate -> sponsor profile -> proposal architecture -> draft packet -> deterministic lint -> specialist review packets -> review PR`

Current human-controlled path:

`specialist review -> revision -> institutional review -> submission -> award activation -> manuscript pipeline`

---

# G0 — Pipeline foundation

**Status:** PASS

## Objective

Establish a shared grant-compilation layer inside Best-Practices-Git.

## Required artifacts

- portfolio-level grant directory;
- source-repository handoff contract;
- daily/manual GitHub Actions workflow;
- generated-draft output area;
- pull-request review boundary.

## Exit criteria

- source repositories remain authoritative for opportunity facts;
- Best-Practices-Git is the drafting/compiler layer;
- generated proposal changes arrive through reviewable Git history;
- automation cannot silently submit an application.

## Evidence

- `grants/README.md`
- `grants/pipeline-config.json`
- `.github/workflows/grant-draft-pipeline.yml`

---

# G1 — Opportunity intake and admission control

**Status:** PASS

## Objective

Prevent stale, low-fit, expired, or structurally unresolved opportunities from entering the drafting queue.

## Required inputs

- opportunity ID;
- sponsor;
- mechanism;
- authoritative source;
- source review date;
- status;
- fit score;
- applicant route;
- eligibility description;
- deadline or rolling-status explanation;
- hard gates.

## Current admission rules

An opportunity is draft-eligible only when:

- freshness is within the configured window;
- deadline has not passed;
- status is draft-enabled;
- strategic fit meets threshold;
- applicant route is present;
- eligibility description is present;
- source URL is present;
- no explicit `draftHold` is set.

## Exit criteria

- stale opportunity cannot silently enter drafting;
- expired opportunity cannot silently enter drafting;
- high strategic fit cannot override eligibility;
- held opportunities remain visible without becoming proposals.

## Evidence

- source-repository opportunity registries;
- source-repository freshness checks;
- `grants/pipeline-config.json`;
- `scripts/build-grant-drafts.py`.

---

# G2 — Freshness and authoritative-source control

**Status:** PASS

## Objective

Make sponsor and opportunity freshness a prerequisite for drafting.

## Required controls

- source review date;
- authoritative source URL;
- deadline validation;
- live-source reachability signal;
- scheduled re-check cadence;
- fail/hold behavior for stale metadata.

## Exit criteria

- source registries fail freshness policy when stale;
- passed deadlines are detected;
- source failures generate visible warnings;
- live sponsor instructions remain authoritative over cached profile rules.

## Evidence

- daily freshness workflows in source repositories;
- source review metadata;
- Best-Practices authority hierarchy.

---

# G3 — Sponsor-profile binding

**Status:** PASS

## Objective

Stop treating every grant as the same document.

## Current profiles

- NIH research project grants / Simplified Review Framework;
- NIH SBIR/STTR;
- NSF research proposals;
- SAMHSA discretionary grants;
- generic research/foundation fallback.

## Required profile fields

- section order;
- required sections;
- required signals;
- review framework;
- page-rule metadata;
- sponsor-specific writing rules;
- authoritative sponsor sources.

## Exit criteria

- compiler resolves a profile for every admitted opportunity;
- live opportunity can override profile assumptions;
- unknown profile cannot silently proceed as a known mechanism;
- reviewer criteria are available to downstream validation.

## Evidence

- `grants/sponsor-profiles.json`
- `grants/WRITING_STANDARD.md`

---

# G4 — Evidence and landscape assembly

**Status:** IN PROGRESS

## Objective

Automatically assemble the evidence package required to justify need, gap, feasibility, novelty, and sponsor fit before substantive prose generation.

## Completed

- [x] grant-writing literature review;
- [x] sponsor guidance review;
- [x] open-source grant compiler review;
- [x] evidence/citation rules encoded;
- [x] funded-project landscape identified as a required pre-draft control.

## Required next artifacts

- [ ] project evidence-manifest schema;
- [ ] structured literature matrix ingestion;
- [ ] preliminary-data manifest ingestion;
- [ ] partner-fact provenance manifest;
- [ ] funded-project / prior-award search adapter;
- [ ] evidence freshness field;
- [ ] claim -> source resolver;
- [ ] unsupported-claim hold state.

## Exit criteria

- every material factual claim can resolve to a source class;
- preliminary-data claims point to a project artifact;
- current related/funded work can be summarized when relevant;
- missing evidence blocks claim promotion instead of inviting invented prose.

## Target output

`grants/generated/<project>/<opportunity>/evidence-manifest.json`

---

# G5 — Aims / objectives architecture

**Status:** PASS FOR SCAFFOLD / IN PROGRESS FOR AUTO-COMPOSITION

## Objective

Make aims or scored objectives the controlling structure of the proposal.

## Completed

- [x] NIH aims scaffold;
- [x] problem -> gap -> objective -> premise -> aims -> outcomes -> impact structure;
- [x] claims-aims-evidence-risk matrix;
- [x] aim count warning logic;
- [x] risk / alternative-strategy expectations;
- [x] budget-owner column;
- [x] reviewer crosswalk.

## Required next capabilities

- [ ] derive candidate aims from project evidence rather than generic placeholders;
- [ ] aim-dependency graph;
- [ ] over-scope detection;
- [ ] aim-to-budget coverage score;
- [ ] aim-to-team-role coverage score;
- [ ] aim-to-endpoint coverage score;
- [ ] null-result usefulness check;
- [ ] automatic structural review before prose generation.

## Exit criteria

- no full narrative is generated until architecture passes;
- each aim has a measurable endpoint;
- each aim has evidence, risk, alternative, deliverable, timeline, and budget ownership;
- excessive aim dependence is flagged;
- scope is mechanism-appropriate.

---

# G6 — Sponsor-aware deterministic draft generation

**Status:** PASS

## Objective

Generate a structured proposal packet without fabricating unresolved facts.

## Current generated content

- provenance header;
- sponsor profile;
- applicant structure;
- sponsor-specific drafting order;
- aims/objectives scaffold;
- claims-aims-evidence-risk matrix;
- reviewer crosswalk;
- sponsor section requirements;
- approach integration rules;
- blockers;
- budget alignment;
- human-subjects/regulatory boundary;
- citation controls;
- manuscript handoff;
- pre-submission controls.

## Exit criteria

- unknown facts remain placeholders or blockers;
- sponsor-specific sections are explicit;
- generated packet is reproducible from registry + profile inputs;
- drafting output remains reviewable Markdown;
- no submission action is performed.

## Evidence

- `scripts/build-grant-drafts.py`

---

# G7 — Deterministic lint and compliance precheck

**Status:** PASS

## Objective

Catch structural problems before expensive or subjective review.

## Current checks

- authoritative source present;
- source review date present;
- required sponsor sections present;
- NIH Specific Aims presence and aim-count sanity;
- NIH gap/objective/outcome/impact/premise signals;
- NSF Project Summary signals;
- reviewer crosswalk present;
- claims/evidence/risk matrix present;
- risk language present;
- alternative-strategy language present;
- milestone/timeline language present;
- unresolved placeholders;
- budget surface;
- evidence/citation traceability surface.

## Exit criteria

- deterministic errors fail the automated drafting workflow;
- warnings are preserved for review;
- lint report is stored with generated drafts;
- linter validates proposal headings rather than only metadata labels.

## Evidence

- `scripts/grant_lint.py`
- `grants/generated/lint-report.json` on automated runs.

---

# G8 — Specialist automated review

**Status:** IN PROGRESS — REVIEW CONTRACT + PACKET/AGGREGATION RUNNERS COMPLETE

## Objective

Add independent reviewer passes that critique the draft from distinct perspectives rather than using one generic review prompt.

## Completed

- [x] machine-readable reviewer result schema;
- [x] severity taxonomy;
- [x] PASS / REVISE / HOLD contract;
- [x] nine specialist reviewer profiles;
- [x] immutable draft SHA-256 in review packets;
- [x] review packet generator;
- [x] scheduled review-packet artifact generation;
- [x] structured review-result validator;
- [x] same-draft / same-profile aggregation guard;
- [x] duplicate-reviewer detection;
- [x] missing-reviewer detection;
- [x] consolidated Markdown + JSON synthesis.

## Remaining

- [ ] **G8.3 model/provider invocation adapter**;
- [ ] record model/provider/version and prompt/response hashes;
- [ ] retry/error policy;
- [ ] panel reviewer runs only after focused review set is complete;
- [ ] automatic CI ingestion of reviewer JSON outputs;
- [ ] criterion-coverage threshold by sponsor profile;
- [ ] cost/token telemetry where supported.

## Required review agents / passes

1. eligibility and compliance;
2. aims/objectives architecture;
3. significance and literature positioning;
4. innovation;
5. methods, rigor, and feasibility;
6. citations and claim verification;
7. budget, timeline, and team consistency;
8. plain-language/readability;
9. final panel-style review.

## Standard review finding

Every finding must include:

- evidence anchor;
- issue;
- likely reviewer impact;
- severity;
- recommended revision;
- verification method;
- funding-constraint note where relevant.

## Required outputs

- machine-readable review JSON;
- human-readable review Markdown;
- consolidated revision queue;
- severity counts;
- criterion coverage score;
- explicit PASS / REVISE / HOLD result.

## Exit criteria

- reviewer passes are independent and reproducible;
- no review pass silently edits scientific facts;
- final panel review uses current sponsor criteria;
- high-severity findings block promotion.

---

# G9 — Controlled revision loop

**Status:** NOT STARTED

## Objective

Turn review findings into traceable revisions without uncontrolled recursive rewriting.

## Required controls

- draft version ID;
- parent version;
- finding IDs addressed;
- before/after section hash;
- revision rationale;
- unresolved findings;
- maximum automated revision rounds;
- human stop/approve control.

## Proposed rule

Automated revision may improve:

- organization;
- clarity;
- criterion coverage;
- explicitness;
- consistency;
- wording.

Automated revision may not independently change:

- preliminary results;
- scientific conclusions;
- eligibility assertions;
- partner commitments;
- regulatory classification;
- budget totals;
- named personnel commitments.

## Exit criteria

- every revision maps to a review finding;
- new claims trigger evidence review;
- resolved findings are verifiable;
- revision loop cannot run indefinitely;
- human approval is required before submission-packaging gate.

---

# G10 — Budget / effort / timeline compiler

**Status:** NOT STARTED

## Objective

Make narrative scope, personnel effort, milestones, and budget mutually consistent.

## Required objects

- work-package registry;
- personnel-role registry;
- effort table;
- partner/subaward scopes;
- direct-cost categories;
- indirect-cost rule;
- milestone timeline;
- deliverable schedule.

## Automated checks

- orphaned work package;
- orphaned budget line;
- named role with zero effort;
- effort with no work ownership;
- milestone outside award period;
- work package with no deliverable;
- partner work with no subaward/role treatment;
- budget category conflicting with sponsor rules.

## Exit criteria

- each major work package has budget ownership;
- each major budget line has narrative purpose;
- timeline fits award period;
- generated budget narrative is derived from structured budget objects.

---

# G11 — Submission packet assembly

**Status:** NOT STARTED

## Objective

Compile sponsor-ready attachment sets while preserving a human-controlled submission boundary.

## Target capabilities

- attachment manifest;
- Markdown -> DOCX/PDF/LaTeX rendering as appropriate;
- sponsor-specific file naming;
- page-count checks;
- attachment checklist;
- bibliography build;
- figures/tables manifest;
- form/portal handoff checklist;
- final immutable submission snapshot.

## Hard boundary

The system may prepare files. It must not autonomously certify institutional approval or submit an application.

## Exit criteria

- required narrative attachments compile;
- page/attachment checks pass;
- unresolved placeholders are zero;
- final lint/review result is PASS;
- institutional review status is explicit;
- human approval is recorded.

---

# G12 — Institutional / partner readiness

**Status:** BLOCKED BY EXTERNAL ACTION

## Objective

Track items automation cannot truthfully manufacture.

## Typical external dependencies

- principal investigator confirmation;
- sponsored-research approval;
- SAM/UEI/Grants.gov/eRA or other registrations;
- subrecipient commitment;
- partner letters;
- facilities/resources attestations;
- institutional indirect-cost treatment;
- human-subjects determination;
- data-use agreements;
- authorized representative approval.

## Exit criteria

- every external requirement has an owner;
- evidence of completion is linked;
- no generated language substitutes for a real commitment.

---

# G13 — Submission readiness decision

**Status:** LOCKED

## Objective

Produce a defensible GO / REVISE / HOLD decision.

## GO requires

- G0-G11 passed;
- G12 external requirements satisfied;
- zero deterministic errors;
- zero unresolved critical reviewer findings;
- current opportunity re-verified;
- budget reconciled;
- citations verified;
- required attachments present;
- institutional approval complete;
- final human review complete.

## Output

`submission-readiness.json`

Recommended fields:

- opportunity;
- profile;
- sourceVerifiedAt;
- lint status;
- reviewer status;
- unresolved critical findings;
- institutional status;
- partner status;
- budget status;
- attachment status;
- decision;
- decision owner;
- decision timestamp.

---

# G14 — Award activation and manuscript handoff

**Status:** SCAFFOLDED

## Objective

Ensure the grant becomes the first controlled artifact in the research/manuscript audit trail.

## Handoff

`funded aims -> award conditions -> final protocol -> data provenance -> analysis/evaluation -> validation -> limitations -> manuscript -> dissemination`

## Required outputs

- funded-aims snapshot;
- award-condition register;
- protocol version;
- deviations log;
- endpoint/analysis registry;
- grant-to-manuscript claim map.

## Exit criteria

- funded work can be traced back to the submitted proposal;
- protocol deviations are visible;
- manuscript claims can be traced through actual data/evidence;
- grant language is not reused as if it were post-award evidence.

---

# Milestone progression

| Milestone | Gate | Status | Unlocks |
|---|---|---|---|
| M0 Compiler foundation | G0 | PASS | automated intake |
| M1 Admission/freshness | G1-G2 | PASS | trusted drafting queue |
| M2 Sponsor binding | G3 | PASS | mechanism-specific drafting |
| M3 Evidence assembly | G4 | IN PROGRESS | evidence-grounded auto-composition |
| M4 Aims architecture | G5 | PARTIAL PASS | structured narrative generation |
| M5 Draft compiler | G6 | PASS | reproducible proposal packets |
| M6 Deterministic QA | G7 | PASS | safe automated review entry |
| M7 Specialist review | G8 | IN PROGRESS | review contract/queue active; model execution next |
| M8 Revision engine | G9 | NOT STARTED | iterative improvement |
| M9 Budget/timeline compiler | G10 | NOT STARTED | full application coherence |
| M10 Submission assembler | G11 | NOT STARTED | sponsor-ready attachment package |
| M11 External readiness | G12 | EXTERNAL | final submission decision |
| M12 GO/HOLD decision | G13 | LOCKED | submission |
| M13 Award handoff | G14 | SCAFFOLDED | protocol/manuscript continuity |

## Immediate next development queue

Priority order:

1. **G8.3 — model/provider review adapter**
   - invoke one specialist packet at a time;
   - require structured JSON output;
   - record provider/model/version;
   - record packet and response hashes;
   - enforce focused-review completion before panel synthesis.

2. **G8.4 — CI review ingestion**
   - validate specialist results;
   - aggregate reviewer findings;
   - expose PASS / REVISE / HOLD in generated PR;
   - block promotion on critical/HOLD findings.

3. **G4.1 — evidence manifest**
   - structured evidence object;
   - source class;
   - retrieval/review date;
   - claim linkage.

4. **G5.1 — aim coverage scoring**
   - evidence;
   - endpoint;
   - risk;
   - alternative;
   - deliverable;
   - budget;
   - owner.

5. **G9.1 — versioned revision ledger**
   - parent draft;
   - finding resolution;
   - section hashes;
   - unresolved findings.

6. **G10.1 — structured budget/work model**
   - work package;
   - role;
   - effort;
   - cost;
   - milestone;
   - deliverable.

## North-star rule

The grant system should optimize for **defensible, reviewable, evidence-grounded proposal assembly**, not maximum prose generation.

The compiler should become increasingly automatic at gathering, structuring, checking, and formatting information while remaining increasingly strict about the places where human scientific, institutional, financial, and ethical judgment is required.
