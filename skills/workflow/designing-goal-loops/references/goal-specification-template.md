# Goal Specification Template

This template defines the exact structure and required fields for an autonomous goal loop (`/goal` or subagent execution). Every section must be fully populated with concrete, verified information from the current workspace before launching an unmonitored agent.

---

```markdown
# Goal Specification: [Clear, Actionable Title]

## 1. Context Pillar (Where & Why)
- **Objective**: [1-2 sentence summary of what is being built or fixed and why it matters.]
- **Primary Target Files**:
  - `[Absolute path to primary file to modify]`
  - `[Absolute path to test file to create/modify]`
- **Reference Modules**:
  - `[Absolute path to read-only interface or helper module for context]`
- **Architectural Constraints**:
  - [Constraint 1: e.g., Must maintain strict backwards compatibility with existing API signature.]
  - [Constraint 2: e.g., Use existing error types from `errors.ts`; do not introduce new custom exception classes.]

## 2. Task Pillar (What & Scope)
- **Vertical Slice Objective**: [The single, atomic behavior to implement and verify in this execution cycle.]
- **Execution Steps**:
  1. Write/update test asserting `[specific behavior]` in `[target test file]`.
  2. Run verification command to confirm RED state (failing as expected).
  3. Implement minimal code in `[target source file]` to satisfy the test.
  4. Run verification command to confirm GREEN state (passing cleanly).
  5. Refactor internal structure if necessary while maintaining GREEN state.
- **Out of Scope (Anti-Goals)**:
  - [Anti-Goal 1: Do NOT refactor adjacent modules or clean up pre-existing dead code.]
  - [Anti-Goal 2: Do NOT add configuration parameters, flags, or speculative features not explicitly listed above.]
  - [Anti-Goal 3: Do NOT modify existing tests to force a failing implementation to pass.]

## 3. Verification Pillar (Proof of Work & Backpressure)
- **Executable Verification Commands**:
  ```bash
  # Primary test command (MUST exit 0)
  [Exact shell command, e.g., npm test path/to/test.ts -t "test_name"]

  # Lint / Typecheck command (MUST exit 0)
  [Exact shell command, e.g., npm run lint && tsc --noEmit]
  ```
- **Proof of Work (Expected Output)**:
  - [Describe what terminal output or assertion confirms success, e.g., "All 4 tests passing in `math.test.ts` with no type errors."]
- **Backpressure & Recovery Strategy**:
  - **On Test Failure**: Analyze stack trace and fix implementation logic; do not disable or alter test assertions.
  - **On Compilation/Syntax Error**: Run the linter/compiler to locate the exact line and make surgical corrections.
  - **Loop Limit**: If verification fails after 3 consecutive attempts, stop and report the specific blocker and error log rather than guessing or spinning indefinitely.
```
