#!/usr/bin/env python3
"""
prepare_scrutiny_audit.py

Analyzes git diffs (staged, unstaged, or against a base branch) to generate 
a structured scrutiny audit checklist. This provides a clean roadmap of changed 
files, functions, and lines to trace end-to-end, as required by the 'scrutinize' skill.
"""

import os
import re
import argparse
import subprocess

def run_cmd(args):
    """
    Runs a shell command and returns the stdout string.
    """
    try:
        res = subprocess.run(args, capture_output=True, text=True, check=True)
        return res.stdout.strip()
    except Exception as e:
        return ""

def parse_diff(diff_output):
    """
    Parses git diff output and returns a dictionary of changed files with changed line ranges.
    """
    changed_files = {}
    current_file = None

    for line in diff_output.splitlines():
        if line.startswith("+++ b/"):
            current_file = line[6:]
            changed_files[current_file] = []
        elif line.startswith("@@ ") and current_file:
            # Parse diff hunk header: @@ -start,len +start,len @@
            match = re.match(r'^@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@', line)
            if match:
                start_line = int(match.group(1))
                hunk_len = int(match.group(2)) if match.group(2) else 1
                end_line = start_line + hunk_len - 1
                changed_files[current_file].append((start_line, end_line))
                
    return changed_files

def main():
    parser = argparse.ArgumentParser(description="Generate a scrutiny audit checklist based on git changes.")
    parser.add_argument("--base", default="HEAD", help="Base branch or commit to diff against. e.g. 'main', 'origin/main', or 'HEAD'.")
    parser.add_argument("--staged", action="store_true", help="Analyze staged changes only.")
    parser.add_argument("--unstaged", action="store_true", help="Analyze unstaged changes only.")
    parser.add_argument("--out", default="scrutiny_audit_checklist.md", help="Output file path.")
    args = parser.parse_args()

    # Determine diff flags
    diff_args = ["git", "diff"]
    if args.staged:
        diff_args.append("--cached")
    elif not args.unstaged and args.base != "HEAD":
        diff_args.append(f"{args.base}...HEAD")

    diff_output = run_cmd(diff_args)
    if not diff_output:
        # Check if we have unstaged working tree changes
        diff_output = run_cmd(["git", "diff"])
        if not diff_output:
            print("No active code changes detected in the git diff. Scrutiny checklist skipped.")
            return

    changed_files = parse_diff(diff_output)

    if not changed_files:
        print("No changed source files found in the diff.")
        return

    # Write the checklist
    with open(args.out, "w", encoding="utf-8") as f:
        f.write("# Scrutiny Audit Checklist\n\n")
        f.write("Use this checklist to walk code paths end-to-end, questioning intent, tracing execution flows, and validating assumptions.\n\n")

        # 1. Intent Section
        f.write("## 1. Intent Audit\n")
        f.write("- [ ] **Core Goal**: Define what this change is trying to achieve in one sentence.\n")
        f.write("- [ ] **Simplification**: Is there a smaller, simpler, or more elegant way to solve this? (e.g. config flag instead of code change, utilizing existing helper methods).\n\n")

        # 2. Changed Files Trace Matrix
        f.write("## 2. Code Trace Checklist\n")
        f.write("Trace the call paths, starting from each changed line range, walking forward and backward to see how state is mutated.\n\n")
        
        for filepath, hunks in changed_files.items():
            f.write(f"### File: `{filepath}`\n")
            for idx, (start, end) in enumerate(hunks):
                f.write(f"- [ ] **Hunk {idx+1} (Lines {start}-{end})**:\n")
                f.write("  - [ ] *Traced Caller*: What enqueues or triggers this? (Verify unchanged parent files / seams).\n")
                f.write("  - [ ] *State Mutation*: What state, files, or properties are mutated here?\n")
                f.write("  - [ ] *Return/Exit*: What is returned? Ensure all exit vectors are safe.\n")
            f.write("\n")

        # 3. Verification Steps
        f.write("## 3. Verification & Stress Checking\n")
        f.write("- [ ] **Edge Cases**: Check empty/null values, concurrent requests, extreme scales.\n")
        f.write("- [ ] **Failure Handling**: How does this behave if network, database, or API queries fail?\n")
        f.write("- [ ] **Test Coverage**: Do the test suites actually execute the modified code branches, or do they bypass them via mocks?\n\n")

        # 4. Final Verdict
        f.write("## 4. Audit Verdict\n")
        f.write("- **Recommendation**: (SHIP / FIX-THEN-SHIP / REWORK / REJECT)\n")
        f.write("- **Primary Reason**: [Insert single biggest reasoning here]\n")

    print(f"Successfully generated scrutiny checklist at: {args.out}")

if __name__ == "__main__":
    main()
