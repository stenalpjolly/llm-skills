---
name: orchestrating-subagents
description: >-
  Orchestrates specialized subagents in parallel to keep the main thread idle and maximize concurrency.
  Use when a task can be decomposed into independent subtasks (such as concurrent code changes, parallel research, or separate validation steps),
  when a task is long-running and the parent thread should remain idle while waiting, or when interactive input is needed to refine features.
  Don't use for simple sequential tasks, single-file edits that cannot be parallelized, or when subagent support is not available in the workspace.
---

A skill to govern the orchestration of background subagents and user interaction. It ensures the main thread acts as a **Conductor**—coordinating work, gathering results, and maintaining an **idle state** while concurrent subtasks run in the **Mesh**.

## Principles

*   **Conductor**: The main agent thread. Its primary role is to plan, delegate, orchestrate, and refine. It does not perform sequential bulk work if it can be parallelized.
*   **Mesh**: The concurrent group of subagents doing the heavy lifting.
*   **Idle State**: The optimal state of the Conductor. After dispatching tasks to the Mesh, the Conductor must stop calling tools to release execution, letting the background runner notify it upon subagent completion.

---

## Workflow

### 1. Deconstruction & Planning
*   Decompose the main task into independent, concurrent goals during the **Planning** phase.
*   Identify boundaries: separate directories, independent source files, parallel research tracks, or isolated verification/testing steps.
*   Define success criteria for each subtask before delegating.
*   **Completion Criterion**: A documented plan detailing the boundary lines, the role of each subagent, and the verification metrics for each.

### 2. Spawning the Mesh
*   Use `invoke_subagent` to launch subagents in parallel.
*   Select the correct subagent type:
    *   `research`: For codebase exploration, log analysis, web research, or documentation mapping.
    *   `self`: For editing source code, implementing features, or validating changes.
*   For specialized roles (e.g., custom linters, migrations, or database auditors), use `define_subagent` first to configure their tools and system prompt.
*   **Completion Criterion**: All required subagents are defined and invoked, and their conversation IDs are logged.

### 3. Conductor Idle Execution
*   Submit all subagent tasks in a single turn if possible, or in parallel waves.
*   **Do not poll**: Avoid checking `status` or running sleep commands.
*   Stop calling tools and yield the turn immediately to enter the **Idle State**. The system will wake the Conductor when a subagent sends a message.
*   **Completion Criterion**: The Conductor has stopped calling tools and yields execution to the background system.

### 4. Interactive Refinement
*   When design decisions, tradeoffs, or requirement gaps are identified:
    *   Use the `ask_question` tool to present a structured multiple-choice modal to the user.
    *   Do not ask open-ended conversational text questions if they can be formatted as distinct options.
    *   Iterate on the implementation based on the user's feedback.
*   **Completion Criterion**: A structured user response is received, and the requirements/plan are updated accordingly.

### 5. Gathering & Verification
*   Upon wakeup, inspect the reports from the Mesh.
*   Verify changes by running the project build and verification tests.
*   Request a code review from a `code-reviewer` subagent or perform a rigorous self-audit before finalizing.
*   **Completion Criterion**: All verification checks/tests must pass, and the code review or self-audit must approve the changes with no remaining critical/high issues.

---

## Reference: Tooling Guide

### Spawning Subagents
Tool: `invoke_subagent`
```json
{
  "Subagents": [
    {
      "TypeName": "research",
      "Role": "API Explorer",
      "Prompt": "Search the codebase for all usages of HttpMcpTransport and list their parameters."
    },
    {
      "TypeName": "self",
      "Role": "Test Implementer",
      "Prompt": "Create unit tests in HttpMcpTransportTest.java for the connection timeout edge cases."
    }
  ]
}
```

### Asking Structured Questions
Tool: `ask_question`
*   Always structure the question as the user's direct response.
*   Place the recommended option first, prefixed with `(Recommended)`.
*   Set `is_multi_select` to `true` if multiple options can be chosen.

```json
{
  "questions": [
    {
      "question": "Which styling library should we adopt for the new dashboards?",
      "is_multi_select": false,
      "options": [
        "(Recommended) Vanilla CSS with HSL design variables",
        "TailwindCSS (requires user confirmation on version)",
        "Material UI styled components"
      ]
    }
  ]
}
```

---

## Failure Modes

*   **Synchronous Polling**: The Conductor remains active, running CLI loops or constantly calling `manage_task` or `status` instead of entering the **Idle State**.
*   **Single-Threading**: Performing sequential tasks (e.g., reading 10 files one by one, refactoring 3 components sequentially) when they could be delegated in parallel.
*   **Conversational Ambiguity**: Asking the user questions in conversational text that result in parsing errors or slow back-and-forth, instead of using the structured `ask_question` tool.
*   **Over-Scoping Subagents**: Giving a subagent too broad of a task, causing it to lose focus or hit token limits. Keep subagent prompts specific, granular, and task-oriented.
