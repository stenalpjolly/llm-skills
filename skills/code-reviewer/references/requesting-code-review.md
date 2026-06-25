# Requesting Code Review Protocol

This protocol defines how and when to request reviews from the `code-reviewer` subagent.

## When to Request Review
*   After completing EACH task in subagent-driven development.
*   After major feature completion or refactoring.
*   Before merging any branch to the `main` branch.

## Review Request Process
1.  **Get Git SHAs**:
    ```bash
    BASE_SHA=$(git rev-parse HEAD~1)
    HEAD_SHA=$(git rev-parse HEAD)
    ```
2.  **Dispatch Subagent**: Invoke the `code-reviewer` subagent via the Task tool, providing:
    *   `WHAT_WAS_IMPLEMENTED`: Summary of implemented changes.
    *   `PLAN_OR_REQUIREMENTS`: Target requirements or specs.
    *   `BASE_SHA`: Base commit SHA.
    *   `HEAD_SHA`: Head commit SHA.
    *   `DESCRIPTION`: Explanation of context or special details.
3.  **Act on Feedback**:
    *   Fix **Critical (🔴)** and **High (🟠)** issues immediately before committing or proceeding.
    *   Note **Medium (🟡)** and **Low (🟢)** findings for later cleanup.
