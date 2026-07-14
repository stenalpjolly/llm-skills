---
name: designing-goal-loops
description: >-
  Converts development tasks, bug reports, or feature ideas into robust, verifiable goal specifications for autonomous LLM execution (/goal or subagents). Use when preparing to run long-running or unmonitored agent loops that require self-contained context, atomic task boundaries, and executable verification criteria to prevent premature completion and looping. Don't use for executing code changes directly or for writing general product requirement documents (use refining-feature-requests).
---

# Designing Goal Loops

An autonomous agent operating without human monitoring requires an ironclad goal specification. A weak goal ("make the test pass and clean up") invites **premature completion**, scope creep, or infinite debugging loops. A strong goal creates a **tight loop** governed by **executable verification** and automated **backpressure**.

This skill guides you through constructing a self-contained, high-integrity Goal Specification built across three mandatory pillars: **Context**, **Task**, and **Verification**.

## Phase 1: Codebase Reconnaissance (Context Grounding)

Never write an autonomous goal specification using unverified assumptions or placeholder paths. Before drafting the goal, perform targeted **legwork** using codebase exploration tools (`grep`, `glob`, `read`, or `code_search`) to ground every instruction in the actual repository state.

1. **Verify Target Paths**: Locate and confirm the exact absolute file paths of all target modules, interfaces, and test suites involved in the task.
2. **Identify Existing Patterns**: Check how adjacent code structures error handling, typing, and public interfaces so the autonomous agent matches existing style without needing subjective guidance.
3. **Verify Execution Commands**: Test-run existing build, lint, and test commands (`npm test`, `blaze test`, `pytest`, `cargo test`) to ensure the baseline is currently passing and to verify the exact syntax required for verification.

**Completion Criterion**: Every file path, symbol name, and shell command intended for the Goal Specification is confirmed to exist and execute cleanly in the current workspace.

## Phase 2: Constructing the Three Pillars

Using the grounded reconnaissance from Phase 1, construct the Goal Specification across three mandatory pillars. See [`references/goal-specification-template.md`](references/goal-specification-template.md) for the structure and detailed formatting rules.

### 1. Context Pillar (Where & Why)
Provide the autonomous agent with the exact background needed to understand its operating environment without asking clarifying questions.
- **Objective & Rationale**: Why this change is being made and what business/technical value it unlocks.
- **Grounded Paths**: The exact absolute file paths to read and modify.
- **Architectural Guardrails**: Explicit constraints (e.g., "Must preserve backwards compatibility for existing public interface `foo()`", "Do not modify database migrations").

### 2. Task Pillar (What & Scope)
Define the objective as an atomic **vertical slice** of behavior that can be implemented and verified in a single autonomous execution cycle.
- **Actionable Execution Steps**: Ordered, concrete steps the agent must take (e.g., 1. Write failing test -> 2. Implement minimal logic -> 3. Verify -> 4. Refactor).
- **Out of Scope (Anti-Goals)**: Explicit boundaries detailing what the agent must *never* touch or attempt to "improve" (e.g., "Do not refactor adjacent helper modules", "Do not add configuration flags that were not requested").

### 3. Verification Pillar (Proof of Work & Backpressure)
Define the exact **executable verification** criteria that serve as the autonomous loop's stopping rule. An unmonitored agent must never rely on subjective visual inspection or vague assertions.
- **Executable Commands**: The exact, runnable shell commands (`npm test path/to/math.test.ts`, `blaze test //package:target`, `pytest -v -k "test_foo"`) that must return exit code 0 (`GREEN`).
- **Observable Proof of Work**: The precise terminal output, assertion result, or log string that proves the task succeeded.
- **Backpressure & Recovery Strategy**: Instructions on how the agent must respond if verification fails (e.g., "If the test fails with a syntax error, run the linter; if logic fails after 3 attempts, recite debugging mantras and inspect stack traces without modifying or deleting the test").

**Completion Criterion**: The three pillars are fully drafted with zero placeholders, containing exact file paths, atomic task boundaries, and runnable verification commands.

## Phase 3: Guardrail Audit & User Alignment

Before finalizing and handing off the goal specification, audit the draft against the three fatal failure modes of unmonitored agent execution:

1. **Audit for Premature Completion**: Does the verification pillar rely on vague statements ("ensure it works properly") instead of checkable, automated assertions? If yes, replace them with exact test or build commands.
2. **Audit for Horizontal Splurging**: Does the task ask the agent to implement multiple independent features at once? If yes, split the specification into smaller, sequential **vertical slices**.
3. **Audit for Speculative Scope**: Does the task invite the agent to build future flexibility or extra abstractions? If yes, prune the scope to the absolute minimum needed to pass verification.

Once audited, present the drafted Goal Specification clearly to the user using markdown formatting or an artifact (`goal_specification.md`), highlighting any assumptions or trade-offs. Ask the user for explicit confirmation or refinement.

**Completion Criterion**: The user explicitly approves the verified Goal Specification without outstanding ambiguities.

## Phase 4: Autonomous Loop Handoff

Upon user confirmation, output the finalized Goal Specification in a clean, self-contained code block or artifact ready for direct execution.

1. If the user intends to launch the `/goal` command, provide the exact prompt string tailored for `/goal`.
2. If delegating to a background subagent (`invoke_subagent`), format the prompt string cleanly so the subagent receives the complete context, task, and verification pillars without needing parent history.

**Completion Criterion**: The finalized, copy-pasteable goal payload is delivered to the user or dispatched via tool call.
