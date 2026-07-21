# Godot Biped Rig Requirements

```text
domain: rigging
body_region: full_body
species: humanoid
sex_or_body_type: any
age_band: adult
style_family: any
deformation_criticality: critical
target_engine: Godot
target_platform: unknown
source_quality: internal_first_pass
last_reviewed: 2026-07-20
linked_docs: knowledge/anatomy/deformation_landmarks.md, knowledge/engine-standards/godot_import_requirements.md
```

## Purpose

Use this when planning or reviewing rigging for Blender-to-Godot character assets.

## Required Decisions

- Target Godot version.
- Skeleton naming convention.
- Rest pose.
- Scale and unit convention.
- Maximum skin influences.
- Required animation clips.
- Whether facial animation uses bones, blend shapes, or no facial deformation.
- Required attachment markers, sockets, hitboxes, or collision nodes.

## Godot Import Expectations

- The imported scene should expose the expected skeleton structure.
- `Skeleton3D` should exist when a skinned character is expected.
- Bone names should remain stable across export and import.
- Skin weights should survive import.
- Animation clips should be available in the imported scene or associated animation resources.
- Blend shapes should survive import when required.

## Pose Tests

- Arm raise.
- Elbow flex.
- Wrist twist.
- Neck turn.
- Jaw open if jaw animation is required.
- Blink if eyelids are required.
- Hip lift.
- Deep crouch.
- Knee bend.
- Foot plant and toe-off.

## Common Failures

- Skeleton naming changes between Blender and Godot.
- Unweighted vertices appear only after import.
- Animation clips import but are not usable in the preview scene.
- Blend shapes exist in Blender but not after import.
- Markers, sockets, or collision requirements are discovered too late.

## Research Needed

Before implementing validators, verify the target Godot version's exact import behavior for `GLB`/`glTF`, animation clips, blend shapes, skeleton naming, and material overrides.
