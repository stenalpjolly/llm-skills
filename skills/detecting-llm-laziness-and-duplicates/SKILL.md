---
name: detecting-llm-laziness-and-duplicates
description: >-
  Identifies LLM-generated duplicate code, TODO/FIXME comments, static/lazy stubs, mock data, and placeholder files in a codebase. Use when reviewing recent LLM-generated PRs or commits, analyzing build failures due to omitted/lazy ellipses, or auditing codebases for structural duplicates. Don't use for generic dependency updates, linting formatting style, or refactoring unrelated clean code.
---

# Detecting LLM Laziness and Duplicates

This skill provides a structured method to detect and resolve common LLM coding defects—such as code duplication, TODO comments, static placeholder stubs, and lazy code truncations (e.g., `// ... rest of code stays the same`).

To scan large repositories without overflowing the LLM's context window, this skill employs a **QCO (Quality Control Oracle)** mechanism. Instead of reading all files into the LLM, a local python scanner extracts suspect snippets, which the LLM then analyzes selectively.

## Core Rules

1. **Verify via Local Parser First**: Do not read random codebase files to hunt for laziness. Run the local QCO parser script (`python3 scripts/detect_laziness_and_duplicates.py`) to generate a structured candidate report first.
2. **Review Snippet Context**: Treat the local parser's candidates as a prioritized queue. Review the surrounding lines in the report to distinguish intentional placeholders/stubs from lazy LLM omissions.
3. **Analyze Duplicates Structurally**: When investigating duplicate code, compare functions or classes for behavioral equivalence. Prioritize refactoring duplicate business logic into shared helper functions. MOC/mock data duplicates in test files are automatically filtered out by the scanner, so anything remaining requires review.
4. **Enforce the Zero-Stub Standard**: Any active code containing temporary static mock data (e.g. hard-coded arrays/lists instead of database/API queries), comment ellipses (e.g., `// ... existing logic`), or `NotImplementedError` that is accessible by production code must be flagged as a critical defect.

## QCO (Quality Control Oracle) Mechanism

To avoid dumping the entire codebase into the LLM (which is expensive, slow, and hits token limits), this skill splits the task into two decoupled components:

```
┌────────────────────────┐      Local Scan      ┌─────────────────────────┐
│     Codebase Files     │─────────────────────>│  Heuristic QCO Report   │
│   (Megabytes of Code)  │  (Fast Python regex) │   (KBs of JSON/MD)      │
└────────────────────────┘                      └─────────────────────────┘
                                                             │
                                                             ▼
┌────────────────────────┐      Deep Analysis   ┌─────────────────────────┐
│    Defect Resolution   │<─────────────────────│      Active LLM         │
│   (Targeted Refactor)  │ (Targeted file edit) │  (Selective Context)    │
└────────────────────────┘                      └─────────────────────────┘
```

1. **The Local Parser (Heuristics)**: Performs high-recall regular expression matches and line-based clone detection. It outputs a lightweight, structured JSON/Markdown candidate report (`qco-report.json`) containing only the filepath, lines, and a few context lines for each suspicious spot.
2. **The LLM (Oracle)**: Consumes the lightweight report. For each candidate, the LLM determines if it represents a genuine laziness defect or a false positive. If it is a defect, the LLM reads *only* that file around the target line and fixes it.

## Execution Workflow

### Step 1: Run the Local Scanner
Execute the heuristic scanning script from the root of the repository:
```bash
python3 skills/code-review/detecting-llm-laziness-and-duplicates/scripts/detect_laziness_and_duplicates.py --path . --output qco-report.json
```

### Step 2: Read and Parse the QCO Report
Read the generated `qco-report.json` using the file read tool. The report categorizes findings into:
*   `laziness_candidates`: Comments, ellipses, or statements indicating omitted implementation (e.g., `// ... existing code`).
*   `todo_candidates`: `TODO`, `FIXME`, or `NEED TO BE DONE` annotations.
*   `duplicate_blocks`: Structural clones (contiguous blocks of identical lines) found across one or more files.

### Step 3: Targeted Verification & Resolution
For each highly-rated candidate:
1. Load the surrounding file context using the `Read` tool.
2. Formulate a plan to either:
   *   Replace comment ellipses or `NotImplementedError` stubs with real, working code.
   *   Refactor duplicate code blocks into shared modules, utility classes, or helper functions.
   *   Complete or register pending TODO items.
3. Apply surgical edits to clean up the code.
4. Run project compilers and tests to verify the fixes.
