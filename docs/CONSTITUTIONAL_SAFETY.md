# Constitutional Safety Rules (Immutable)

These rules are hardcoded at the agent system level and cannot be overridden by runtime prompts or state mutations.

1. **No External Exfiltration**: Default offline mode forbids network transmission of private state without explicit, audited user override.
2. **Privilege Minimization**: All host actions execute under least-privilege sandbox.
3. **Telemetry Blinding**: Background telemetry processes are isolated or neutralized before sensitive operations.
4. **State Integrity**: No mutation may be applied without prior Merkle commitment path.
5. **Deterministic Physics**: All spatial/physical changes must satisfy CFT + AC-3 constraints; non-deterministic or unbounded edits are rejected.
6. **Human Override Precedence**: Explicit user abort signals take absolute priority over autonomous loops.

Violations result in immediate halt and audit log generation.
