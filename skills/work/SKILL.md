---
name: harness-work
description: Execute a lightweight work-item lane for small enhancements or refactors by generating a brief technical approach, pausing for approval, then implementing with repository-local rules.
examples:
  - "$harness-work ISSUE-123"
  - "Read this work item and propose a brief implementation plan, then implement after approval ($harness-work)"
when_to_use:
  - "Small enhancement or refactor that does not need a full analyze, architect, plan, and develop lane."
  - "Work should be implemented from a concise reviewed approach."
when_not_to_use:
  - "Large net-new capabilities that need the full harness lane."
  - "Bug or regression tickets (use $harness-fixbug)."
---

## Required Resources
Always load before running:

- `references/persona.md`
- `references/approach.md`
- `references/considerations.md`
- `references/issue_intake.md` when issue tracking is enabled
- `references/epic_context.md` when parent or epic context exists
- `references/approval_gate.md`
- `references/execution_guardrails.md`
- `references/output_requirements.md`
- `ARCHITECTURE.md`
- `harness.yml`
- `docs/STACK.md`
- `docs/TOOLING.md`
- `docs/TESTING.md`
- `docs/PRODUCT_SENSE.md`
- `docs/FRONTEND.md`
- `docs/BACKEND.md`
- implementation phase must also load the develop references for coding, validation, and execution quality

## Phase 1: Technical Approach and Planning
1. Read the issue or request.
2. If issue tracking is enabled, use `docs/ISSUE_TRACKING.md` and `references/issue_intake.md` to resolve the work item.
3. Extract concise requirements and constraints.
4. If the issue is a bug or regression, stop and route to `$harness-fixbug`.
5. If parent or epic context exists, read local work-item docs or repository context that constrain the work.
6. Produce a brief technical approach, a short numbered implementation plan, risks, assumptions, and test strategy.
7. Pause for user approval using the approval gate.

## Phase 2: Implementation
1. After approval, load the required implementation references from `skills/develop/references/`.
2. Implement the approved scope only.
3. Add or update required tests.
4. Run required verification and test commands.
5. If code review is enabled, run `$harness-review`.
6. Report implementation summary, files changed, commands run, outcomes, and residual risks.
