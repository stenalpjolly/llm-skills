---
name: bootstrapping-projects
description: >-
  Bootstraps a new project or initializes an existing directory with standard structures, documentation, planning files, version control setups, and framework-agnostic AI agent rules.
  Use when starting a new codebase or adding initial structure (git, docs, planning) to an existing project.
  Don't use if the project is already fully initialized with git, planning, and documentation frameworks.
---

# Bootstrapping Projects

## Overview
Automates the setup of folders, files, planning trackers, version control, and AI guidelines for new or ongoing codebases. This skill uses a combination of a deterministic Python script to create base structures and adaptive LLM logic to write personalized context.

## Bootstrapping Workflow

```mermaid
graph TD
    A[Start Bootstrapping] --> B[Analyze Current Directory & Context]
    B --> C{Files/Signals Found?}
    C -- Yes (Detect Tech Stack) --> D[Run bootstrap.py with Stack Args]
    C -- No (Ask or Infer) --> E[Run bootstrap.py with Generic/Selected Stack]
    D --> F[Create Base Directories & Standard Files]
    E --> F
    F --> G[LLM Populates Custom Files]
    G --> G1[README.md & Docs]
    G --> G2[PLAN.md & Milestones]
    G --> G3[Agnostic AGENTS.md Rules]
    G1 --> H[Verify & Present Project Tree]
    G2 --> H
    G3 --> H
    H --> I[Ready for Implementation]
```

## Best Practices
- **Analyze Before Action:** Always inspect the target directory first. Never blindly overwrite existing files; instead, augment them.
- **Combined Bootstrapping:** Use the helper Python script (`scripts/bootstrap.py`) to create empty directories and write boilerplate gitignores. Let the LLM fill in high-context files (`PLAN.md`, `README.md`, `AGENTS.md`).
- **Agnostic Agent Rules:** Ensure generated agent instructions (e.g., `AGENTS.md`) are standard and agnostic to specific IDE extensions or agent frameworks (e.g., compatible with Claude Code, Roo, Cursor, Kilo, etc.).
- **Plan-First Strategy:** Always start with a `PLAN.md` containing verifiable, realistic milestones before writing any application source code.
- **Strict Git Boundaries:** Always initialize a Git repository (`git init`) and a comprehensive `.gitignore` configured specifically for the target stack.

## Process

### 1. Analyze and Infer
1. Check if the directory is empty or contains existing configuration files (e.g., `package.json`, `pyproject.toml`, `go.mod`, etc.).
2. Deduce the target tech stack. If unclear, prompt the user with a few concise options.

### 2. Run the Bootstrap Script
Run the automated python script to generate the physical directory tree and default files:
```bash
python3 skills/bootstrapping-projects/scripts/bootstrap.py --stack [detected-stack]
```
*(Valid stacks: `generic`, `python`, `typescript`, `go`, `rust`)*

### 3. Customize and Hydrate
The script creates placeholder templates. Your job as the LLM is to overwrite them with project-specific detail:
1. **README.md:** Formulate a professional overview of the project, including quickstart instructions and architectural layouts.
2. **PLAN.md:** Establish phase-based goals and success criteria for the project's development.
3. **AGENTS.md:** Customize general coding practices, formatting rules, and testing strategies for the selected tech stack.

### 4. Verification
Run a directory tree listing (excluding node_modules/venv/etc.) to confirm structure matches expectation:
```bash
git status && ls -la
```

## Common Pitfalls
- **Overwriting Work:** Destroying existing user code during the setup of a pre-existing directory.
- **Template Bloat:** Creating folder structures (e.g., deeply nested `domain/application/infrastructure` directories) before a single line of actual feature code is written. Keep it minimal first.
- **Generic Gitignore:** Forgetting to configure stack-specific exclusions, leading to commit pollution (e.g., committing `node_modules` or `.venv`).
