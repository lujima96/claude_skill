# Godot Adapter

This folder contains the first engine adapter.

The Godot adapter validates that exported character assets import and preview correctly in Godot. It should check:

- `GLB` or `glTF` package completeness
- imported scene opens cleanly
- expected `Skeleton3D` exists
- skin weights survive import
- materials bind
- textures are referenced
- animation clips import and play
- blend shapes import when required
- collision, hitbox, attachment, or marker nodes exist when required
- preview scene renders under known lighting

Godot validation is required before an asset is considered complete.

## Files

- `import_checklist.md`: required import checks.
- `preview_scene_checklist.md`: required preview-scene checks.
- `validation_report.md`: Markdown report contract.
- `scripts/import_probe.gd`: Godot-side scene inspection helper.

## Validator

Use:

```bash
python3 validators/validate_godot_validation.py path/to/godot_validation_report.md
```
