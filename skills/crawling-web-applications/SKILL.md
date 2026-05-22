---
name: crawling-web-applications
description: >-
  Crawls, navigates, and audits a web application's links, buttons, and interactive elements. Performs systematic backtracking to map page states, pop-ups, modals, and forms. Returns a mercilessly detailed QA report of working and broken paths, non-standard UI button elements, and interactive failures. Use when performing deep post-deployment testing, link checks, or visual/functional QA. Don't use for unit testing source code, static linting, or backend API performance benchmarking.
---

# Crawling and Auditing Web Applications

This skill enables an agent to operate as an exhaustive, merciless QA tester. Starting with an entry URL (such as `http://localhost:3000` or a remote staging link), the agent crawls every hyperlink, interacts with buttons and state-changing components (pop-ups, modals, dropdowns, menus), systematically backtracks when dead ends are reached, and uncovers visual, functional, and accessibility issues.

## Rules
1. **Zero Mercy Philosophy.** If an element looks like a button but is actually a `<div>` or `<span>` without appropriate aria roles or tab index, log it as a semantic/accessibility bug. If a click does not yield a visible or state-based reaction, log it as a dead-click.
2. **State Backtracking.** Do not get stuck in infinite loops. Maintain a strict set of visited page-states (combination of page URL + active overlay/modal state). When a path is fully explored or hits a dead-end, systematically backtrack (e.g., by clicking "Close" buttons, going back in history, or pressing Escape) and resume exploration.
3. **Strict Validation.** Any broken links (returning HTTP status >= 400), unhandled client-side exceptions (seen in console logs), or visual overlap bugs must be captured with precise contexts.
4. **Use Deterministic Baselines first.** Run the helper crawler script `python3 scripts/web_crawler.py` to extract all standard static and dynamic anchor links, forms, and HTTP response codes. Use this baseline to drive the subsequent manual/interactive audits.

## Workflow

```
[Target URL] ──> [Run Baseline Crawler Script] ──> [Interactive Session (Clicking, Modals, Backtracking)] ──> [Analyze & Classify UI Elements] ──> [Generate QA Report]
```

### 1. Establish the Baseline Map
Run the automated crawler helper script to perform an initial, fast scan of the site hierarchy, links, and forms.
```bash
python3 scripts/web_crawler.py --url {target_url} --max-depth 3 --output-json baseline_map.json
```
This baseline identifies standard pages, anchor links, form inputs, and immediate 404/500 broken links.

#### Aligning with LLM Reasoning (Form and File Upload Injection)
If the crawler encounters dynamic multi-phase forms or screens that require input values (such as email, password, or file uploads) to transition to the next phase, the LLM agent can act as a reasoning engine:
1. **Analyze Form Requirements:** Inspect the discovered `<form>` structures and their field requirements logged in the `baseline_map.json`.
2. **Formulate Inputs Mapping:** Construct a JSON mapping of input names to target values or file descriptors.
3. **Execute Guided Audits:** Pass this mapping to the crawler via the `--form-inputs` argument.
4. **Automated Submission & Traversal:** The crawler automatically binds these values, packages multipart/form-data for file inputs (reading local files or injecting robust mock files), submits the forms (handling POST and GET transitions), and recursively audits all downstream stages.

**Example Command (Inline JSON):**
```bash
python3 scripts/web_crawler.py --url http://localhost:3000 --form-inputs '{"username": "admin", "resume_upload": "/path/to/resume.pdf"}' --output-json qa_report.json
```

**Example Command (JSON file):**
```bash
python3 scripts/web_crawler.py --url http://localhost:3000 --form-inputs form_values.json --output-json qa_report.json
```

### 2. Deep Interactive Audit & State Backtracking
For each discovered page, perform interactive exploration of dynamic UI states:
*   **Identify Interactive Targets:** Locate elements that look like buttons, dropdown triggers, accordion headers, tab heads, and menu items.
*   **Track States:** Let each UI state be represented as:
    $$\text{State} = (\text{URL}, \{\text{Active Overlays/Modals}\})$$
*   **DFS with Backtracking:**
    1. Click an unvisited interactive element (e.g., "Open Modal").
    2. Document state changes (e.g., modal is visible, screen is dimmed).
    3. Explore links/buttons inside that new state (recursively).
    4. Backtrack by executing a close action (clicking "X", clicking backdrop, or sending Escape).
    5. Verify the UI returned successfully to the parent state.

### 3. Classify UI Elements
Examine elements visually and semantically:
*   **Semantic Button:** `<button>` or `<input type="button">`. Accessible, focusable, clickable.
*   **Imposter Button:** `<div>`, `<span>`, or `<a>` styled like a button but missing `role="button"`, `tabindex="0"`, or keyboard event listeners.
*   **Broken Link:** Any anchor `<a>` tag with missing `href`, empty string, `href="#"` (unless verified javascript attachment), or pointing to a non-existent or 404 page.

### 4. Create the QA Report
Consolidate findings into the structured format defined in `references/qa-report-template.md`. Save the final report as `qa_audit_report.md`.
