# Tertiary Detail Brow Wedge Refinement Task Card

## Metadata

- `task_id`: stylized_orc_bruiser-tertiary-detail-brow-wedge-refinement-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: tertiary_detail
- `stage_name`: Tertiary detail
- `created_by`: Character Director
- `created_at`: 2026-07-21
- `status`: approved

## Goal

- `goal`: Refine the paired rectangular brow slabs into tapered stylized wedges while preserving their approved spacing, stern angle, and eye clearance.
- `current_stage`: tertiary_detail
- `previous_stage`: tertiary_detail
- `next_stage`: tertiary_detail

## Constraints

- `allowed_tools`: protected working copy; read-only Blender MCP vertex inspection; topology-preserving Blender MCP vertex-position edit; quick facial screenshots; scene-delta and log validators
- `disallowed_tools`: object transforms; addition; deletion; rename; merge; remesh; topology-count change; transform application; materials; changes outside ORC_brow_L/R; changes to eyes, head, nose, cheeks, mouth, tusks, ears, body, or gear; rigging; export
- `known_constraints`: brow centers, separation, rotations, and hair material were approved after the earlier intersection fix; each brow is an eight-vertex cuboid
- `style_constraints`: retain a heavy stern orc brow without returning to center overlap or hiding the eyes
- `technical_constraints`: preserve object matrices, topology counts, materials, and collections; change existing local coordinates only
- `godot_constraints`: no export or engine-facing change

## Inputs

- `input_refs`: approved facial mechanics and tusk gate; heroic stylized style family
- `input_artifacts`: `examples/stylized_orc_bruiser/source/tertiary_detail/tusk_silhouette/working/stylized_orc_bruiser.tertiary-detail-tusk-silhouette-001.working.blend`
- `input_reports`: tusk gate review and secondary facial review
- `previous_handoff`: `examples/stylized_orc_bruiser/handoffs/secondary_anatomy_to_tertiary_detail.md`
- `assumptions`: tapering outer and lower brow corners can reduce the block shape without altering expression or placement

## Output Contract

- `required_outputs`: protected backup and working `.blend`; quick receipt; front and three-quarter facial screenshots; compact MCP action log
- `output_paths`: `examples/stylized_orc_bruiser/source/tertiary_detail/brow_wedge/working/stylized_orc_bruiser.tertiary-detail-brow-wedge-refinement-001.working.blend`
- `report_paths`: `examples/stylized_orc_bruiser/reports/blender/tertiary_detail_brow_wedge_refinement/quick_iteration_001/`
- `screenshot_requirements`: front; three_quarter facial composition at 512 pixels or greater
- `handoff_format`: `templates/stage_handoff.md`

## Acceptance Tests

- `acceptance_tests`: only ORC_brow_L/R coordinates change; centers, transforms, materials, and approved separation remain fixed; both brows become mirrored tapered wedges; eyes remain visible; no center intersection returns; topology, all other objects, source, and backup remain unchanged
- `required_validators`: validate_stage_task_card; validate_mcp_iteration_receipt; validate_mcp_action_log
- `manual_review_required`: no
- `hard_failure_checks`: center overlap; eye occlusion; broken symmetry; topology or material change; unexpected drift; source or evidence failure

## Stop Conditions

- `stop_conditions`: stop on protection mismatch, unsupported vertex layout, eye coverage, brow detachment, non-target change, topology drift, or failed evidence
- `requires_human_approval`: yes
- `rollback_required_if`: brow readability regresses or any non-target state changes
- `do_not_continue_if`: task, capability, isolation, protection, filepath, vertex layout, or delta preflight fails

## Execution Notes

- `assigned_specialist`: Anatomy Reviewer and Style Keeper with Blender MCP Operator
- `microtasks`: Taper only the paired brow mesh corners into mirrored wedges without moving either brow object
- `mcp_microtask_id`: tertiary-detail-brow-wedge-refinement-001
- `evidence_tier`: quick_iteration
- `iteration_budget`: 3
- `iteration_views`: front; three_quarter
- `target_objects`: ORC_brow_L; ORC_brow_R
- `allowed_change_types`: vertex_positions
- `execution_authorized_by`: repository user
- `execution_authorized_at`: 2026-07-21
- `risks`: over-tapering could weaken the stern expression or expose an unintended gap
- `questions_for_director`: none

## Completion

- `completed_outputs`: protected backup and working `.blend`; quick facial screenshots; passing paired-brow delta receipt; compact action log
- `validation_summary`: only ORC_brow_L/R outer-end coordinates changed; inner ends, object transforms, topology, materials, 73 protected objects, source, and backup remain unchanged
- `review_summary`: Gate review approves the paired wedge taper; center separation, eye visibility, stern expression, and facial hierarchy remain intact.
- `blocking_issues`: none inside this bounded brow task
- `approved_by`: repository user
- `approved_at`: 2026-07-21
