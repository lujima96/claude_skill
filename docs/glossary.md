# Glossary

## Adapter

A layer that connects the framework to an external tool such as Blender MCP, Blender CLI scripts, or Godot. Adapters do not define production truth; contracts and validators do.

## Artifact

Any file or report produced by a stage. Examples include briefs, reference records, `.blend` files, screenshots, validation reports, handoffs, texture sets, `GLB` files, and Godot scenes.

## Asset Manifest

The inventory file for one character asset. It tracks source files, exports, Godot imports, reports, screenshots, validation state, and current approval state.

## Character Director

The orchestration role that owns stage order, task cards, handoffs, routing, stop conditions, and progression decisions.

## DCC

Digital Content Creation software. In this framework, Blender is the first supported DCC.

## Gate

A required checkpoint between stages. A gate usually requires artifacts, reviews, validations, a QA decision, and human approval.

## GLB

A binary glTF package. This is the preferred default Blender-to-Godot interchange format unless a project records a reason to use separate `.gltf` files.

## glTF

The interchange format used to move assets from Blender into Godot. It may be stored as separate `.gltf` plus external resources or as a binary `.glb`.

## Godot Readiness

The state where an exported character imports, opens, previews, animates, and binds materials correctly in the target Godot project.

## Handoff

The document that transfers one completed stage to the next. It summarizes outputs, artifacts, validation, review state, known issues, and next-stage instructions.

## Hard Failure

A blocking condition that stops progression regardless of QA score. Hard failures are defined in `docs/pipeline/hard_failures.md`.

## MCP

Model Context Protocol. In this project MCP is a tool connection layer, not the source of truth. MCP-controlled edits must be bounded, logged, reviewed, and validated.

## QA Audit

The aggregate quality report that combines specialist reviews, validator outputs, hard-failure status, weighted scoring, diagnosis, and progression decision.

## Reference Record

A structured entry describing a reference source, its metadata, its intended use, and whether it is approved for the asset.

## Revision Task

A scoped task card that returns to an earlier stage to fix a specific problem. Revisions prevent silent cross-stage changes.

## Specialist Skill

A focused skill responsible for a narrow domain such as reference gathering, style, anatomy, topology, rigging, materials, Godot export, or QA.

## Stage

One production step in the character pipeline. Stage order is defined in `docs/pipeline/stage_list.md`.

## Stage Task Card

The work order for one bounded stage task. It defines goal, current stage, tools, constraints, inputs, output contract, acceptance tests, stop conditions, and handoff format.

## Validator

A deterministic check that produces a validation report. Validators should catch missing fields, broken file references, invalid geometry, import failures, naming violations, or other machine-checkable issues.
