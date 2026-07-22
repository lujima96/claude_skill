# Clothing, Hard Surface, and Hair Active Session Task Card

- `schema_version`: 0.3

## Metadata

- `task_id`: stylized_orc_bruiser-clothing-hardsurface-hair-session-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: clothing_hardsurface_hair
- `stage_name`: Clothing, hard surface, and hair
- `created_by`: Character Director
- `created_at`: 2026-07-22
- `status`: in_progress

## Goal

- `goal`: Convert the approved tertiary-detail silhouette into a bounded clothing, gear, and hair production pass without disturbing the locked body and facial read.
- `current_stage`: clothing_hardsurface_hair
- `previous_stage`: tertiary_detail
- `next_stage`: retopology

## Constraints

- `allowed_tools`: Blender MCP; protected deterministic session scripts; viewport screenshot
- `disallowed_tools`: addition; deletion; rename; merge; remesh; topology changes; material changes; rigging; export; stage progression
- `known_constraints`: preserve approved body proportions, stance, facial placement, and collection membership; no non-target drift
- `style_constraints`: heroic stylized orc forms; bulky readable costume and gear; no thin elf-like silhouettes
- `technical_constraints`: at most six exact runtime targets; safe absolute operations only; save only after clean deterministic delta; keep changes reversible
- `godot_constraints`: no export or engine-facing changes during clothing, hard-surface, and hair

## Inputs

- `input_refs`: approved tertiary-detail checkpoint; heroic stylized style family; existing clothing and gear blockout references
- `input_artifacts`: `examples/stylized_orc_bruiser/source/mcp_sessions/tertiary-detail-session-001/working/stylized_orc_bruiser.tertiary-detail-session-001.working.blend`
- `input_reports`: `examples/stylized_orc_bruiser/validations/tertiary_detail_session_checkpoint_validation.md`; `examples/stylized_orc_bruiser/reviews/tertiary_detail_session_checkpoint_review.md`; `examples/stylized_orc_bruiser/audit_tertiary_detail_session_checkpoint.md`
- `previous_handoff`: `examples/stylized_orc_bruiser/handoffs/tertiary_detail_to_clothing_hardsurface_hair.md`
- `assumptions`: the blocky loincloth, bracers, shoulder pad, belt, and related gear placeholders are the first safe costume targets

## Output Contract

- `required_outputs`: protected backup and clothing-stage working `.blend`; validated JSONL journal; one viewport preview per accepted edit
- `output_paths`: `examples/stylized_orc_bruiser/source/mcp_sessions/clothing-hardsurface-hair-session-001/working/stylized_orc_bruiser.clothing-hardsurface-hair-session-001.working.blend`
- `report_paths`: `examples/stylized_orc_bruiser/mcp_sessions/clothing-hardsurface-hair-session-001.jsonl`
- `screenshot_requirements`: one relevant-angle viewport preview; one 512px Eevee fallback only if viewport capture is unavailable
- `handoff_format`: `templates/stage_handoff.md`

## Acceptance Tests

- `acceptance_tests`: each accepted edit changes only its exact runtime targets and authorized fields; silhouette and facial placement remain stable; topology, materials, collections, and non-targets remain unchanged; source and backup hashes validate
- `required_validators`: validate_stage_task_card; validate_mcp_session
- `manual_review_required`: yes
- `hard_failure_checks`: wrong or dirty file; unexpected drift; topology or material change; missing preview; source or protection mismatch; collection drift outside the authorized envelope

## Stop Conditions

- `stop_conditions`: stop on scope expansion, structural or destructive work, uncertainty, drift, evidence failure, stage transition, or tool error
- `requires_human_approval`: yes
- `rollback_required_if`: any accepted clothing change regresses the approved silhouette or any non-target state changes
- `do_not_continue_if`: task, capability, protection, filepath, hash, or preview validation fails

## Execution Notes

- `assigned_specialist`: Blender MCP Operator; Style Keeper at checkpoint
- `microtasks`: first bounded clothing pass on the loincloth and nearby gear placeholders before any broader costume refinement
- `mcp_microtask_id`: none
- `evidence_tier`: quick_iteration
- `iteration_budget`: 1-3
- `iteration_views`: front; three_quarter for quick_iteration, or the full required view set for gate_review
- `target_objects`: none unless Blender MCP is allowed
- `allowed_change_types`: none unless Blender MCP is allowed
- `execution_authorized_by`: repository user
- `execution_authorized_at`: 2026-07-22
- `risks`: costume work can obscure the locked silhouette or overgrow the approved body read
- `questions_for_director`: none

## Active Edit Session (Schema 0.3)

- `workflow_mode`: active_session
- `session_id`: clothing-hardsurface-hair-session-001
- `authorized_collections`: ORC_BLOCKOUT
- `safe_change_types`: absolute_transform; visibility; collection_membership; vertex_positions
- `max_targets_per_edit`: 6
- `viewport_preview_policy`: one relevant-angle get_viewport_screenshot; fallback one 512px Eevee render
- `checkpoint_triggers`: explicit checkpoint; stage transition; scope expansion; structural or destructive work; uncertainty; drift; evidence failure
- `pipeline_state`: examples/stylized_orc_bruiser/pipeline_state.json
- `session_journal`: examples/stylized_orc_bruiser/mcp_sessions/clothing-hardsurface-hair-session-001.jsonl
- `source_file`: examples/stylized_orc_bruiser/source/mcp_sessions/tertiary-detail-session-001/working/stylized_orc_bruiser.tertiary-detail-session-001.working.blend
- `backup_file`: examples/stylized_orc_bruiser/source/mcp_sessions/clothing-hardsurface-hair-session-001/backups/stylized_orc_bruiser.clothing-hardsurface-hair-session-001.before.blend
- `working_file`: examples/stylized_orc_bruiser/source/mcp_sessions/clothing-hardsurface-hair-session-001/working/stylized_orc_bruiser.clothing-hardsurface-hair-session-001.working.blend
- `source_protection_receipt`: examples/stylized_orc_bruiser/source/mcp_sessions/clothing-hardsurface-hair-session-001/protection.json
- `preflight_cache_key`: mcp__blender; Blender 5.2.0 LTS; execute_blender_code; get_viewport_screenshot; working filepath and SHA-256

## Completion

- `completed_outputs`: pending
- `validation_summary`: pending
- `review_summary`: pending
- `blocking_issues`: none
- `approved_by`: repository user
- `approved_at`: 2026-07-22
