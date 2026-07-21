# Example Stylized Biped Task Card

This example shows the first task card the Character Director should be able to produce from the prompt: "stylized orc bruiser for a third-person game."

## Metadata

- `task_id`: stylized_orc_bruiser-concept_interpretation-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: concept_interpretation
- `stage_name`: Concept interpretation
- `created_by`: Character Director
- `created_at`: TBD
- `status`: draft

## Goal

- `goal`: Convert the raw idea into a production-ready character brief for a stylized biped character targeting Godot.
- `current_stage`: concept_interpretation
- `previous_stage`: none
- `next_stage`: reference_gathering

## Constraints

- `allowed_tools`: local templates, pipeline contracts, user-provided constraints
- `disallowed_tools`: Blender MCP, Blender editing scripts, Godot import tools, topology tools, rigging tools
- `known_constraints`: stylized orc bruiser; third-person game; Blender source; Godot target; `GLB` or `glTF` export path
- `style_constraints`: heroic stylized fantasy unless user specifies another style family
- `technical_constraints`: unknown poly budget, material slot budget, texture budget, skeleton spec, animation list, and target Godot version
- `godot_constraints`: target engine is Godot; imported asset must eventually validate as a Godot scene with skeleton, materials, textures, animations, and preview rendering

## Inputs

- `input_refs`: none yet
- `input_artifacts`: raw prompt
- `input_reports`: none
- `previous_handoff`: none
- `assumptions`: third-person camera means silhouette and gameplay-distance readability matter from the blockout stage onward

## Output Contract

- `required_outputs`: completed `templates/character_brief.md` draft with open questions marked
- `output_paths`: `examples/stylized_orc_bruiser/brief.md`
- `report_paths`: none for this stage
- `screenshot_requirements`: none for this stage
- `handoff_format`: `templates/stage_handoff.md`

## Acceptance Tests

- `acceptance_tests`: brief defines character role, gameplay function, style family, Godot target, Blender source, interchange format, camera context, rig needs, animation needs, scope, deliverables, and open questions
- `required_validators`: none in Phase 2
- `manual_review_required`: yes
- `hard_failure_checks`: missing target engine, missing style family, missing camera context, missing deliverables, unknown budgets not recorded as open questions

## Stop Conditions

- `stop_conditions`: stop after draft brief and open questions are produced; do not gather references or create geometry in this stage
- `requires_human_approval`: yes
- `rollback_required_if`: not applicable
- `do_not_continue_if`: target engine, camera context, style family, or core deliverables are missing and not recorded

## Execution Notes

- `assigned_specialist`: Character Director
- `microtasks`: parse raw idea; identify production assumptions; fill brief; list open questions; prepare handoff to reference gathering
- `risks`: unknown technical budgets may block later approval
- `questions_for_director`: none

## Completion

- `completed_outputs`: pending
- `validation_summary`: no validators required
- `review_summary`: pending human review
- `blocking_issues`: target Godot version, target platform, poly budget, texture budget, material slot budget, skeleton spec, and animation list are unknown
- `approved_by`:
- `approved_at`:
