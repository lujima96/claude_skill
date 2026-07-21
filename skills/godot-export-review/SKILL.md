---
name: godot-export-review
description: Review Godot import validation, preview scene evidence, GLB/glTF package completeness, Skeleton3D, materials, textures, animations, blend shapes, markers, collision nodes, and final engine-readiness gates for Blender-to-Godot character assets.
---

# Godot Export Review

The Godot Export Reviewer checks whether the asset works in Godot, not only in Blender.

## Use

Use this skill when:

- A `GLB` or `glTF` package is ready for Godot validation.
- A Godot import report needs review.
- Preview scene screenshots or render evidence need approval.
- Skeleton, materials, textures, animations, blend shapes, markers, or collision nodes need engine-side verification.
- Final QA needs evidence that the asset is Godot-ready.

## Inputs

- `engine/godot/import_checklist.md`
- `engine/godot/preview_scene_checklist.md`
- `engine/godot/validation_report.md`
- `templates/review_report.md`
- `knowledge/engine-standards/godot_import_requirements.md`

## Required Output

Produce a `templates/review_report.md`-compatible report with:

- Import success findings.
- Scene structure findings.
- Skeleton, skin, bone-name, animation, and blend-shape findings.
- Material, texture, and path findings.
- Marker, socket, hitbox, and collision findings.
- Preview scene findings.
- Decision: `approve`, `approve_with_notes`, `revise`, or `block`.

## Review Rules

- Do not approve final readiness without a Godot validation report.
- Do not accept Blender-only screenshots for final engine validation.
- Treat missing preview render evidence as blocking.
- If expected rig, animation, blend-shape, texture, marker, or collision data is missing after import, block progression.
- Route Blender export package issues back to Optimization Reviewer or Materials Reviewer.
