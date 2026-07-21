# Tertiary Detail Ear Silhouette Refinement Task Card

## Metadata

- `task_id`: stylized_orc_bruiser-tertiary-detail-ear-silhouette-refinement-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: tertiary_detail
- `stage_name`: Tertiary detail
- `created_by`: Character Director
- `created_at`: 2026-07-21
- `status`: in_progress

## Goal

- `goal`: Refine the paired simple ear spikes into tapered stylized orc ears with clearer outward points and restrained backward sweep while preserving their approved seating and head placement.
- `current_stage`: tertiary_detail
- `previous_stage`: tertiary_detail
- `next_stage`: tertiary_detail

## Constraints

- `allowed_tools`: protected working copy; read-only Blender MCP vertex inspection; topology-preserving Blender MCP vertex-position edit; quick facial screenshots; scene-delta and log validators
- `disallowed_tools`: object transforms; addition; deletion; rename; merge; remesh; topology-count change; transform application; materials; changes outside ORC_ear_L/R; changes to head, eyes, brows, nose, mouth, tusks, body, or gear; rigging; export
- `known_constraints`: each ear is a low-resolution 20-vertex mesh with approved object placement beside the head
- `style_constraints`: retain broad heroic-orc ear roots and readable outward points; avoid thin elf ears or extreme length
- `technical_constraints`: preserve seated head-side base vertices, object matrices, topology counts, materials, and collections; change existing local coordinates only
- `godot_constraints`: no export or engine-facing change

## Inputs

- `input_refs`: approved brow gate; approved facial mechanics; heroic stylized style family
- `input_artifacts`: `examples/stylized_orc_bruiser/source/tertiary_detail/brow_wedge/working/stylized_orc_bruiser.tertiary-detail-brow-wedge-refinement-001.working.blend`
- `input_reports`: brow gate review and secondary facial review
- `previous_handoff`: `examples/stylized_orc_bruiser/handoffs/secondary_anatomy_to_tertiary_detail.md`
- `assumptions`: a small tip-ring refinement can improve the ear silhouette without changing approved head placement

## Output Contract

- `required_outputs`: protected backup and working `.blend`; quick receipt; front and three-quarter facial screenshots; compact MCP action log
- `output_paths`: `examples/stylized_orc_bruiser/source/tertiary_detail/ear_silhouette/working/stylized_orc_bruiser.tertiary-detail-ear-silhouette-refinement-001.working.blend`
- `report_paths`: `examples/stylized_orc_bruiser/reports/blender/tertiary_detail_ear_silhouette_refinement/quick_iteration_001/`
- `screenshot_requirements`: front; three_quarter facial composition at 512 pixels or greater
- `handoff_format`: `templates/stage_handoff.md`

## Acceptance Tests

- `acceptance_tests`: only ORC_ear_L/R coordinates change; head-side bases and object transforms remain fixed; both ears gain mirrored tapered outward points with subtle backward sweep; no head gaps appear; topology, materials, all other objects, source, and backup remain unchanged
- `required_validators`: validate_stage_task_card; validate_mcp_iteration_receipt; validate_mcp_action_log
- `manual_review_required`: no
- `hard_failure_checks`: detached base; elf-like length; broken symmetry; topology or material change; unexpected drift; source or evidence failure

## Stop Conditions

- `stop_conditions`: stop on protection mismatch, unsupported vertex layout, base detachment, excessive point length, non-target change, topology drift, or failed evidence
- `requires_human_approval`: yes
- `rollback_required_if`: ear readability regresses or any non-target state changes
- `do_not_continue_if`: task, capability, isolation, protection, filepath, vertex layout, or delta preflight fails

## Execution Notes

- `assigned_specialist`: Anatomy Reviewer and Style Keeper with Blender MCP Operator
- `microtasks`: Refine only the paired ear tip geometry while leaving seated bases and object placement unchanged
- `mcp_microtask_id`: tertiary-detail-ear-silhouette-refinement-001
- `evidence_tier`: quick_iteration
- `iteration_budget`: 3
- `iteration_views`: front; three_quarter
- `target_objects`: ORC_ear_L; ORC_ear_R
- `allowed_change_types`: vertex_positions
- `execution_authorized_by`: repository user
- `execution_authorized_at`: 2026-07-21
- `risks`: low vertex density could produce an angular tip or reveal a gap at the head
- `questions_for_director`: none

## Completion

- `completed_outputs`: protected backup and working `.blend`; quick facial screenshots; passing paired-ear delta receipt; compact action log
- `validation_summary`: only ORC_ear_L/R tip-ring coordinates changed; both base rings, object transforms, topology, materials, 73 protected objects, source, and backup remain unchanged
- `review_summary`: quick views show clearer outward heroic-orc points with broad seated roots and restrained backward sweep; gate review pending
- `blocking_issues`: none; retain for user review or a second subtle ear refinement
- `approved_by`: none
- `approved_at`: none
