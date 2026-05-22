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
| `migrating-react-to-angular` | Converts React components (.jsx/.tsx) into standalone Angular 17+ components using Angular Material. | `skills/migrating-react-to-angular` |
| `migrating-nextjs-to-python` | Translates Next.js JavaScript/TypeScript API routes (req, res) into clean FastAPI Python backend endpoints. | `skills/migrating-nextjs-to-python` |
| `validating-migration-builds` | Provides build and lint validation checks for migrated Angular and Python code. | `skills/validating-migration-builds` |

## Discovery & Backlog Migration Pipeline

These three skills work in sequence to facilitate the migration of a Next.js application to an Angular (frontend) and Python (backend) architecture:

1. **`scanning-codebase`**: Analyzes the source Next.js application, identifying component structures, routes, API calls, and state management strategies.
2. **`drafting-migration-issues`**: Translates the discovered components, pages, and API endpoints into discrete, well-defined migration tasks and drafts them as structured issue templates.
3. **`managing-github-backlog`**: Publishes, prioritizes, and tracks the drafted migration issues on GitHub, establishing an organized pipeline for execution.

## Phase 2: Sprint Execution & Code Translation Pipeline

Once the backlog is established, the following Phase 2 skills execute the translation and validation pipeline:

1. **`migrating-react-to-angular`**: Converts React/JSX components into modern, standalone Angular 17+ components using Angular Material. It uses a Python scaffolding helper to generate syntactically correct boilerplate first, and leverages structured mapping references to map state hooks to Angular Signals and React components to Material standards cleanly.
2. **`migrating-nextjs-to-python`**: Converts serverless Next.js JavaScript/TypeScript API routes into high-performance, type-hinted FastAPI backend endpoints. It translates TypeScript interfaces to Pydantic schemas via automated script-based schema generation, implements SQLModel handlers, and translates JS errors to FastAPI HTTPExceptions.
3. **`validating-migration-builds`**: Acts as a self-correcting validation check loop. It runs local builders, compilers, and linters (such as Angular component compilation and Python syntax checks) to catch and parse errors, allowing the agent to dynamically repair code failures prior to committing changes.
