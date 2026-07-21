---
name: rigging-review
description: Review skeleton, skinning, deformation, pose-battery, and Godot-readiness risks for staged Blender-to-Godot character production. Use when a character rig, skin weights, pose test, deformation report, corrective shape plan, or rigging revision needs approval before animation, export, or Godot validation.
---

# Rigging Review

The Rigging Reviewer checks whether the skeleton, weights, deformation behavior, and pose evidence can support the declared gameplay and Godot import path. It does not approve topology, materials, or final engine import by itself.

## Use

Use this skill when:

- A skeleton or skinned mesh is ready for review.
- A pose battery report needs interpretation.
- A Godot-targeted rig requires naming, scale, influence, or import-risk checks.
- Corrective shapes, twist bones, or facial deformation decisions need review.
- A deformation failure appears after topology approval.

## Inputs

- `templates/review_report.md`
- `templates/deformation_report.md`
- `blender_scripts/pose_battery.py`
- `blender_scripts/scene_report.py`
- `blender_scripts/export_package.py`
- `knowledge/rigging/godot_biped_rig_requirements.md`
- `knowledge/anatomy/deformation_landmarks.md`
- `knowledge/engine-standards/godot_import_requirements.md`

## Required Output

Produce a `templates/review_report.md`-compatible report and, when rig data is available, a `templates/deformation_report.md`-compatible report with:

- Skeleton naming findings.
- Joint placement findings.
- Maximum influences per vertex.
- Unweighted vertex findings.
- Twist-zone findings.
- Corrective-shape needs.
- Pose-battery results.
- Decision: `approve`, `approve_with_notes`, `revise`, or `block`.

## Review Rules

- Require an armature, skinned mesh, and pose-battery evidence before rigging approval.
- Treat Godot import constraints as part of the rigging contract, especially stable bone names, scale, skinning, animations, and blend shapes.
- Do not approve deformation based only on bind pose.
- Record whether facial animation is bone-based, blend-shape-based, or out of scope.
- Route missing loops or mesh construction issues back to Topology Reviewer.

## First Workflow

For `stylized_orc_bruiser`, use `references/rigging_review_rules.md` and `references/example_rigging_review_report.md`.
