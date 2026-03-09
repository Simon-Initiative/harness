---
name: harness-bootstrap
description: Seed a target repository with the required harness contract files and directory structure, and optionally draft initial repository-specific content when enough context is available.
examples:
  - "$harness-bootstrap /path/to/target-repo"
  - "Seed this repository with the harness contract ($harness-bootstrap)"
  - "Bootstrap this Phoenix repository for a retirement-planning web app with a future React frontend ($harness-bootstrap)"
when_to_use:
  - "A repository needs the required harness artifacts created for the first time."
  - "A repository needs the standard contract structure restored."
  - "A repository needs the harness contract plus an initial pass at repository-specific docs."
when_not_to_use:
  - "The repository already has a valid harness contract and only needs content updates."
---

## Purpose

Create the required harness contract files and directories in a target repository.

When the invocation includes enough context, also draft an initial pass of repository-specific content into the seeded docs.

## Workflow

1. Resolve the target repository root.
2. Run `python3 ./seed_harness_contract.py <target_repo>`.
3. Inspect available context signals:
   - user-provided description of the intended product, stack, architecture, or workflow
   - existing repository files such as `AGENTS.md`, `README*`, `mix.exs`, `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, `Dockerfile*`, CI files, and framework entrypoints
   - existing docs that already describe architecture, testing, operations, frontend, or tooling
4. Decide whether there is enough context to populate content:
   - If there is no meaningful repository or product context, stop after seeding and validation.
   - If there is meaningful context, draft initial content for the seeded harness files using that context.
5. Content population rules:
   - Never overwrite substantive existing repository files unless the user explicitly asks.
   - Prefer filling files that are empty, placeholder-only, or clearly harness-seeded boilerplate.
   - Reuse existing repository wording and conventions when they are already documented.
   - Use high-confidence facts from the repository for stack, tooling, and architecture sections.
   - Use user-provided product description for product goals, likely system shape, and initial planning context.
   - Mark inferred content as assumptions when it is not directly grounded in repository evidence.
6. Prioritize initial population of:
   - `AGENTS.md`
   - `ARCHITECTURE.md`
   - `harness.yml`
   - `docs/STACK.md`
   - `docs/TOOLING.md`
   - `docs/TESTING.md`
   - `docs/OPERATIONS.md`
   - `docs/FRONTEND.md`
   - `docs/PRODUCT_SENSE.md`
7. Run `python3 ./validate_harness_contract.py <target_repo>`.
8. If validation fails, fix the seeded files immediately.

## Output Contract

- Report the target repository path.
- Report whether the seed run created new files or reused existing files.
- Report whether content population was skipped or performed.
- When content population was performed, report which files were materially drafted from repository or user-provided context.
- Report the validation result.
