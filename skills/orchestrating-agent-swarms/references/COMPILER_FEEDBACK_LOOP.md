# Compiler Diagnostic Feedback Loop (Self-Healing)

This reference defines how compiler diagnostics are automatically fed back to worker agents to achieve rapid self-healing code generation.

## 1. Feedback Loop Architecture

```
+------------------+         +------------------+         +------------------+
|  Worker Agent    | ------> | Compile Command  | ------> | Pass / Fail Gate |
|  emits code      |         | (cargo / tsc)    |         |                  |
+------------------+         +------------------+         +------------------+
         ^                                                         |
         |                   Raw Compiler Diagnostics              |
         +---------------------------------------------------------+
```

## 2. Compiler Execution Protocol

After writing or modifying code in its worktree, the worker agent executes local compilation:

```bash
# For Rust targets:
cargo check --message-format=short 2>&1 | head -n 40

# For C/C++ targets:
make check 2>&1 | head -n 40

# For TypeScript targets:
npx tsc --noEmit 2>&1 | head -n 40
```

## 3. Context Injection Format

When compilation fails, the worker agent receives an immediate high-priority diagnostic payload:

```markdown
[COMPILER ERROR FEEDBACK - Iteration {N}/5]
Target File: src/http/parser.rs
Command Output:
error[E0382]: use of moved value: `buffer`
  --> src/http/parser.rs:42:18
   |
38 |     let req = parse_raw(buffer);
   |                         ------ value moved here
42 |     println!("{:?}", buffer);
   |                      ^^^^^^ value used here after move

INSTRUCTION: Fix ownership/borrowing error without using `unsafe` blocks or unnecessary heap clones (`Arc`/`Mutex`) unless specified in PORTING.md.
```

## 4. Retry Discipline & Termination Criteria

1. **Max Retry Cap**: Maximum 5 feedback loop iterations per file/module.
2. **Escalation Trigger**: If a module fails 5 consecutive compilation attempts, the worker agent flags the issue to the **Conductor** with the blocking diagnostic log and stops.
3. **No-Bypass Rule**: Agents are strictly forbidden from disabling compiler checks (e.g. `#![allow(warnings)]`, `// @ts-ignore`, or wrapping failing blocks in `unsafe`) to pass compilation.
