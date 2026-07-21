---
name: implementing-test-driven-issue-resolution
description: >-
  Converts user assumptions, feature requests, or bug reports into verified, test-driven code changes. 
  Searches GitHub for existing tickets, creates/updates them with user confirmation, and strictly applies 
  the incremental Red-Green-Refactor (TDD) micro-loop. Use when starting any new feature, bugfix, 
  or requirement resolution requiring issue tracking or high-integrity code implementation. 
  Don't use for bulk issues creation without user interaction or non-testable codebase maintenance.
---

# Implementing Test-Driven Issue Resolution

This skill manages the lifecycle of a user-requested feature or bugfix from assumption to verified code, using a strict **TDD (Test-Driven Development) issue resolution loop**. It combines issue tracking via GitHub, requirement clarification, and Red-Green-Refactor test execution.

## TDD Philosophy: Behaviors vs. Implementations

*   **Core Principle**: Tests must verify behavior through public interfaces, not internal implementation details. Code can change entirely; tests should not have to.
*   **Good Tests (Integration-style)**: Exercise real code paths through public APIs. They describe *what* the system does, not *how* it does it (e.g. "user can checkout with valid cart"). These tests survive internal refactorings because they are decoupled from the code's internal structure.
*   **Bad Tests (Coupled to Implementation)**: Mock internal collaborators, assert against private methods, or verify behavior through external shortcuts (like direct DB querying instead of using the service interface). A key warning sign: your test breaks during a refactor even though the external behavior is entirely unchanged.

---

## Anti-Pattern: Horizontal Slicing

**DO NOT write all tests first, then all implementation.** This is "horizontal slicing"—treating RED as "write all tests" and GREEN as "write all code." It leads to brittle tests based on imagined instead of actual behavior, making you outrun your headlights and commit to test structures before understanding implementation details.

**Correct Approach (Vertical Slicing via Tracer Bullets)**: One test → one implementation → repeat. Each test responds to what you learned in the previous cycle, maintaining focus on observable behavior.

```text
WRONG (Horizontal):
  RED:   test1, test2, test3, test4, test5
  GREEN: impl1, impl2, impl3, impl4, impl5

RIGHT (Vertical):
  RED→GREEN: test1→impl1
  RED→GREEN: test2→impl2
  RED→GREEN: test3→impl3
  ...
```

---

## Core Rules

1.  **Deconstruct Assumptions**: Begin by checking the codebase to convert vague user inputs or feature requests into precise technical requirements.
2.  **Verify Existing Tickets First**: Before drafting a new issue, always check if a tracking ticket or GitHub issue already exists for the work. Never create duplicate issues.
3.  **Mandatory User Confirmation**: Do not start implementing code until the user has confirmed the drafted issue description, reproduction steps, and high-level implementation plan.
4.  **TDD Loop (Red-Green-Refactor Mechanics)**: 
    *   **No "Horizontal Splurging"**: You are strictly forbidden from writing multiple tests at once. You must follow the vertical slicing incremental loop: **Write 1 Test -> See it Fail (Red) -> Write 1 Fix -> See it Pass (Green) -> Refactor**. Repeat this loop for every sub-feature.
    *   **Impose Backpressure**: Use automated assertions and strong typing (TypeScript/Node.js) as backpressure to prevent guessing or playing in the mud with low-quality code.
    *   **Verification of Integrity**: Never modify an existing test to make a failing implementation pass. If a test must change, it must be because the requirement changed, not because the code is difficult to write.

---

## Workflow Execution

### Step 1: Analyze Input & Identify Expectations
Check the codebase using search tools (`grep`, `glob`, `read`) to understand the feasibility of the request, locate relevant modules, and transform user assumptions into specific features/bug definitions.
*   Read `CONTEXT.md` (if it exists) so that test names and interface vocabulary match the project's domain language.
*   Respect existing Architecture Decision Records (ADRs) in the target modules.

### Step 2: Check or Sync GitHub Issues
Run the helper script `manage_github_issue.py` to search for existing issues matching the request:
```bash
python3 skills/testing/implementing-test-driven-issue-resolution/scripts/manage_github_issue.py --repo {owner/repo} --search "{query}"
```
*   **If found**: Return the issue URL and details. If requested, update it using the script.
*   **If not found**: Scaffold and create the issue using:
    ```bash
    python3 skills/testing/implementing-test-driven-issue-resolution/scripts/manage_github_issue.py --repo {owner/repo} --create --title "{title}" --body-file "{issue_body_path}"
    ```

### Step 3: Present for User Confirmation
Before writing any code, show the user:
*   The issue ID/URL.
*   The reproduction steps or use-case.
*   The proposed test-case structure and target file.
*   Confirm with the user what interface changes are needed and which behaviors to test (prioritize behavior, not implementation steps).
*   Ask: *"What should the public interface look like? Which behaviors are most important to test?"*
*   Identify opportunities for deep modules (small interfaces, deep implementations).
*   Ask for the user's explicit confirmation before proceeding.

### Step 4: Write the Failing Test (Red Phase)
Write a single, focused test case or script (e.g. in Vitest, Jest, or Pytest) that directly asserts the next small piece of behavior through a public interface.
*   Do not write multiple tests at once (avoid horizontal slicing).
*   Run the test command (e.g. `npm test`) to confirm that it **fails**.
*   Verify that the failure is related to the missing logic (e.g., `ReferenceError: add is not defined` or a failed assertion) and not a configuration error.
*   Capture the failing output as proof of the Red state.

### Step 5: Implement the Solution (Green Phase)
Surgically edit the codebase to resolve the failing test.
*   Write the simplest, most minimal code that satisfies the test. Do not build for the future; focus strictly on making the current "Red" test pass.
*   Run the test command. All tests must be Green.
*   The transition from Red to Green is the "Proof of Work" for the developer.

### Step 6: Verify and Clean Up (Refactor Phase)
Improve the code structure while maintaining the "Green" state.
*   **Never refactor while RED.** Get to GREEN first.
*   Look for refactor candidates:
    *   [ ] **Duplication** → Extract into a dedicated function or class.
    *   [ ] **Long Methods** → Break into smaller private helper functions (while keeping tests focused solely on the public interface).
    *   [ ] **Shallow Modules** → Combine modules or deepen them to hide complexity.
    *   [ ] **Feature Envy** → Move business/computational logic closer to where the data actually lives.
    *   [ ] **Primitive Obsession** → Introduce descriptive value objects/domain types instead of generic primitives.
    *   [ ] **Structural Revelations** → Evaluate and refactor existing code that the newly added code reveals as problematic, messy, or brittle.
*   **Safety Net**: Rerun the tests after every single change. If they turn Red, revert the change immediately.
*   Execute standard build, linting, and typecheck checks (e.g., `tsc`, `npm run lint`) to ensure codebase health.
*   Remove any temporary test configurations or dummy files.

### Step 7: Comment and Close the Issue with PR Details
After committing and verifying the changes, add a new comment containing the PR details and git commit ID (SHA) to the tracking GitHub issue, and then close it. Do not update or overwrite the main issue description (body), so that the original description remains intact (matching JIRA specifications).

Close and comment on the issue using:
```bash
python3 skills/testing/implementing-test-driven-issue-resolution/scripts/manage_github_issue.py --repo {owner/repo} --update {issue_number} --comment "Resolved in PR #123 (Commit: {commit_sha})" --state closed
```

---

## Checklist Per Cycle

Ensure each incremental TDD loop meets the following criteria:
- [ ] Test describes behavior, not internal implementation details
- [ ] Test exercises the system exclusively through its public interface
- [ ] Test is resilient and would survive a complete internal refactoring
- [ ] Code written is the absolute minimum required to satisfy this specific test
- [ ] No speculative features, flexibility, or unnecessary abstractions were added

---

## Example Micro-Workflow (TypeScript + Vitest)

### Step 1: Red (Failing Test)
```typescript
// math.test.ts
import { describe, it, expect } from 'vitest';
import { add } from './math';

describe('add', () => {
  it('should sum two numbers', () => {
    expect(add(2, 2)).toBe(4); // Fails: ReferenceError: add is not defined
  });
});
```

### Step 2: Green (Minimal Pass)
```typescript
// math.ts
export const add = (a: any, b: any) => {
  return 4; // Passes: Minimal code to satisfy the test
};
```

### Step 3: Refactor (Clean Code with Type Safety)
```typescript
// math.ts
/**
 * Sums two numbers with explicit type safety.
 */
export const add = (a: number, b: number): number => {
  return a + b; // Passes: Proper implementation with safety net
};
```
