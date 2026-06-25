---
name: code-reviewer
description:
  Use this skill to review code. It supports both local changes (staged or working tree)
  and remote Pull Requests (by ID or URL). It focuses on correctness, maintainability,
  and adherence to project standards.
---

# Code Reviewer

This skill guides the agent in conducting professional and thorough code reviews for both local development and remote Pull Requests in the `mcp-toolbox` ecosystem.

## Core Principle
**Technical correctness over social comfort. Verify before implementing. Ask before assuming. Evidence before claims.**
No performative agreement (e.g., "You're absolutely right!", "Great point!", "Thanks for [anything]"). Speak with technical rigor and evidence-based claims.

---

## Workflow

### 1. Determine Review Target
*   **Remote PR**: If the user provides a PR number or URL (e.g., "Review PR #123"), target that remote PR.
*   **Local Changes**: If no specific PR is mentioned, or if the user asks to "review my changes", target the current local file system states (staged and unstaged changes).
*   **Identify Submodules**: Determine which submodules are modified (e.g., `mcp-toolbox-sdk-java`, `mcp-toolbox-sdk-js`, `mcp-toolbox-sdk-go`, `mcp-toolbox-sdk-python`, `mcp-toolbox`).

### 2. Pre-Review ADR Gate (Mandatory)
Before any review executes, the ADR gate runs:
1.  **Classify**: Trivial changes (typos, deps, tests-only) skip the gate.
2.  **Discover**: Scan `docs/adr/`, `_project_specs/`, or git history for linked ADRs and specs.
3.  **Enforce**: If no ADRs are found for non-trivial changes:
    *   *Interactive (default)*: Draft ADR from git history and ask the user to confirm.
    *   *Unattended (CI)*: Write as `Status: proposed` and proceed.
4.  **Inject**: Feed discovered ADRs + specs into the review prompt as architectural context.

### 3. Preparation & Verification Gates

#### For Remote PRs:
1.  **Checkout**: Use the GitHub CLI to checkout the PR.
    ```bash
    gh pr checkout <PR_NUMBER>
    ```
2.  **Context**: Read the PR description and comments to understand the goal and history.
3.  **PR Template & Rule Check**: Verify that the PR description follows the standardized template (sections: Summary, Expectation & Implementation, Test cases, Acceptance criteria, Breaking changes) and does *not* mention internal agent customization files (like `AGENTS.md`).
4.  **Preflight**: Execute verification checks according to the modified submodules (see Preflight Verification below).

#### For Local Changes:
1.  **Identify Changes**: Check status (`git status`) and read diffs (`git diff` and/or `git diff --staged`).
2.  **Preflight (Optional)**: If changes are substantial, run the Preflight Verification below.

---

## Preflight Verification (The Iron Law)
**NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE.**
To claim tests pass or the build succeeds, run the verification command, read the output, confirm, and provide the exact command run and its result. Avoid red flags like using "should", "probably", or "seems to".

### For Java SDK (`mcp-toolbox-sdk-java`):
1.  **Formatting Check**:
    *   Run `google-java-format` directly with JVM module exports for `jdk.compiler` on JDK 22+ (do not use `fmt-maven-plugin`).
2.  **Local Tests**:
    *   Run JUnit tests locally, excluding E2E integration tests:
        ```bash
        mvn clean test -Dtest="*Test,!*E2ETest"
        ```
    *   If running under JDK 22+, always include the VM property `-Dnet.bytebuddy.experimental=true`.
3.  **Coverage**:
    *   Verify coverage locally using the Maven Jacoco check plugin. If running on JDK 22+ (where static `jacoco:check` fails due to class version 70), generate the report using `mvn jacoco:report` and verify coverage by reading `target/site/jacoco/jacoco.csv`.
    *   Ensure all modified and new classes have **100.00% line coverage**.

### For Reference Repositories (Go, JS, Python SDKs):
1.  **Upstream Check**:
    *   Always pull the latest changes from their upstream/origin (`git pull` or `git fetch` and merge/rebase on target branch) to ensure reference checks are based on the latest codebase state.

---

## 4. In-Depth Analysis
Analyze the code changes based on the following pillars, paying close attention to repo-specific rules:

### Java-Specific Code Correctness & Patterns (`mcp-toolbox-sdk-java`)
*   **100% Coverage**: Verify that all modified or newly introduced Java classes achieve **100.00% line coverage** in the JUnit tests.
*   **Asynchronous Initialization**: Ensure async initialization caches and reuses a single `CompletableFuture<Void> initFuture` synchronized on its creation (instead of a boolean flag with method-level synchronization).
*   **HTTP Headers**: Ensure HTTP header processing/assertions are case-insensitive or normalize keys to lowercase.
*   **Asynchronous JUnit Tests**: Ensure tests executing async operations have class-level or method-level `@Timeout` annotations.
*   **File Length**: Ensure no single Java file exceeds **700 lines**.
*   **Mutable Defaults**: Verify that default values injected from tool schemas into invocation arguments are deep-copied rather than passed by reference.
*   **API Records**: Verify that any new fields added to Java record structures used in public APIs define a secondary constructor mapping to the original properties to preserve backward compatibility.

### General Review Dimensions
*   **ADR Compliance**: Conformance to documented decisions, no undocumented architectural shifts (Contradiction = Critical; Undocumented Shift = High; Stale ADR = Medium).
*   **Correctness**: Does the code achieve its stated purpose without bugs or logical errors?
*   **Security**: Ensure no SQL injection, XSS, exposed secrets, insecure cryptos, or missing auth on endpoints.
*   **Performance**: Verify there are no memory leaks, N+1 query patterns, or missing database indexes.
*   **Readability & Maintainability**: Verify code clarity, modularity, and adherence to design patterns.

---

## 5. Feedback Protocols & Response Structure

### Rigor and Evidence Requirements
*   **Justification and Confidence**: For every identified issue (Critical, High, Medium, Low), the reviewer must explicitly provide:
    *   **Justification**: A clear technical explanation of *why* this is an issue, what could go wrong, or the specific project rule it violates.
    *   **Confidence Score**: A percentage (e.g. `100%`, `90%`) indicating confidence that this is a true positive, accompanied by a brief reasoning (e.g. "Confirmed by checking execution flow in auth.ts", "Potential issue, need to verify runtime behavior").

### Receiving Feedback Protocol
*   See detailed protocol at [code-review-reception.md](file:///Users/stenalpjolly/github/Google/opensource/.agents/skills/code-reviewer/references/code-review-reception.md).
*   Follow the pattern: READ → UNDERSTAND → VERIFY → EVALUATE → RESPOND → IMPLEMENT.
*   Strictly avoid performative agreement and enforce technical correctness over social comfort.

### Requesting Review Protocol
*   See detailed protocol at [requesting-code-review.md](file:///Users/stenalpjolly/github/Google/opensource/.agents/skills/code-reviewer/references/requesting-code-review.md).
*   Request review after EACH task in subagent-driven development.

### Verification Gates Protocol
*   See detailed protocol at [verification-before-completion.md](file:///Users/stenalpjolly/github/Google/opensource/.agents/skills/code-reviewer/references/verification-before-completion.md).
*   Apply the Iron Law of verification to every completion claim.

### Feedback Response Template
```markdown
## Code Review Results

### 🔴 Critical Issues (Must Fix)
1. **SQL Injection in userController.ts:45**
   - **Issue**: User input directly interpolated into query
   - **Justification**: Directly interpolating raw user input into database queries allows attackers to execute arbitrary SQL commands, bypassing authentication or accessing unauthorized data.
   - **Confidence Score**: 100% (Static code analysis clearly shows `req.query.id` is concatenated into the query string)
   - **Fix**: Use parameterized query
   - **Code**: `db.query('SELECT * FROM users WHERE id = $1', [userId])`

### 🟠 High Issues (Should Fix)
1. **Missing authentication on /api/admin endpoints**
   - **Issue**: Admin routes accessible without auth
   - **Justification**: Exposing administrative actions without authorization allows unauthenticated users to perform sensitive operations.
   - **Confidence Score**: 100% (The route handler does not call `verifyAuthToken` middleware)
   - **Fix**: Add auth middleware

### 🟡 Medium Issues (Fix Soon)
1. **N+1 query in getOrders function**
   - **Issue**: Order retrieval queries inside user loop
   - **Justification**: Querying the database sequentially inside a loop creates significant performance overhead as dataset size grows.
   - **Confidence Score**: 90% (Looping pattern is clear; verify if ORM has lazy loading configured elsewhere)
   - **Fix**: Eager load or fetch with a batch query

### 🟢 Low Issues (Nice to Have)
1. **Consider extracting validation logic to separate file**
   - **Issue**: Validation checks inline in controller
   - **Justification**: Moving validation checks to separate validator files keeps controller files slim (under 700 lines) and improves readability.
   - **Confidence Score**: 100% (Code quality suggestion)

### ✅ Strengths
- Good test coverage
- Clear function names
- Proper error handling

### 📊 Summary
- Critical: 1 | High: 1 | Medium: 1 | Low: 1
- **Status: ❌ BLOCKED** - Fix critical/high issues before commit
```


---

## 6. Cleanup & Decision Logging
*   **Cleanup (Remote PRs)**: Offer to switch back to the default branch (e.g. `main` or `master`).
*   **Post-Review Decision Extraction**:
    *   If review flagged new architectural choices → prompt to create ADR in `docs/adr/`.
    *   If review approved a new pattern → log to `_project_specs/session/decisions.md`.
