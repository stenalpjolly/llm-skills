# LLM Agent Skills Repository

A repository to store, organize, and load agentic LLM skills.

## Purpose and Structure

This repository acts as a centralized store for LLM agent skills. These skills define specific workflows, instructions, and tools that enhance the capabilities of AI agents, enabling them to handle complex, domain-specific tasks with high efficiency and reliability.

### Repository Structure
- **`builtin/`**: Built-in or configured skills loaded by Kilo.
- **`skills/`**: Custom, domain-specific agent skills.
- **`README.md`**: Overview of the repository and skills index.

## Sample Skills

Below is a list of sample skills contained in this repository:

| Skill Name | Description | Location |
| :--- | :--- | :--- |
| `kilo-config` | Guide for Kilo configuration and Agent Manager. | `builtin/kilo-config` |
| `scanning-codebase` | Scans codebase architecture, technologies, and dependencies for migration. | `skills/scanning-codebase` |
| `drafting-migration-issues` | Drafts detailed migration issues to track the steps needed to migrate components. | `skills/drafting-migration-issues` |
| `managing-github-backlog` | Manages, prioritizes, and updates the backlog of migration issues on GitHub. | `skills/managing-github-backlog` |

## Discovery & Backlog Migration Pipeline

These three skills work in sequence to facilitate the migration of a Next.js application to an Angular (frontend) and Python (backend) architecture:

1. **`scanning-codebase`**: Analyzes the source Next.js application, identifying component structures, routes, API calls, and state management strategies.
2. **`drafting-migration-issues`**: Translates the discovered components, pages, and API endpoints into discrete, well-defined migration tasks and drafts them as structured issue templates.
3. **`managing-github-backlog`**: Publishes, prioritizes, and tracks the drafted migration issues on GitHub, establishing an organized pipeline for execution.
