# Running Debug Ledger

**Date**: YYYY-MM-DD  
**Status**: IN_PROGRESS  
**Target Issue**: [Brief issue description / JIRA key]  

---

## Verbatim Recital

> **Mantra:**
> 1. **First is reproducibility.** Can the issue be reproduced reliably?
> 2. **Know the fail path.** Debugger first; then source trace + knob enumeration; then in-code instrumentation.
> 3. **Question your hypothesis.** What would disprove it?
> 4. **Every run is a breadcrumb.** Cross-reference all of them.

---

## 1. Reliable Reproducer Checklist
- [ ] **Repro Code / Script**: [e.g. `pytest tests/test_auth.py::test_login_fails` or `curl ...`]
- [ ] **Environment**: [e.g. Python 3.11, macOS, local development DB]
- [ ] **Determinism**: [e.g. 100% deterministic, or fails 8 out of 10 times]

---

## 2. Hypothesis Matrix
Rank your hypotheses from most likely to least likely. What is the single experiment to confirm or disprove each?

| Rank | Hypothesis | Clues/Evidence For | Proof / Disproof Experiment | Outcome |
|:---:|:---|:---|:---|:---|
| 1 | [Hypothesis A] | [Why you suspect this] | [What experiment will test this] | [PENDING / DISPROVED / CONFIRMED] |
| 2 | [Hypothesis B] | [Why you suspect this] | [What experiment will test this] | [PENDING / DISPROVED / CONFIRMED] |

---

## 3. Experiment Ledger (Breadcrumbs)
Add an entry for **every single run**. Do not skip any execution!

### Run #1
*   **Time / ID**: HH:MM / `[DBG-xxxx]` (if instrumented)
*   **What was changed**: [e.g., set `config_flag = False` or added log statement in `auth.ts`]
*   **Observations / Logs**: [What did the run output? Include exact error/trace]
*   **Conclusion**: [Did this rule something in or out? Update hypotheses above accordingly]

---

### Run #2
*   **Time / ID**: HH:MM / `[DBG-xxxx]`
*   **What was changed**:
*   **Observations / Logs**:
*   **Conclusion**:
