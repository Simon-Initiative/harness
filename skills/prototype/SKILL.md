---
name: harness-prototype
description: Run a small experiment to answer a concrete feasibility question.
---

Start with the request, applicable repository instructions (including `AGENTS.md`), and the artifact being acted on. Investigate affected code progressively; read architecture, domain, operations, security, testing, tooling, or issue guidance when relevant to the next decision. Read `harness.yml` when configured behavior matters. Reuse unchanged context; reread after changes, missing handoff context, or uncertainty. No context-loading log is required.

Define the question and the observation that would answer it. Build the smallest useful experiment and run the smoke check or measurement needed to answer that question. Skip production hardening and broad regression work unless relevant or requested.

Report what was demonstrated, actual evidence, what remains unknown, and the practical path to production. No spec pack is required. If delivering code, perform the final review after the experiment unless automatic review is disabled; describe experimental limitations to the reviewer.
