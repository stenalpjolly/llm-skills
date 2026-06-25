# Receiving Feedback Protocol

This protocol defines how to process, evaluate, and respond to incoming code review comments.

## Protocol: READ → UNDERSTAND → VERIFY → EVALUATE → RESPOND → IMPLEMENT

1.  **READ**: Carefully read the feedback comments.
2.  **UNDERSTAND**: Make sure the issue is fully understood.
    *   *Rule*: If unclear, STOP and ask for clarification on ALL unclear items first.
3.  **VERIFY**: Verify the feedback technically against the active codebase.
    *   *Rule*: Do not implement before verification.
    *   *Rule*: YAGNI check: grep for usage in the codebase before implementing suggested "proper" features.
4.  **EVALUATE**: Assess whether the feedback is correct and aligned with project design.
5.  **RESPOND**: Write your response based on the source of the review:
    *   *Rule*: No performative agreement (e.g., "You're absolutely right!", "Great point!", "Thanks for [anything]"). Keep responses objective.
    *   *Rule*: Restate the requirements, ask clarifying questions, or push back with technical reasons.
6.  **IMPLEMENT**: Only implement changes that have been verified and agreed upon.

## Source Handling
*   **Human Partner**: Trusted. Implement after understanding, avoiding performative agreement.
*   **External Reviewers / Automated Checkers**: Verify technical correctness. Check for potential breakage. Push back if suggestions are wrong.
