---
name: harness-analyze
description: Clarify a substantial feature into a compact PRD and canonical acceptance criteria.
---

Start with the request, applicable repository instructions (including `AGENTS.md`), and the artifact being acted on. Investigate affected code progressively; read architecture, domain, operations, security, testing, tooling, or issue guidance when relevant to the next decision. Read `harness.yml` when configured behavior matters. Reuse unchanged context; reread after changes, missing handoff context, or uncertainty. No context-loading log is required.

Read the request or existing specification and clarify the problem, desired outcome, scope, non-goals, and constraints. Write `prd.md`, normally in `docs/exec-plans/current/<work-item>/`. Use the optional [template](assets/templates/prd_template.md) as guidance, not a required heading schema.

Keep detailed requirements in one canonical source. For substantial features use nested `requirements.yml` via `$harness-requirements` and link to it; a ticket or concise specification can suffice for small work. Record open decisions only when present. Do not manufacture missing artifacts merely for ceremony.

Finish with the artifact path, scope decisions, and unresolved questions. An analysis-only request ends here.
