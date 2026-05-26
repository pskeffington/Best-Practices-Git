# Author Metadata Integration

Author metadata is intentionally not stored in this public manuscript package.

## Source of truth

The reusable author profile object is stored in the private CV repository:

```text
pskeffington/CV
objects/author_profile.json
```

## Build-time pattern

Final submission builds should pull the author profile object from the private CV repository and inject the `latex.author_block` field into the manuscript source before producing the submission PDF.

## Repository policy

The public manuscript repository should retain generic placeholders for author identity and correspondence fields. Personal author/contact metadata should remain private or be entered directly into the journal submission portal.

## Why

This separates public framework artifacts from private submission metadata while preserving a reusable object-oriented author profile for LaTeX generation.
