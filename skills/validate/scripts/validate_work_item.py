#!/usr/bin/env python3
"""Validate work item markdown artifacts in docs/exec-plans/current/."""

from __future__ import annotations

from pathlib import Path
import argparse
import re
import sys

REQUIRED = {
    'prd': ['prd.md'],
    'fdd': ['fdd.md'],
    'plan': ['plan.md'],
    'all': ['prd.md', 'fdd.md', 'plan.md'],
}

HEADER_PATTERN = re.compile(r'^#', re.M)
TODO_PATTERN = re.compile(r'\bTODO\b')


def check_file(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f'missing required file: {path.name}']
    text = path.read_text()
    if not HEADER_PATTERN.search(text):
        errors.append(f'{path.name} has no markdown headings')
    if TODO_PATTERN.search(text):
        errors.append(f'{path.name} contains unresolved TODO markers')
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('work_item_dir', help='Work item directory, e.g. docs/exec-plans/current/my-work-item')
    parser.add_argument('--check', default='all', choices=['all', 'prd', 'fdd', 'plan', 'design'])
    parser.add_argument('--file')
    args = parser.parse_args()

    work_item_dir = Path(args.work_item_dir)
    if not work_item_dir.exists():
        print(f'ERROR: work item directory not found: {work_item_dir}')
        return 1

    errors: list[str] = []
    if args.check == 'design':
        if not args.file:
            print('ERROR: --file is required for --check design')
            return 1
        errors.extend(check_file(Path(args.file)))
    else:
        for rel in REQUIRED[args.check]:
            errors.extend(check_file(work_item_dir / rel))

    if args.check in {'all', 'prd'} and not (work_item_dir / 'requirements.yml').exists():
        errors.append('requirements.yml is missing')

    if errors:
        for error in errors:
            print(f'ERROR: {error}')
        return 1
    print('Work item validation passed.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
