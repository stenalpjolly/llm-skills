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
1. Append it to the project memory file (e.g., `AGENTS.md`).
2. Use clear conditional formatting: "When doing X, always Y because Z".

### 4. Summarize Output
Provide a concise, direct list of:
- Skills created (with key best practices encoded).
- Memory entries added (with target file location).

## Common Pitfalls
- Storing a multi-step workflow in `AGENTS.md` (it pollutes the global context and should be a progressive skill).
- Creating a skill without clear triggers/anti-triggers in the description (the framework won't know when to load it).
- Writing descriptions in the imperative or first person instead of the third person.
- Naming a skill as a noun instead of a gerund (e.g., using `capture-knowledge` instead of `capturing-knowledge`).