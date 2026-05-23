#!/usr/bin/env python3
"""
manage_github_issue.py

A helper script wrapping the GitHub CLI (gh) to search, create, and update
repository issues. This streamlines the issue-tracking workflow for the
test-driven issue resolution skill.
"""

import os
import sys
import json
import argparse
import subprocess

def run_gh_cmd(args):
    """
    Executes a GitHub CLI (gh) command and returns the JSON parsed output or string output.
    """
    full_cmd = ["gh"] + args
    try:
        # Check if gh CLI is installed and configured
        result = subprocess.run(full_cmd, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing GitHub CLI command: {' '.join(full_cmd)}", file=sys.stderr)
        print(f"Stdout: {e.stdout}", file=sys.stderr)
        print(f"Stderr: {e.stderr}", file=sys.stderr)
        sys.exit(e.returncode)
    except FileNotFoundError:
        print("Error: The 'gh' CLI tool is not installed or not in your system's PATH.", file=sys.stderr)
        print("Please ensure GitHub CLI is installed to use this skill.", file=sys.stderr)
        sys.exit(127)

def search_issues(repo, query):
    """
    Searches for existing issues matching the query in the given repository.
    """
    args = [
        "issue", "list",
        "--repo", repo,
        "--search", query,
        "--state", "all",
        "--limit", "10",
        "--json", "number,title,state,url"
    ]
    stdout = run_gh_cmd(args)
    if not stdout:
        return []
    try:
        return json.loads(stdout)
    except json.JSONDecodeError:
        return []

def create_issue(repo, title, body, labels=None):
    """
    Creates a new issue in the given repository.
    """
    args = [
        "issue", "create",
        "--repo", repo,
        "--title", title,
        "--body", body
    ]
    if labels:
        args.extend(["--label", ",".join(labels)])
    
    # Run the command
    output = run_gh_cmd(args)
    return output

def update_issue(repo, number, title=None, body=None, labels=None, state=None):
    """
    Updates an existing issue.
    """
    args = ["issue", "edit", str(number), "--repo", repo]
    if title:
        args.extend(["--title", title])
    if body:
        args.extend(["--body", body])
    if labels:
        args.extend(["--add-label", ",".join(labels)])
    
    # Apply changes
    run_gh_cmd(args)

    # If state transition is requested, run close or reopen separately
    if state == "closed":
        run_gh_cmd(["issue", "close", str(number), "--repo", repo])
    elif state == "open":
        run_gh_cmd(["issue", "reopen", str(number), "--repo", repo])
    
    print(f"Successfully updated issue #{number} in {repo}")

def main():
    parser = argparse.ArgumentParser(description="Manage GitHub Issues for test-driven workflows.")
    parser.add_argument("--repo", required=True, help="GitHub repository name in the format 'owner/repo' (e.g., thananon/9arm-skills).")
    
    # Mutually exclusive actions
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--search", help="Search query to locate existing issues.")
    group.add_argument("--create", action="store_true", help="Create a new issue.")
    group.add_argument("--update", type=int, help="Issue number to update.")
    
    # Optional parameters for creation or updating
    parser.add_argument("--title", help="Title for the issue.")
    parser.add_argument("--body", help="Inline body text for the issue.")
    parser.add_argument("--body-file", help="Path to a file containing the markdown body.")
    parser.add_argument("--labels", nargs="+", help="Labels to associate with the issue.")
    parser.add_argument("--state", choices=["open", "closed"], help="Target state when updating an issue.")
    args = parser.parse_args()

    # Read body from file if specified
    body_content = args.body or ""
    if args.body_file:
        try:
            with open(os.path.abspath(args.body_file), "r", encoding="utf-8") as f:
                body_content = f.read()
        except Exception as e:
            print(f"Error reading body-file: {e}", file=sys.stderr)
            sys.exit(1)

    # Execute Search Action
    if args.search:
        print(f"Searching for issues matching '{args.search}' in {args.repo}...")
        issues = search_issues(args.repo, args.search)
        if not issues:
            print("No matching issues found.")
        else:
            print(f"Found {len(issues)} matching issue(s):")
            print(json.dumps(issues, indent=2))

    # Execute Create Action
    elif args.create:
        if not args.title:
            print("Error: --title is required when creating an issue.", file=sys.stderr)
            sys.exit(1)
        if not body_content:
            print("Error: --body or --body-file is required when creating an issue.", file=sys.stderr)
            sys.exit(1)
        
        print(f"Creating a new issue in {args.repo}...")
        issue_url = create_issue(args.repo, args.title, body_content, args.labels)
        print(f"Successfully created issue: {issue_url}")

    # Execute Update Action
    elif args.update:
        if not (args.title or body_content or args.labels or args.state):
            print("Error: At least one modification field (--title, --body, --body-file, --labels, --state) must be specified for updates.", file=sys.stderr)
            sys.exit(1)
        
        print(f"Updating issue #{args.update} in {args.repo}...")
        update_issue(args.repo, args.update, args.title, body_content, args.labels, args.state)

if __name__ == "__main__":
    main()
