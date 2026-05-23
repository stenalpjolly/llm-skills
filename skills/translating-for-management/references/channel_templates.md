# Channel Communication Templates for Leadership

This reference provides exact formatting and layout structures for translating engineering updates across different channels.

---

## 1. JIRA Comment / Status Report

Use this structured, markdown-rich format directly inside a JIRA issue or official engineering status update document.

### Template
```markdown
**Status: [Current Status / Bold TL;DR sentence]**

*   **Impact**: [Who is affected, how severely, and what they observe in user or workload terms]
*   **What Broke**: [Short paragraph with a plain-English explanation of the underlying mechanism. No function names or SHAs]
*   **Why Now / Slip Analysis**: [Optional: CI gap, latent regression, unexercised config]
*   **Owner**: [Assignee Name] ([Team Name]) | [PR / Commit Link]
*   **Next Steps**:
    1. [Immediate step, e.g. Code review / Merge]
    2. [Secondary step, e.g. Hotfix backport]
    3. [Longer-term step, e.g. Nightly test integration]
```

### Example
> **Status: Fixed pending code-review and merge.**
>
> *   **Impact**: Customers using the training pipelines hung indefinitely at model evaluation steps, blocking fine-tuning runs across the platform.
> *   **What Broke**: Our GPU synchronization engine took an unsafe fast-path shortcut under single-stream workloads. The GPUs ended up attempting to read from an unallocated memory buffer and hung waiting for a ready signal that never arrived.
> *   **Owner**: Alex Rivera (Frameworks Team) | PR #5751
> *   **Next Steps**:
>     1. Code review PR #5751 and merge to main.
>     2. Backport hotfix to release branch v7.2.
>     3. Integrate single-stream verification into nightly regression runs.

---

## 2. Slack (Channel Post or Direct Message)

Slack posts must be brief, direct, and leverage minimal formatting.

### Template
```text
*[TL;DR sentence in bold]* (JIRA-XXXX / Link)

• *Impact*: [Brief impact statement]
• *Status/Owner*: [Current state] • [Assignee Name] ([PR / Branch Link])
• *Mitigation/Workaround*: [Workaround if available today]
```

### Example
> **Tada fine-tuning hang under dumbModel is fixed pending merge.** (JIRA-12345)
>
> • *Impact*: Blocked all 8-GPU training workloads during model evaluation steps.
• *Status/Owner*: Fix authored and in review • Alex Rivera (PR #5751)
• *Mitigation*: Teams hitting this today can temporarily disable IPC registration as a workaround.

---

## 3. Async Standup Note

Briefest text format, perfect for automated Slack standup channels or quick status logs.

### Template
```text
[State Verb] [Thing/Feature/Bug] ([JIRA-XXXX]). [PR/Commit Link]. [Owner Name if not you]. [Immediate Next Step].
```

### Example
> Fixed Tada communication hang on 8-GPU model evaluation (JIRA-12345). PR #5751 in review. Alex Rivera backporting to release v7.2 next.

---

## 4. Email (Internal Exec / Cross-Team)

Email communications require a formal greeting, narrative paragraphs instead of bullet lists, and a clear call-to-action signature.

### Template
```text
Subject: [Status Noun Phrase]: [TL;DR Summary] (JIRA-XXXX)

Hi [Name/Team],

I wanted to provide an update regarding the [Issue Description]. We have successfully [current status, e.g., identified and resolved the issue].

The root cause was a [brief plain-English mechanism]. This occurred because [how it slipped through / why now]. The fix is [description of the fix, e.g., in review on PR #XXXX] and is being tested against adjacent workloads.

[Workaround / mitigation info, if active]. 

We expect to [merge/deploy/release] by [Estimated Time]. I will follow up once [condition is met].

Best regards,

[Your Name]
[Your Title]
```

---

## 5. Meeting Talking Points

Designed for verbal delivery. Keep statements extremely short, punchy, and front-load essential metrics.

### Template
```text
* [High-level summary of what happened]
* [Business or customer impact]
* [Current resolution status and PR number]
* [Immediate delivery timeline]
```

### Example
* We resolved the model fine-tuning hang affecting our GPU cluster.
* This was a blocker holding up training evaluations for major customers.
* The fix is in code review under PR #5751 and has been fully validated on 8-GPU configurations.
* Alex expects to merge and roll this out by 4 PM today.
