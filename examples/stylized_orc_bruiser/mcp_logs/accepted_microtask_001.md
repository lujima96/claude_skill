# Accepted MCP Microtask Example

## Metadata

- `log_id`: stylized_orc_bruiser-mcp-blockout-camera-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: blockout
- `microtask_id`: blockout-review-camera-marker-001
- `created_by`: Blender MCP Operator
- `created_at`: 2026-07-21
- `status`: approved
- `execution_mode`: example

## Scope

- `task_card`: `task_cards/blockout_camera_marker.example.md`
- `specialist_owner`: Anatomy Reviewer
- `microtask_goal`: Add one non-rendering review marker named `MCP_REVIEW_scale_height_marker` beside the blockout for screenshot scale reference.
- `allowed_tools`: Blender MCP object creation; Blender MCP object rename; screenshot capture; scene report; naming report
- `disallowed_tools`: sculpt edits; mesh merge; delete objects; apply transforms; retopology; rigging; export
- `acceptance_tests`: marker exists; marker is not parented to character mesh; marker does not alter character geometry; screenshots and naming report exist
- `stop_conditions`: stop if source backup is missing, marker creation affects character geometry, screenshots fail, or naming report fails

## Source Protection

- `source_file`: `source/stylized_orc_bruiser_blockout.blend`
- `backup_file`: `source/backups/stylized_orc_bruiser_blockout.before_blockout-review-camera-marker-001.blend`
- `working_file`: `source/working/stylized_orc_bruiser_blockout.blockout-review-camera-marker-001.blend`
- `backup_verified`: yes
- `destructive_operations_requested`: no
- `destructive_operations_approved_by`: none
- `destructive_operations_approved_at`: none

## Action Trace

| Step | Tool Or Command | Intent | Result | Artifact |
|---:|---|---|---|---|
| 1 | Blender MCP copy/open working file | Protect source before edit | backup and working paths verified | `source/backups/stylized_orc_bruiser_blockout.before_blockout-review-camera-marker-001.blend` |
| 2 | Blender MCP add empty cube marker | Add screenshot scale marker | marker created beside character bounds | `source/working/stylized_orc_bruiser_blockout.blockout-review-camera-marker-001.blend` |
| 3 | Blender MCP rename object | Apply naming contract | object named `MCP_REVIEW_scale_height_marker` | working `.blend` |
| 4 | `screenshot_set.py` | Capture review evidence | required views captured | `screenshots/blockout_camera_marker/screenshot_manifest.json` |
| 5 | `scene_report.py`; `naming_report.py` | Verify object and naming state | reports passed with no hard failures | `reports/blender/blockout_camera_marker/` |

## Evidence

- `screenshots`: `screenshots/blockout_camera_marker/screenshot_manifest.json`
- `blender_reports`: `reports/blender/blockout_camera_marker/scene_report.json`; `reports/blender/blockout_camera_marker/naming_report.json`
- `validation_reports`: `validations/blockout_camera_marker_action_log.md`
- `specialist_review`: `reviews/blockout_camera_marker_anatomy_review.example.md`
- `qa_audit`: `audits/blockout_camera_marker_qa.example.md`

## Outcome

- `structural_change_made`: yes
- `hard_failures_present`: no
- `blocked_stage_progression`: no
- `rollback_required`: no
- `rollback_artifact`: none
- `decision`: approved
- `decision_reason`: The microtask stayed in scope, preserved the source file, produced review screenshots, and added only the requested review marker.
- `human_approval_required`: yes
- `approved_by`: Lucas
- `approved_at`: 2026-07-21

Note: This is a Phase 9 example log. No real Blender MCP session or source `.blend` exists in this workspace yet.
