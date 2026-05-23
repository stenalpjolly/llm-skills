#!/usr/bin/env python3
"""
scaffold_post_mortem.py

Generates a post-mortem document skeleton pre-populated with today's date, 
ticket IDs, title, and standard sections to jumpstart engineering writing.
"""

import os
import argparse
from datetime import date

def main():
    parser = argparse.ArgumentParser(description="Scaffold a new post-mortem document.")
    parser.add_argument("--ticket", required=True, help="JIRA or GitHub Issue tracking ID (e.g., JIRA-4022).")
    parser.add_argument("--title", required=True, help="Title of the bug or post-mortem.")
    parser.add_argument("--owner", default="[Insert Owner Name]", help="Name of the engineer authoring the document.")
    parser.add_argument("--out", help="Optional output path. Defaults to 'postmortems/<ticket>.md'.")
    args = parser.parse_args()

    # Determine default or custom output path
    if args.out:
        out_path = os.path.abspath(args.out)
    else:
        out_dir = os.path.abspath(os.path.join(os.getcwd(), "postmortems"))
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, f"{args.ticket.upper().replace('/', '_')}.md")

    # Attempt to locate the template relative to this script
    script_dir = os.path.dirname(os.path.realpath(__file__))
    template_path = os.path.abspath(os.path.join(script_dir, "../references/post_mortem_template.md"))
    
    template_content = ""
    if os.path.exists(template_path):
        with open(template_path, "r", encoding="utf-8") as tf:
            template_content = tf.read()
    else:
        # Fallback inline template in case file isn't found
        template_content = """# Post-Mortem: {ticket} - {title}

**Date**: {date}  
**Owner**: {owner}  
**PR/Commit Link**: [URL to PR or Commit]  

---

## 1. Summary
*One-paragraph TL;DR. What broke in user/workload terms, and what fixed it in a single sentence.*

## 2. Symptom
*What was actually observed? (Include exact test outputs, error logs, stack traces, or customer reports.)*

## 3. Root Cause
*The actual bug mechanism. Code-level identifiers are expected here (e.g. file paths, function names, variable mutations, race states).*

## 4. Why It Produced the Symptom
*Walk the cause chain from the root cause to the observed symptom.*

## 5. Fix
*What changed, and why does this change resolve the root cause permanently?*

## 6. How It Was Found
*The exact debugging path (deterministic repro, techniques, hypotheses tried/rejected).*

## 7. Why It Slipped Through
*What allowed this bug to reach production / main branch? (Blameless analysis).*

## 8. Validation
*Concrete proof that the fix works (test result links, metrics, benchmarks).*

## 9. Action Items / Follow-ups
*Trackable next-steps with owner and tracking ID.*
"""

    # Populate the placeholders
    today = date.today().strftime("%Y-%m-%d")
    scaffold = template_content
    scaffold = scaffold.replace("[JIRA Ticket ID / Bug Name]", f"{args.ticket} - {args.title}")
    scaffold = scaffold.replace("YYYY-MM-DD", today)
    scaffold = scaffold.replace("[Assignee / Team]", args.owner)
    
    # Also support formatting variables in fallback case
    scaffold = scaffold.format(ticket=args.ticket, title=args.title, date=today, owner=args.owner)

    # Ensure output directories exist and write
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(scaffold)

    print(f"Successfully generated post-mortem template at: {out_path}")

if __name__ == "__main__":
    main()
