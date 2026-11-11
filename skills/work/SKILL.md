---
name: harness-work
description: Implement a bounded enhancement or refactor with a short approach and relevant verification.
---

Start with the request, applicable repository instructions (including `AGENTS.md`), and the artifact being acted on. Investigate affected code progressively; read architecture, domain, operations, security, testing, tooling, or issue guidance when relevant to the next decision. Read `harness.yml` when configured behavior matters. Reuse unchanged context; reread after changes, missing handoff context, or uncertainty. No context-loading log is required.

Identify scope, acceptance behavior, and constraints from the task or ticket. Explain a short approach and task list in chat; no spec pack or YAML is required. If implementation is authorized, proceed, including autonomously assigned tasks. Pause only for a material unresolved decision, genuine authorization boundary, or explicit proposal-before-coding request.

Implement the bounded change and run affected verification. Maintain existing docs only where authoritative content changes. Use `fixbug` for defects; expand to feature planning only where useful human decisions or durable handoffs warrant it.

After the complete deliverable passes relevant verification, run `$harness-review` once unless automatic review is explicitly disabled in repository policy. A user-requested review still runs. Resolve substantive findings and rerun affected checks; broader re-review is needed only if the fixes justify it.

Report behavior changed, verification and review results, and remaining risks.
