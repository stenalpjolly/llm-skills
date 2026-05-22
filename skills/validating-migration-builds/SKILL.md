---
name: validating-migration-builds
description: >-
  Provides build and lint validation checks for migrated Angular and Python code. Use when self-correcting compilation failures, syntax errors, or linting violations in migrated modules. Don't use for drafting GitHub issue templates, codebase scans, or writing the code translation itself.
---

# Validating Migration Builds

This skill executes self-correcting validation loops by running local builders/compilers, parsing error streams, and presenting actionable fixes.

## Rules
1. **Never commit unchecked code.** Before finalizing any frontend or backend migration task, always execute verification scripts to ensure zero compilation or syntax warnings.
2. **Execute build checks.** Use `python3 scripts/check_angular_compile.py` to compile Angular components.
3. **Execute python linting.** Use `python3 scripts/check_python_lint.py` to syntax check FastAPI endpoints.
4. **Fix and retry.** If any checks output failures, feed the error back into your context, correct the source file, and run the validator script again until it compiles cleanly.

## Execution
Run verification scripts depending on the module:
```bash
# Frontend Compilation Check
python3 scripts/check_angular_compile.py --target {path_to_angular_project_or_file}

# Backend Syntax/Compile Check
python3 scripts/check_python_lint.py --file {path_to_fastapi_python_file}
```
