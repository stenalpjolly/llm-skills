#!/usr/bin/env python3
"""
init_debug_session.py

Creates a new 'debug-ledger.md' file in the current working directory,
providing the verbatim mantra recital and an experiment tracker ledger
to systematically trace and falsify hypotheses.
"""

import os
import argparse
from datetime import date

def main():
    parser = argparse.ArgumentParser(description="Initialize a systematic debugging ledger.")
    parser.add_argument("--issue", required=True, help="Description or tracker key of the bug being investigated.")
    parser.add_argument("--out", default="debug-ledger.md", help="Output filepath. Defaults to 'debug-ledger.md'.")
    args = parser.parse_args()

    out_path = os.path.abspath(args.out)

    # Locate template file relative to this script
    script_dir = os.path.dirname(os.path.realpath(__file__))
    template_path = os.path.abspath(os.path.join(script_dir, "../references/debug_ledger_template.md"))

    template_content = ""
    if os.path.exists(template_path):
        with open(template_path, "r", encoding="utf-8") as tf:
            template_content = tf.read()
    else:
        # Fallback inline ledger in case file isn't found
        template_content = """# Running Debug Ledger

**Date**: {date}  
**Status**: IN_PROGRESS  
**Target Issue**: {issue}  

---

## Verbatim Recital

> **Mantra:**
> 1. **First is reproducibility.** Can the issue be reproduced reliably?
> 2. **Know the fail path.** Debugger first; then source trace + knob enumeration; then in-code instrumentation.
> 3. **Question your hypothesis.** What would disprove it?
> 4. **Every run is a breadcrumb.** Cross-reference all of them.

---

## 1. Reliable Reproducer Checklist
- [ ] **Repro Code / Script**: 
- [ ] **Environment**: 
- [ ] **Determinism**: 

---

## 2. Hypothesis Matrix
Rank your hypotheses. What is the single experiment to confirm or disprove each?

| Rank | Hypothesis | Clues/Evidence For | Proof / Disproof Experiment | Outcome |
|:---:|:---|:---|:---|:---|
| 1 | | | | |

---

## 3. Experiment Ledger (Breadcrumbs)
Add an entry for every single run. Do not skip any execution!

### Run #1
*   **What was changed**: 
*   **Observations / Logs**: 
*   **Conclusion**: 
"""

    today = date.today().strftime("%Y-%m-%d")
    scaffold = template_content
    scaffold = scaffold.replace("YYYY-MM-DD", today)
    scaffold = scaffold.replace("[Brief issue description / JIRA key]", args.issue)
    
    # Also support formatting variables in fallback case
    scaffold = scaffold.format(date=today, issue=args.issue)

    # Write out the ledger file
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(scaffold)

    print(f"Successfully initialized systematic debug ledger at: {out_path}")
    print("Recite the mantra first, fill in your hypotheses, and log every run!")

if __name__ == "__main__":
    main()
