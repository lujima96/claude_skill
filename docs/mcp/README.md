# MCP Operating Docs

This folder defines the bounded Blender MCP operating loop introduced in Phase 9.

## Documents

| Document | Purpose |
|---|---|
| `blender_mcp_usage_policy.md` | Rules for safe, bounded Blender MCP editing. |
| `action_log_format.md` | Field contract and review expectations for MCP action logs. |

## Rule

Blender MCP may make only one bounded microtask change per loop. Every loop must create or reference an action log, screenshots, validator output, specialist review, QA decision, and human approval state.
