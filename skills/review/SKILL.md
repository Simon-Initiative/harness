---
name: harness-review
description: Perform a concise, prioritized review of current code changes with concrete fixes, using the repository’s configured review policy and guides.
examples:
  - "$harness-review"
  - "Review this diff for risks before I open a PR ($harness-review)"
when_to_use:
  - "Implementation is complete and needs a quality pass."
  - "The user asks for a review, risk scan, or PR readiness check."
when_not_to_use:
  - "No meaningful changes are present to review."
  - "The task is pure document drafting with no code or behavior diff."
---

## Workflow

1. Inspect the changed files and identify behavior-impacting risks first.
2. Read `harness.yml`.
3. If code review is disabled, stop and report that no repository review gate is configured.
4. Read `docs/CODEREVIEW.md` and every repository-local review guide it points to and follow and implement a code review as prescribed.
5. Return findings in severity order.

## Output Contract

- Findings first.
- Then residual risks or test gaps.
