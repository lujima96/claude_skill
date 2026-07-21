# Example Anatomy Review Report

## Metadata

- `review_id`: stylized_orc_bruiser-concept_interpretation-anatomy_review-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: concept_interpretation
- `review_type`: anatomy
- `reviewer`: Anatomy Reviewer
- `created_at`: TBD
- `status`: complete

## Inputs Reviewed

- `task_card`: `skills/character-director/references/example_stylized_biped_task_card.md`
- `artifacts`: `skills/character-director/references/example_stylized_biped_brief.md`
- `screenshots`: none
- `validation_reports`: none
- `references`: none yet

## Review Scope

- `in_scope`: anatomy and deformation risks implied by the brief
- `out_of_scope`: approving sculpt, topology, rigging, or Godot import
- `assumptions`: heroic stylized adult orc biped

## Findings

| Severity | Category | Finding | Evidence | Recommendation | Blocking |
|---|---|---|---|---|---|
| medium | proportion | Heavy upper-body exaggeration is appropriate but must be anchored by ribcage and pelvis planning. | Brief prioritizes broad shoulders, thick neck, heavy jaw, hands, and forearms. | Require proportion plan before blockout detail. | no |
| medium | deformation | Shoulder, neck, jaw, wrist, hip, and knee are high-risk zones. | Orc bruiser silhouette emphasizes those areas. | Require deformation landmark checks in proportion planning. | no |
| medium | face | Tusks and jaw need construction planning before sculpt detail. | Brief calls for readable tusks and heavy jaw. | Gather head, tusk, mouth, and jaw references. | no |

## Hard Failure Check

- `hard_failures_present`: no
- `hard_failures`: none at concept stage
- `blocked_stage_progression`: no

## Score Contribution

- `category_scores`: anatomy/structure pending; proportions pending
- `score_notes`: anatomy risks are identified clearly enough for reference gathering
- `confidence`: medium

## Decision

- `decision`: approve_with_notes
- `decision_reason`: the brief is anatomically reviewable, but proportion and deformation references are required before blockout approval
- `required_next_actions`: gather anatomy and deformation references for the risk zones
- `suggested_next_actions`: ask user whether facial animation is required
- `approved_by`:
- `approved_at`:
