# Blender Scripts

These scripts are the Phase 7 Blender script pack. They are designed to run inside Blender and produce deterministic JSON or Markdown reports before any MCP-controlled editing exists.

The default posture preserves the source `.blend`. Reports, screenshot manifests, screenshots, and explicit exports are separate artifacts and refuse to overwrite existing evidence unless `--overwrite` is passed.

## Scripts

- `scene_report.py`: scene, object, collection, camera, light, unit, and render-engine summary.
- `mesh_report.py`: mesh object counts, vertices, edges, faces, triangle estimate, material slots, modifiers, shape keys, vertex groups.
- `material_report.py`: materials, node usage, image texture references, missing image warnings.
- `naming_report.py`: object naming, generated suffixes, unapplied scale, negative scale.
- `screenshot_set.py`: captures the required review views and writes a screenshot manifest.
- `pose_battery.py`: reports armature and skinned-mesh readiness for later deformation tests.
- `export_package.py`: reports GLB/glTF export readiness; optional explicit export.

## Running In Blender

Use Blender's `--` separator to pass script arguments:

```bash
blender --background path/to/character.blend --python blender_scripts/scene_report.py -- --asset-id stylized_orc_bruiser --stage-id blockout --out examples/stylized_orc_bruiser/reports/blender/scene_report.json
blender --background path/to/character.blend --python blender_scripts/mesh_report.py -- --asset-id stylized_orc_bruiser --stage-id blockout --out examples/stylized_orc_bruiser/reports/blender/mesh_report.json
blender --background path/to/character.blend --python blender_scripts/material_report.py -- --asset-id stylized_orc_bruiser --stage-id blockout --out examples/stylized_orc_bruiser/reports/blender/material_report.json
blender --background path/to/character.blend --python blender_scripts/naming_report.py -- --asset-id stylized_orc_bruiser --stage-id blockout --out examples/stylized_orc_bruiser/reports/blender/naming_report.json
```

Screenshot manifest and planned/captured views:

```bash
blender --background path/to/character.blend --python blender_scripts/screenshot_set.py -- --asset-id stylized_orc_bruiser --stage-id blockout --target-collection CHARACTER --screenshot-dir examples/stylized_orc_bruiser/screenshots --out examples/stylized_orc_bruiser/reports/blender/screenshot_set.json
```

Readiness-only reports:

```bash
blender --background path/to/character.blend --python blender_scripts/pose_battery.py -- --asset-id stylized_orc_bruiser --stage-id blockout --out examples/stylized_orc_bruiser/reports/blender/pose_battery.json
blender --background path/to/character.blend --python blender_scripts/export_package.py -- --asset-id stylized_orc_bruiser --stage-id blockout --out examples/stylized_orc_bruiser/reports/blender/export_package.json
```

Explicit export requires an extra flag:

```bash
blender --background path/to/character.blend --python blender_scripts/export_package.py -- --asset-id stylized_orc_bruiser --stage-id export_godot_validation --export-path exports/stylized_orc_bruiser.glb --execute-export --out reports/blender/export_package.json
```

## Screenshot Manifest Format

`screenshot_set.py` writes a JSON manifest with:

- `asset_id`
- `stage_id`
- `source_file`
- `screenshots`: list of `{ view, path, status, required_for_review }`

Required first-pass views are `front`, `side`, `back`, `three_quarter`, and `gameplay_distance`.

The screenshot script frames named targets from world-space bounds, uses a temporary camera/light rig, verifies every PNG, and restores the original scene state. Real MCP task cards must pass either `--target-collection` or `--target-objects` explicitly.

## Sample Reports

Sample Phase 7 reports are committed under:

`examples/stylized_orc_bruiser/reports/blender/`

These are format examples until a real `.blend` file exists.
