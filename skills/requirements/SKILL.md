---
name: harness-requirements
description: Maintain canonical nested requirements and explicit evidence for substantial features.
---

Start with the request, applicable repository instructions (including `AGENTS.md`), and the artifact being acted on. Investigate affected code progressively; read architecture, domain, operations, security, testing, tooling, or issue guidance when relevant to the next decision. Read `harness.yml` when configured behavior matters. Reuse unchanged context; reread after changes, missing handoff context, or uncertainty. No context-loading log is required.

Use [schema](references/schema.md) when authoring or updating `requirements.yml`; the [template](assets/templates/requirements_template.yml) illustrates it. Preserve stable FR and AC identifiers. Small tasks may use their ticket or task description instead.

Run `python3 <this-skill>/scripts/requirements_trace.py <work-item> --action validate` for structure and explicit evidence locations. To create or update, use `--action capture --bulk-file <payload>`: IDs are mandatory; existing requirements are replaced by ID, omitted requirements retained, and each supplied requirement replaces its full nested criteria. Review removals before capture. Repeating an identical payload is idempotent.

Validation establishes structure and referenced file existence only. Recorded execution evidence describes an actual check and result; the agent and final reviewer assess whether it supports the criterion. Do not scan source for AC tokens or label file presence as implementation proof. Never invent evidence. Report validation separately from execution results and semantic coverage.
