---
name: harness-plan
description: Turn authoritative scope and design into a dependency-ordered implementation plan.
---

Start with the request, applicable repository instructions (including `AGENTS.md`), and the artifact being acted on. Investigate affected code progressively; read architecture, domain, operations, security, testing, tooling, or issue guidance when relevant to the next decision. Read `harness.yml` when configured behavior matters. Reuse unchanged context; reread after changes, missing handoff context, or uncertainty. No context-loading log is required.

Use existing authoritative inputs; do not require a PRD or FDD if a ticket or concise specification is sufficient. Write `plan.md` with scope links, checkbox tasks or phases in dependency order, and relevant verification per phase. Usually goal, tasks, and verification suffice; state dependencies only where unclear. One phase is enough when appropriate.

Use the optional [template](assets/templates/plan_template.md). Include one final completion section for integration checks, requirements coverage, and final independent review of the entire deliverable. Ordinary phases have no formal review gate.

Finish with the plan path and unresolved decisions. A planning-only request stops here; existing implementation authorization permits continuing.
