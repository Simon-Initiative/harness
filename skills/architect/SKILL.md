---
name: harness-architect
description: Design technical boundaries and decisions when a feature warrants architecture work.
---

Start with the request, applicable repository instructions (including `AGENTS.md`), and the artifact being acted on. Investigate affected code progressively; read architecture, domain, operations, security, testing, tooling, or issue guidance when relevant to the next decision. Read `harness.yml` when configured behavior matters. Reuse unchanged context; reread after changes, missing handoff context, or uncertainty. No context-loading log is required.

Use the authoritative request, ticket, PRD, or approved design; no prerequisite PRD is required. Inspect affected code before proposing boundaries. Write `fdd.md` covering design, decisions and tradeoffs, relevant interfaces/data/failure behavior, verification, and material risks. Distinguish inspected facts from assumptions and reference canonical requirements without copying them.

Add migration, security, consistency, caching, rollout, or performance detail only where substantive. 

Always focus on the simplicity in design and approach.  Pay attention to and follow both existing patterns in the codebase and standard best practices.  

The optional [template](assets/templates/fdd_template.md) is a starting point. Finish with design path, key decisions, and unresolved decisions. Architecture-only requests do not authorize implementation.
