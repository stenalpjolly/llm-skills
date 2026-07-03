---
name: refining-feature-requests
description: >-
  Converts vague feature requests into structured product requirements (PRDs) and sprint-ready user stories. Use when scoping and planning a feature in a Product Manager or Scrum Master capacity. Don't use to write or modify application code.
---

# Refining Feature Requests

This skill enforces strict Product Management and Agile (Scrum) methodologies to transform raw ideas into execution-ready engineering plans. You will act as both a Product Manager (defining "Why" and "What") and a Scrum Master (defining execution readiness).

## Phase 1: Context Gathering (Product Manager)
1. **Analyze the Request & Initial Reconnaissance:** Extract the core objective and use codebase exploration tools (`glob`, `grep`, `read`) to scan for existing domain models, APIs, and conventions related to the request.
2. **The Codebase Guardrail:** Never ask the user a question about the existing system or design that can be answered by exploring the codebase directly. Auto-resolve any decision that can be grounded in the existing code.
3. **Recursive Interrogation Loop:**
   - **Identify Unresolved Decisions:** Map out the remaining technical and product decisions required to build the feature (e.g., target audience/persona, edge cases/error states, NFRs, and success metrics).
   - **Group & Formulate Questions:** Group the remaining unresolved decisions into logically cohesive themes (e.g., Database, UI/UX, Security). Ensure none of the questions in the group depend directly on the answers of other questions in the same group.
   - **Provide Recommendations:** For each question in the group, formulate a precise question paired with a "Recommended Answer" based on repository standards to reduce user friction.
   - **Themed Stretch Delivery:** Present the themed group of questions to the user in a single stretch using the `question` tool.
   - **Strict Iteration Loop:** Once the user answers, do **NOT** automatically jump to Phase 2 (PRD Drafting). Instead, analyze the answers, resolve dependencies, update your plan, and identify any new or remaining gaps. You must present the updated state and explicitly ask the user: "Would you like to refine the feature further with another round of questions, or are you ready to approve and proceed to Phase 2 (PRD Drafting)?"
   - **Loop & Branch:** Repeat this interrogation loop recursively. You are strictly forbidden from drafting the PRD in Phase 2 until the user explicitly gives approval to proceed (e.g., by saying "proceed", "approve", "ready for PRD", or choosing a "Proceed to PRD Drafting" option).

## Phase 2: Product Requirements Document (PRD) Drafting
1. Draft a structured PRD containing exactly these sections:
   - **Objective:** 1-2 sentence summary of the business value.
   - **User Stories:** Format as "As a [persona], I want [action] so that [value]."
   - **Acceptance Criteria (AC):** Use Given/When/Then (BDD) format for every user story.
   - **Technical Strategy:** High-level architectural approach based on Phase 1 reconnaissance.
   - **Out of Scope:** Explicitly list what will *not* be built to prevent scope creep.
2. Present the PRD to the user and request explicit approval.

## Phase 3: Sprint Planning (Scrum Master)
1. **Apply INVEST Criteria:** Break the approved PRD down into atomic engineering issues. Every issue must be Independent, Negotiable, Valuable, Estimable, Small, and Testable.
2. **Map Dependencies:** Explicitly list which issues block others (e.g., "Backend API endpoint must be built before Frontend UI consumption").
3. **Format for Delegation:** Group these tasks logically (e.g., Epics).
4. **Handoff:** Load the `drafting-github-issues` skill using the `skill` tool (with name `drafting-github-issues`) and follow its workflow to format the tasks and prepare them for GitHub upload.