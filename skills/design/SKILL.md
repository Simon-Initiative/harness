---
name: harness-design
description: Resolve a difficult technical slice with a focused optional design.
---

Start with the request, applicable repository instructions (including `AGENTS.md`), and the artifact being acted on. Investigate affected code progressively; read architecture, domain, operations, security, testing, tooling, or issue guidance when relevant to the next decision. Read `harness.yml` when configured behavior matters. Reuse unchanged context; reread after changes, missing handoff context, or uncertainty. No context-loading log is required.

Identify the specific uncertainty, inspect relevant code and authoritative requirements, and write `design/<slice>.md` describing the decision, affected interfaces, failure cases and verification that resolve it. Use the optional [template](assets/templates/design_slice_template.md). Do not duplicate the full feature scope or require other documents to exist. Finish with the decision, supporting evidence, and any remaining uncertainty.
