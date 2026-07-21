# Primary-Mass Blockout Anatomy Review

## Metadata

- `review_id`: stylized_orc_bruiser-blockout-anatomy-review-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: blockout
- `review_type`: anatomy
- `reviewer`: Anatomy Reviewer
- `created_at`: 2026-07-21
- `status`: complete

## Inputs Reviewed

- `task_card`: `examples/stylized_orc_bruiser/task_cards/blockout_primary_masses.md`
- `artifacts`: `examples/stylized_orc_bruiser/source/working/stylized_orc_bruiser.blockout-primary-masses-001.working.blend`; scene and mesh reports
- `screenshots`: five-view set at `examples/stylized_orc_bruiser/screenshots/blockout_primary_masses/`
- `validation_reports`: `examples/stylized_orc_bruiser/validations/blockout_primary_masses_validation.md`
- `references`: approved reference board; anatomy plan; stylized biped anatomy rules

## Review Scope

- `in_scope`: primary mass relationships, visible joint landmarks, center of mass, head/jaw/tusk construction intent, and future deformation risks
- `out_of_scope`: sculpt quality, topology, UVs, rigging, skinning, animation, and Godot validation
- `assumptions`: intentionally crude primitive blockout in neutral stance; no facial-animation decision yet

## Findings

| Severity | Category | Finding | Evidence | Recommendation | Blocking |
|---|---|---|---|---|---|
| low | proportion | The broad ribcage, large shoulders, forearms, hands, and compact legs establish the intended bruiser mass hierarchy. | Front, back, and gameplay-distance views. | Preserve the shoulder-to-waist taper during primary forms. | no |
| medium | side_structure | The side view is thin and stacks chest, pelvis, and legs with limited depth separation. | Side screenshot. | In primary forms, clarify ribcage tilt, pelvis depth, heel, and glute/calf relationships. | no |
| medium | shoulder_neck | The left shoulder pad and enlarged deltoid crowd the neck and future arm-raise lane. | Front and three-quarter screenshots. | Keep the pad separate and establish clavicle, armpit, and deltoid attachment before costume refinement. | no |
| medium | face | Jaw, brow, ears, nose, and tusks read, but eye globes, mouth volume, and tusk roots are not constructed. | Front and three-quarter screenshots. | Build eye sockets/globes and a mouth cylinder before secondary facial forms; resolve facial-animation scope before topology. | no |
| low | joints | Elbow, wrist, hip, knee, and ankle masses are separately named and visible. | Mesh report and five-view set. | Retain these separations as deformation landmarks through the next stage. | no |

## Hard Failure Check

- `hard_failures_present`: no
- `hard_failures`: none for the declared primitive-blockout scope
- `blocked_stage_progression`: no

## Score Contribution

- `category_scores`: proportions and landmarks 7/10; anatomy or structural logic 6/10; deformation-readiness intent 4/10
- `score_notes`: the blockout proves the intended massing but deliberately lacks primary-form anatomy and deformation-ready construction
- `confidence`: high

## Decision

- `decision`: approve_with_notes
- `decision_reason`: the primary-mass blockout is sufficient to enter human review and, if accepted, begin primary forms without adding detail
- `required_next_actions`: preserve named landmarks; add ribcage/pelvis depth, eye and mouth construction, and shoulder clearance during primary forms
- `suggested_next_actions`: keep facial-animation requirements open but resolve them before topology
- `approved_by`: repository user
- `approved_at`: 2026-07-21
