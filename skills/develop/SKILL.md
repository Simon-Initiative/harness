---
name: harness-develop
description: Implement all remaining authorized plan phases, or an explicitly selected phase.
---

Start with the request, applicable repository instructions (including `AGENTS.md`), and the artifact being acted on. Investigate affected code progressively; read architecture, domain, operations, security, testing, tooling, or issue guidance when relevant to the next decision. Read `harness.yml` when configured behavior matters. Reuse unchanged context; reread after changes, missing handoff context, or uncertainty. No context-loading log is required.

Read the plan and its authoritative inputs as needed. Establish the deliverable base before editing so final review includes committed and uncommitted changes across every phase. Without a phase selector, execute all remaining authorized phases in dependency order; with a selector, honor that scope. Continue through routine phase boundaries without renewed approval.

Testing and quality are critical to implementation, not optional cleanup at the end. Before implementing, you must read the target repository's `docs/TESTING.md` and follow its testing guidelines; reuse it if already read and unchanged in this session. If it is missing, report the gap and consult existing repository test guidance rather than inventing policy. Add or update meaningful tests for changed behavior, cover relevant failure cases and regressions, and run the required checks as work progresses. Investigate failures and verify fixes; never present skipped, unavailable, or failing checks as passing, or claim completion while required verification remains unresolved.

Validate structured inputs when first needed, and again only when changed. Implement and run relevant verification during each phase; reuse still-valid evidence. Keep completed checkboxes, blockers, material deviations, and useful verification evidence in the plan. No standalone execution record is required.

Update only affected authoritative docs: acceptance behavior in requirements/product scope, contracts in design, order/progress in the plan. Never silently weaken requirements to fit implementation. Record decisions once. Pause only for a material unresolved decision, authorization boundary, or explicit user request.

A selected non-final phase can finish without formal review: report final review pending. Default formal review occurs once after ALL phases and relevant checks complete; earlier review requires an explicit request or specific consequential milestone, not routine risk classification.

After the complete deliverable passes relevant verification, run `$harness-review` once unless automatic review is explicitly disabled in repository policy. A user-requested review still runs. Resolve substantive findings and rerun affected checks; broader re-review is needed only if the fixes justify it.

Always favor simple, straight-forward implementations.  Avoid complexity, always avoid over-engineering. Never "gold plate" work by inventing and adding new features. 

Finish with completed scope, verification results, final review outcome (or pending status), blockers and residual risks. Keep one concise final verification summary in the plan or PR description.
