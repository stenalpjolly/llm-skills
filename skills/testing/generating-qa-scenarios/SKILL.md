---
name: generating-qa-scenarios
description: >-
  Generates conversational user evaluation scenarios and test case checklists for software flows or user journeys. 
  Use when a user asks to create a testing scenario, QA checklist, or evaluation questions for a feature. 
  Don't use for unit testing or writing automated test code.
---

# Generating QA Scenarios

Create conversational, realistic evaluation scenarios that walk testers through a software flow and ask them to verify specific actions, edge cases, fallback mechanisms, and access controls.

## Guidelines for Generating Scenarios

1.  **Format**: Present the scenario as a conversational checklist starting with a prompt like "Were you able to do the following:".
2.  **Coverage**: Ensure the generated checklist comprehensively covers various aspects of the user journey:
    *   **Happy Path**: Standard core user actions (e.g., selection, creation, configuration).
    *   **Automated/Complex Features**: Verifying system-generated outputs or complex logic (note that users should watch for inaccuracies).
    *   **Manual Fallbacks**: Ensuring manual overrides or basic inputs work if automation/complexity fails.
    *   **Support & Context**: Interacting with support/collaborators, maintaining context, and providing external validation (e.g., sharing artifacts, links, or screens).
    *   **Submissions/Completions**: The final state or handoff to conclude the flow.
    *   **Negative Testing & Access Controls**: Explicitly verifying things the user *should not* see or do (e.g., verifying restricted data is hidden from regular users).
3.  **Tone**: Conversational, direct, and pragmatic.

## Execution Workflow

1.  Analyze the requested feature, system, or user flow.
2.  Map out the key actions, automated touchpoints, fallback elements, and access control boundaries for that specific system.
3.  Draft the scenario mirroring the tone and structure found in `references/example-scenario.md`.
4.  Adapt the template placeholders to fit the exact domain requested.
5.  Output the final checklist directly to the user.

## References

See `references/example-scenario.md` for the tone and structural pacing.