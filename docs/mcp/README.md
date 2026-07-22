# MCP Operating Docs

This folder defines legacy bounded loops and persistent stage-scoped Blender MCP edit sessions.

## Documents

| Document | Purpose |
|---|---|
| `blender_mcp_usage_policy.md` | Rules for safe, bounded Blender MCP editing. |
| `action_log_format.md` | Field contract and review expectations for MCP action logs. |
| `session_journal_format.md` | Versioned active-session JSONL records, hash chaining, previews, timings, rollback, and checkpoints. |

## Rule

Routine work stays within one validated stage envelope, uses at most six exact targets per edit, and writes one machine-readable journal record plus one preview. Full action logs, report bundles, specialist review, QA, and human approval occur at checkpoints. Legacy evidence-tier loops remain valid.
