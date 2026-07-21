# Verification Gates Protocol

The Iron Law: **NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE.**

## Verification Gate Workflow
1.  **IDENTIFY** the correct validation command (e.g., maven test, formatting check).
2.  **RUN** the full command.
3.  **READ** the complete output.
4.  **VERIFY** that the output confirms your claim.
5.  **CLAIM** success only after verification is confirmed.

Skipping any step is considered a failure to verify.

## Verification Requirements
*   **Tests Pass**: Test execution output shows 0 failures.
*   **Build Succeeds**: Compilation and build tools exit with code 0.
*   **Bug Fixed**: The original reproducing test/script passes.
*   **Requirements Met**: A line-by-line checklist of user requirements is verified.

## Red Flags (STOP)
Do not use phrases like "should", "probably", "seems to", or express satisfaction before verification is complete. Do not commit code or trust summary reports without running fresh verification checks.
