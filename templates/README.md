# Pipeline Templates

These templates are the Phase 1 data contracts for the character pipeline. They are intentionally plain Markdown so they can be filled by humans first and validated by scripts later.

## Templates

| Template | Purpose |
|---|---|
| `character_brief.md` | Converts a raw character idea into production constraints and deliverables. |
| `reference_board.md` | Presents candidate references from local or online discovery for approval before records are finalized. |
| `reference_record.md` | Captures source metadata, classification, usage notes, and approval state for references. |
| `stage_task_card.md` | Defines one bounded stage task with inputs, outputs, acceptance tests, and stop conditions. |
| `stage_handoff.md` | Transfers artifacts and review state from one stage to the next. |
| `review_report.md` | Records specialist review findings and domain-specific decisions. |
| `topology_report.md` | Records mesh topology, deformation-loop, pole, density, and bake-readiness checks. |
| `deformation_report.md` | Records rig, skinning, pose-battery, corrective, and Godot deformation checks. |
| `uv_bake_report.md` | Records UV set, overlap, texel density, padding, bake pairing, and bake artifact checks. |
| `material_texture_report.md` | Records material slot, texture naming, texture size, channel packing, and Godot path checks. |
| `optimization_report.md` | Records LOD, budget, texture memory, package completeness, and export-readiness checks. |
| `mcp_action_log.md` | Records bounded Blender MCP edit scope, source protection, actions, evidence, and approval state. |
| `workflow_completion_report.md` | Records all-stage coverage and final completion or blocking state. |
| `validation_report.md` | Records deterministic validator results, warnings, and hard failures. |
| `qa_audit_report.md` | Aggregates reviews and validation into score, diagnosis, and progression decision. |
| `asset_manifest.md` | Tracks all source, export, Godot, report, and validation artifacts for one asset. |
| `pipeline_state.json` | Points to the current stage, card, active session, working file, checkpoint, handoff, and hard-failure state. |

## Required Contract Docs

- `docs/pipeline/stage_list.md`
- `docs/pipeline/hard_failures.md`
- `docs/pipeline/scoring_rubric.md`

## Usage Rule

Every stage must have a task card before work starts and a handoff before the next stage begins. A hard failure in any review or validation report blocks progression until fixed or converted into a Director-approved revision task.
