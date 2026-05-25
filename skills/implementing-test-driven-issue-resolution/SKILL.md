---
name: implementing-test-driven-issue-resolution
description: >-
  Converts user assumptions, feature requests, or bug reports into verified, test-driven code changes. Searches GitHub for existing tickets, creates/updates them with user confirmation, authors a failing test (Red phase), and implements the fix to make it pass (Green phase). Use when starting any new feature, bugfix, or requirement resolution. Don't use for bulk issues creation without user interaction or generic codebase maintenance.
---

# Implementing Test-Driven Issue Resolution

This skill manages the lifecycle of a user-requested feature or bugfix from assumption to verified code, using a strict **TDD (Test-Driven Development) issue resolution loop**. It combines issue tracking via GitHub, requirement clarification, and Red-Green-Refactor test execution.

## Core Rules

1.  **Deconstruct Assumptions**: Begin by checking the codebase to convert vague user inputs or feature requests into precise technical requirements.
2.  **Verify Existing Tickets First**: Before drafting a new issue, always check if a tracking ticket or GitHub issue already exists for the work. Never create duplicate issues.
3.  **Mandatory User Confirmation**: Do not start implementing code until the user has confirmed the drafted issue description, reproduction steps, and high-level implementation plan.
4.  **TDD Loop (Red-Green-Refactor)**: 
    *   **Red**: Write a failing test case or reproduction harness *before* writing the fix. Execute it to verify that it fails under the current codebase.
    *   **Green**: Apply the minimal necessary code edits to make the test pass.
    *   **Refactor/Verify**: Run the test suite again to confirm success, and run project compilers, linters, or formatters to ensure zero regressions.

## Workflow Execution

### Step 1: Analyze Input & Identify Expectations
Check the codebase using search tools (`grep`, `glob`, `read`) to understand the feasibility of the request, locate relevant modules, and transform user assumptions into specific features/bug definitions.

### Step 2: Check or Sync GitHub Issues
Run the helper script `manage_github_issue.py` to search for existing issues matching the request:
```bash
python3 skills/implementing-test-driven-issue-resolution/scripts/manage_github_issue.py --repo {owner/repo} --search "{query}"
```
*   **If found**: Return the issue URL and details. If requested, update it using the script.
*   **If not found**: Scaffold and create the issue using:
    ```bash
    python3 skills/implementing-test-driven-issue-resolution/scripts/manage_github_issue.py --repo {owner/repo} --create --title "{title}" --body-file "{issue_body_path}"
    ```

### Step 3: Present for User Confirmation
Show the user:
*   The issue ID/URL.
*   The reproduction steps or use-case.
*   The proposed test-case structure and target file.
*   Ask for the user's explicit confirmation using a "Yes or No, with suggestions" question format before proceeding.
*   If the user answers "No" or proposes a change/suggestion, revalidate the requirements, recreate the plan, and present it for confirmation again.

### Step 4: Write the Failing Test (Red Phase)
Write a unit test, integration test, or script that directly asserts the new feature or exercises the bug.
*   Run the test command (e.g. `pytest`, `npm test`) to confirm that it **fails**.
*   Capture the failing output to demonstrate the code is currently lacking the feature or broken.

### Step 5: Implement the Solution (Green Phase)
Surgically edit the codebase to resolve the issue. Avoid writing non-essential helper code. Focus exclusively on satisfying the failing test.

### Step 6: Verify and Clean Up (Refactor Phase)
1.  Run the test suite again to confirm the test now **passes**.
2.  Execute standard build, linting, and typecheck checks to ensure code health.
3.  Remove any temporary test configurations or dummy files.

### Step 7: Close the Issue with Commit Reference
After committing the verified changes, close the tracking GitHub issue. Ensure that you retrieve the git commit ID (SHA) of the fix and refer to it when closing the issue to establish a clear link between the resolution and the code.
Close the issue using:
```bash
python3 skills/implementing-test-driven-issue-resolution/scripts/manage_github_issue.py --repo {owner/repo} --update {issue_number} --state closed
```
