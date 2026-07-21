# MCP Action Log Format

MCP action logs record what was allowed, what happened, what changed, and how the result was reviewed.

Use `templates/mcp_action_log.md` for every Blender MCP loop.

## Required Evidence

- The task card that bounded the work.
- The source file and backup copy.
- The working file changed by MCP.
- The exact allowed tools or commands.
- A chronological action table.
- Screenshot manifest after structural change.
- Blender reports and document validator output.
- Specialist review.
- QA audit or QA decision.
- Human approval state.

## Blocking Conditions

- Missing backup.
- Missing action rows.
- Missing screenshot manifest after structural change.
- Missing validator output.
- Missing specialist review.
- Destructive operation without explicit approval.
- Final decision says approved while hard failures are present.
- Loop changes more than one microtask.
