# Prompt Evaluation & Debugging Checklist

Use this checklist during **Phase 5: Debugging & Effectiveness Audit** to verify draft prompt quality before synthesizing the final verbose prompt. Every check item must pass without ambiguity.

## 1. Objective & Scope Verification
- [ ] **Single Purpose**: Does the prompt serve exactly one clearly defined operational goal without horizontal scope creep?
- [ ] **Executor Alignment**: Is the technical depth and formatting calibrated to the target executor (e.g., human vs. coding agent vs. analytical LLM)?
- [ ] **Terminal State**: Is the desired success state explicit and verifiable?

## 2. Instruction Precision
- [ ] **Imperative Verbs**: Do all step instructions use direct imperative verbs (`Extract`, `Audit`, `Compare`, `Verify`) rather than passive or optional language (`try to`, `should consider`)?
- [ ] **Sequential Ordering**: Are multi-step actions ordered chronologically from initialization to validation?
- [ ] **Precision Tips**: Does every step include actionable tips for clarity, boundary handling, or parsing rules?
- [ ] **No-Op Elimination**: Has every sentence been checked for relevance, removing prose that does not change model behavior versus default pretrained behavior?

## 3. Constraint & Guardrail Audit
- [ ] **Negative Constraints (Anti-Goals)**: Are explicit prohibitions documented for common failure modes (e.g., conversational filler, modifying adjacent files, inventing unrequested features)?
- [ ] **Tone & Density**: Is the required tone and verbosity explicitly bounded?
- [ ] **Structural Boundaries**: Are formatting requirements (e.g., markdown headings, code blocks, JSON schemas) specified unambiguously?

## 4. Example Alignment
- [ ] **Representative Input/Output**: Is there at least one complete example illustrating both input context and well-formed output?
- [ ] **Schema Compliance**: Does the example output strictly match the output schema defined in Phase 1?
- [ ] **Edge-Case Coverage**: Does the example demonstrate how to handle non-obvious formatting or boundary conditions?

## 5. Anti-Pattern Inspection
- [ ] **No Fuzzy Quantifiers**: Are subjective terms (`appropriate`, `better`, `as needed`, `reasonable`) replaced with binary observable criteria (turning gates **red** or green)?
- [ ] **No Premature Completion Triggers**: Are post-completion steps or vague stopping rules replaced with exhaustive, checkable completion criteria?
