---
name: topology-review
description: Review deformation-ready character mesh topology for staged Blender-to-Godot production. Use when a retopology mesh, mesh report, screenshots, bake-prep mesh, cloth mesh, or topology revision needs edge-flow, pole, triangle, density, and deformation-zone approval before rigging, baking, or export.
---

# Topology Review

The Topology Reviewer checks whether the mesh can deform, bake, and survive later rigging. It does not approve anatomy, rig weights, materials, or Godot import by itself.

## Use

Use this skill when:

- A retopology mesh is ready for specialist review.
- Blender mesh reports or topology screenshots need interpretation.
- A mesh is being prepared for bake, skinning, or deformation testing.
- A later deformation failure appears to originate in edge flow or mesh density.
- Cloth, hair cards, armor, or accessories cross deformation zones.

## Inputs

- `templates/review_report.md`
- `templates/topology_report.md`
- `blender_scripts/mesh_report.py`
- `blender_scripts/naming_report.py`
- `knowledge/topology/biped_deformation_loops.md`
- `knowledge/anatomy/deformation_landmarks.md`
- `knowledge/critique-patterns/stylized_biped_review_failures.md`

## Required Output

Produce a `templates/review_report.md`-compatible report and, when mesh data is available, a `templates/topology_report.md`-compatible report with:

- Edge-flow findings for eyes, mouth, shoulders, elbows, hips, knees, neck, fingers, and cloth bend zones.
- Pole and triangle hot-spot findings.
- Loop-density findings by deformation zone.
- Bake-readiness risks.
- Mesh report evidence, screenshots, or explicit missing-input blockers.
- Decision: `approve`, `approve_with_notes`, `revise`, or `block`.

## Review Rules

- Approve topology for deformation, not for still-image cleanliness.
- Treat missing mesh reports or missing deformation-zone screenshots as blockers for topology approval.
- Keep poles and triangles away from eyelids, mouth corners, shoulders, elbows, wrists, hips, knees, ankles, fingers, jaw, and neck.
- Do not approve auto-remeshed topology in critical deformation zones unless manual corrective loops are visible.
- Require cloth, belts, armor, hair, and accessories to respect body bend zones underneath.
- Route weight, skeleton, pose-battery, and corrective-shape issues to Rigging Reviewer.

## First Workflow

For `stylized_orc_bruiser`, use `references/topology_review_rules.md` and `references/example_topology_review_report.md`.
