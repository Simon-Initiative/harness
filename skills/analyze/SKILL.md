---
name: harness-analyze
description: Convert an informal feature idea into a concise, implementation-ready PRD in a work item directory under docs/exec-plans/current/.
examples:
  - "$harness-analyze docs/exec-plans/current/gradebook-overrides"
  - "$harness-analyze docs/exec-plans/current/platform-modernization/gradebook-overrides"
when_to_use:
  - "A new work item needs a PRD."
  - "A work item needs clarified scope, success criteria, or requirements traceability."
when_not_to_use:
  - "The task is architecture design (use $harness-architect)."
  - "The task is direct implementation (use $harness-develop)."
---

## Required Resources
Always load before drafting:

- `references/persona.md`
- `references/approach.md`
- `references/considerations.md`
- `references/output_requirements.md`
- `references/prd_checklist.md`
- `references/definition_of_done.md`
- `references/validation.md`
- `assets/templates/prd_template.md`
- repository context: `ARCHITECTURE.md`, `harness.yml`, `docs/STACK.md`, `docs/TOOLING.md`, `docs/TESTING.md`, `docs/PRODUCT_SENSE.md`, `docs/FRONTEND.md`, `docs/BACKEND.md`, `docs/OPERATIONS.md`

## Workflow
1. Resolve the work item directory under `docs/exec-plans/current/...`.
2. Open or create `<work_item_dir>/prd.md`.
3. Restate the request in product terms: user value, scope, constraints, risks, and success signals.
4. Copy the exact section structure from `assets/templates/prd_template.md`.
5. Use the reference files to fill the PRD with concrete, testable content.
6. Keep detailed FR/AC entries canonical in `requirements.yml`.
   - In `Functional Requirements`, include exactly: `Requirements are found in requirements.yml`
   - In `Acceptance Criteria`, include exactly: `Requirements are found in requirements.yml`
7. Use `harness.yml` to decide whether feature flags, telemetry, performance requirements, code review, and issue tracking should be considered by default.
8. When a capability is enabled, read the repository-local detail file named in `harness.yml` before deciding how it applies.
9. Resolve `<skills_root>` as the directory that contains the installed harness skills (`analyze/`, `requirements/`, `validate/`, etc.). Do not resolve script paths relative to the repository or current working directory.
10. Run these commands sequentially:
   - `python3 <skills_root>/requirements/scripts/requirements_trace.py <work_item_dir> --action capture --bulk-file <bulk_payload_path>`
   - `python3 <skills_root>/requirements/scripts/requirements_trace.py <work_item_dir> --action validate_structure`
   - `python3 <skills_root>/validate/scripts/validate_work_item.py <work_item_dir> --check prd`
11. Do not start PRD validation until the requirements capture step has created or updated `<work_item_dir>/requirements.yml`.

## Output Contract
- Update `<work_item_dir>/prd.md`.
- Ensure `<work_item_dir>/requirements.yml` exists.
- Final response: updated path, key decisions, open questions.
