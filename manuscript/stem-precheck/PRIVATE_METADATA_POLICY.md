# Private Metadata Policy

This submission package should not store personal contact details in the repository.

## Rule

Keep manuscript and cover-letter files repository-safe. Use placeholders in committed files for author identity, institutional affiliation, and correspondence fields.

## Where final metadata belongs

Enter final author metadata directly in the journal submission portal or in a local private copy prepared outside version control.

## Do not commit

Do not commit files containing:

- personal email addresses,
- private phone numbers,
- private mailing addresses,
- non-public identifiers,
- journal portal credentials,
- private submission correspondence.

## Recommended public repository pattern

Committed source files may use placeholders such as:

```text
Author Name
Institutional Affiliation
Corresponding author: [entered in submission portal]
```

## Local-only workflow

Create any final personalized submission files outside the repository or in an ignored local file. Keep the repository version generic and reusable.

## Reason

The repository is intended to hold the framework, manuscript source, audit schemas, templates, and reproducibility package. Personal submission metadata should remain outside the public audit package unless intentionally added at final journal submission.
