---
name: resolving-merge-conflicts
description: >-
  Resolves in-progress git merge or rebase conflicts by locating conflicting files, tracing original intents of both branches through commit messages and PR history, resolving each hunk to preserve intents without inventing new behavior, running local automated checks (builds, tests, linters) to verify correctness, and finalizing the merge or rebase process. Use when git operations report a conflict, or the repository enters a merging/rebasing state. Don't use when there are no active git conflicts.
---

# Resolving Merge Conflicts

Follow this disciplined workflow to safely resolve in-progress git merge or rebase conflicts.

## 1. See the Current State

Determine the topology of the branch divergence and identify all conflicted files.

- Run `git status` to find files with unresolved conflicts (listed under "Unmerged paths").
- Alternatively, run `git diff --name-only --diff-filter=U` to get a clean list of conflicting files.
- Run `git log --graph --oneline --left-right HEAD...MERGE_HEAD` (or `REBASE_HEAD`) to visualize the commits on both sides of the divergence. This establishes context for the incoming changes relative to your local branch.

## 2. Find the Primary Sources

Understand *why* each conflicting change was made to avoid breaking existing or incoming functionality.

- For each conflict, identify the commit that introduced the changes on both sides:
  - Run `git log -S "conflicting line"` or `git log -G "regex"` to search the commit history of both branches.
  - Use `git blame -L <start>,<end> <file>` on the parents of the merge/rebase commits to see who changed those lines and in which commits.
- Read the commit messages, associated pull request descriptions, or issue/ticket references linked in those commits to understand the underlying intent of both authors.
- **Critical Context on Roles:**
  - **During a Merge:** `HEAD` (ours) is your current branch. `MERGE_HEAD` (theirs) is the incoming branch.
  - **During a Rebase:** The roles are swapped. `HEAD` is the upstream base commit you are rebasing onto (ours), and the commit currently being applied is the incoming commit from your branch (theirs).

## 3. Resolve Each Hunk

Resolve the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`) with surgical precision.

- Open the conflicting files and locate the conflict markers.
- Analyze both hunks to preserve both intents where possible:
  - If both additions/modifications are necessary and independent, combine them logically.
  - If one change refactors structure and the other adds logic, adapt the logic to the new structure.
- When hunks are incompatible, prioritize the change that matches the merge's stated goal. Clearly note the trade-off in the final commit or code comments if required.
- **Do not invent new behavior.** Your role is to integrate the two existing intents, not design a third, unrequested feature.
- **Always resolve; never abort.** Do not use `git merge --abort` or `git rebase --abort` unless the entire merge/rebase operation is fundamentally invalid and requested by the user.

## 4. Run Automated Checks

Ensure that the conflict resolution has not introduced syntax errors, build failures, or regressions.

- Locate the project's package, build, and configuration files to discover available verification tools (e.g., `package.json`, `Cargo.toml`, `requirements.txt`).
- Execute verification steps in this order:
  1. **Typecheck/Compile:** Run `tsc`, `npm run build`, `cargo check`, or equivalent commands to verify compilation.
  2. **Test Suite:** Run `npm run test`, `pytest`, `cargo test`, or equivalent to ensure all tests pass.
  3. **Lint/Format:** Run `npm run lint`, `ruff check .`, or equivalent linter and formatter commands.
- Fix any failures or broken imports immediately before proceeding.

## 5. Finish the Merge/Rebase

Finalize the resolution by staging the resolved files and completing the git operation.

- Stage each resolved file:
  - Run `git add <file>`
- Check the status again with `git status` to ensure all conflicts are marked as resolved.
- Complete the process:
  - **If in a Merge:** Run `git merge --continue` (or `git commit` if `--continue` is not supported in the git version) to finish.
  - **If in a Rebase:** Run `git rebase --continue`.
- If rebasing and subsequent commits encounter conflicts, repeat steps 1–5 for each conflicting commit until the entire rebase is completed.
