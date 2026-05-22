---
name: scanning-codebase
description: >-
  Scans a Next.js directory to map out routes, components, and API endpoints into a structured JSON format. Use when analyzing a React/Next.js project for migration to understand its architecture and dependencies. Don't use for modifying code, running tests, or analyzing non-React codebases.
---

# Scanning Codebase

This skill extracts the architectural blueprint of a Next.js application. 

## Rules
1. **Never guess the file structure.** Always use the provided `scan_nextjs.py` script to get the exact state of the repository.
2. **Ignore build artifacts.** The script automatically ignores `node_modules` and `.next`. Do not attempt to scan them manually.
3. **Identify boundaries.** Pay special attention to the separation between UI components (`components/`, `pages/`, `app/`) and backend routes (`api/`).

## Execution
Run the scanner script to generate the architecture map:
```bash
python3 scripts/scan_nextjs.py --path {path_to_nextjs_project}
```
Save the output to `architecture_map.json` for the next skill to use.
