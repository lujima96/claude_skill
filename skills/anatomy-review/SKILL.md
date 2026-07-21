---
name: anatomy-review
description: Review character proportions, construction, anatomical landmarks, asymmetry, facial structure, deformation landmarks, and pose risks for staged Blender-to-Godot character production. Use when a concept, proportion plan, blockout, sculpt, or revision needs anatomy and structural critique before proceeding.
---

# Anatomy Review

The Anatomy Reviewer checks whether the character is structurally believable for the chosen style and whether it can survive later deformation. It does not perform topology approval, rigging approval, or Godot import validation.

## Use

Use this skill when:

- A brief needs anatomy risks identified.
- A proportion plan needs review.
- A blockout needs primary-form critique.
- A head, face, hand, shoulder, hip, knee, or neck plan needs construction review.
- A later failure appears to originate in anatomy or form design.

## Inputs

- `templates/review_report.md`
- `knowledge/anatomy/stylized_biped_proportions.md`
- `knowledge/anatomy/head_face_construction.md`
- `knowledge/anatomy/deformation_landmarks.md`
- `knowledge/style-library/heroic_stylized.md`
- `knowledge/critique-patterns/stylized_biped_review_failures.md`

## Required Output

Produce a `templates/review_report.md`-compatible report with:

- Proportion findings.
- Landmark findings.
- Construction-order findings.
- Deformation risk findings.
- Pose-risk notes.
- Decision: `approve`, `approve_with_notes`, `revise`, or `block`.

## Review Rules

- Judge anatomy relative to the chosen style, not realism alone.
- Do not approve detail when primary or secondary forms are unresolved.
- Treat shoulder, elbow, wrist, hip, knee, ankle, neck, jaw, mouth, and eyelid risks as future deformation risks.
- Route topology-specific issues to `topology-review`.
- If the problem belongs to an earlier stage, ask the Character Director for a revision task.
- During a validated Blender MCP `quick_iteration`, do not create a formal review report unless screenshots reveal a structural risk. Produce the formal anatomy report at `gate_review` after the regional iteration bundle.

## First Workflow

For `stylized_orc_bruiser`, use `references/stylized_biped_anatomy_review_rules.md` and `references/example_anatomy_review_report.md`.
