# AGENTS.md - Agent Instructions and Guidelines

This file governs any AI agent operating in this repository. Ensure all guidelines are strictly adhered to.

## General Principles
1. **Be Technical and Direct:** Avoid conversational padding, polite fillers, preambles, or status affirmations (e.g., "Certainly!", "Sure, I can help with that."). Get straight to the technical result.
2. **Surgical Modifications:** Touch only what is necessary to complete the task. Do not reformat adjacent files or rewrite code that isn't broken.
3. **Plan Before Implementation:** State assumptions, outline steps, and get verification if there is any ambiguity.

## Coding Standards & Style
- **Modularity:** Ensure code is well-structured and broken into testable, single-purpose components.
- **Documentation:** Use meaningful names for variables and functions. Use code comments sparingly, focusing on the *why* (complex logical rationale) rather than the *what* (obvious operations).
- **Dead Code:** Clean up imports, variables, or functions that are made redundant by your updates. Do not delete pre-existing dead code unless explicitly requested.

## Testing & Verification
- Write localized, clean tests for all new modules or modifications.
- Ensure all existing and newly created tests pass successfully before declaring a task complete.
- Do not bypass linter errors; resolve them structurally.
