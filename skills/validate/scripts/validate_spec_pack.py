#!/usr/bin/env python3
"""Compatibility entry point; use validate_work_item.py with explicit workflow."""
import sys
from validate_work_item import main
if __name__ == '__main__':
    print('Deprecated wrapper: use validate_work_item.py --workflow feature', file=sys.stderr)
    if '--workflow' not in sys.argv and '--check' not in sys.argv:
        sys.argv.extend(['--workflow', 'feature'])
    raise SystemExit(main())
