# Adversarial Red-Team Auditing

This reference details the secondary verification phase where dedicated Red-Team auditor subagents inspect code produced by worker agents.

## 1. Auditor Pair Pattern

For every module converted by a **Translator Agent**, an **Auditor Agent** is spawned with an explicit adversarial prompt to break or critique the code.

```
[Translator Agent]  ---> Emits Rust Code ---> [Auditor Agent (Red-Team)]
                                                     |
                                            Checks Safety & Invariants
                                                     |
                                            Approve / Reject Diff
```

## 2. Red-Team Audit Checklist

The auditor subagent evaluates the diff against 5 critical audit dimensions:

1. **Unsafe Block Discipline**:
   - Are all `unsafe` blocks accompanied by a `// SAFETY:` explanation comment?
   - Can raw pointer arithmetic or FFI dereferences be replaced with safe abstraction wrappers?
2. **Memory & Concurrency Hazards**:
   - Are there hidden memory leaks or circular `Arc` references?
   - Are data structures lock-free or properly synchronized without deadlocks?
3. **Lazy Code & Stub Detection**:
   - Are there TODO/FIXME comments, `todo!()` macros, or unhandled `unwrap()` calls in error paths?
4. **Architectural Compliance (`PORTING.md`)**:
   - Did the translator introduce banned external dependencies or runtime overhead?
5. **API & Contract Parity**:
   - Does the signature and behavior match the original specification exactly?

## 3. Remediation Protocol

If the Auditor Agent rejects a diff:
1. It generates a structured audit report detailing the exact line numbers and risk severity (CRITICAL, HIGH, MEDIUM).
2. The Translator Agent receives the report and must issue a targeted remediation diff addressing every flagged item.
3. Code is merged into the integration branch ONLY when the Auditor Agent returns `STATUS: APPROVED`.
