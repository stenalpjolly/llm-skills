# Worktree Provisioning & Isolation (Swarm-Fence)

This guide outlines the protocol for allocating and isolating Git worktrees to prevent merge locks during parallel multi-agent swarms.

## 1. Directory Structure

Worktrees are dynamically created under `.agent_worktrees/`:

```
.agent_worktrees/
├── wt-tier1-module-a/   (Assigned to Worker Agent 1)
├── wt-tier1-module-b/   (Assigned to Worker Agent 2)
├── wt-tier2-module-c/   (Assigned to Worker Agent 3)
└── wt-tier2-module-d/   (Assigned to Worker Agent 4)
```

## 2. Allocation Commands

```bash
# Step 1: Create isolated worktree branch from main integration branch
git worktree add -b swarm/tier1-module-a .agent_worktrees/wt-tier1-module-a HEAD

# Step 2: Assign worker workspace path in invoke_subagent call
# Workspace parameter: "inherit" or absolute directory path
```

## 3. Boundary Rules (Swarm-Fence)

1. **Strict File Boundaries**: Each worker agent is granted write permission ONLY to its assigned subdirectory/module path.
2. **Shared Static Artifacts**: Core header files, `PORTING.md`, and global type definition files are read-only.
3. **No Cross-Worktree Edits**: Workers are forbidden from modifying files outside their allocated worktree directory.

## 4. Teardown Protocol

```bash
# Step 1: Merge approved feature branch
git merge --no-ff swarm/tier1-module-a

# Step 2: Prune worktree and delete branch
git worktree remove .agent_worktrees/wt-tier1-module-a
git branch -d swarm/tier1-module-a
```
