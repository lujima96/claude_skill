# Godot Scripts

These scripts are adapter-side helpers for Phase 11. They are intentionally small and report-oriented.

## Scripts

- `import_probe.gd`: attach to or run inside a Godot project to inspect an imported scene and write a JSON summary.

The Markdown validator in `validators/validate_godot_validation.py` validates the report contract after a human or script fills `engine/godot/validation_report.md`.
