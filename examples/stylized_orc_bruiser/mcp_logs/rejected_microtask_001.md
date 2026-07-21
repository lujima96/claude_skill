# Rejected MCP Microtask Example

## Metadata

- `log_id`: stylized_orc_bruiser-mcp-shoulder-bulk-edit-001
- `asset_id`: stylized_orc_bruiser
- `stage_id`: blockout
- `microtask_id`: blockout-shoulder-width-001
- `created_by`: Blender MCP Operator
- `created_at`: 2026-07-21
- `status`: rejected
- `execution_mode`: example

## Scope

- `task_card`: `task_cards/blockout_shoulder_width.example.md`
- `specialist_owner`: Anatomy Reviewer
- `microtask_goal`: Widen only the left and right shoulder blockout masses by a small amount while preserving neck clearance.
- `allowed_tools`: Blender MCP object transform on shoulder blockout objects; screenshot capture; mesh report; naming report
- `disallowed_tools`: torso sculpting; head edits; weapon edits; mesh deletion; apply transforms; retopology; rigging; export
- `acceptance_tests`: shoulder silhouette widens; neck clearance remains visible; torso, head, arms, and gear are unchanged; screenshots and reports exist
- `stop_conditions`: stop if non-shoulder objects are modified, source backup is missing, screenshots fail, or any destructive operation is attempted

## Source Protection

- `source_file`: `source/stylized_orc_bruiser_blockout.blend`
- `backup_file`: `source/backups/stylized_orc_bruiser_blockout.before_blockout-shoulder-width-001.blend`
- `working_file`: `source/working/stylized_orc_bruiser_blockout.blockout-shoulder-width-001.blend`
- `backup_verified`: yes
- `destructive_operations_requested`: no
- `destructive_operations_approved_by`: none
- `destructive_operations_approved_at`: none

## Action Trace

| Step | Tool Or Command | Intent | Result | Artifact |
|---:|---|---|---|---|
| 1 | Blender MCP copy/open working file | Protect source before edit | backup and working paths verified | `source/backups/stylized_orc_bruiser_blockout.before_blockout-shoulder-width-001.blend` |
| 2 | Blender MCP transform shoulder masses | Widen shoulders | shoulders widened, but upper torso scale also changed | `source/working/stylized_orc_bruiser_blockout.blockout-shoulder-width-001.blend` |
| 3 | `screenshot_set.py` | Capture review evidence | front and three-quarter views captured | `screenshots/blockout_shoulder_width/screenshot_manifest.json` |
| 4 | `mesh_report.py`; `naming_report.py` | Verify edit surface | reports produced; scope drift found by screenshot review | `reports/blender/blockout_shoulder_width/` |

## Evidence

- `screenshots`: `screenshots/blockout_shoulder_width/screenshot_manifest.json`
- `blender_reports`: `reports/blender/blockout_shoulder_width/mesh_report.json`; `reports/blender/blockout_shoulder_width/naming_report.json`
- `validation_reports`: `validations/blockout_shoulder_width_action_log.md`
- `specialist_review`: `reviews/blockout_shoulder_width_anatomy_review.example.md`
- `qa_audit`: `audits/blockout_shoulder_width_qa.example.md`

## Outcome

- `structural_change_made`: yes
- `hard_failures_present`: yes
- `blocked_stage_progression`: yes
- `rollback_required`: yes
- `rollback_artifact`: `source/backups/stylized_orc_bruiser_blockout.before_blockout-shoulder-width-001.blend`
- `decision`: rejected
- `decision_reason`: The edit changed upper torso scale outside the authorized shoulder-only microtask, so the working file must not replace the source asset.
- `human_approval_required`: yes
- `approved_by`: none
- `approved_at`: none

Note: This is a Phase 9 rejected-change example. It documents rollback behavior without relying on a connected Blender MCP session.
