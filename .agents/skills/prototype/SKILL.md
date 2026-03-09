---
name: harness-prototype
description: Build a fast, low-ceremony prototype to validate an idea quickly, then report the shortest path to production hardening.
examples:
  - "$harness-prototype Build a quick spike for inline editing"
  - "Prototype a rough ingestion flow for uploaded content"
when_to_use:
  - "The user wants a throwaway spike, proof of concept, or feasibility check."
when_not_to_use:
  - "The task is a bug fix requiring regression-first workflow."
  - "The task needs durable planning artifacts first."
---

## Required Resources
Always load before prototyping:

- `references/persona.md`
- `references/approach.md`
- `references/considerations.md`
- `references/output_requirements.md`
- `ARCHITECTURE.md`
- `harness.yml`
- `docs/STACK.md`
- `docs/TOOLING.md`
- `docs/TESTING.md`
- `docs/PRODUCT_SENSE.md`
- `docs/FRONTEND.md`
- `docs/BACKEND.md`

## Workflow
1. Define the prototype question being answered.
2. Implement the smallest runnable prototype that answers it.
3. Skip hardening (that means NO testing also) unless the user explicitly asks for it.
4. Report what was validated, what remains unknown, and the shortest path to productionization.
