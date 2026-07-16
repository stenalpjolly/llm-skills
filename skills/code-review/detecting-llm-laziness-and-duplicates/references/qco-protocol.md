# QCO (Quality Control Oracle) Protocol and Schema

This document defines the QCO protocol, the structured JSON report schema, and the decision workflows used by the LLM Oracle to validate and resolve laziness and duplication defects.

---

## 1. The QCO Report Schema (`qco-report.json`)

The local scanner outputs a structured JSON object containing three primary candidate arrays, plus summary metadata. This structure is designed to minimize token usage while providing sufficient context to the LLM Oracle.

### Schema Fields

- `summary`: Metadata overview of the scan.
  - `total_laziness_candidates`: Count of stubs, ellipses, and shortcuts found.
  - `total_todo_candidates`: Count of comments flagged with TODO or FIXME.
  - `total_duplicate_blocks`: Count of merged code clones found.
  - `scanned_files_count`: Total number of code files scanned in the repository.
- `laziness_candidates`: List of candidates indicating incomplete implementation.
  - `file`: Path to the file, relative to the repository root.
  - `line_num`: Line number of the match (1-indexed).
  - `category`: Classification (e.g., `ellipses_comment`, `lazy_placeholder`, `not_implemented_stub`, `static_mock_return`).
  - `description`: Human-readable trigger explanation.
  - `matched_text`: Exact line content matching the heuristic.
  - `context`: Array of surrounding line objects:
    - `line_num`: The line number.
    - `text`: Content of that line.
    - `is_target`: Boolean indicating if this is the matching line.
- `todo_candidates`: List of pending TODOs and FIXMEs. Contains the same fields as `laziness_candidates`.
- `duplicate_blocks`: Structural duplicate segments detected using diagonal-merging.
  - `file_a`: File path of copy A.
  - `file_a_start`: Starting line number of block A.
  - `file_a_end`: Ending line number of block A.
  - `file_b`: File path of copy B.
  - `file_b_start`: Starting line number of block B.
  - `file_b_end`: Ending line number of block B.
  - `duplicate_non_trivial_lines`: Number of non-trivial lines matching.
  - `code_preview`: Snippet list (from Location A) to aid rapid confirmation.

---

## 2. The LLM Oracle Method: Verifying and Classifying Candidates

When the LLM receives the `qco-report.json`, it must process findings systematically. Instead of opening every file, the LLM uses the embedded `context` and `code_preview` data to perform an initial filter.

### Verification Matrix

| Finding Type | Clues pointing to a TRUE DEFECT | Clues pointing to a FALSE POSITIVE (Ignore) |
| :--- | :--- | :--- |
| **Ellipses / Lazy Shortcuts** | • Inside high-traffic source code files (e.g., `src/`, `lib/`, `pages/`).<br>• Break functional flow or syntax. | • Comments inside a documentation file or Markdown instruction.<br>• Comments in standard test fixtures explicitly showcasing stub patterns. |
| **Static / Mock Returns** | • Functions inside production code returning static variables, mock user data, or dummy error messages under normal flow. | • Intentional stub files or interfaces.<br>• Mock classes inside a `test/` directory. |
| **Duplicate Code Blocks** | • Identical business logic (e.g., validations, encryption, data transformation) copied and pasted in separate modules. | • Boilerplate configs (e.g., repeating import blocks, boilerplate package configurations).<br>• Boilerplate UI elements (e.g., identical standard import headers in frontend files). |

---

## 3. Resolution Workflows

Once a candidate is validated as a true positive defect, the LLM must execute the following resolution procedures:

### Workflow A: Resolving Ellipses and Lazy Truncations
LLMs sometimes leave `// ... existing code stays here` comments. Developers can accidentally copy-paste this, leading to broken builds or missing functionality.
1.  **Read complete context**: Call the `Read` tool on the target file with a large window (e.g., 50 lines before/after) or check the Git log to find what was deleted.
2.  **Retrieve original logic**: Look up prior conversations or standard implementation practices to find what the missing logic was.
3.  **Restore and Refactor**: Replace the ellipses comment with the *full* implementation.
4.  **Confirm Syntax**: Ensure no bracket mismatches or duplicate imports were introduced by the truncation.

### Workflow B: Resolving Static / Mock Return Placeholders
1.  **Analyze Intended Behavior**: Read the function's signature and docstring. Determine what dynamic source of truth (e.g., database, REST API, state store, environment variables) it should query.
2.  **Implement Logic**: Complete the mathematical calculations, API fetches, or query calls.
3.  **Handle Errors**: Replace simple empty mock returns with robust try-catch blocks and correct error handling.

### Workflow C: Resolving Duplicate Code Blocks
1.  **Locate Shared Parent / Utility Module**: Identify where helper or utility files exist (e.g., `src/utils/`, `src/helpers/`, or shared helper packages).
2.  **Extract Method**:
    *   Create a single, parameterizable helper function in the utility module.
    *   Add clear typed parameters and return types.
    *   Explain the shared purpose in a brief, technical comment.
3.  **Replace Clones**: Edit both `file_a` and `file_b` to import and call the newly created helper function.
4.  **Verify**: Run lint and unit tests to ensure that functional behavior remains unchanged and all tests pass.
