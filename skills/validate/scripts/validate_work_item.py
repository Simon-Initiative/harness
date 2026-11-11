#!/usr/bin/env python3
"""Check selected nonempty artifacts and canonical structured requirements."""
from pathlib import Path
import argparse
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'requirements/scripts'))
from requirements_trace import load, validate
import yaml


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('work_item_dir', type=Path)
    p.add_argument('--workflow', choices=['feature', 'work', 'bug', 'prototype', 'epic'], default='work')
    p.add_argument('--check', choices=['prd', 'fdd', 'plan', 'design', 'requirements'])
    p.add_argument('--file')
    p.add_argument('--repo-root', type=Path)
    a = p.parse_args()
    try:
        root = a.work_item_dir.resolve()
        if not root.is_dir(): raise ValueError('work item directory does not exist')
        if a.file and a.check != 'design': raise ValueError('--file is only supported for design')
        names = []
        if a.check == 'design':
            if not a.file: raise ValueError('--file is required for design (relative to work item)')
            names = [a.file]
        elif a.check and a.check != 'requirements': names = [a.check + '.md']
        elif not a.check and a.workflow in ('feature', 'epic'): names = ['plan.md']
        for name in names:
            path = (root / name).resolve()
            if not path.is_relative_to(root) or not path.is_file() or not path.read_text().strip():
                raise ValueError(f'missing, empty or out-of-scope artifact: {name}')
        req = root / 'requirements.yml'
        if req.exists() or a.check == 'requirements' or (not a.check and a.workflow == 'feature'):
            validate(load(req), root, a.repo_root)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        p.exit(1, f'ERROR: {exc}\n')
    print('Selected artifact presence and requirements structure valid; no execution or semantic coverage claim.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
