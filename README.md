<p align="center">
  <img src="https://img.icons8.com/color/120/000000/brain.png" alt="LLM Skills Logo" width="80" height="80" />
</p>
<h1 align="center">🤖 LLM Agent Skills Repository</h1>
<p align="center">
  <strong>An opinionated, production-ready catalog of AI agent skills, workflows, and deterministic validation scripts.</strong>
</p>

<p align="center">
  <a href="https://github.com/stenalpjolly/llm-skills/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
  <a href="https://github.com/stenalpjolly/llm-skills"><img src="https://img.shields.io/badge/skills-27--active-success" alt="Skills Active"></a>
  <a href="https://github.com/stenalpjolly/llm-skills"><img src="https://img.shields.io/badge/agent--support-Kilo--enabled-orange" alt="Agent Support"></a>
  <a href="https://github.com/stenalpjolly/llm-skills"><img src="https://img.shields.io/badge/style-Strands--SDK-blueviolet" alt="Documentation Style"></a>
</p>

---

## 📖 Overview

This repository acts as a centralized store for LLM agent skills. These skills define specific workflows, instructions, templates, and scripts that enhance the capabilities of AI agents (such as Kilo), enabling them to handle complex, domain-specific tasks with high efficiency and reliability.

By bridging pure LLM instructions with deterministic code-execution validation, this architecture eliminates common LLM failures:
- **Avoiding the "Instruction-Only" Trap:** Standardizes processes by replacing fragile instruction lists with executable scripts (Python/Bash) under `scripts/`.
- **Progressive Disclosure:** Uses lightweight YAML frontmatter metadata to ensure agents load deep context only when relevant.
- **Surgical, Verified Changes:** Emphasizes test-driven cycles and local build validation to guarantee correctness.

---

## 📦 Installation & Usage

You can install and use these skills with any supported AI coding agent (e.g., `antigravity`, `claude-code`, `cursor`) using the **[Agent Skills CLI](https://github.com/vercel-labs/agent-skills)**.

### List Available Skills
To list all skills available in this repository without installing:
```bash
npx skills add stenalpjolly/llm-skills --list
```

### Install a Specific Skill
To install a specific skill (e.g., `designing-tasteful-frontends`) to a target agent:
```bash
npx skills add stenalpjolly/llm-skills --skill designing-tasteful-frontends --agent antigravity
```

### Install All Skills
To install all skills in this repository to all detected agents on your system:
```bash
npx skills add stenalpjolly/llm-skills --all
```

### Use a Skill Without Installing
To generate a prompt for a skill and pipe it directly to a coding agent:
```bash
npx skills use stenalpjolly/llm-skills --skill designing-tasteful-frontends --agent claude-code
```

---

## 🛠 Repository Structure

```text
llm-skills/
├── AGENTS.md             # Core agent guidelines, Karpathy rules, and creation standards
├── builtin/              # Core built-in skills configured natively
│   └── kilo-config/      # Built-in Kilo configuration helper
├── skills/               # Custom, domain-specific agent skills
│   ├── [skill-name]/     
│   │   ├── SKILL.md      # Skill YAML frontmatter + markdown guidelines
│   │   ├── scripts/      # Deterministic helper scripts (Python/Bash)
│   │   └── references/   # Static reference templates and schemas
└── README.md             # Repository overview and skills index (this file)
```

---

## 🗺️ Pipeline Architecture

The skills within this repository are designed to compose seamlessly into specialized pipelines:

```text
 ┌──────────────────────────────────────────────────────────────────────────┐
 │                     Product Planning & Backlog Pipeline                  │
 │                                                                          │
 │   [Refining Feature Requests] ──> [Drafting Issues] ──> [Managing Backlog] │
 └────────────────────────────────────┬─────────────────────────────────────┘
                                      │
                                      ▼
 ┌──────────────────────────────────────────────────────────────────────────┐
 │                     Execution & Development Loop                         │
 │                                                                          │
 │   [Test-Driven Issue Resolution] ──> [Debugging Mantras] ──> [Scrutinize]│
 └────────────────────────────────────┬─────────────────────────────────────┘
                                      │
                                      ▼
 ┌──────────────────────────────────────────────────────────────────────────┐
 │                  Code Translation & Validation Pipeline                  │
 │                                                                          │
 │   [Scanning Codebase] ──> [React to Angular] ──> [Validating Builds]     │
 └──────────────────────────────────────────────────────────────────────────┘
```

---

## 🗂️ Skills Index

### 🛡️ Core Guardrails & Guidelines
| Skill Name | Location | Description |
| :--- | :--- | :--- |
| `bootstrapping-projects` | [`skills/bootstrapping-projects`](skills/bootstrapping-projects) | Bootstraps a new project or initializes an existing directory with standard structures, planning files, version control, and agnostic AI agent rules. |
| `karpathy-guidelines` | [`skills/karpathy-guidelines`](skills/karpathy-guidelines) | Behavioral guidelines to reduce common LLM coding mistakes, focus on surgical changes, simplicity, and verifiable goals. |
| `detecting-llm-laziness-and-duplicates` | [`skills/detecting-llm-laziness-and-duplicates`](skills/detecting-llm-laziness-and-duplicates) | Identifies LLM-generated duplicate code, TODO/FIXME comments, static/lazy stubs, mock data, and placeholder files. |
| `kilo-config` (Built-in) | [`builtin/kilo-config`](builtin/kilo-config) | Guide for Kilo configuration: config paths, kilo.json fields, commands, agents, skills, permissions, MCPs, providers, TUI settings. |

### 📋 Product Planning & Issue Management
| Skill Name | Location | Description |
| :--- | :--- | :--- |
| `refining-feature-requests` | [`skills/refining-feature-requests`](skills/refining-feature-requests) | Converts vague feature requests into structured product requirements (PRDs) and sprint-ready user stories. |
| `drafting-github-issues` | [`skills/drafting-github-issues`](skills/drafting-github-issues) | Converts project specifications, task lists, or architectural maps into granular GitHub issue drafts. |
| `managing-github-backlog` | [`skills/managing-github-backlog`](skills/managing-github-backlog) | Creates labels and publishes drafted JSON issues to a GitHub repository. |

### ⚙️ Execution & Development Workflows
| Skill Name | Location | Description |
| :--- | :--- | :--- |
| `implementing-test-driven-issue-resolution` | [`skills/implementing-test-driven-issue-resolution`](skills/implementing-test-driven-issue-resolution) | Converts user assumptions, feature requests, or bug reports into verified, test-driven code changes. |
| `debugging-with-mantras` | [`skills/debugging-with-mantras`](skills/debugging-with-mantras) | Four-mantra debugging discipline—reproduce, trace the fail path, falsify the hypothesis, cross-reference every breadcrumb. |
| `orchestrating-subagents` | [`skills/orchestrating-subagents`](skills/orchestrating-subagents) | Orchestrates specialized subagents in parallel to keep the main thread idle and maximize concurrency. |
| `resolving-merge-conflicts` | [`skills/resolving-merge-conflicts`](skills/resolving-merge-conflicts) | Resolves in-progress git merge or rebase conflicts by locating conflicting files and tracing original intents. |
| `scrutinizing-code-changes` | [`skills/scrutinizing-code-changes`](skills/scrutinizing-code-changes) | Outsider-perspective end-to-end review of a plan, PR, or code change to verify intent and code paths. |
| `writing-post-mortems` | [`skills/writing-post-mortems`](skills/writing-post-mortems) | Writes the canonical engineering record of a fixed bug—root cause, mechanism, fix, validation, and prevention. |

### 🚀 App Migration & Code Translation Pipeline
| Skill Name | Location | Description |
| :--- | :--- | :--- |
| `scanning-codebase` | [`skills/scanning-codebase`](skills/scanning-codebase) | Scans a Next.js directory to map out routes, components, and API endpoints into a structured JSON format. |
| `migrating-react-to-angular` | [`skills/migrating-react-to-angular`](skills/migrating-react-to-angular) | Converts React components (.jsx/.tsx) into standalone Angular 17+ components using Angular Material. |
| `migrating-nextjs-to-python` | [`skills/migrating-nextjs-to-python`](skills/migrating-nextjs-to-python) | Translates Next.js JavaScript/TypeScript API routes into clean FastAPI Python backend endpoints. |
| `validating-workspace-builds` | [`skills/validating-workspace-builds`](skills/validating-workspace-builds) | Provides build and lint validation checks for the active workspace code. |

### 🔍 UI/UX & Web Standards Auditing
| Skill Name | Location | Description |
| :--- | :--- | :--- |
| `applying-marketing-web-standards` | [`skills/applying-marketing-web-standards`](skills/applying-marketing-web-standards) | Provides guidelines, visual specs, and accessibility rules for Google-branded marketing websites. |
| `auditing-ui-ux` | [`skills/auditing-ui-ux`](skills/auditing-ui-ux) | Performs a comprehensive UI/UX design audit on application screens or components. |
| `crawling-web-applications` | [`skills/crawling-web-applications`](skills/crawling-web-applications) | Crawls, navigates, and audits a web application's links, buttons, and interactive elements. |
| `designing-tasteful-frontends` | [`skills/designing-tasteful-frontends`](skills/designing-tasteful-frontends) | Upgrades AI-built frontends (landing pages, portfolios, marketing sites) to premium, Awwwards-level quality. |
| `generating-qa-scenarios` | [`skills/generating-qa-scenarios`](skills/generating-qa-scenarios) | Generates conversational user evaluation scenarios and test case checklists for software flows or user journeys. |

### 📝 Knowledge, Communication & Standards
| Skill Name | Location | Description |
| :--- | :--- | :--- |
| `capturing-knowledge` | [`skills/capturing-knowledge`](skills/capturing-knowledge) | Extracts and categorizes best practices, workflows, and project conventions from a conversation context. |
| `generating-mermaid-diagrams` | [`skills/generating-mermaid-diagrams`](skills/generating-mermaid-diagrams) | Generates syntax-valid, render-safe Mermaid.js diagrams (flowcharts, sequence diagrams, ERDs, Gantt charts). |
| `translating-for-management` | [`skills/translating-for-management`](skills/translating-for-management) | Rewrites engineer-to-engineer content for engineering-org leadership and shapes it for specific channels (JIRA, Slack, etc.). |
| `updating-readme` | [`skills/updating-readme`](skills/updating-readme) | Standardizes how agents update and manage README.md files, adopting the Deep Insight/Strands SDK style. |
| `writing-great-skills` | [`skills/writing-great-skills`](skills/writing-great-skills) | Reference for writing and editing skills well—the vocabulary and principles that make a skill predictable. |

---

## 🔄 Featured Pipelines

### 📡 Discovery & Backlog Migration Pipeline

These three skills work in sequence to facilitate the migration of a Next.js application to an Angular (frontend) and Python (backend) architecture:

1. **`scanning-codebase`**: Analyzes the source Next.js application, identifying component structures, routes, API calls, and state management strategies.
2. **`drafting-github-issues`**: Translates the discovered components, pages, and API endpoints into discrete, well-defined migration tasks and drafts them as structured issue templates.
3. **`managing-github-backlog`**: Publishes, prioritizes, and tracks the drafted migration issues on GitHub, establishing an organized pipeline for execution.

### ⚡ Sprint Execution & Code Translation Pipeline

Once the backlog is established, the following skills execute the translation and validation pipeline:

1. **`migrating-react-to-angular`**: Converts React/JSX components into modern, standalone Angular 17+ components using Angular Material. It uses a Python scaffolding helper to generate syntactically correct boilerplate first, and leverages structured mapping references to map state hooks to Angular Signals and React components to Material standards cleanly.
2. **`migrating-nextjs-to-python`**: Converts serverless Next.js JavaScript/TypeScript API routes into high-performance, type-hinted FastAPI backend endpoints. It translates TypeScript interfaces to Pydantic schemas via automated script-based schema generation, implements SQLModel handlers, and translates JS errors to FastAPI HTTPExceptions.
3. **`validating-workspace-builds`**: Acts as a self-correcting validation check loop. It runs local builders, compilers, and linters (such as Angular component compilation and Python syntax checks) to catch and parse errors, allowing the agent to dynamically repair code failures prior to committing changes.

### 🧪 Quality Assurance & Standards Audit Pipeline

Ensures production-readiness, visual alignment, and robust test coverage before deployment:

1. **`applying-marketing-web-standards`**: Enforces brand identity, responsive layout grids, high contrast, and screen-reader accessibility across components.
2. **`auditing-ui-ux`**: Benchmarks implementations against premium design systems, pointing out hierarchy gaps, alignment issues, and spacing inconsistencies.
3. **`crawling-web-applications`**: Executes systematic visual-state crawling and regression checklists to uncover broken links, dead flows, or modal loop traps.
4. **`generating-qa-scenarios`**: Formulates naturalistic checklists and evaluation flows to verify critical paths with stakeholders.

---

## ➕ Creating & Loading Custom Skills

Skills in this repository are structured for **Progressive Disclosure**. Agents use the lightweight frontmatter structure at the top of the skill file to determine relevancy.

### 1. Skill Format Template (`SKILL.md`)

```yaml
---
name: your-skill-name
description: >-
  Brief description summarizing the purpose of the skill.
  Use when the user asks for [triggers]...
  Don't use for [anti-triggers]...
---

# Your Skill Name

Detailed markdown instructions, rules, and workflows for the agent.
```

### 2. Best Practices for Skill Creators

- **Include Deterministic Scripts:** Do not rely on instruction prompts alone for complex tasks. Place Python/Bash scripts under `scripts/` and instruct the agent to run them.
- **Provide Actionable Schemas:** Use `references/` for extensive files, JSON schemas, or template formats to preserve space in the main instructions.
- **Keep it Focused:** Each skill should do exactly one job extremely well.

---

## 🌐 Recommended Skills Repositories

You can install and reference excellent agent skills from other official and community repositories directly using the CLI:

- **[Addy Osmani's Agent Skills](https://github.com/addyosmani/agent-skills)**: A repository of production-grade engineering skills, quality gates, and best practices for AI coding agents.
  ```bash
  npx skills add addyosmani/agent-skills
  ```
- **[Awesome Claude Skills](https://github.com/ComposioHQ/awesome-claude-skills)**: A curated list of production-ready Claude skills, plugins, and tools for customizing AI workflows.
  ```bash
  npx skills add ComposioHQ/awesome-claude-skills
  ```
- **[Flutter Agent Skills](https://github.com/flutter/skills)**: A collection of specialized skills for Flutter and Dart development, widget design, and state management optimization.
  ```bash
  npx skills add flutter/skills
  ```
- **[Google Agent Skills](https://github.com/google/skills)**: Official Google repository hosting standard agent workflows, developer tool integrations, and engineering best practice skills.
  ```bash
  npx skills add google/skills
  ```
- **[Matt Pocock Skills](https://github.com/mattpocock/skills)**: A collection of agent skills, workflows, and developer utilities curated by Matt Pocock.
  ```bash
  npx skills add mattpocock/skills
  ```

---

## 📜 License

This repository is licensed under the [MIT License](LICENSE).
