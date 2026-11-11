---
name: harness-review
description: Independently review a complete deliverable or explicitly requested scope.
---

Start with the request, applicable repository instructions (including `AGENTS.md`), and the artifact being acted on. Investigate affected code progressively; read architecture, domain, operations, security, testing, tooling, or issue guidance when relevant to the next decision. Read `harness.yml` when configured behavior matters. Reuse unchanged context; reread after changes, missing handoff context, or uncertainty. No context-loading log is required.

When review is due, read `harness.yml` if present and follow `capabilities.code_review.details_file` as the repository review entry point; if no path is configured, read `docs/CODEREVIEW.md` when present. Also honor applicable `AGENTS.md` review instructions. Read this entry point before selecting reviewers: it defines application-specific reviewer roles, mandatory and conditional review lenses, and delegation rules. A missing configured file is a configuration gap to report, not permission to silently replace the policy with a generic review.

Resolve the correct base and inspect the complete deliverable diff, including committed and uncommitted changes and untracked deliverable files. Do not assume outstanding working-tree changes represent the whole feature. Read requirements and affected code/tests directly. Select the repository's required reviewers using this complete scope.

One final review means one review stage, not one reviewer. When repository policy calls for separate reviewers, launch a fresh subagent for each selected role/checklist, using repository-defined agents where available. Pass each its assigned guide path, deliverable base and complete scope, authoritative requirements, and relevant verification evidence. Let reviewers read their own checklists rather than loading every checklist into the coordinator. Run independent reviewers concurrently where supported (batch to runtime limits), wait for all selected reviewers, then merge and deduplicate their findings. Do not substitute a single general reviewer for required specialist reviewers.

Without repository-specific delegation, use a fresh general reviewer context or agent where supported. The runtime or repository chooses the model. Keep reviewer execution read-only where supported. If a named role is unavailable, use a fresh available agent with that role's instructions; if independent execution is unavailable, assess each selected lens in a clearly labeled self-review and report which independent reviews remain unavailable. Never claim a separate reviewer ran or that a required independent review completed when it did not.

An explicit review request runs even when automatic review is disabled. For automatic review, honor `capabilities.code_review.adoption: disabled` or `default: exclude` in `harness.yml`; absent policy defaults to final review. Review once at the end of all implementation phases after relevant verification. Earlier formal review requires explicit request or a specific consequential milestone. Intentionally separate PR deliverables each need their own final review.

Return concrete findings in severity order with file/line evidence, impact and useful reproduction details, then residual risks or test gaps. Avoid style-only noise. Resolve substantive findings, rerun affected checks and verify fixes; repeat broader review only when changes justify it.
