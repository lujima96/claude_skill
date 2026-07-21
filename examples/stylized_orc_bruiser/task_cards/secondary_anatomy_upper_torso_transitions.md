# Secondary Anatomy Upper-Torso Transitions Task Card

## Metadata

- `task_id`: stylized_orc_bruiser-secondary-anatomy-upper-torso-transitions-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: secondary_anatomy
- `stage_name`: Secondary anatomy
- `created_by`: Character Director
- `created_at`: 2026-07-21
- `status`: approved

## Goal

- `goal`: Establish the clavicle, pectoral, and lateral ribcage transition planes that connect the approved neck, ribcage, and shoulder masses without changing the heroic silhouette.
- `current_stage`: secondary_anatomy
- `previous_stage`: primary_forms
- `next_stage`: secondary_anatomy

## Constraints

- `allowed_tools`: protected working-copy script; read-only Blender MCP inspection; one scoped Blender MCP creation burst for six named secondary-form primitives; screenshot and report scripts
- `disallowed_tools`: deletion; changes to approved primary objects or gear; facial work; lower-body work; merge; remesh; topology; UVs; rigging; tertiary detail; export
- `known_constraints`: the left pauldron is user-adjusted and must remain unchanged; shoulder raise clearance remains a future test
- `style_constraints`: broad bruiser chest, thick supported neck, simplified confident planes, no striations or surface detail
- `technical_constraints`: new forms must remain reversible and subordinate to the approved ribcage, shoulder, neck, and arm masses
- `godot_constraints`: no engine work; preserve clear shoulder and armpit deformation lanes

## Inputs

- `input_refs`: stylized biped proportions; deformation landmarks; heroic stylized style family; primary-forms anatomy reviews
- `input_artifacts`: `examples/stylized_orc_bruiser/source/primary_forms/extremities/revisions/working/stylized_orc_bruiser.primary-forms-footwear-readability-revision-001.working.blend`
- `input_reports`: final primary-forms validation, anatomy review, QA audit, and approved handoff
- `previous_handoff`: `examples/stylized_orc_bruiser/handoffs/primary_forms_to_secondary_anatomy.md`
- `assumptions`: paired clavicle, pectoral, and lat transition masses are the smallest safe opening secondary-anatomy task

## Output Contract

- `required_outputs`: protected backup and secondary-anatomy working `.blend`; paired clavicle, pectoral, and lat transition primitives; five-view screenshots; Blender reports; validation, anatomy review, QA audit, and action log
- `output_paths`: `examples/stylized_orc_bruiser/source/secondary_anatomy/upper_torso/working/stylized_orc_bruiser.secondary-anatomy-upper-torso-transitions-001.working.blend`
- `report_paths`: `examples/stylized_orc_bruiser/reports/blender/secondary_anatomy_upper_torso_transitions/`
- `screenshot_requirements`: front; side; back; three_quarter; gameplay_distance targeting `ORC_BLOCKOUT`
- `handoff_format`: `templates/stage_handoff.md`

## Acceptance Tests

- `acceptance_tests`: paired clavicles establish shoulder-girdle slope; paired pectorals support the broad chest without covering the sternum lane; paired lat masses connect ribcage toward upper arms without closing the armpit; neck and shoulder attachments read more coherently; approved silhouette, gear, stance, face, and extremities remain unchanged; source hash and evidence validate
- `required_validators`: validate_stage_task_card; validate_blender_report; validate_screenshot_manifest; validate_mcp_action_log; validate_review_report; validate_qa_audit
- `manual_review_required`: yes
- `hard_failure_checks`: missing transition landmarks; closed armpit; pauldron drift; silhouette regression; protected-object change; source or evidence failure

## Stop Conditions

- `stop_conditions`: stop on protection failure, missing target collection/material, overlap that obscures the sternum or armpit, protected-object drift, or evidence failure
- `requires_human_approval`: yes
- `rollback_required_if`: any pre-existing object changes
- `do_not_continue_if`: task, capability, isolation, protection, or target inspection fails

## Execution Notes

- `assigned_specialist`: Anatomy Reviewer with Blender MCP Operator
- `microtasks`: Create only paired ORC_clavicle, ORC_pectoral, and ORC_lat secondary-form primitives
- `mcp_microtask_id`: secondary-anatomy-upper-torso-transitions-001
- `target_objects`: new ORC_clavicle_L/R; new ORC_pectoral_L/R; new ORC_lat_L/R; inspect-only ORC_neck, ORC_ribcage, ORC_shoulder_L/R, ORC_upperarm_L/R, ORC_trapezius_L/R, ORC_shoulder_pad_L
- `allowed_change_types`: inspect named existing objects; create, name, position, scale, rotate, and assign existing skin blockout material to six specified new primitives; save only protected secondary-anatomy working copy
- `execution_authorized_by`: repository user
- `execution_authorized_at`: 2026-07-21
- `risks`: excessive chest layering; closed armpits; clavicles becoming decorative bars; lat masses widening the silhouette
- `questions_for_director`: none

## Completion

- `completed_outputs`: protected backup and secondary-anatomy working `.blend`; six paired upper-torso transition primitives; refined shallow pectoral and lat planes; five-view screenshots; five Blender reports; validation, anatomy review, QA audit, and MCP action log
- `validation_summary`: pass; source and backup hashes match, five reports and screenshot manifest validate, and all 69 approved pre-existing objects remained unchanged
- `review_summary`: Anatomy Reviewer approves this bounded pass with notes; QA keeps the asset in secondary anatomy for remaining joint, lower-body, and facial transitions
- `blocking_issues`: human approval required after this bounded pass
- `approved_by`: repository user
- `approved_at`: 2026-07-21
