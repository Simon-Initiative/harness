#!/usr/bin/env python3
"""Seed the harness contract into a target repository."""

from __future__ import annotations

from pathlib import Path
import argparse


FILES = {
    "AGENTS.md": "# AGENTS\n\nUse this file as the table of contents for repository-local harness context.\n",
    "ARCHITECTURE.md": "# Architecture\n\n## System Map\n\nTODO\n",
    "harness.yml": """version: 1

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

providers:
  observability:
    name: none
  issue_tracker:
    name: none

links: {}
""",
    "docs/CODEREVIEW.md": "# Code Review\n\n## Policy\n\nTODO\n\n## Review Guides\n\nTODO\n",
    "docs/ISSUE_TRACKING.md": "# Issue Tracking\n\n## System Of Record\n\nTODO\n\n## Intake Workflow\n\nTODO\n",
    "docs/OPERATIONS.md": "# Operations\n\n## Observability\n\nTODO\n\n## Performance\n\nTODO\n\n## Rollout\n\nTODO\n",
    "docs/STACK.md": "# Stack\n\n## Languages\n\nTODO\n\n## Frameworks\n\nTODO\n\n## Storage\n\nTODO\n",
    "docs/BACKEND.md": "# Backend\n\n## Service Architecture\n\nTODO\n\n## Backend Boundaries\n\nTODO\n",
    "docs/TESTING.md": "# Testing\n\n## Test Types\n\nTODO\n\n## Required Gates\n\nTODO\n",
    "docs/TOOLING.md": "# Tooling\n\n## Commands\n\nTODO\n\n## Required Gates\n\nTODO\n",
    "docs/DESIGN.md": "# Design\n\n## Principles\n\nTODO\n",
    "docs/FRONTEND.md": "# Frontend\n\n## UI Rules\n\nTODO\n",
    "docs/PLANS.md": "# Plans\n\n## Work Item Model\n\nActive work lives under `docs/exec-plans/current/`.\n",
    "docs/PRODUCT_SENSE.md": "# Product Sense\n\n## Product Goals\n\nTODO\n",
    "docs/QUALITY_SCORE.md": "# Quality Score\n\n## Current State\n\nTODO\n",
    "docs/RELIABILITY.md": "# Reliability\n\n## Expectations\n\nTODO\n",
    "docs/SECURITY.md": "# Security\n\n## Requirements\n\nTODO\n",
    "docs/design-docs/index.md": "# Design Docs Index\n",
    "docs/design-docs/core-beliefs.md": "# Core Beliefs\n",
    "docs/exec-plans/tech-debt-tracker.md": "# Tech Debt Tracker\n",
    "docs/generated/db-schema.md": "# Database Schema\n\nGenerated artifact placeholder.\n",
    "docs/product-specs/index.md": "# Product Specs Index\n",
    "docs/product-specs/new-user-onboarding.md": "# New User Onboarding\n",
    "docs/references/design-system-reference-llms.txt": "",
    "docs/references/nixpacks-llms.txt": "",
    "docs/references/uv-llms.txt": "",
}


DIRS = [
    "docs/design-docs",
    "docs/exec-plans/current",
    "docs/exec-plans/archive",
    "docs/generated",
    "docs/product-specs",
    "docs/references",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("target_repo")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    root = Path(args.target_repo).resolve()
    root.mkdir(parents=True, exist_ok=True)

    skipped = 0
    warnings: list[str] = []

    for rel_dir in DIRS:
        dir_path = root / rel_dir
        if dir_path.exists() and not dir_path.is_dir():
            warnings.append(
                f"skip directory {dir_path}: a non-directory path already exists there"
            )
            skipped += 1
            continue
        dir_path.mkdir(parents=True, exist_ok=True)

    created = 0
    for rel_path, content in FILES.items():
        path = root / rel_path
        if path.parent.exists() and not path.parent.is_dir():
            warnings.append(
                f"skip file {path}: parent path {path.parent} exists and is not a directory"
            )
            skipped += 1
            continue

        try:
            path.parent.mkdir(parents=True, exist_ok=True)
        except FileExistsError:
            warnings.append(
                f"skip file {path}: could not create parent directory {path.parent}"
            )
            skipped += 1
            continue

        if path.exists() and not args.force:
            skipped += 1
            continue

        if path.exists() and path.is_dir():
            warnings.append(f"skip file {path}: a directory already exists there")
            skipped += 1
            continue

        path.write_text(content)
        created += 1

    print(
        f"Seeded harness contract in {root} "
        f"({created} files written, {skipped} paths skipped)"
    )
    for warning in warnings:
        print(f"warning: {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
