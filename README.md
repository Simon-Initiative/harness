# Harness Engineering Skills

This repository is a reusable engineering harness for agent-assisted software development. It is meant to be paired with tools like Claude Code or Codex CLI so the same disciplined workflow can be applied across arbitrary applications, regardless of language, framework, or product domain.

The key idea is simple: the reusable skills live here, but the durable project context lives in the target repository. The harness depends on convention. Agents work reliably only when the target repository exposes a stable, versioned set of required files and directories that define architecture, product intent, tooling, testing, operations, plans, and review standards.

Do not install this repository into each application repository. Instead, install these skills into your user-level agent skills directory, then run the bootstrap skill from inside the target repository you want to prepare.

## How It Works

The operating model is:

1. Keep this repository as the source of truth for the reusable skills.
2. Install those skills into your user-level agent skills directory.
3. Open the target repository you want to work on.
4. Invoke `$harness-bootstrap` inside that target repository.
5. Let the bootstrap skill create the required harness contract files and directories.
6. Use the other harness skills against that seeded target repository.

Once bootstrapped, the target repository becomes the system of record. The agent should read repository-local files such as `AGENTS.md`, `ARCHITECTURE.md`, `harness.yml`, and the `docs/` contract before doing substantive work.

## Getting Started

### 1. Install the skills globally

Install these skills into your user-level skills directory so they are available across repositories. For Codex-style setups, that means the user-scoped `.agents/skills` area, not the repository you plan to build.

This repository should remain a reusable skill source, not a subdirectory inside the target application repository.

### 2. Open your target repository

Change into the repository where you want the harness contract to exist. This can be a new or existing project in any stack.

### 3. Run the bootstrap skill

Invoke the bootstrap skill from inside the target repository:

```text
$harness-bootstrap
```

The bootstrap workflow uses the seed and validation scripts in this repository to:

- create the required harness files and directories
- preserve existing substantive files unless you explicitly choose to overwrite them
- optionally draft initial repository-specific content when the target repo already provides enough context
- validate the resulting contract

## Required Target Repository Layout

The harness expects the target repository to expose this baseline structure:

```text
AGENTS.md
ARCHITECTURE.md
harness.yml
docs/
├── BACKEND.md
├── CODEREVIEW.md
├── DESIGN.md
├── FRONTEND.md
├── ISSUE_TRACKING.md
├── OPERATIONS.md
├── PLANS.md
├── PRODUCT_SENSE.md
├── QUALITY_SCORE.md
├── RELIABILITY.md
├── SECURITY.md
├── STACK.md
├── TESTING.md
├── TOOLING.md
├── design-docs/
│   ├── core-beliefs.md
│   └── index.md
├── exec-plans/
│   ├── archive/
│   ├── current/
│   └── tech-debt-tracker.md
├── generated/
│   └── db-schema.md
├── product-specs/
│   ├── index.md
│   └── new-user-onboarding.md
└── references/
    ├── design-system-reference-llms.txt
    ├── nixpacks-llms.txt
    └── uv-llms.txt
```

This is not just an example layout. It is the contract the harness expects to find in the target repository.

## What Goes Where

### Core files

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Short routing document for the agent. Point to the real repository-local sources of truth instead of duplicating them. |
| `ARCHITECTURE.md` | High-level system map, major boundaries, integration seams, and architectural constraints. |
| `harness.yml` | Machine-readable capability policy describing which concerns are enabled and where their detailed guidance lives. |

## Example `harness.yml`

The `harness.yml` file is the machine-readable switchboard for the harness. Today, the harness actively uses it in two ways:

- the bootstrap validator checks that the expected capability schema exists and that each capability points at a real repository-local details file
- the planning and execution skills read the capability entries to decide which cross-cutting concerns should be treated as in-scope by default

To keep the README aligned with the code, the example below only shows fields that are currently part of that active contract.

Example:

```yaml
version: 1

capabilities:
  feature_flags:
    adoption: disabled
    default: exclude
    details_file: docs/OPERATIONS.md
  telemetry:
    adoption: enabled
    default: include
    details_file: docs/OPERATIONS.md
  performance_requirements:
    adoption: enabled
    default: exclude
    details_file: docs/OPERATIONS.md
  code_review:
    adoption: enabled
    default: include
    details_file: docs/CODEREVIEW.md
  issue_tracking:
    adoption: enabled
    default: include
    details_file: docs/ISSUE_TRACKING.md
```

In practice, this file answers questions like:

- whether the agent should assume feature flags exist in this repository
- whether telemetry should be considered part of the default implementation path
- whether performance requirements should be called out by default
- where the agent should look for the repository's code review rules
- whether issue tracking is part of the expected workflow

The markdown files hold the narrative guidance. `harness.yml` gives the agent a compact policy layer it can inspect quickly and apply consistently.

### Repository standards

| Path | Purpose |
| --- | --- |
| `docs/STACK.md` | Languages, frameworks, runtimes, storage, infrastructure basics, and major technical choices. |
| `docs/TOOLING.md` | Canonical commands for build, lint, format, typecheck, test, and local development workflows. |
| `docs/TESTING.md` | Test strategy, required gates, and any repository-specific testing conventions. |
| `docs/OPERATIONS.md` | Observability, rollout, performance expectations, incidents, and runtime concerns. |
| `docs/CODEREVIEW.md` | Review policy, required review lenses, and repository-specific review standards. |
| `docs/ISSUE_TRACKING.md` | Ticket workflow, system of record, intake path, and how work is tracked. |
| `docs/SECURITY.md` | Security requirements, data handling rules, auth boundaries, and review expectations. |
| `docs/RELIABILITY.md` | Reliability expectations, fault tolerance concerns, and service health requirements. |
| `docs/QUALITY_SCORE.md` | How quality is evaluated in this repo and what currently blocks higher confidence. |

### Product and implementation guidance

| Path | Purpose |
| --- | --- |
| `docs/PRODUCT_SENSE.md` | Product goals, target users, priorities, and decision-making guidance for tradeoffs. |
| `docs/FRONTEND.md` | UI architecture, frontend boundaries, client-side conventions, and design implementation rules. |
| `docs/BACKEND.md` | Service boundaries, API rules, domain logic placement, and backend implementation guidance. |
| `docs/DESIGN.md` | Design principles, interaction expectations, and experience-level standards. |
| `docs/PLANS.md` | How work items are structured, where active execution plans live, and planning expectations. |

### Working directories

| Path | Purpose |
| --- | --- |
| `docs/exec-plans/current/` | Active work items, including PRDs, designs, plans, and proof artifacts for in-flight changes. |
| `docs/exec-plans/archive/` | Completed or superseded work items that should remain available for historical context. |
| `docs/exec-plans/tech-debt-tracker.md` | Explicit technical debt inventory and deferred engineering work. |
| `docs/design-docs/` | Decision records, design history, and durable engineering beliefs. |
| `docs/product-specs/` | Feature-level product specs and user-facing behavior definitions. |
| `docs/generated/` | Generated reference artifacts such as schema inventories or other machine-produced facts. |
| `docs/references/` | External framework, platform, design-system, or tool references that agents may need during implementation. |

## Bootstrap Behavior

The bootstrap skill in this repository currently runs:

- `.agents/scripts/seed_harness_contract.py`
- `.agents/scripts/validate_harness_contract.py`

The seed script creates the baseline contract. The validation script checks that required files and directories exist and that `harness.yml` conforms to the expected capability schema.

## Available Skills

This repository includes reusable skills for:

- analyzing ideas into PRDs
- turning PRDs into architecture and detailed designs
- planning implementation slices
- developing planned work
- bootstrapping new target repositories
- reviewing changes
- fixing bugs
- validating harness work items and repository contract structure
- updating planning docs after implementation drift

Those skills are intended to be installed once and reused across many projects.

## Intention

This repository exists to make agent-driven engineering more repeatable. The harness is deliberately stack-agnostic and domain-agnostic, but it is not convention-agnostic. Reuse comes from keeping the skills generic while requiring each target repository to expose a consistent, inspectable operating context that both humans and agents can trust.
