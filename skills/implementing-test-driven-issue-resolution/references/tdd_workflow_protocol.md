# Test-Driven Issue Resolution (TDIR) Protocol

This protocol defines the strict Red-Green-Refactor development pipeline required to resolve user assumptions, feature requests, or bug reports in a safe, verifiable manner.

---

## 1. Requirement & Expectation Identification

Before writing code or issues, map the user's raw statement to a concrete technical categorization.

### Feature Request vs. Bug Identification

| Input Category | Characteristics | Core Action |
|:---|:---|:---|
| **Feature Request** | • Introduces entirely new workflows or behaviors.<br>• Modifies or extends API surfaces / configuration options. | Map to target modules, determine extension points, and design a clean API seam. |
| **Bug Report** | • Existing behavior does not function as intended.<br>• Code crashes, errors out, or enters incorrect states. | Isolate the exact file and lines, trace variable states, and understand the failing condition. |

---

## 2. GitHub Issue Lifecycle & Synching

Always maintain a strict correlation between active changes and GitHub tracking tickets.

```
                  ┌──────────────────────────────┐
                  │      Analyze User Input      │
                  └──────────────┬───────────────┘
                                 │
                                 ▼
              /─────────────────────────────────────\
             <  Does matching issue already exist?   >
              \─────────────────────────────────────/
                         /               \
                 YES    /                 \   NO
                       ▼                   ▼
          ┌─────────────────────────┐ ┌─────────────────────────┐
          │ Return URL to User &    │ │ Create standard Issue   │
          │ confirm if edits needed │ │ via manage_github_issue │
          └─────────────────────────┘ └─────────────────────────┘
```

### Script Usage
- **Search Query**: Run `--search` to find duplicate issues before creating any new ticket.
- **Creation**: Run `--create` using `--body-file` pointing to a prepared issue description.
- **Update**: Run `--update <issue_number>` to append comments or change states.

---

## 3. The 4-Stage Test-Driven Loop

```
  ┌──────────────┐      Verify       ┌──────────────┐
  │   RED STEP   │──────────────────>│  GREEN STEP  │
  │ Failing Test │  (Capture trace)  │ Minimal Fix  │
  └──────────────┘                   └──────┬───────┘
         ▲                                  │
         │                                  │ Run tests again
         │                                  ▼
  ┌──────┴───────┐      Regress      ┌──────────────┐
  │  Clean Up /  │<──────────────────│  REFACTOR /  │
  │ Commit Files │  (Zero-warnings)  │ VERIFY STEP  │
  └──────────────┘                   └──────────────┘
```

### Stage 1: Write a Failing Test (RED)
Write the test case *before* making any changes to production source files.
- **Convention**: Name tests following standard patterns (e.g. `tests/test_feature_name.py`, `src/__tests__/featureName.test.ts`).
- **Assertion**: Use direct, explicit assertions (e.g. `assert results == expected`). Avoid loose assertions or catching exceptions silently.
- **Verify Failure**: Execute the test command and **confirm it fails**. Save the failing terminal stack trace to verify the test is valid and correctly targets the issue.

### Stage 2: Implement the Minimal Solution (GREEN)
Surgically write the minimum code required to satisfy the failing test.
- **Rule of Simplicity**: Do not write speculative helper code, abstractions, or unused configuration options.
- **Match Style**: Strictly adhere to neighboring conventions, names, and patterns.
- **Surgical Edits**: Touch only the lines directly related to the fix.

### Stage 3: Verify the Solution (REFACTOR)
Run the test again to verify it has turned green.
- **Verify Green**: Confirm the test suite executes and passes completely.
- **Comprehensive Verification**: Execute project-specific compilers, linters, and checkers (e.g., `tsc`, `npm run lint`, `ruff check .`) to verify that no style violations or build errors are introduced.

### Stage 4: Commit and Clean Up
- **Clean Artifacts**: Delete any test databases, logs, or intermediate workspace noise before preparing commits.
- **Record**: Ensure the tracking GitHub Issue is updated with a comment containing the final PR/Commit links, and then closed. Never overwrite or edit the main issue description with commit details, ensuring the JIRA-like description is preserved.
