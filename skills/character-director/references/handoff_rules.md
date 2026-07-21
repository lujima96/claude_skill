# Handoff Rules

Use these rules whenever creating, checking, or approving stage task cards and handoffs.

## Required Files

Each asset should eventually maintain:

- Character brief.
- Asset manifest.
- One task card per attempted stage.
- One handoff per completed stage.
- Review reports for specialist reviews.
- Validation reports for deterministic checks.
- QA audit report for progression decisions.

## Task Card Rules

- A task card must be created before stage work starts.
- A task card must name exactly one `current_stage`.
- Allowed tools must match the stage.
- Output contract must list expected artifacts and report paths.
- Acceptance tests must include hard-failure checks.
- Stop conditions must be explicit.
- Human approval must be required for progression.

## Handoff Rules

- A handoff must summarize completed work and changed artifacts.
- A handoff must list required artifacts and report paths.
- A handoff must identify validators run and whether hard failures exist.
- A handoff must include review and QA state.
- A handoff must name the next stage and its required inputs.
- A handoff cannot be approved if required artifacts are missing.

## Approval Rules

- Approval must name the approver and date.
- Approval cannot be inferred from silence.
- Approval can allow non-blocking deferred work only if the risk is recorded.
- Approval cannot override hard failures.

## Missing Information

When required information is unknown:

1. Record it under `open_questions` or `blocking_issues`.
2. Decide whether it blocks the current stage or only a later stage.
3. If it blocks approval, mark the artifact `draft` or `blocked`.
4. Do not invent production budgets, target versions, or platform constraints.
