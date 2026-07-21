# Tertiary Detail Tusk Silhouette Task Card

## Metadata

- `task_id`: stylized_orc_bruiser-tertiary-detail-tusk-silhouette-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: tertiary_detail
- `stage_name`: Tertiary detail
- `created_by`: Character Director
- `created_at`: 2026-07-21
- `status`: approved

## Goal

- `goal`: Refine the paired tusks from straight blockout cones into a clearer stylized taper and subtle outward flare while preserving their approved placement and facial hierarchy.
- `current_stage`: tertiary_detail
- `previous_stage`: secondary_anatomy
- `next_stage`: tertiary_detail

## Constraints

- `allowed_tools`: protected working-copy script; read-only Blender MCP inspection; topology-preserving vertex-position edit; quick facial screenshots; scene-delta and MCP-log validators
- `disallowed_tools`: object transforms; addition; deletion; rename; merge; remesh; topology-count changes; transform application; material changes; changes outside ORC_tusk_L/R; changes to mouth, cheeks, jaw, eyes, brows, nose, ears, body, or gear; rigging; export
- `known_constraints`: tusk locations and scales were approved at the secondary-anatomy gate; each tusk is a low-resolution 20-vertex tapered mesh
- `style_constraints`: retain blunt heroic-orc tusks with readable paired symmetry and avoid thin realistic fangs
- `technical_constraints`: preserve object matrices, vertex/edge/face counts, materials, and collection membership; edit only existing local vertex coordinates
- `godot_constraints`: no export or engine-facing change in this task

## Inputs

- `input_refs`: approved facial-mechanics gate; secondary-anatomy handoff; heroic stylized style family
- `input_artifacts`: `examples/stylized_orc_bruiser/source/secondary_anatomy/facial_mechanics/working/stylized_orc_bruiser.secondary-anatomy-facial-mechanics-001.working.blend`
- `input_reports`: secondary-anatomy completion audit and facial anatomy review
- `previous_handoff`: `examples/stylized_orc_bruiser/handoffs/secondary_anatomy_to_tertiary_detail.md`
- `assumptions`: a small local-coordinate flare can add character without altering approved facial placement

## Output Contract

- `required_outputs`: protected backup and working `.blend`; quick scene-delta receipt; front and three-quarter facial screenshots; compact MCP action log
- `output_paths`: `examples/stylized_orc_bruiser/source/tertiary_detail/tusk_silhouette/working/stylized_orc_bruiser.tertiary-detail-tusk-silhouette-001.working.blend`
- `report_paths`: `examples/stylized_orc_bruiser/reports/blender/tertiary_detail_tusk_silhouette/quick_iteration_001/`
- `screenshot_requirements`: front; three_quarter facial composition at 512 pixels or greater
- `handoff_format`: `templates/stage_handoff.md`

## Acceptance Tests

- `acceptance_tests`: only ORC_tusk_L/R mesh coordinates change; object transforms and approved placement remain unchanged; both tusks gain a readable taper and subtle outward flare; bases remain seated; symmetry remains controlled; topology counts, materials, collections, all other objects, source, and backup remain unchanged
- `required_validators`: validate_stage_task_card; validate_mcp_iteration_receipt; validate_mcp_action_log
- `manual_review_required`: no
- `hard_failure_checks`: topology-count change; unexpected object drift; detached base; needle-like tusk; broken symmetry; facial readability regression; source or evidence failure

## Stop Conditions

- `stop_conditions`: stop on protection mismatch, non-target change, topology or material drift, base detachment, excessive bend, screenshot failure, or validator failure
- `requires_human_approval`: yes
- `rollback_required_if`: any non-target changes or the tusks read worse than the approved secondary source
- `do_not_continue_if`: task, capability, isolation, protection, filepath, vertex-layout, or scene-delta preflight fails

## Execution Notes

- `assigned_specialist`: Anatomy Reviewer and Style Keeper with Blender MCP Operator
- `microtasks`: Add a restrained paired tusk taper and outward flare by changing only existing tusk vertex coordinates
- `mcp_microtask_id`: tertiary-detail-tusk-silhouette-001
- `evidence_tier`: quick_iteration
- `iteration_budget`: 3
- `iteration_views`: front; three_quarter
- `target_objects`: ORC_tusk_L; ORC_tusk_R
- `allowed_change_types`: vertex_positions
- `execution_authorized_by`: repository user
- `execution_authorized_at`: 2026-07-21
- `risks`: low vertex density could make the curve angular or detach the base silhouette
- `questions_for_director`: none

## Completion

- `completed_outputs`: protected backup and working `.blend`; quick iteration 1 facial screenshots; passing two-object scene-delta receipt; compact MCP action log
- `validation_summary`: only ORC_tusk_L/R vertex coordinates changed; both base rings, 73 non-target objects, object transforms, topology counts, materials, collections, source, and backup remain unchanged
- `review_summary`: Gate review approves the paired sharper flare with seated bases and preserved facial hierarchy.
- `blocking_issues`: none inside this bounded tusk task
- `approved_by`: repository user
- `approved_at`: 2026-07-21
