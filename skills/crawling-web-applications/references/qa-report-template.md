# Merciless QA Audit Report: [Application Name / Link]

## 1. Executive Summary
Provide a high-level assessment of the application's UX and functional stability. Detail any fatal bottlenecks, critical crashes, or severe usability issues.

### Quality Metrics Dashboard
| Metric | Count / Value | Status (PASS/FAIL/WARN) | Comments |
| :--- | :--- | :--- | :--- |
| **Total Pages Crawled** | | | |
| **Total Unique Links** | | | |
| **Working Links (200 OK)** | | | |
| **Broken Links (>=400 / Connection Failures)** | | | |
| **Semantic Buttons Checked** | | | |
| **Imposter Buttons (A11Y Alerts)** | | | |
| **Interactive Modals/Popups Logged** | | | |
| **Forms Audited & Submitted** | | | |

---

## 2. Interactive Crawl & State Space Log
Document the traversal path of the audit, including the order in which links/elements were opened and how backtracking was performed.

```
[Start Node]
   ├── [Child URL A] (Depth 1)
   │      └── [Modal X] ──> Verified Backtrack to [Child URL A]
   └── [Child URL B] (Depth 1)
```

### State Transition Log
| Source State (Page URL) | Element Clicked (Selector/Text) | Destination State (URL / Modal Name) | Backtrack Action Used (Back button / "X" / Escape) | Backtrack Success (Yes/No) |
| :--- | :--- | :--- | :--- | :--- |
| | | | | |

---

## 3. Link Audit Details

### ❌ Broken & Failing Links
| Broken URL | HTTP Status / Error | Location (Parent Page URL) | Element Text / Anchor Label |
| :--- | :--- | :--- | :--- |
| | | | |

###  Working Links (200 OK)
| URL | Content Type | Parent Page URL(s) | Element Text / Anchor Label |
| :--- | :--- | :--- | :--- |
| | | | |

---

## 4. UI Buttons & Element Interactivity Audit

###  Semantic Buttons (HTML Standard compliant)
*These are `<button>` or `<input type="button">` tags.*
| Page URL | Button Label / Selector | Type (submit/button) | Click Interaction Outcome (State change / API call) | State Verification Status |
| :--- | :--- | :--- | :--- | :--- |
| | | | | |

### ⚠️ Imposter Buttons (Semantic Violations / Accessibility Risks)
*These are `<div>`, `<span>`, or `<a>` tags designed or behaving as buttons but lacking proper semantics.*
| Page URL | Element Tag | Selector / Class | Display Text | Missing Roles (`role="button"`, `tabindex="0"`)? | Click Interaction Outcome (Does it work?) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| | | | | | |

---

## 5. Overlays, Modals, and Pop-ups Log
| Page URL | Modal/Popup Description | Trigger Element | Modal Content/Header | Backtrack / Close Button Used | Dismissal Verification (Did it return to normal?) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| | | | | | |

---

## 6. Form Audits
| Page URL | Form Selector / ID | Input Fields Tested | Test Values Injected | Submit Button Used | Response Verification (Success Toast/Error/Redirect) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| | | | | | |

---

## 7. Discovered Bugs and Bad UI Patterns
Mercilessly describe any layout reflows, hidden errors, slow responsiveness, or broken workflows discovered during the audit.
1. **[Bug Name / Category]:** Detailed explanation, step-by-step reproduction, and recommendation.
