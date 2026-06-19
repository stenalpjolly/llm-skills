---
name: capturing-knowledge
description: >-
  Extracts and categorizes best practices, workflows, and project conventions from a conversation context. 
  Use when a user asks to review a session for insights, extract best practices, update project memory, or create reusable workflow skills. 
  Don't use for generic summarization without an intent to store the knowledge.
---

# Capturing Knowledge

## Overview
Systematically extracts valuable insights from conversations and persists them as reusable skills or static project memory.

## Best Practices
- Prioritize patterns that worked well, anti-patterns to avoid, and decision rationale.
- Default to `AGENTS.md` for continuous static rules, preferences, and style guidelines.
- Escalate to a full Skill (`skills/<skill-name>/SKILL.md`) only for multi-step processes or reproducible methodologies.
- Keep recorded rules atomic and contextual (explain the *why*).

## Process

### 1. Identify Key Learnings
Scan the conversation context specifically for:
- **Best Practices:** Effective approaches, anti-patterns, quality standards, and rationale.
- **Conventions:** Style preferences, architecture decisions, and workflow steps.

### 2. Scaffold Skills for Complex Workflows
If the extracted knowledge forms a multi-step, reusable procedure:
1. Create a gerund-named directory: `skills/<gerund-name>/`.
2. Create `SKILL.md` inside it.
3. Write strict YAML frontmatter with a `kebab-case` gerund name and a third-person description using `>-`.
4. Include explicit "Use when..." (triggers) and "Don't use for..." (anti-triggers) in the description.
5. Encode best practices prominently at the top.
6. Write step-by-step instructions in the imperative form ("Run the script", not "You should run the script").

### 3. Update Memory for Static Rules
If the extracted knowledge is a simple guideline, preference, or architectural rule:
1. **Draft Candidate Rules:** Formulate each guideline using the atomic, generic XYZ conditional rule format: *"When doing [Context] (X), always [Action] (Y) because [Technical Rationale] (Z)."* Strip away any instance-specific details (like exact file paths or variable names).
2. **Present Options to the User:** Use the `ask_question` tool with `is_multi_select: true` to present the drafted rules as options for selection. Format each option as the drafted rule itself. The question should ask the user to select which rules to add to `AGENTS.md`.
3. **Wait for User Input:** Do not edit or append to the project memory file (`AGENTS.md`) until the tool response has been received.
4. **Append Only Approved Rules:**
   - If the user selects one or more rules, append only those selected rules to the memory file.
   - If the user selects none (or skips), do not modify the memory file and proceed to summarize the outcome.

### 4. Summarize Output
Provide a concise, direct list of:
- Skills created (with key best practices encoded).
- Memory entries added (with target file location).

## Common Pitfalls
- Storing a multi-step workflow in `AGENTS.md` (it pollutes the global context and should be a progressive skill).
- Creating a skill without clear triggers/anti-triggers in the description (the framework won't know when to load it).
- Writing descriptions in the imperative or first person instead of the third person.
- Naming a skill as a noun instead of a gerund (e.g., using `capture-knowledge` instead of `capturing-knowledge`).