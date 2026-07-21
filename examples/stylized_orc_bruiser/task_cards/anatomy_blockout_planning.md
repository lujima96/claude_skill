# Anatomy Blockout Planning Task Card

## Metadata

- `task_id`: stylized_orc_bruiser-anatomy_blockout_planning-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: anatomy_blockout_planning
- `stage_name`: Anatomy blockout planning
- `created_by`: Character Director
- `created_at`: 2026-07-21
- `status`: approved

## Goal

- `goal`: Define the proportion, landmark, and deformation-risk plan that the first manual Blender blockout must follow.
- `current_stage`: anatomy_blockout_planning
- `previous_stage`: style_lock
- `next_stage`: manual_blockout

## Constraints

- `allowed_tools`: approved references, anatomy knowledge notes, style review, anatomy review template
- `disallowed_tools`: final sculpt detail, retopology, rigging, UVs, textures, Godot import
- `known_constraints`: heroic stylized exaggeration must still preserve plausible biped landmarks
- `style_constraints`: exaggerated upper-body mass; readable tusks, jaw, neck, shoulders, forearms, hands
- `technical_constraints`: blockout must be reviewable from front, side, back, three-quarter, and gameplay-distance views
- `godot_constraints`: deformation-critical areas must not be hidden by gear decisions at planning time

## Inputs

- `input_refs`: approved board plus anatomy references `ref-009`, `ref-010`, `ref-011`
- `input_artifacts`: `examples/stylized_orc_bruiser/brief.md`
- `input_reports`: `examples/stylized_orc_bruiser/reviews/reference_librarian.md`; `examples/stylized_orc_bruiser/reviews/style_keeper.md`
- `previous_handoff`: `examples/stylized_orc_bruiser/handoffs/style_to_anatomy.md`
- `assumptions`: no production mesh exists yet; this stage approves a blockout plan only

## Output Contract

- `required_outputs`: anatomy review and blockout instructions for manual Blender work
- `output_paths`: `examples/stylized_orc_bruiser/reviews/anatomy_review.md`
- `report_paths`: `examples/stylized_orc_bruiser/reviews/anatomy_review.md`
- `screenshot_requirements`: none for planning; screenshots required during manual blockout
- `handoff_format`: `examples/stylized_orc_bruiser/handoffs/anatomy_to_manual_blockout.md`

## Acceptance Tests

- `acceptance_tests`: plan names major masses, landmarks, high-risk deformation zones, face/tusk construction rules, and screenshot requirements for the next stage
- `required_validators`: none in Phase 5
- `manual_review_required`: yes
- `hard_failure_checks`: no shoulder/neck plan; no pelvis/ribcage relationship; no face/tusk construction; no deformation-risk list

## Stop Conditions

- `stop_conditions`: stop before blockout if proportion plan is vague or contradicts style lock
- `requires_human_approval`: yes
- `rollback_required_if`: later animation or facial requirements invalidate the landmark plan
- `do_not_continue_if`: next stage lacks screenshot and review requirements

## Execution Notes

- `assigned_specialist`: Anatomy Reviewer
- `microtasks`: identify primary forms; define landmark checks; define deformation risk zones; define blockout review views
- `risks`: facial animation and skeleton requirements are unknown
- `questions_for_director`: target platform and animation list should be resolved before topology or rigging stages

## Completion

- `completed_outputs`: `examples/stylized_orc_bruiser/reviews/anatomy_review.md`
- `validation_summary`: no validators required
- `review_summary`: anatomy blockout plan approved with notes
- `blocking_issues`: none for manual blockout
- `approved_by`: Lucas
- `approved_at`: 2026-07-21
