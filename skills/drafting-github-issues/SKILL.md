---
name: drafting-github-issues
description: >-
  Converts project specifications, task lists, or architectural maps into granular GitHub issue drafts. Use when breaking down a project into actionable sprint tasks. Don't use for pushing issues directly to GitHub.
---

# Drafting GitHub Issues

This skill translates project requirements or architecture maps into atomic, actionable tasks. 

## Rules
1. **Granularity.** Do not bundle multiple disjointed tasks into a single issue unless they are tightly coupled. Keep tasks focused and atomic.
2. **Establish Dependencies.** If one task depends on another, the issue MUST list the dependency clearly.
3. **Strict Formatting.** You must format every drafted issue exactly according to the template in `references/issue-template.md` if available, or a standard markdown issue format.

## Workflow
1. Read the provided project context, architecture map, or task list.
2. Group the tasks into logical Epics (e.g., "Authentication", "Dashboard").
3. Draft the issues using the standard reference template.
4. Save all drafted issues into a single file named `drafted_issues.json`.
5. Hand off to the `managing-github-backlog` skill (using `@skills/managing-github-backlog`) and ask it to create/update the issues on GitHub.
6. Once the issues are successfully updated by the backlog manager, clean up any temporary files (e.g., `drafted_issues.json`).
