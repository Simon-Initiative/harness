# Validation

Primary command:

```bash
python3 <skills_root>/validate/scripts/validate_work_item.py <work_item_dir> --check prd
```

Resolve `<skills_root>` as the directory that contains the installed harness skills. Do not resolve the validator path relative to the repository or current working directory.

This is a hard gate. If validation fails, fix the PRD and rerun the validator.
