---
name: harness-update_docs
description: Reconcile authoritative work-item documents with changed scope or implementation.
---

Start with the request, applicable repository instructions (including `AGENTS.md`), and the artifact being acted on. Investigate affected code progressively; read architecture, domain, operations, security, testing, tooling, or issue guidance when relevant to the next decision. Read `harness.yml` when configured behavior matters. Reuse unchanged context; reread after changes, missing handoff context, or uncertainty. No context-loading log is required.

Compare the requested change and inspected implementation with existing authoritative artifacts. Update requirements and product scope for changed acceptance behavior, design for interfaces/architecture/data contracts, and plan for task order/progress. Do not create unrelated documents or append duplicate decision logs.

Do not silently alter requirements to make code compliant. Resolve material scope decisions using existing authorization or ask when a genuine decision remains. Record each material decision once and link where helpful. Validate changed structured inputs only. Report changed paths, substantive reconciliations and unresolved mismatches. Ordinary implementation performs this maintenance directly; invoking this skill is optional.
