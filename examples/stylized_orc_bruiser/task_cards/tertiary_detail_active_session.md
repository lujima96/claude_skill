# Tertiary Detail Active Session Task Card

- `schema_version`: 0.3

## Metadata

- `task_id`: stylized_orc_bruiser-tertiary-detail-session-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: tertiary_detail
- `stage_name`: Tertiary detail
- `created_by`: Character Director
- `created_at`: 2026-07-22
- `status`: approved

## Goal

- `goal`: Continue restrained silhouette-supporting tertiary refinement without changing approved secondary proportions or facial placement.
- `current_stage`: tertiary_detail
- `previous_stage`: secondary_anatomy
- `next_stage`: clothing_hardsurface_hair

## Constraints

- `allowed_tools`: Blender MCP; protected deterministic session scripts; viewport screenshot
- `disallowed_tools`: addition; deletion; rename; merge; remesh; topology or material changes; transform application; rigging; export; stage progression
- `known_constraints`: preserve approved proportions, stance, facial hierarchy, object placement, topology counts, materials, and retirement collection
- `style_constraints`: heroic stylized orc forms; broad readable features; no thin elf-like ears or noisy detail
- `technical_constraints`: at most six exact runtime targets; safe absolute operations only; save only after clean deterministic delta
- `godot_constraints`: no export or engine-facing changes during tertiary detail

## Inputs

- `input_refs`: approved tertiary brow and tusk evidence; pending ear refinement; heroic stylized style family
- `input_artifacts`: source/tertiary_detail/ear_silhouette/working/stylized_orc_bruiser.tertiary-detail-ear-silhouette-refinement-001.working.blend
- `input_reports`: task_cards/tertiary_detail_ear_silhouette_refinement.md
- `previous_handoff`: handoffs/secondary_anatomy_to_tertiary_detail.md
- `assumptions`: the existing ear pass is the latest accepted tertiary working artifact

## Output Contract

- `required_outputs`: protected active-session working file; validated JSONL journal; one viewport preview per accepted edit
- `output_paths`: source/mcp_sessions/tertiary-detail-session-001/working/stylized_orc_bruiser.tertiary-detail-session-001.working.blend
- `report_paths`: mcp_sessions/tertiary-detail-session-001.jsonl
- `screenshot_requirements`: one relevant-angle viewport preview; one 512px Eevee fallback only if viewport capture is unavailable
- `handoff_format`: templates/stage_handoff.md

## Acceptance Tests

- `acceptance_tests`: each edit changes only its exact runtime targets and authorized fields; topology, materials, collections, non-targets, source, and backup remain unchanged; requested absolute values are realized
- `required_validators`: validate_stage_task_card; validate_mcp_session
- `manual_review_required`: yes
- `hard_failure_checks`: source or protection mismatch; wrong or dirty file; unexpected drift; topology or material change; missing preview; silhouette or facial readability regression

## Stop Conditions

- `stop_conditions`: stop on scope expansion, structural work, uncertainty, drift, evidence failure, tool error, or stage transition
- `requires_human_approval`: yes
- `rollback_required_if`: any accepted feature regresses or any non-target state changes
- `do_not_continue_if`: task card, preflight, protection, filepath, hash, target authorization, delta, or preview validation fails

## Execution Notes

- `assigned_specialist`: Blender MCP Operator; Anatomy Reviewer and Style Keeper at checkpoint
- `microtasks`: related safe tertiary-detail refinements within this stage envelope
- `mcp_microtask_id`: none; exact targets are recorded per runtime iteration
- `evidence_tier`: legacy evidence tier not used
- `iteration_budget`: not count-gated
- `iteration_views`: one relevant angle per edit
- `target_objects`: exact targets recorded in the session journal
- `allowed_change_types`: exact normalized operations recorded in the session journal
- `execution_authorized_by`: repository user
- `execution_authorized_at`: 2026-07-22
- `risks`: over-refinement could weaken the approved graphic silhouette
- `questions_for_director`: none

## Active Edit Session (Schema 0.3)

- `workflow_mode`: active_session
- `session_id`: tertiary-detail-session-001
- `authorized_collections`: ORC_BLOCKOUT
- `safe_change_types`: absolute_transform; visibility; collection_membership; vertex_positions
- `max_targets_per_edit`: 6
- `viewport_preview_policy`: one relevant-angle get_viewport_screenshot; fallback one 512px Eevee render
- `checkpoint_triggers`: explicit checkpoint; stage transition; scope expansion; structural or destructive work; uncertainty; drift; evidence failure
- `pipeline_state`: pipeline_state.json
- `session_journal`: mcp_sessions/tertiary-detail-session-001.jsonl
- `source_file`: source/tertiary_detail/ear_silhouette/working/stylized_orc_bruiser.tertiary-detail-ear-silhouette-refinement-001.working.blend
- `backup_file`: source/mcp_sessions/tertiary-detail-session-001/backups/stylized_orc_bruiser.tertiary-detail-session-001.before.blend
- `working_file`: source/mcp_sessions/tertiary-detail-session-001/working/stylized_orc_bruiser.tertiary-detail-session-001.working.blend
- `source_protection_receipt`: source/mcp_sessions/tertiary-detail-session-001/protection.json
- `preflight_cache_key`: mcp__blender; Blender 5.2.0 LTS; execute_blender_code; get_viewport_screenshot; working filepath and SHA-256

## Completion

- `completed_outputs`: protected active session; one accepted paired-ear iteration; preview evidence; five-view checkpoint; bundled Blender reports; validation, specialist review, QA audit, and action log
- `validation_summary`: warning only for 67 construction scales and the stage-expected absence of an armature; no failures or hard failures
- `review_summary`: anatomy and style approve with notes; QA recommends clothing_hardsurface_hair
- `blocking_issues`: none
- `approved_by`: repository user
- `approved_at`: 2026-07-22
