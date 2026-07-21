# QA Scoring Rubric

The QA score helps prioritize revision work. It does not override hard failures. Any hard failure places the asset in `structural_rework` until fixed.

## Score Bands

| Band | Score | Meaning |
|---|---:|---|
| `ship_candidate` | 85-100 | Strong enough to proceed or ship for the declared scope, assuming no hard failures. |
| `targeted_revision` | 70-84 | Usable direction, but needs focused fixes before approval. |
| `structural_rework` | 0-69 | Core problems require substantial revision. |

## Weighted Categories

| Category | Weight | Score Represents |
|---|---:|---|
| Proportions and landmarks | 15 | Skeletal plausibility, age or species fit, center of mass, and major landmark placement. |
| Silhouette and readability | 10 | Recognition at distance, camera readability, pose clarity, and negative-space strength. |
| Anatomy or structural logic | 15 | Primary and secondary forms, believable attachments, facial construction, and creature logic where applicable. |
| Symmetry and intentional asymmetry | 5 | Accidental asymmetry caught and intentional asymmetry documented. |
| Topology and edge flow | 15 | Loops for eyes, mouth, shoulders, elbows, knees, hips, neck, fingers, and cloth. |
| UVs and baking readiness | 10 | UV legality, seam placement, texel strategy, and bake cleanliness. |
| Materials and texture logic | 10 | PBR or stylized consistency, channel validity, material separation, and storytelling. |
| Deformation readiness | 10 | Weight distribution, twist zones, correctives, and pose-test performance. |
| Performance and LODs | 5 | Budgets, material-slot discipline, and LOD or Godot scene-variant integrity. |
| Godot readiness | 5 | Godot import success, `Skeleton3D` and skin preservation, blend shapes where required, animation clips, material binding, texture references, and naming. |

## Category Scoring Guide

Use 0-10 for each category before applying weight.

| Raw Score | Meaning |
|---:|---|
| 10 | Excellent for the declared style, platform, and stage. |
| 8-9 | Strong with minor issues that do not threaten progression. |
| 6-7 | Acceptable direction but needs targeted revision. |
| 4-5 | Weak; progression is risky without revision. |
| 1-3 | Severe problems; likely structural rework. |
| 0 | Missing, unreviewable, or failed. |

## Calculation

Weighted contribution:

```text
(raw_category_score / 10) * category_weight
```

Total score:

```text
sum(weighted_contributions)
```

## Decision Rules

- `ship_candidate` requires a score of 85 or higher and no hard failures.
- `targeted_revision` requires a score from 70 to 84 and no hard failures.
- `structural_rework` applies below 70 or whenever hard failures are present.
- A category may receive a low score without blocking progression if no hard failure exists and the QA Auditor records the risk.
- The Character Director has final responsibility for deciding whether a non-blocking issue can be deferred.

## Phase 10 Evidence

Production-readiness categories should cite these reports when they are in scope:

- `UVs and baking readiness`: `templates/uv_bake_report.md` and `validate_uv_bake_readiness.py`.
- `Materials and texture logic`: `templates/material_texture_report.md` and `validate_texture_readiness.py`.
- `Performance and LODs`: `templates/optimization_report.md` and `validate_lod_readiness.py`.
- `Godot readiness`: export package evidence from optimization review until the Phase 11 Godot adapter exists.
