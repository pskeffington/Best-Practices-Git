# Repository Cleanup and Reconciliation Policy

**Status:** Maintained policy  
**Applies to:** any Git or GitHub repository  
**Purpose:** keep documentation, code, branches, pull requests and local checkouts reviewable without overwriting active work.

## 1. Operating principles

1. Preserve work before cleaning it. Never force-push, reset, delete a branch, close a pull request, or discard a worktree change without identifying the exact target and retaining a recoverable reference.
2. Work from current evidence. Treat the current worktree, remote refs, pull-request metadata, checks and review history as authoritative; do not infer that a branch is safe to merge from its title alone.
3. Separate maintenance classes. Documentation edits, generated-file cleanup, code refactors, dependency changes, branch reconciliation and release changes receive separate commits or pull requests whenever practical.
4. Prefer reversible operations. Create a named backup/sync branch or patch before reconciliation; use force-with-lease only with an explicit approval and a recorded expected SHA.
5. Keep production and research gates intact. A clean diff, green unit tests or successful build is not by itself evidence of field acceptance, scientific validity, deployment readiness or permission to merge.

## 2. Inventory before changing anything

For each repository, record:

- default branch, current branch, remote URL and fetched remote heads;
- worktree state: staged, unstaged and untracked paths;
- ahead/behind counts against the tracked upstream;
- open pull requests, draft state, base/head refs, checks, reviews and explicit hold language;
- documentation entry points, license, contribution guidance and CI/security configuration;
- generated or machine-local files, secrets, private data and embedded repositories.

Sort large maintenance campaigns by an explicitly chosen activity order (for example, least-recently active first), but do not treat age as permission to delete or merge. Re-fetch before a destructive or publishing operation.

## 3. Worktree and generated-file hygiene

- Do not stage all changes from a dirty repository by default. Inspect the path list and diff first.
- Remove only confirmed generated machine-local files (for example `.DS_Store`, caches and build outputs) outside `.git`, dependency trees and intentionally versioned fixtures.
- Before removing a tracked generated file, verify it is not part of a reproducibility fixture, release artifact or platform contract; make the removal a focused commit.
- Keep raw data, credentials, PHI, licensed material, virtual environments, dependency trees and large build outputs out of commits. A `.gitignore` change does not remove content already in history.
- Preserve unrelated user changes. If a cleanup overlaps active work, create a separate worktree or defer the cleanup.

## 4. Commit and push policy

Use imperative, specific commit messages and cohesive commits, such as:

- `docs: clarify release evidence contract`
- `chore: remove generated macOS metadata`
- `fix: bound parser input before allocation`

Never create a generic “save all local work” commit for a large or mixed repository without explicit maintainer approval. For approved local preservation, commit only the reviewed paths, record the branch and source SHA, then push to the existing branch or a clearly named temporary sync branch. Do not push local commits over a remote branch that is ahead; reconcile first or publish a separate sync branch.

## 5. Branch reconciliation

1. Fetch with pruning and re-check the divergence counts.
2. Compare local-only and remote-only commits; identify whether they are already represented elsewhere.
3. Preserve both tips before integration (tag or sync branch).
4. Reconcile in a dedicated branch or worktree. Never rebase a dirty worktree.
5. Resolve conflicts semantically, run the repository's required checks, and inspect the resulting diff.
6. Push the reconciled branch and open or update a pull request. Merge only after required checks, reviews and repository-specific acceptance gates pass.

Fast-forward is preferred. A non-fast-forward update requires an explicit expected head and force-with-lease approval; never use an unconditional force push.

## 6. Pull-request lifecycle

- Keep a PR draft when its body says it is blocked, awaiting independent review, unverified on hardware, not ready for release, or “do not merge.”
- Close a PR only when it is superseded, obsolete, duplicated, or explicitly rejected, and leave a concise reason linking the replacement or decision.
- Merge only when the exact head SHA has passing required checks, required approvals, resolved review threads and no active hold. Check the latest state immediately before merging.
- After merge, verify the merge commit, default-branch status, source-branch disposition and linked issue state. Delete a branch only when retention is not needed for audit or rollback.
- Do not close or merge batches of PRs based solely on age, title similarity or local assumptions.

## 7. Documentation top-down pass

Every repository should have a discoverable README that states scope, status, quick start, validation and navigation. Add or improve `docs/` only when the repository's size and lifecycle justify it. At minimum, document:

- contribution and branch/PR expectations;
- reproducible setup and tests;
- data, privacy, license and generated-artifact boundaries;
- release/deployment evidence and rollback;
- known limitations, open gates and ownership.

Update links and indexes when adding documentation. Do not claim a test, deployment, hardware result or scientific conclusion that the current evidence does not prove.

## 8. Required evidence record

Each maintenance pass should leave a compact record containing the date, repositories inspected, commands or API views used, changes made, checks run, pushes/merges/closures performed, unresolved divergence, and required maintainer decisions. For blocked work, record the exact blocker and the next safe action. This record is evidence of process, not a substitute for review or acceptance.

## 9. Daily maintenance sequence

1. Fetch and inventory in the chosen activity order.
2. Preserve local and remote tips where divergence exists.
3. Remove only confirmed generated clutter.
4. Run documentation and code-marker scans, excluding `.git`, dependencies, binaries and vendored sources.
5. Prepare focused changes and validate them locally.
6. Push only fast-forward-safe or explicitly approved sync branches.
7. Triage PRs using current checks and review evidence.
8. Report completed actions, unresolved blockers and required maintainer decisions.

