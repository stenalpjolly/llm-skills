# Post-Mortem: [JIRA Ticket ID / Bug Name]

**Date**: YYYY-MM-DD  
**Owner**: [Assignee / Team]  
**PR/Commit Link**: [URL to PR or Commit]  

---

## 1. Summary
*One-paragraph TL;DR. What broke in user/workload terms, and what fixed it in a single sentence.*

## 2. Symptom
*What was actually observed? (Include exact test outputs, error logs, stack traces, performance metrics, or customer reports. Avoid paraphrasing.)*

```text
[Insert exact log output or error stack trace here]
```

## 3. Root Cause
*The actual bug mechanism. Code-level identifiers are expected here (e.g. file paths, function names, variable mutations, race states, branch logic).*

## 4. Why It Produced the Symptom
*Walk the cause-and-effect chain from the root cause to the observed symptom. Connect the code-level flaw to the high-level visible failure.*

## 5. Fix
*What changed, and why does this change resolve the root cause permanently instead of just hiding the symptom? (Link to PR / Commit)*

## 6. How It Was Found
*The exact debugging path:*
- *What repro made it deterministic?*
- *What tools or techniques cracked it? (e.g. debugger, logs, probe instrumentation)*
- *What hypotheses were tried and rejected, and why?*
- *The single experiment that confirmed the root cause.*

## 7. Why It Slipped Through
*What allowed this bug to reach production / main branch? (Choose the real, blameless reason, e.g. CI testing gap, latent code side-effect, unexercised configuration, review oversight).*

## 8. Validation
*Concrete proof that the fix works:*
- *Test result links or name of new regression test.*
- *Performance benchmarking numbers (before vs. after).*
- *Scale/soak test duration and outcome.*

## 9. Action Items / Follow-ups
*Trackable next-steps that aren't in the fix PR itself. Include owner and tracking ID.*

| Item ID | Action Description | Owner | Tracking Artifact (JIRA / GitHub Issue) |
|:---|:---|:---|:---|
| ACT-1 | Add regression test `[test_name]` at `<seam>` | [Name] | [JIRA-XXXX / Issue #] |
| ACT-2 | [Adjacent refactor or CI gap closure] | [Name] | [JIRA-XXXX / Issue #] |
