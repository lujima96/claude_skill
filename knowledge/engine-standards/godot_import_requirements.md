# Godot Import Requirements

```text
domain: engine_standards
body_region: full_body
species: any
sex_or_body_type: any
age_band: any
style_family: any
deformation_criticality: critical
target_engine: Godot
target_platform: unknown
source_quality: internal_first_pass
last_reviewed: 2026-07-20
linked_docs: knowledge/rigging/godot_biped_rig_requirements.md, knowledge/materials/godot_character_materials.md
```

## Purpose

Use this when defining Godot export and validation task cards.

## Default Assumption

Use `GLB` as the default interchange package from Blender to Godot unless the project records a reason to use separate `glTF` files.

## Required Validation

- Export package exists.
- Package references are complete.
- Godot import succeeds.
- Imported scene opens in the target project.
- Expected mesh nodes exist.
- Expected `Skeleton3D` exists for skinned characters.
- Skin weights survive import.
- Material slots match the asset manifest.
- Texture references exist and load.
- Animation clips import and play in a preview scene.
- Blend shapes import when required.
- Collision, hitbox, attachment, or marker nodes exist when required.
- Preview scene renders under known lighting and camera distance.

## Suggested Preview Scene Checks

- Neutral turntable or static preview.
- Gameplay-distance camera.
- Default lighting.
- Test animation playback.
- Pose test playback if available.
- Material and texture visibility.
- Hair or alpha-material visibility if applicable.

## Common Failures

- Blender export succeeds but Godot import produces missing textures.
- Imported scene structure differs from the manifest.
- Skeleton exists but skin weights or animations do not behave correctly.
- Blend shapes are lost or renamed.
- Material overrides are needed but not documented.
- Asset is visually acceptable in Blender but unreadable under Godot lighting.

## Research Needed

Before scripting validators, verify target Godot version, import CLI or editor automation options, expected folder structure, material override policy, and animation/preview-scene conventions.
