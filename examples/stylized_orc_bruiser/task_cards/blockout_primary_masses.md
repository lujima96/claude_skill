# Stylized Orc Bruiser Primary-Mass Blockout Task Card

## Metadata

- `task_id`: stylized_orc_bruiser-blockout-primary-masses-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: blockout
- `stage_name`: Blockout
- `created_by`: Character Director
- `created_at`: 2026-07-21
- `status`: approved

## Goal

- `goal`: Create one reviewable, low-detail orc blockout from named Blender primitives that proves the approved heroic silhouette and major anatomical masses.
- `current_stage`: blockout
- `previous_stage`: anatomy_blockout_planning
- `next_stage`: primary_forms

## Constraints

- `allowed_tools`: Blender MCP `get_scene_info`; narrowly scoped Blender MCP Python for collection, primitive, material, camera, light, and working-file creation; screenshot capture; read-only Blender reports
- `disallowed_tools`: generated-model services; deletion of existing objects; sculpting; remesh; boolean; mesh merge; transform application; retopology; UVs; baking; rigging; animation; export; source-file overwrite
- `known_constraints`: work only in the protected working copy; preserve the source scene; use simple separable primitives; third-person gameplay readability takes priority over detail
- `style_constraints`: broad shoulder-to-waist taper; thick neck; heavy jaw and brow; readable tusks; large hands and forearms; compact stance; large simple primary masses
- `technical_constraints`: target height approximately 2.15 m; bilateral masses remain separately named; deformation landmarks must remain visible; all generated objects live in `ORC_BLOCKOUT`
- `godot_constraints`: no Godot work is authorized; forms should remain suitable for later retopology and a GLB path

## Inputs

- `input_refs`: `examples/stylized_orc_bruiser/reference_boards/approved_initial_board.md`; `examples/stylized_orc_bruiser/reviews/style_keeper.md`; `examples/stylized_orc_bruiser/reviews/anatomy_review.md`
- `input_artifacts`: `examples/stylized_orc_bruiser/brief.md`
- `input_reports`: `examples/stylized_orc_bruiser/audit.md`
- `previous_handoff`: `examples/stylized_orc_bruiser/handoffs/anatomy_to_manual_blockout.md`
- `assumptions`: this is an intentionally simple primary-mass proof, not an approved sculpt or production mesh

## Output Contract

- `required_outputs`: protected source, backup, and working `.blend` files; named primitive blockout; MCP action log; front, side, back, three-quarter, and gameplay-distance screenshots; scene, mesh, material, and naming reports
- `output_paths`: `examples/stylized_orc_bruiser/source/working/stylized_orc_bruiser.blockout-primary-masses-001.working.blend`
- `report_paths`: `examples/stylized_orc_bruiser/reports/blender/blockout_primary_masses/`
- `screenshot_requirements`: front; side; back; three_quarter; gameplay_distance, all targeting `ORC_BLOCKOUT`
- `handoff_format`: `templates/stage_handoff.md`

## Acceptance Tests

- `acceptance_tests`: blockout reads as a broad muscular orc in all five required views; head, ribcage, pelvis, shoulders, upper arms, forearms, hands, thighs, shins, feet, jaw, brow, and tusks are separately named and visible; source hash remains unchanged; evidence validators pass
- `required_validators`: validate_stage_task_card; validate_blender_report; validate_screenshot_manifest; validate_mcp_action_log
- `manual_review_required`: yes
- `hard_failure_checks`: missing protected working copy; source hash change; scope drift; missing required mass; unreadable gameplay silhouette; hidden shoulder, elbow, hip, or knee landmarks; missing evidence

## Stop Conditions

- `stop_conditions`: stop if the source cannot be protected, Blender Python exceeds the named creation scope, any existing object would be deleted or changed, the working file cannot be saved, or required evidence cannot be captured
- `requires_human_approval`: yes
- `rollback_required_if`: any existing scene object changes or the result exceeds primitive blockout scope
- `do_not_continue_if`: capability or isolation preflight fails, source/backup/working paths are not distinct, or arbitrary Blender Python is not explicitly approved at execution

## Execution Notes

- `assigned_specialist`: Blender MCP Operator with Anatomy Reviewer and Style Keeper review
- `microtasks`: Create the named low-detail orc primary-mass primitive set in collection `ORC_BLOCKOUT` and save only the protected working copy
- `mcp_microtask_id`: blockout-primary-masses-001
- `target_objects`: new collection `ORC_BLOCKOUT`; new objects prefixed `ORC_`; new materials prefixed `MAT_ORC_`; review camera and lights prefixed `ORC_REVIEW_`
- `allowed_change_types`: create and name collections, primitives, materials, camera, and lights; set transforms and display properties only on new objects; save protected source initialization and working copy
- `execution_authorized_by`: repository user request
- `execution_authorized_at`: 2026-07-21
- `risks`: primitive intersections are expected; facial animation requirements and production budgets remain unknown; arbitrary Python is powerful and must remain limited to this exact object list
- `questions_for_director`: none for this blockout pass

## Completion

- `completed_outputs`: protected source, backup, and working `.blend`; 44-object `ORC_BLOCKOUT` collection; five-view screenshot set; scene, mesh, material, naming, and screenshot reports; anatomy and style reviews; QA audit
- `validation_summary`: all required task-card, Blender-report, screenshot-manifest, specialist-review, and QA-audit validators pass; no blockout hard failures
- `review_summary`: Anatomy Reviewer and Style Keeper both return `approve_with_notes`; QA recommends `approve_next_stage`
- `blocking_issues`: none for primary-forms entry; downstream production requirements remain open
- `approved_by`: repository user
- `approved_at`: 2026-07-21
