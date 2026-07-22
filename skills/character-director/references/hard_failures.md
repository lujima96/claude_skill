# Director Hard-Failure Rules

The full hard-failure list lives in `docs/pipeline/hard_failures.md`. This reference contains the Director-level rules that decide whether work may progress.

## Always Block

Block progression when any of these are true:

- Required character brief is missing.
- Current stage authorization envelope is missing. A validated schema-0.3 active-session task card plus exact runtime target receipt satisfies this requirement; legacy task cards remain valid.
- Current stage handoff is missing.
- Human approval is required and absent.
- Required artifact path is missing or unresolved.
- A validation report has `hard_failures_present: yes`.
- A review report has `blocked_stage_progression: yes`.
- QA audit decision is `block_progression`.
- The requested next step skips retopology, rigging, deformation testing, or Godot validation.
- The request asks for broad free-running edits instead of a bounded stage task.

## Usually Block

Block unless the Character Director records a specific exception:

- Target Godot version is unknown after export work begins.
- Target platform is unknown after optimization begins.
- Camera context is unknown after blockout begins.
- Facial animation requirements are unknown before topology begins.
- Blend-shape requirements are unknown before rigging begins.
- LOD or Godot scene-variant requirements are unknown before optimization begins.

## Do Not Block By Itself

These issues do not automatically block progression unless they become hard failures:

- Low confidence in a specialist review.
- Minor naming inconsistencies before export.
- Missing optional reference types.
- Non-critical style notes.
- Deferred material polish before UV approval.

## Revision Rule

If a hard failure belongs to an earlier stage, create a revision task card for that earlier stage. Do not patch it silently inside the current stage.
