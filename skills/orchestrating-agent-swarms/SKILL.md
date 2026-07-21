---
name: orchestrating-agent-swarms
description: Orchestrates high-throughput parallel agent swarms for large-scale code migrations, multi-worktree isolation, compiler feedback loops, and test oracle verification.
disable-model-invocation: true
---

# Orchestrating Agent Swarms

A skill to govern large-scale, automated code migrations and multi-file rewrites using concurrent agent swarms. Extends conductor-mesh orchestration by adding git worktree isolation (**Swarm-Fence**), compiler error feedback loops (**Self-Healing**), test-suite referee gates (**Oracle**), and adversarial reviewer pairs (**Red-Team**).

---

## Relationship to /orchestrating-subagents

This skill is a specialized extension of [orchestrating-subagents](file:///usr/local/google/home/stenalpjolly/.gemini/config/skills/orchestrating-subagents/SKILL.md). It inherits the core **Conductor-Mesh** idle execution model (`invoke_subagent`, yielding the turn immediately after fan-out, and receiving reactive notifications on wakeup) and adds production-grade swarm engineering controls for large-scale code transformations.


## Leading Vocabulary

* **Conductor**: The lead orchestrator thread responsible for planning, workspace partitioning, and convergence. Maintains an idle state during fan-out execution.
* **Mesh**: The active swarm of concurrent worker agents executing parallel file conversions in isolated environments.
* **Swarm-Fence**: Git worktree or directory isolation bounds assigned per worker agent to eliminate merge locks.
* **Oracle**: The language-agnostic test suite or specification acting as the invariant ground-truth referee.
* **Red-Team**: Adversarial auditor subagents assigned to inspect generated code for unsafe bypasses, memory hazards, or silent regressions.
* **Legwork**: Exhaustive upfront dependency tree parsing, AST mapping, and rule specification before spawning workers.

---

## Workflow

### Phase 1: Reconnaissance & Rule Scaffolding (Legwork)
1. Scan the source codebase to construct a complete **file dependency graph**.
2. Identify independent, non-overlapping modules that can be migrated concurrently.
3. Draft the migration rulebook (`PORTING.md` and type/lifetime mapping tables) to enforce structural invariants across all worker agents.
4. **Completion Criterion**: `PORTING.md` is committed/staged, and a JSON/TSV dependency tree mapping every file to an isolated tier is created.

### Phase 2: Worktree Provisioning (Swarm-Fence)
1. Partition the workspace into $N$ isolated Git worktrees (`git worktree add`).
2. Assign exactly one module/file tier to each worktree path.
3. For details on worktree allocation and clean teardown, consult [`WORKTREE_SCHEME.md`](references/WORKTREE_SCHEME.md).
4. **Completion Criterion**: All $N$ worktree paths exist on disk, verified isolated, with zero uncommitted state in main.

### Phase 3: Fan-Out & Self-Healing Execution
1. Spawn worker agents in parallel via `invoke_subagent` across the active worktree paths.
2. Direct worker agents to compile code locally (`cargo check`, `tsc`, `clang`) after translation.
3. If compilation fails, pipe the raw compiler output directly back into the worker agent context window for iterative correction.
4. For rules on context feed-back loops and retry caps, consult [`COMPILER_FEEDBACK_LOOP.md`](references/COMPILER_FEEDBACK_LOOP.md).
5. **Completion Criterion**: All worker agents complete execution, achieving a 100% clean compilation pass across all worktrees.

### Phase 4: Adversarial Audit (Red-Team)
1. Spawn dedicated auditor subagents to review generated code in each worktree.
2. The auditor subagents scan specifically for:
   - Unjustified `unsafe` blocks or raw pointer alias hazards.
   - Heavy wrapper allocations (e.g. overusing `Arc<Mutex<T>>`).
   - Silent panic paths or ignored error returns.
3. For auditing checklists and automated remediation triggers, consult [`ADVERSARIAL_AUDITING.md`](references/ADVERSARIAL_AUDITING.md).
4. **Completion Criterion**: Red-Team auditors approve all worktree outputs with zero high/critical security or safety flags.

### Phase 5: Merging & Oracle Convergence
1. Merge approved worktrees sequentially into the primary integration branch.
2. Execute the full project test suite (**Oracle**).
3. If regressions occur, isolate the offending module and re-dispatch a targeted worker agent with the failing test output.
4. **Completion Criterion**: All worktrees are merged, worktree folders are removed (`git worktree remove`), and 100% of Oracle test suite assertions pass.

---

## Progressive Disclosure References

* [Worktree Provisioning & Isolation](references/WORKTREE_SCHEME.md)
* [Compiler Diagnostic Feedback Loops](references/COMPILER_FEEDBACK_LOOP.md)
* [Adversarial Red-Team Auditing](references/ADVERSARIAL_AUDITING.md)
