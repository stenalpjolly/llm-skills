# Verbose Prompt Synthesis Template

Use this template during **Phase 6: Verbose Prompt Synthesis** to construct the `<OUTPUT>` payload under the `### The Final Verbose Prompt: <OUTPUT>` heading. Replace all bracketed `<PLACEHOLDERS>` with verified domain content. Do not leave any placeholder text in the final output.

````markdown
# <PROMPT TITLE / MISSION>

## Core Objective & Rationale
<Clear, concise statement of what must be accomplished and why it matters>

## Target Audience & Output Schema
- **Target Executor**: <Target model, agent, or human consumer>
- **Output Format**: <Exact formatting, markdown requirements, or JSON schema>

## Execution Process
Follow these sequential steps to accomplish the task:

1. **<Step 1 Title>**
   - **Action**: <Imperative instruction on what to do>
   - **Precision Tip**: <Concrete tip for clarity, boundary handling, or accuracy>

2. **<Step 2 Title>**
   - **Action**: <Imperative instruction on what to do>
   - **Precision Tip**: <Concrete tip for clarity, boundary handling, or accuracy>

3. **<Step 3 Title>**
   - **Action**: <Imperative instruction on what to do>
   - **Precision Tip**: <Concrete tip for clarity, boundary handling, or accuracy>

## Reference Example
```<LANGUAGE/FORMAT>
<Concrete input/output example demonstrating expected behavior and structure>
```

## Constraints & Guardrails
- **Tone & Style**: <Required tone, e.g., technical, direct, professional>
- **Mandatory Requirements**: <Explicit list of required inclusions or behaviors>
- **Negative Constraints (Anti-Goals)**: <Explicit list of what must NEVER be done>
- **Boundary Conditions**: <Length limits, error fallbacks, or data handling rules>

## Verification & Completion Criteria
- **Checkable Done State**: <How the executor verifies the task is complete and correct>
````
