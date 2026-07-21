# Anatomy Review

## Metadata

- `review_id`: stylized_orc_bruiser-anatomy_blockout_planning-anatomy_review-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: anatomy_blockout_planning
- `review_type`: anatomy
- `reviewer`: Anatomy Reviewer
- `created_at`: 2026-07-21
- `status`: complete

## Inputs Reviewed

- `task_card`: `examples/stylized_orc_bruiser/task_cards/anatomy_blockout_planning.md`
- `artifacts`: `examples/stylized_orc_bruiser/brief.md`; `examples/stylized_orc_bruiser/reference_boards/approved_initial_board.md`
- `screenshots`: none
- `validation_reports`: none
- `references`: `ref-007`, `ref-008`, `ref-009`, `ref-010`, `ref-011`

## Review Scope

- `in_scope`: proportion plan, biped landmarks, shoulder/neck logic, face/tusk construction, deformation-risk planning, screenshot requirements for blockout
- `out_of_scope`: approving a sculpt, topology, skinning, facial rigging, animation, Godot import
- `assumptions`: adult heroic stylized orc; exaggerated but still riggable biped structure

## Findings

| Severity | Category | Finding | Evidence | Recommendation | Blocking |
|---|---|---|---|---|---|
| low | proportion | Upper-body exaggeration is appropriate if ribcage and pelvis stay legible. | Brief calls for broad shoulders, thick neck, heavy jaw, large hands, and strong forearms. | Block in ribcage and pelvis as separate readable masses before armor. | no |
| medium | shoulder_neck | Shoulder and neck are the highest-risk silhouette/anatomy zone. | Style lock emphasizes heavy shoulders and thick neck; anatomy refs cover deltoids and shoulder bones. | Keep clavicle/scapula/deltoid logic visible in blockout, even when stylized. | no |
| medium | face_tusks | Jaw and tusks need construction before expression or detail. | Brief requires readable tusks and heavy jaw; `ref-008` supports head/tusk planning. | Anchor tusks to mouth/jaw structure and leave mouth deformation space until facial needs are known. | no |
| medium | hands_forearms | Large hands and forearms are style-critical and deformation-sensitive. | Brief lists large hands and strong forearms as silhouette priorities. | Add explicit hand reference before hand modeling or rigging gates. | no |
| medium | hips_knees | Lower-body landmarks are less referenced than shoulders/head. | Approved board notes hip and knee references may be needed later. | Keep pelvis, knee, ankle, and foot alignment simple in blockout; gather more refs before topology. | no |

## Hard Failure Check

- `hard_failures_present`: no
- `hard_failures`: none for anatomy blockout planning
- `blocked_stage_progression`: no

## Score Contribution

- `category_scores`: proportion planning ready; anatomy risk zones identified; deformation readiness limited to planning stage
- `score_notes`: enough to begin a manual blockout; not enough for topology or rigging approval
- `confidence`: medium

## Decision

- `decision`: approve_with_notes
- `decision_reason`: anatomy plan is clear enough for the first blockout, with later reference gaps tracked
- `required_next_actions`: block out ribcage, pelvis, skull, jaw, neck, shoulders, hands, hips, knees, and feet as visible masses; capture review screenshots
- `suggested_next_actions`: resolve facial animation requirements before committing to mouth/tusk topology
- `approved_by`: Lucas
- `approved_at`: 2026-07-21
