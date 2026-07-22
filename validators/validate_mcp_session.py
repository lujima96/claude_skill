#!/usr/bin/env python3
"""Validate an append-only, hash-chained Blender MCP edit session journal."""

from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from datetime import datetime
from pathlib import Path

from rules.markdown_fields import CheckResult, render_validation_report


VERSION = "0.1.0"
SCHEMA_VERSION = "0.1.0"
RECORD_TYPES = {
    "session_started", "iteration_accepted", "iteration_rejected", "preview_result",
    "checkpoint_completed", "rollback", "session_closed",
}
SAFE_OPERATIONS = {"absolute_transform", "visibility", "collection_membership", "vertex_positions"}


def _session_module():
    path = Path(__file__).resolve().parents[1] / "skills/blender-mcp-operator/scripts/mcp_session.py"
    spec = importlib.util.spec_from_file_location("mcp_session_contract", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader
    spec.loader.exec_module(module)
    return module


def validate(path: Path):
    failures: list[CheckResult] = []
    warnings: list[CheckResult] = []
    records = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except Exception as exc:
        return [CheckResult("journal_read", "Journal must be readable", str(exc), "Restore the session journal.")], warnings, records, {}
    if not lines:
        return [CheckResult("journal_nonempty", "Journal must contain records", "empty", "Start the session journal.")], warnings, records, {}
    module = _session_module()
    for index, line in enumerate(lines, 1):
        if not line.strip():
            failures.append(CheckResult("jsonl_blank", "JSONL must not contain blank lines", str(index), "Remove the blank line without rewriting valid records."))
            continue
        try:
            value = json.loads(line)
            if not isinstance(value, dict):
                raise TypeError("record is not an object")
            records.append(value)
        except Exception as exc:
            failures.append(CheckResult("valid_jsonl", "Each journal line must be a JSON object", f"line {index}: {exc}", "Restore the unmodified append-only record."))
    if not records:
        return failures, warnings, records, {"record_count": 0}

    session_id = records[0].get("session_id")
    authorized_task_card = records[0].get("details", {}).get("task_card")
    pending_previews: set[int] = set()
    checkpoint_count = 0
    for index, record in enumerate(records, 1):
        required = {
            "schema_version", "session_id", "sequence", "previous_record_hash", "record_hash",
            "record_type", "timestamp", "targets", "operations", "before_hash", "after_hash",
            "drift", "durations_ms", "details",
        }
        missing = sorted(required - set(record))
        if missing:
            failures.append(CheckResult("record_fields", "Session record fields are required", f"line {index}: {', '.join(missing)}", "Regenerate the record with mcp_session.py."))
            continue
        if record["schema_version"] != SCHEMA_VERSION:
            failures.append(CheckResult("schema_version", "Session schema version must be supported", str(record["schema_version"]), f"Use {SCHEMA_VERSION}."))
        if record["session_id"] != session_id:
            failures.append(CheckResult("session_consistency", "All records must share one session ID", f"line {index}", "Use one journal per session."))
        if record["sequence"] != index:
            failures.append(CheckResult("sequence", "Record sequence must be contiguous", f"line {index}: {record['sequence']}", "Append records through mcp_session.py."))
        expected_previous = "" if index == 1 else records[index - 2].get("record_hash", "")
        if record["previous_record_hash"] != expected_previous:
            failures.append(CheckResult("hash_chain", "Previous-record hash must match", f"line {index}", "Restore the append-only journal."))
        if record["record_hash"] != module.calculate_record_hash(record):
            failures.append(CheckResult("record_hash", "Record hash must match canonical content", f"line {index}", "Restore the unmodified record."))
        if record["record_type"] not in RECORD_TYPES:
            failures.append(CheckResult("record_type", "Record type must be known", str(record["record_type"]), "Use a versioned session event."))
        try:
            datetime.fromisoformat(record["timestamp"].replace("Z", "+00:00"))
        except Exception:
            failures.append(CheckResult("timestamp", "Record timestamp must be ISO-8601", str(record["timestamp"]), "Write a timezone-aware timestamp."))
        targets = record["targets"]
        if not isinstance(targets, list) or len(targets) != len(set(targets)) or len(targets) > 6:
            failures.append(CheckResult("target_limit", "Each edit may name at most six unique targets", str(targets), "Reduce the edit scope."))
        operations = record["operations"]
        if not isinstance(operations, list) or any(op.get("type") not in SAFE_OPERATIONS for op in operations if isinstance(op, dict)):
            failures.append(CheckResult("safe_operations", "Operations must use the safe declarative allowlist", str(operations), "Escalate structural work to a checkpoint."))
        if any(not isinstance(op, dict) or op.get("target") not in targets for op in operations):
            failures.append(CheckResult("exact_targets", "Every operation must name an exact listed target", str(operations), "Normalize the operation receipt."))
        try:
            if module.normalize_operations(operations) != operations:
                failures.append(CheckResult("normalized_operations", "Journal operations must be canonical absolute operations", f"line {index}", "Append the normalized quick-edit result."))
        except Exception as exc:
            failures.append(CheckResult("normalized_operations", "Journal operations must be canonical absolute operations", f"line {index}: {exc}", "Append the normalized quick-edit result."))
        durations = record["durations_ms"]
        if not isinstance(durations, dict) or "total" not in durations or any(not isinstance(value, (int, float)) or value < 0 for value in durations.values()):
            failures.append(CheckResult("timings", "Phase and total durations must be non-negative numbers", str(durations), "Record internal timings."))

        kind = record["record_type"]
        if kind == "session_started":
            details = record["details"]
            required_start = {
                "asset_id", "stage_id", "task_card", "authorized_collections", "safe_change_types",
                "max_targets_per_edit", "source_file", "backup_file", "working_file",
                "source_protection_receipt", "capability_preflight",
            }
            missing_start = sorted(required_start - set(details))
            if missing_start:
                failures.append(CheckResult("session_start_contract", "Session start must capture protection, scope, and preflight", ", ".join(missing_start), "Open the session with mcp_session.open_session()."))
            protected = [Path(details.get(name, "")) for name in ("source_file", "backup_file", "working_file")]
            if len({str(item.resolve()) for item in protected}) != 3:
                failures.append(CheckResult("protected_paths", "Source, backup, and working files must be distinct", str(protected), "Create non-overwriting protection files."))
            for artifact in [*protected, Path(details.get("source_protection_receipt", "")), Path(details.get("task_card", ""))]:
                if not artifact.is_file():
                    failures.append(CheckResult("session_artifact", "Session protection and task artifacts must exist", str(artifact), "Recover the session protection envelope."))
            if details.get("max_targets_per_edit") != 6:
                failures.append(CheckResult("session_target_contract", "Session must retain the six-target edit limit", str(details.get("max_targets_per_edit")), "Open a schema-compliant session."))
        elif kind == "iteration_accepted":
            if record["drift"].get("status") != "pass" or record["drift"].get("issues"):
                failures.append(CheckResult("accepted_clean_delta", "Accepted iterations require a clean delta", f"line {index}", "Reject and recover the iteration."))
            if not record["before_hash"] or not record["after_hash"]:
                failures.append(CheckResult("iteration_hashes", "Accepted iterations require before and after hashes", f"line {index}", "Record deterministic fingerprints."))
            pending_previews.add(index)
        elif kind == "preview_result":
            details = record["details"]
            iteration_sequence = details.get("iteration_sequence")
            preview = details.get("preview", {})
            if iteration_sequence not in pending_previews:
                failures.append(CheckResult("preview_iteration", "Preview must reference a pending accepted iteration", f"line {index}", "Reference the accepted iteration sequence."))
            if preview.get("status") not in {"captured", "rendered_fallback"}:
                failures.append(CheckResult("preview_status", "Preview must be captured or rendered fallback", str(preview), "Capture one viewport image or one 512px Eevee fallback."))
            if not preview.get("tool") or not preview.get("view") or not preview.get("timestamp"):
                failures.append(CheckResult("preview_metadata", "Preview tool, view, and timestamp are required", str(preview), "Record preview metadata."))
            dimensions = preview.get("dimensions")
            if not isinstance(dimensions, list) or len(dimensions) != 2 or any(not isinstance(value, int) or value <= 0 for value in dimensions):
                failures.append(CheckResult("preview_dimensions", "Preview dimensions must be positive integers", str(dimensions), "Record [width, height]."))
            pending_previews.discard(iteration_sequence)
        elif kind == "checkpoint_completed":
            checkpoint_count += 1
            if record["details"].get("task_card") != authorized_task_card:
                failures.append(CheckResult("checkpoint_task_card", "Checkpoint must reuse the session's stage task card", str(record["details"].get("task_card")), "Reference the original authorization envelope."))
            artifacts = record["details"].get("artifacts", [])
            if not isinstance(artifacts, list) or len(artifacts) < 5:
                failures.append(CheckResult("checkpoint_bundle", "Checkpoint must reference the bundled screenshot manifest and four Blender reports", str(artifacts), "Generate the five checkpoint artifacts in one Blender call."))
            elif len(set(artifacts)) != len(artifacts) or any(not Path(artifact).is_file() for artifact in artifacts):
                failures.append(CheckResult("checkpoint_artifacts", "Checkpoint artifact paths must be distinct existing files", str(artifacts), "Regenerate and validate the checkpoint bundle."))
        elif kind == "session_closed" and record["details"].get("task_card") != authorized_task_card:
            failures.append(CheckResult("closure_task_card", "Session closure must reuse the session's stage task card", str(record["details"].get("task_card")), "Close the original authorization envelope."))

    if records[0].get("record_type") != "session_started":
        failures.append(CheckResult("session_start", "First record must start the session", str(records[0].get("record_type")), "Create a new valid journal."))
    if sum(record.get("record_type") == "session_started" for record in records) != 1:
        failures.append(CheckResult("single_start", "Journal must contain one session start", session_id or "", "Use one journal per session."))
    if any(record.get("record_type") == "session_closed" for record in records[:-1]):
        failures.append(CheckResult("closed_is_final", "Session closure must be the final record", session_id or "", "Do not append after closure."))
    for sequence in sorted(pending_previews):
        failures.append(CheckResult("preview_required", "Every accepted iteration requires one preview result", str(sequence), "Capture the viewport preview or Eevee fallback."))
    measurements = {
        "record_count": len(records),
        "accepted_iterations": sum(record.get("record_type") == "iteration_accepted" for record in records),
        "checkpoint_count": checkpoint_count,
    }
    return failures, warnings, records, measurements


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    failures, warnings, records, measurements = validate(args.path)
    first = records[0] if records else {}
    print(render_validation_report(
        validator_name="validate_mcp_session", validator_version=VERSION, input_path=args.path,
        repo_root=args.repo_root, asset_id=first.get("details", {}).get("asset_id", ""),
        stage_id=first.get("details", {}).get("stage_id", ""), failures=failures,
        warnings=warnings, measurements=measurements,
    ))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
