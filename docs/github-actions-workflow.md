# GitHub Actions Workflow

All manuscript production and audit workflows should run through GitHub Actions.

## Public workflows

### CI

Workflow file:

```text
.github/workflows/ci.yml
```

Runs on push and pull request to `main`.

Responsibilities:

- install the package,
- run tests,
- check the workflow CLI,
- initialize manuscript artifacts,
- run the workflow audit,
- upload audit artifacts.

### Build Manuscript

Workflow file:

```text
.github/workflows/build-manuscript.yml
```

Runs on manuscript changes, pull requests, and manual dispatch.

Responsibilities:

- build the public-safe manuscript PDF,
- keep author metadata generic,
- upload the public manuscript PDF as an artifact.

## Private submission workflow

### Private Submission Build

Workflow file:

```text
.github/workflows/private-submission-build.yml
```

Runs only by manual dispatch.

Responsibilities:

- check out the public manuscript repository,
- check out the private CV repository,
- read the reusable author object,
- inject the private author block into a local build copy,
- build the personalized submission PDF,
- upload the PDF as a private workflow artifact,
- avoid committing private author metadata to the public repository.

## Required secret

The private submission build requires a repository secret in `Best-Practices-Git`:

```text
CV_REPO_TOKEN
```

The token must have read access to:

```text
pskeffington/CV
```

## Private author metadata source

The reusable author object lives in the private CV repository:

```text
pskeffington/CV
objects/author_profile.json
```

The public repository should never store the personalized author block, correspondence email, or final submission metadata.

## Expected artifact outputs

| Workflow | Artifact |
|---|---|
| CI | `workflow-audit-artifacts` |
| Build Manuscript | `public-manuscript-pdf` |
| Private Submission Build | `private-submission-pdf` |

## Operating rule

Do not build final submission artifacts manually on an untracked local path. Use GitHub Actions so each build is logged, reproducible, and auditable.
