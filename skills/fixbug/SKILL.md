---
name: harness-fixbug
description: Execute a regression-safe, TDD-first bug-fix workflow using the repository’s configured issue intake, testing, and review rules.
examples:
  - "$harness-fixbug ISSUE-123"
  - "Fix this regression using the repository bug workflow ($harness-fixbug)"
when_to_use:
  - "A minimal safe bug fix is needed."
  - "The repository expects regression-first bug work."
when_not_to_use:
  - "The work is a net-new feature workflow."
  - "The user asks for an exploratory prototype."
---

## Required Resources
Always load before working:

- `references/persona.md`
- `references/approach.md`
- `references/considerations.md`
- `references/output_requirements.md`
- `ARCHITECTURE.md`
- `harness.yml`
- `docs/STACK.md`
- `docs/TOOLING.md`
- `docs/TESTING.md`
- `docs/PRODUCT_SENSE.md`
- `docs/FRONTEND.md`
- `docs/BACKEND.md`
- `docs/CODEREVIEW.md` when review is enabled
- `docs/ISSUE_TRACKING.md` when issue tracking is enabled

## Workflow
1. Resolve the bug report from the configured issue intake when available.
2. Restate expected vs actual behavior.
3. Reproduce the bug locally when possible.
4. Add or update a failing regression test first.
5. Implement the smallest safe fix that makes the test pass.
6. Run required verification and test commands.
7. If code review is enabled, run `$harness-review`.
8. Update docs only when the bug fix changes a documented behavior contract.
