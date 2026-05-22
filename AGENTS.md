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

### 3. Modularity and Coding Standards
- Write clean, modular, and self-documenting code that strictly conforms to the repository's established style.
- Add code comments sparingly, focusing on the *why* (complex logical rationale) rather than the *what* (obvious operations).
- Never add commentary to the user within code files.

### 4. Skill Discovery
- This repository is designed as a centralized store of "Agentic LLM Skills".
- When tasked with specialized domain-specific operations, agents must search the `skills/` or `builtin/` directories.
- Look for defined workflows, read the corresponding `SKILL.md` (or other documentation files), and load/execute the specialized steps directly.

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
