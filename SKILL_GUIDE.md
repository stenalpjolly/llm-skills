# Production-Ready Agentic Skill Creation Guide

Based on the internal engineering standards provided, creating a skill is not just about writing a prompt; it is a product development process. A skill is an **opinionated cheatsheet** or **context injection** designed to fix specific, observable failures in an agent's workflow.

Here is the comprehensive, step-by-step guide on how to create a new, production-ready agentic skill.

---

### Phase 1: Decide if You Actually Need a Skill
Before writing anything, verify that a skill is the correct solution. Skills consume valuable context window tokens.

1. **Check existing skills:** Search the directory to see if a similar skill exists. If it does, **extend it** rather than creating a new one.
2. **Consider tool fixes first:** If the agent is failing because a CLI outputs bloated text or bad error messages, fix the CLI itself rather than writing a skill to work around it.
3. **Identify the gap:** Run the agent on your task *without* any skills loaded. If it succeeds, you don't need a skill. If it fails reliably (e.g., misses a specific flag, hallucinates a path, misunderstands a domain concept), **that failure is the justification for your skill.**

### Phase 2: Experience Before Theory
Do not guess what the agent might get wrong. **Experience it.**

1. **Do the task manually:** Run the commands yourself.
2. **Find the gotchas:** What undocumented flags did you need? What errors did you hit? 
3. **Identify fragile steps:** Are there steps that require exact syntax or complex parsing? Note these down—they should become Python/Bash scripts rather than LLM instructions.

### Phase 3: Scaffold the Directory Structure
Every skill lives in its own isolated directory. The structure is strictly enforced to support **Progressive Disclosure** (loading context only when needed).

```text
your_skill_name/
├── SKILL.md              # Required: YAML frontmatter + markdown instructions
├── scripts/              # Optional: Deterministic helper scripts (Python, Bash)
├── references/           # Optional: Deep context (schemas, templates)
└── assets/               # Optional: Static files used in outputs
```

### Phase 4: Write the `SKILL.md` Frontmatter (Crucial)
The YAML frontmatter is the **only** thing the agent reads to decide if it should trigger your skill. If this is poorly written, your skill will never be used.

*   **Name:** Must be `kebab-case` and use the **gerund form** (verb + -ing). Example: `processing-pdfs`, `debugging-spanner`.
*   **Description:** Must be under 1024 characters, written in the **third person**, and use `>-` to ensure proper parsing.

**Example of Perfect Frontmatter:**
```yaml
---
name: migrating-react-components
description: >-
  Converts React/Next.js components into Angular 17+ components using Angular Material. 
  Use when a user asks to migrate frontend code, translate JSX to HTML, or swap React hooks for Angular Signals. 
  Don't use for backend API migration or database schema changes.
---
```
*Notice the explicit "Use when..." (triggers) and "Don't use for..." (anti-triggers).*

### Phase 5: Write the `SKILL.md` Body
The body of the `SKILL.md` is loaded only after the skill is triggered. 

1. **Keep it under 500 lines:** If it gets longer, move detailed schemas or examples into the `references/` folder.
2. **Explain the *Why*:** Models comply better with rationale. Instead of `Always use --force`, write `Use --force because the legacy API requires bypassing the cache`.
3. **Signal, Not Noise:** Do not include boilerplate like "Always validate your output" or "I am an AI." The model already knows this.
4. **Use Imperative Language:** Write "Run the validator," not "You should run the validator."

### Phase 6: Bundle Scripts for Fragile Tasks (Avoid the "Instruction-Only Trap")
If a task requires 5 exact, deterministic steps (e.g., parsing a complex JSON, calling a strict API, or executing a fragile git rebase), **do not ask the LLM to do it via instructions.** 

Instead, write a script in the `scripts/` directory and instruct the LLM to run it.
*   *Bad:* "Read the file, find the regex pattern, extract the ID, and pass it to curl."
*   *Good:* "Run `python3 scripts/extract_and_call.py --file {target}`."

### Phase 7: Use References for Deep Context
If you have a large JSON schema, a massive API table, or a long prompt template, put it in `references/`. 
*   **Rule:** Keep references **one level deep**. Link them directly from `SKILL.md` (e.g., `See references/api-schema.md`). Do not link a reference from another reference.

### Phase 8: Evaluate and Iterate
A skill is a contract. You must prove it works.

1. **Write an Eval:** Create an `EVAL.txtpb` (or equivalent test case) that defines the exact prompt and the expected outcome.
2. **Run Ablation Testing:** Run the task *with* the skill and *without* the skill. 
3. **Measure the Delta:** The skill is only ready to ship if the pass rate is meaningfully higher *with* the skill than without it.
4. **Test on Smaller Models:** If your ecosystem has different model tiers (e.g., Flash vs. Pro), test your skill on the smaller/faster model. If the instructions are clear enough for the smaller model, they will be bulletproof for the larger one.

---

### Summary Checklist: Anti-Patterns to Avoid
Before finalizing your skill, ensure you haven't committed these common errors:
*   [ ] **The Everything Bagel:** Does this skill do more than one job? (If yes, split it).
*   [ ] **Performative Padding:** Did you include polite filler text? (If yes, delete it).
*   [ ] **Persona Ghosting:** Did you tell the model "You are an expert developer"? (If yes, remove it. Focus on the task, not the persona).
*   [ ] **Output Ambiguity:** Did you ask for a "report" without providing a JSON schema or Markdown template? (If yes, add a strict template to `references/`).
