# AGENTS.md - Agent Instructions and Guidelines

This file contains system instructions, workspace rules, and loading standards that govern any AI agent operating in this repository. All active AI assistants must read, understand, and strictly adhere to these guidelines to ensure consistency, quality, and safety.

## Framework Integration Matrix

Different AI agent and assistant frameworks have specific conventions for loading custom system instructions or repository rules. The table below maps how each framework integrates and loads instructions within this workspace:

| Framework | Target File / Location | How Instructions are Loaded |
| :--- | :--- | :--- |
| **Kilo** | `AGENTS.md`, `.kilo/agent/*.md`, `.kilo/command/*.md` | Automatically scans for `AGENTS.md` at the project root for general rules. Custom agents can be defined under `.kilo/agent/*.md`, and custom commands under `.kilo/command/*.md`. |
| **Roo Code (Roo Cline)** | `.clinerules` | Reads the `.clinerules` file at the workspace root upon startup. It is recommended to symlink or copy `AGENTS.md` contents into `.clinerules`. |
| **Cursor** | `.cursorrules` | Automatically loads and appends instructions from `.cursorrules` at the workspace root to the assistant's system prompt. |
| **Claude Code** | `.clauderules` | Looks for a `.clauderules` file at the project root to ingest project-specific instructions and preferences. |
| **Windsurf** | `.windsurfrules` | Ingests instructions from `.windsurfrules` at the workspace root to customize the agent's behavior and environment awareness. |
| **Anti-gravity / General** | Workspace files or configuration | Reads general workspace documentation files directly, or can be explicitly pointed to `AGENTS.md` via agent-specific system prompts. |

---

## Core Agent Guidelines (The "Basics")

### 1. Be Technical and Direct
- Avoid conversational filler, polite greetings, preambles, or postambles (e.g., "Great", "Certainly", "Sure", "Okay").
- Keep responses concise, precise, and highly technical, focusing entirely on results.
- Do not explain obvious things or summarize standard changes unless explicitly requested by the user.

### 2. Use Tools Wisely
- **Verification First**: Always check if files and directories exist before attempting to read them.
- **Pathing**: Construct and use full absolute paths for all file-system actions.
- **Wave-based Execution**: Organize your task execution in logical, disciplined phases:
  1. **Planning**: Formulate a solid plan before modifying any code.
  2. **Searching**: Use precise content and pattern search tools (like glob and grep).
  3. **Implementing**: Apply clean, precise replacements or additions.
  4. **Validating**: Run project tests, linters, and compilers to verify changes.
- **Interactive Questions**: When asking the user to choose between multiple options, decisions, or candidate rules, always use the `ask_question` tool with appropriate options because it presents a structured interactive modal that avoids conversational parsing errors and provides a cleaner user experience.

### 3. Modularity and Coding Standards
- Write clean, modular, and self-documenting code that strictly conforms to the repository's established style.
- Add code comments sparingly, focusing on the *why* (complex logical rationale) rather than the *what* (obvious operations).
- Never add commentary to the user within code files.

### 4. Skill Discovery
- This repository is designed as a centralized store of "Agentic LLM Skills".
- When tasked with specialized domain-specific operations, agents must search the `skills/` or `builtin/` directories.
- Look for defined workflows, read the corresponding `SKILL.md` (or other documentation files), and load/execute the specialized steps directly.

### 5. Constructive and Rigorous Code Reviews
- Balance deep, path-tracing technical scrutiny (verifying correctness, edge cases, exceptions, performance, and best practices) with constructive professional courtesy.
- Highlight genuine positive implementation details (strengths, elegant patterns, or thorough tests).
- Direct style/linting comments at standard coding conventions (e.g., PEP 8, Google Style Guides) but avoid padding reviews with minor, formatting-only nits unless strict compliance is required.
- If a change lacks critical context or is overly complex, explicitly stop and ask for clarification.

---

## Karpathy Guidelines

Behavioral guidelines to reduce common LLM coding mistakes, derived from [Andrej Karpathy's observations](https://x.com/karpathy/status/2015883857489522876) on LLM coding pitfalls.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

### 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

### 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

### 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

### 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

---

## How to Configure and Use Skills

To maintain this repository as an extensible repository of AI knowledge, skills can be easily added and configured:

### Adding a New Skill
1. Create a directory for your skill under `skills/<skill-name>/` (or under `builtin/` for core Kilo skills).
2. Within this directory, create a `SKILL.md` (or relevant skill description file) containing:
   - **Name**: The identifier of the skill.
   - **Description**: A clear summary of the skill's purpose.
   - **Instructions / Workflows**: Detailed guidelines, execution steps, and scripts for the agent to follow.
   - **Tools & Environment Requirements**: Any specialized MCPs, commands, or packages required.

### Loading and Executing Skills
- **Automatic Loaders**: Specialized agent frameworks (like Kilo) can ingest these skills automatically via defined configuration paths (e.g., as listed in `kilo.json` or through built-in skill catalogs).
- **Manual Loaders**: Other frameworks should perform a file search for `SKILL.md` files matching the domain, read the file content using standard file-read tools, and append the workflows to their active system instructions.

---

## Production-Ready Agentic Skill Creation Guide

Based on the internal engineering standards provided, creating a skill is not just about writing a prompt; it is a product development process. A skill is an **opinionated cheatsheet** or **context injection** designed to fix specific, observable failures in an agent's workflow.

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
