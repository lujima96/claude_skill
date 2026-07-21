---
name: optimization-review
description: Review character optimization, LOD naming, LOD polycount budgets, material-slot budgets, texture memory, collision/marker scope, and GLB/glTF package completeness for Godot-targeted character production. Use when an asset is approaching export, LOD creation, performance review, or package readiness.
---

# Optimization Review

The Optimization Reviewer checks whether the asset can meet performance and package-readiness requirements. It does not approve final Godot import by itself.

## Use

Use this skill when:

- LOD naming and polycount budgets need validation.
- Material slots or texture sizes need performance review.
- GLB/glTF package completeness needs a pre-Godot check.
- Collision, markers, sockets, or attachment nodes affect runtime budget.
- Export readiness depends on multiple Blender reports.

## Inputs

- `templates/review_report.md`
- `templates/optimization_report.md`
- `templates/asset_manifest.md`
- `blender_scripts/mesh_report.py`
- `blender_scripts/material_report.py`
- `blender_scripts/export_package.py`
- `knowledge/engine-standards/godot_import_requirements.md`
- `knowledge/materials/godot_character_materials.md`

## Required Output

Produce a `templates/review_report.md`-compatible report and, when optimization data is available, a `templates/optimization_report.md`-compatible report with:

- LOD naming findings.
- LOD polycount budget findings.
- Material slot and texture size budget findings.
- Collision, marker, and socket scope findings.
- GLB/glTF package completeness findings.
- Godot export texture path findings.
- Decision: `approve`, `approve_with_notes`, `revise`, or `block`.

## Review Rules

- Missing LOD policy blocks optimization approval when LODs are required.
- LOD names must be stable and sortable.
- LOD triangle counts must meet declared budgets.
- Export package completeness must include meshes, materials, textures, skeleton and animations when required.
- Texture paths must resolve inside the expected export/Godot project structure.
- Route final import behavior to the Godot export adapter once available.

## First Workflow

For `stylized_orc_bruiser`, use `references/optimization_review_rules.md` and `references/example_optimization_review_report.md`.
