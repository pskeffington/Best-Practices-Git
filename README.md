# Best Practices Git — Biomedical Research Software Engineering

**Author: Paul Skeffington · Prepared with OpenAI**  
**Literature and documentation reviewed: 2026-10-11**

A practical, evidence-informed guide for building, reviewing, deploying and maintaining reproducible biomedical research software with Git and GitHub. The workflow covers exploratory analysis, R/Python pipelines, machine learning, figures, research manuscripts and public-facing scientific applications.

The organizing principle is **traceability from question to claim**: a scientific result should be attributable to a defined input, documented transformation, code revision, validated environment and explicit review decision. Git provides version history; research design, tests and human review give that history scientific meaning.

## Reading routes

| Reader goal | Start |
| --- | --- |
| Launch a research repository | [1. Scaffold with intent](#1-scaffold-with-intent) |
| Choose a branch, pull-request and merge model | [2. Govern change](#2-govern-change) |
| Build safe GitHub Actions workflows | [3. Validate every change](#3-validate-every-change) |
| Release a web application or research service | [4. Deploy in stages](#4-deploy-in-stages) |
| Build biomedical ML with reproducible evidence | [5. Connect the software lifecycle to the scientific lifecycle](#5-connect-the-software-lifecycle-to-the-scientific-lifecycle) |
| Find peer-reviewed foundations and authoritative standards | [Literature and standards matrix](#literature-and-standards-matrix) |
| Adopt quality gates immediately | [Acceptance checklist](#acceptance-checklist) |

## The integrated research-to-release workflow

A research project starts with a question, not a deployment target. State the population or sample, outcome, intended analysis, data rights and validation approach first. Then establish a version-controlled skeleton that distinguishes **source inputs**, **transformation code**, **intermediate outputs**, **figures**, **models** and **claims**. The result is a provenance chain:

```text
research question / protocol
    -> data inventory + usage permission + schema
    -> immutable inputs and versioned transformations
    -> analysis / model development
    -> tests + scientific review + validation evidence
    -> figure / table / model / manuscript
    -> reviewed release or approved deployment
    -> monitoring, issue triage and reproducibility record
```

A successful build means the code ran. Scientific acceptance separately requires appropriate design, accurate denominators and units, reproducible methods, representative evaluation, and bounded interpretation.

**Reusable starting materials:** [biomedical research README template](templates/biomedical-research/README.template.md) · [scaffold implementation guide](docs/SCAFFOLD_IMPLEMENTATION_GUIDE.md) · [research release gates](checklists/research-release-gates.md).

## 1. Scaffold with intent

The initial repository structure should let a new collaborator answer five questions without reverse-engineering the code: *What problem is being studied? Which data may I use? How do I run the analysis? How is correctness checked? Where are results explained?*

Suggested scaffold (adapt to project size; directories need not be created until useful):

```text
research-project/
├── README.md                # question, scope, quick start, status, navigation
├── LICENSE                  # distribution rights, when appropriate
├── CITATION.cff             # software citation metadata
├── .gitignore               # local data, PHI, credentials and generated outputs
├── .github/
│   ├── workflows/ci.yml     # build, test, audit, security checks
│   └── pull_request_template.md
├── docs/
│   ├── protocol.md          # hypothesis, cohorts, estimand and design
│   ├── data_dictionary.md   # units, coding, missingness and identifiers
│   ├── source_register.md   # version, retrieval, license and provenance
│   └── decisions/           # concise analysis/design decision records
├── src/                     # reusable processing and analysis functions
├── tests/                   # fast tests, fixtures and regression checks
├── configs/                 # versioned parameters; no secrets
├── scripts/                 # reproducible entry points
├── notebooks/               # exploratory work, promoted to src as needed
├── references/              # verified bibliography and literature matrix
└── artifacts/               # generated locally / by CI, usually gitignored
```

**Data boundary.** Treat raw clinical datasets, direct identifiers, secrets, private tokens, restricted models and licensed source material as separately governed inputs. Record where authorized users retrieve data without committing the data or disclosing sensitive paths. Use intentionally synthetic fixtures for public tests. A `.gitignore` prevents routine staging, but does not erase already committed material; inspect history and access controls when remediating disclosures.

**Reproducibility baseline.** Declare runtime versions, lock dependencies where possible, pin container images by digest when suitable, record input checksums and execution parameters, and keep a one-command smoke test. For R, consider `renv`; for Python, use a documented package environment and lockfile. Emit machine-readable run metadata linking code SHA, input identifier, package versions, seed and output checksums. Random seeds help reproduce stochastic results but do not guarantee determinism across hardware or libraries.

**Git hygiene.** Make cohesive commits with meaningful messages, exclude transient caches and large binary outputs, add a source register and data dictionary before serious analysis, and use descriptive paths and function names. Promote stable notebook logic to tested modules rather than treating execution order as an implicit dependency.

## 2. Govern change

Use a protected `main` branch as the accepted research or release baseline. Develop narrowly scoped features in short-lived branches such as `docs/methods-review`, `feat/normalized-cohort-loader`, `fix/missingness-denominator` or `test/external-validation-fixtures`. Each pull request should describe the **scientific reason for change**, the files and outputs affected, the evidence supporting it and the rollback plan.

A high-quality pull request answers:

1. **Intent:** Which research question, defect or reproducibility gap does this address?
2. **Input and assumptions:** Did cohorts, data dictionaries, filters, units or licenses change?
3. **Evidence:** What tests, figure comparisons or independent checks passed?
4. **Impact:** Does the change alter reported numbers, manuscript statements, interfaces or deployment behavior?
5. **Risk and review:** Which independent reviewer or domain expert must approve it?

Protect the default branch with required CI checks, reviewer approval as appropriate, conversation resolution and restricted force pushes. Keep job names unique so required statuses are unambiguous. Merge only after the relevant checks succeed; an administrative bypass should be an exceptional, recorded governance decision, never a routine fix for red CI. See the [GitHub branch-protection reference](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches).

For multi-repository work, define explicit contracts and versioned outputs. A consuming application should accept only approved, schema-validated research artifacts; a private analysis environment should not automatically publish raw records, private metadata or unreviewed figures.

## 3. Validate every change

CI should be **fast at the first gate, deeper at later gates**. A practical matrix is:

| Gate | Minimum checks | Evidence retained |
| --- | --- | --- |
| G0 — structure | required files, path sanity, prohibited-file/secret scan | machine-readable repository audit |
| G1 — code | lint, formatting, static type or syntax checks, unit tests | versioned test report |
| G2 — data | schema, ranges, units, allowed categories, missingness and join cardinality | validation summary and fixture results |
| G3 — analysis | stable numeric expectations, negative controls, statistical assumptions, train/test isolation | numerical regression report |
| G4 — publication | citations, figure labels, accessibility, provenance, permissions and claimed limitations | review checklist and artifact manifest |
| G5 — release | reproducible build, vulnerability/dependency review, deployment smoke checks, rollback readiness | release ID, source SHA and deployment record |

Do not turn an exploratory p-value, a model metric or a green GitHub badge into a claim of clinical validity. Test the transformations that produce denominators, outcomes and covariates; for biomedical ML, prevent patient-level or temporal leakage between development and evaluation splits. Report missingness, sample selection, confidence intervals when justified and subgroup performance where relevant.

**GitHub Actions baseline:** set `permissions: contents: read` by default, grant elevated scope only to the job that needs it, avoid executing untrusted pull-request content with privileged credentials, and pin trusted third-party actions to full commit SHAs where feasible. Audit action provenance before adoption. GitHub's [secure-use reference](https://docs.github.com/en/actions/reference/security/secure-use) provides the current operational guidance. Never fabricate a pin SHA: resolve and review the chosen upstream release first.

Keep CI artifacts free of identifiers and sensitive paths. Retention, visibility and download permissions require deliberate review. A passing test run should be associated with the *exact* commit intended for release.

## 4. Deploy in stages

Separate the scientific analysis from the application serving its approved outputs. For web dashboards and APIs, use a gated route:

```text
feature branch -> PR checks -> reviewed main
    -> isolated preview (non-sensitive fixtures)
    -> staging integration + smoke test
    -> approved production release
    -> observed health + rollback capability
```

Preview deployments may execute code from untrusted branches: supply synthetic test data and scoped credentials only. Production environments should require an explicit release identity, restricted deployment permissions and approved configuration. Prefer OpenID Connect (OIDC) with short-lived cloud credentials where supported instead of persistent deployment secrets. GitHub provides an [OIDC deployment guide](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments).

**Deployment evidence contract:** capture source commit SHA, dependency/build identity, environment, deployment URL, timestamp, smoke-test results, approver, externally visible dataset version, monitoring owner and rollback target. Distinguish a **successful build**, **successful deployment** and **validated functioning product**. For a scientific HUD, also check data freshness, empty and partial sources, labels/units, last-update timestamps, fallbacks and whether an output is explicitly release-approved.

Recommended promotion strategy: **develop → preview → verify → approve → release → observe**. Do not trigger additional production builds merely for README edits when the deployment policy or rate budget calls for batching.

## 5. Connect the software lifecycle to the scientific lifecycle

A biomedical repository is useful only when its structure supports genuine scientific reasoning. Begin with the estimand, target population and data-generating process. Record collection mechanisms, eligibility criteria and the distinction between observed, imputed, transformed and simulated values. In genomics, preserve sample identifiers, assay scale and batch details; in patient trajectories, define visit chronology and repeated measures; in imaging or ECG pipelines, preserve acquisition, preprocessing and evaluation partitions.

**Literature-informed ML practice.** Pre-register or clearly version evaluation plans when appropriate. Fit preprocessing within training folds, reserve evaluation data, tune on separate data, and assess calibration and transportability in addition to discrimination. TRIPOD+AI guides transparent reporting of clinical prediction modeling, irrespective of regression versus machine-learning method; it does not itself validate a deployed model. For generated visualizations, include complete units, cohort counts, handling of missing values, palette meaning and a plain-language figure interpretation.

**Traceability model:** each published figure or result should link to an analysis script, inputs or safe input IDs, software revision, parameter file, environment manifest and interpretive text. A source change that alters quantitative results should prompt both numerical tests and a manuscript/figure review; a documentation-only change need not retrain an unrelated model.

## Literature and standards matrix

The matrix combines **peer-reviewed methodological foundations** with **maintainer standards and platform documentation**. The final column translates a source into a verifiable practice; it is an implementation recommendation, not a claim that a source endorses the entire repository design.

| ID | Source and type | Key lesson | Implementation / acceptance evidence |
| --- | --- | --- | --- |
| L01 | [Sandve et al., 2013, *Ten Simple Rules for Reproducible Computational Research*](https://doi.org/10.1371/journal.pcbi.1003285) — peer-reviewed methods | Record intermediate steps, parameters and software, enabling replay | Source-to-output manifest, repeatable execution script, preserved decisions |
| L02 | [Osborne et al., 2014, *Ten Simple Rules for Effective Computational Research*](https://doi.org/10.1371/journal.pcbi.1003506) — peer-reviewed methods | Computational research benefits from maintainable organization, verification and communication | Modular code, documented runs, testable functions and readable results |
| L03 | [Wilkinson et al., 2016, FAIR Guiding Principles](https://doi.org/10.1038/sdata.2016.18) — peer-reviewed data stewardship | Findable, accessible, interoperable and reusable research objects require rich metadata and provenance | Source register, metadata dictionary, rights field, stable identifiers |
| L04 | [NIST SP 800-218, Secure Software Development Framework](https://csrc.nist.gov/pubs/sp/800/218/final) — official standard guidance | Embed security into the software lifecycle instead of relying on a final scan | Threat review, dependency screening, security fixes and release evidence |
| L05 | [GitHub: Managing protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches) — platform documentation | Protected branches can require reviews and successful checks | Branch rules, required jobs, bounded merge privileges |
| L06 | [GitHub: Secure use reference](https://docs.github.com/en/actions/reference/security/secure-use) — platform security guidance | Least privilege, safe handling of secrets, trusted actions and pinning reduce workflow risks | Job permissions audit, approved actions, verified SHA pins, secret scan |
| L07 | [GitHub: Security hardening deployments with OIDC](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments) — platform security guidance | Federated, short-lived cloud credentials reduce reliance on stored long-lived secrets | Environment policy, OIDC trust boundary, approval and deploy receipt |
| L08 | [Collins et al., 2024, TRIPOD+AI](https://doi.org/10.1136/bmj-2023-078378) — peer-reviewed reporting guideline | Clinical prediction reports should disclose data, methods, evaluation and limitations transparently | Reporting checklist, split definitions, performance/calibration discussion, limitations |

### How to interpret the evidence

Peer-reviewed methods papers motivate reproducibility and transparent reporting; they do **not** prescribe a single folder tree or GitHub workflow syntax. GitHub documentation specifies available platform controls but can change with product updates. NIST SSDF is a secure-development framework, not a proof of compliance from one pipeline run. Record source version and review date when copying practices into another project; apply stricter requirements for projects involving human subjects, regulated environments or clinical decision support.

## Acceptance checklist

- [ ] The README identifies the scientific question, scope, responsible maintainer and execution path.
- [ ] Inputs have provenance, data dictionaries, units, privacy boundaries and usage permissions.
- [ ] Code, configuration, generated artifacts and protected datasets are separated.
- [ ] A clean environment can run the smoke test and reproducibly rebuild the permitted sample output.
- [ ] Main is protected; pull requests describe scientific impact and pass required checks.
- [ ] Test coverage includes bad inputs, missingness, join cardinality and numerical regression where relevant.
- [ ] ML evaluation controls leakage and distinguishes development, tuning and independent evaluation.
- [ ] Figures and manuscripts link to source revision, inputs, methods and reviewed interpretations.
- [ ] Dependencies, action provenance and deployment credentials are reviewed.
- [ ] Preview, staging and production are separated, with bounded secrets and rollback evidence.
- [ ] Release is approved by the appropriate technical and domain reviewers.
- [ ] Monitoring detects failures and stale research inputs without silently overstating findings.

## Applying this repository

Existing project materials remain in [docs/](docs/), [checklists/](checklists/), [templates/](templates/), [references/](references/) and [manuscript/](manuscript/). The repository's Python package and CI workflow continue to support local validation, artifact initialization and workflow auditing. This README provides the common decision framework; project-specific protocols and validation records belong alongside the projects that execute them.

For a first local run, install the package as documented by its Python project configuration, run `pytest`, inspect `bpg-workflow status`, then run `bpg-workflow audit --root .` after initializing any required artifact directories. Check actual command availability and project dependencies rather than assuming every environment contains the CLI.

**Editorial maintenance:** Review the source matrix when GitHub Actions, cloud authentication, security standards or biomedical reporting guidelines change. Add dated references and record decisions instead of repeatedly pasting generic disclaimers across teaching pages.
