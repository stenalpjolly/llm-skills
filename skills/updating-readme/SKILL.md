---
name: updating-readme
description: >-
  Standardizes how agents update and manage README.md files, adopting the Deep Insight/Strands SDK documentation style.
  Use when creating a new README from scratch, improving an existing README, or converting technical docs to user-friendly formats.
  When creating or editing Mermaid diagrams in the README, load and use the `generating-mermaid-diagrams` skill.
  Don't use for API-only documentation or internal technical specs.
---

# Updating README

A well-written README enables users to understand what the project does in 30 seconds, see visual proof (logos, diagrams), get it running in 2-5 minutes, find detailed resources, and feel confident about the project's quality.

## Key Principles
- **Visual first:** Prioritize a logo, centered layout, badges, and architecture diagrams. **If creating or editing Mermaid architecture diagrams, load and strictly follow the `generating-mermaid-diagrams` skill to prevent parser errors.**
- **Balanced depth:** Substantial enough to be useful, focused enough to stay readable.
- **Progressive disclosure:** Quick value at the top, deep details further down.
- **Code-first:** Show working examples, not just descriptions.
- **Professional yet accessible:** Clear language without excessive jargon.

## Execution Workflow

1. **Format Analysis:** Analyze the current `README.md` to learn and understand the format, structure, tone, and badge usage. Ensure it aligns with or transitions toward the Deep Insight/Strands SDK documentation style.
2. **Sanitize Internal Details:** Ensure the public-facing README does not contain internal details. Actively remove and desensitize any proprietary logic, sensitive system architecture, credentials, or internal references.
3. **Git History Context (For Existing Projects):**
   - Check when the `README.md` was last updated.
   - Check if the project is a git repository.
   - If it is a git repo, identify what changes (commits) have been made since the last update to the README.
4. **Planning:** Based on the identified changes or project requirements, make a structured list of items defining what needs to be updated and what needs to be changed, strictly adhering to the identified format and Key Principles.
5. **Deep Code Analysis:**
   - Go through the relevant code pieces in detail, utilizing the depth and context provided by the commits since the last README update.
   - If the recent commits do not provide enough context to identify the changes, ask the user for clarification OR trace back to the initial commit that introduced the feature.
   - If no specific commits or user guidance are available, analyze the complete code pieces one by one.
6. **Surgical Updates:** Apply the updates to the README based on the plan. Only modify the related sections. Avoid rewriting existing sections that are factually correct. Do not overwrite or modify existing CI/CD, version, or license badges unless explicitly instructed.
7. **Actionable Instructions:** When adding setup or installation commands, ensure they are in proper markdown code blocks (e.g., `bash`, `python`) and reflect the project's actual package manager.

## Validation
Before finalizing, verify:
- **Visual appeal:** Includes logo, centered header, proper spacing, and badges. **Validate any Mermaid diagrams using the `generating-mermaid-diagrams` Python validation script to ensure they compile/render without syntax errors.**
- **Completeness:** All essential sections are present.
- **Accuracy:** All commands and links work correctly.
- **Clarity:** A non-technical user can follow the instructions.
- **Style:** Matches the Deep Insight/Strands SDK pattern.
