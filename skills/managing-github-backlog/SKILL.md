---
name: managing-github-backlog
description: >-
  Creates labels and publishes drafted JSON issues to a GitHub repository. Use when a set of migration tasks has been drafted and needs to be pushed to the issue tracker. Don't use for reading existing issues, managing pull requests, or drafting the issues themselves.
---

# Managing GitHub Backlog

This skill executes the final step of the planning phase by pushing drafted issues to GitHub.

## Rules
1. **Do not use curl or gh cli manually.** The GitHub API is strict. Always use the bundled `push_issues.py` script to ensure idempotency and correct formatting.
2. **Verify Input.** Ensure `drafted_issues.json` exists and is valid JSON before running the script.

## Execution
Run the script to push the issues. You will need the repository name (e.g., `owner/repo`) and a GitHub token.

```bash
export GITHUB_TOKEN="your_token_here"
python3 scripts/push_issues.py --repo {owner/repo} --file drafted_issues.json
```
