#!/usr/bin/env python3
"""Create only a missing routing entry point; never overwrite repository files."""
from pathlib import Path
import argparse


def seed(root):
    root.mkdir(parents=True, exist_ok=True)
    path = root / 'AGENTS.md'
    links = [p for p in ('README.md', 'ARCHITECTURE.md', 'docs/TOOLING.md', 'docs/TESTING.md', 'docs/CODEREVIEW.md', 'harness.yml') if (root / p).is_file()]
    content = '# Repository guidance\n\nStart with the request and inspect affected code progressively.\n'
    if links:
        content += '\nRead these existing sources when relevant:\n\n' + ''.join(f'- [{p}]({p})\n' for p in links)
    content += '\nDiscover verification commands from repository tooling and CI before running checks.\nRecord unresolved knowledge honestly; this entry point does not establish operational readiness.\n'
    try:
        with path.open('x') as f: f.write(content)
        return 'Created AGENTS.md; adapt its routing to repository facts.'
    except FileExistsError:
        return 'Preserved existing AGENTS.md and all repository documentation.'


def main():
    p = argparse.ArgumentParser(description=__doc__); p.add_argument('target_repo', type=Path)
    a = p.parse_args()
    try: print(seed(a.target_repo))
    except OSError as exc: p.exit(1, f'ERROR: {exc}\n')


if __name__ == '__main__': main()
