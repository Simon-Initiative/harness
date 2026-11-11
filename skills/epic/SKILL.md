---
name: harness-epic
description: Coordinate a multi-feature initiative through ownership and dependencies.
---

Start with the request, applicable repository instructions (including `AGENTS.md`), and the artifact being acted on. Investigate affected code progressively; read architecture, domain, operations, security, testing, tooling, or issue guidance when relevant to the next decision. Read `harness.yml` when configured behavior matters. Reuse unchanged context; reread after changes, missing handoff context, or uncertainty. No context-loading log is required.

Read the source proposal and relevant child artifacts progressively. Write or update the parent `plan.md` with feature groupings, ownership boundaries, dependency order and meaningful concurrency. Preserve useful existing scope and identify unresolved ownership or dependency questions. A dependency diagram is optional when it clarifies coordination.

Use the optional [template](assets/templates/epic_plan_template.md). Do not create child spec packs unless requested. Finish with the parent plan path and the next unblocked work.
