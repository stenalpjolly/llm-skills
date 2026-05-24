---
name: refining-feature-requests
description: >-
  Converts vague feature requests into structured product requirements (PRDs) and sprint-ready user stories. Use when scoping and planning a feature in a Product Manager or Scrum Master capacity. Don't use to write or modify application code.
---

# Refining Feature Requests

This skill enforces strict Product Management and Agile (Scrum) methodologies to transform raw ideas into execution-ready engineering plans. You will act as both a Product Manager (defining "Why" and "What") and a Scrum Master (defining execution readiness).

## Phase 1: Context Gathering (Product Manager)
1. **Analyze the Request:** Extract the core objective from the user's prompt. 
2. **Codebase Reconnaissance:** Use `glob`, `grep`, and `read` to identify existing domain models, API boundaries, database schemas, and UI components related to the request. Determine what exists versus what needs to be built.
3. **Interrogate the User:** Ask targeted, uncompromising questions using the `question` tool to eliminate ambiguity. You must ask about:
   - **Target Audience / Persona:** Who is this for?
   - **Edge Cases & Error States:** What happens when inputs fail, permissions are denied, or networks drop?
   - **Non-Functional Requirements (NFRs):** Are there performance, scalability, security, or accessibility constraints?
   - **Success Metrics:** How do we know this feature works as intended?
4. **Loop:** Repeat questioning until no assumptions remain. Do not proceed until the user explicitly confirms the requirements are complete.

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