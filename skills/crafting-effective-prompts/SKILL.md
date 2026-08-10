---
name: crafting-effective-prompts
description: >-
  Creates high-clarity, unambiguous, and effective prompts for LLMs and autonomous agents using structured prompt engineering techniques. Use when a user asks to craft, improve, refine, or write a prompt, design a complex instruction for an AI model, or convert a task query into a verbose prompt. Don't use for writing general product requirement documents (use refining-feature-requests) or for drafting autonomous goal specifications (use designing-goal-loops).
---

# Crafting Effective Prompts

High-performance prompt engineering requires structured decomposition before final synthesis. Never jump straight to writing the final prompt (**premature completion**). Follow the mandatory six-phase analysis pipeline to ground instructions, eliminate ambiguity, and verify effectiveness before emitting the final verbose prompt.

## Phase 1: Purpose & Outcome Definition (Legwork)

Perform upfront **legwork** to clarify the exact operational task and terminal success state before drafting instructions, because unspoken assumptions cause scope drift and misaligned model outputs.

1. **Define Core Objective**: State precisely what problem the prompt solves or what artifact it generates.
2. **Identify Target Executor**: Specify the intended consumer (e.g., human user, coding agent, creative LLM, or specialized pipeline) to calibrate technical depth and formatting.
3. **Specify Output Schema**: Define the required structural format (e.g., markdown report, JSON payload, code diff, or structured prose).

**Completion Criterion**: The prompt's core objective, target executor, and exact output schema are documented with zero placeholders.

## Phase 2: Step-by-Step Process Decomposition

Break down the task into an ordered sequence of atomic execution steps, because LLMs execute reliable reasoning only when multi-step procedures are explicitly sequenced.

1. **Sequence Atomic Actions**: Divide the user query into chronological, numbered execution steps from initialization to final validation.
2. **Specify Action Imperatives**: Write each step using direct imperative verbs (`Extract`, `Audit`, `Compare`, `Verify`), avoiding vague suggestions (`consider`, `try to`).
3. **Attach Precision Tips**: For each step, provide concrete precision tips (e.g., regex boundaries, edge-case fallbacks, or parsing rules) to eliminate interpretation variance.

**Completion Criterion**: Every required action is decomposed into numbered, sequential steps with accompanying precision tips.

## Phase 3: Domain Grounding & Concrete Examples

Construct at least one domain-relevant reference example, because abstract instructions invite hallucinations while concrete examples anchor model behavior and demonstrate expected tone and formatting.

1. **Formulate Reference Input/Output**: Build a realistic example showing both the representative input context and the expected well-formed output.
2. **Illustrate Edge Cases**: Highlight non-obvious patterns in the example that demonstrate how to handle boundary conditions or formatting gotchas.
3. **Verify Schema Alignment**: Check that the example output strictly conforms to the schema defined in Phase 1.

**Completion Criterion**: At least one complete, domain-relevant input/output example is formulated and verified against the target schema.

## Phase 4: Clarity, Specificity & Guardrails

Establish explicit constraints and negative rules, because models obey explicit prohibitions more reliably than implicit assumptions and need strict boundaries to prevent bloat.

1. **Set Tone & Verbosity**: Specify the required tone and density (e.g., technical and direct, zero conversational filler, professional analytical).
2. **Define Negative Constraints (Anti-Goals)**: Explicitly list what the executor must *never* do (e.g., "Do not include preambles or postambles", "Do not modify adjacent helper modules").
3. **Set Structural Boundaries**: Define length limits, required markdown headings, or syntax tags needed for reliable downstream parsing.

**Completion Criterion**: Tone specifications, structural boundaries, and at least two explicit negative constraints are documented.

## Phase 5: Debugging & Effectiveness Audit

Execute a **tight loop** check against explicit failure modes before publishing, because auditing draft instructions prevents shipping brittle or ambiguous prompts.

1. **Consult Evaluation Checklist**: Open and apply [`references/prompt-evaluation-checklist.md`](references/prompt-evaluation-checklist.md) to audit the draft prompt across objective clarity, instruction precision, guardrails, and example alignment.
2. **Test for No-Ops and Ambiguities**: Identify any sentence that fails to change model behavior versus the default and delete or replace it with binary observable rules (making fuzzy criteria **red** or green).
3. **Resolve Failures**: Fix all identified ambiguities, missing edge cases, or weak completion criteria before proceeding to synthesis.

**Completion Criterion**: Every check item in [`references/prompt-evaluation-checklist.md`](references/prompt-evaluation-checklist.md) is verified with zero outstanding ambiguities or no-ops.

## Phase 6: Verbose Prompt Synthesis

Synthesize the verified analysis into a self-contained payload, because combining purpose, process, examples, and guardrails into an atomic prompt ensures immediate, error-free execution.

1. **Present Structured Analysis**: Output the five analysis sections (Purpose, Process, Examples, Clarity & Specificity, Review Audit) for user visibility and alignment.
2. **Emit Verbose Prompt**: Under an explicit `### The Final Verbose Prompt: <OUTPUT>` header, synthesize the complete prompt using the format in [`references/verbose-prompt-template.md`](references/verbose-prompt-template.md).
3. **Verify Self-Containment**: Ensure the final `<OUTPUT>` block is copy-pasteable, self-contained, and contains zero placeholders or TODOs.

**Completion Criterion**: The five structured analysis sections and the finalized verbose prompt under `### The Final Verbose Prompt: <OUTPUT>` are delivered to the user with zero placeholder text.
