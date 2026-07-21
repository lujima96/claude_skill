# Pipeline Stage List

This is the canonical stage order for the first supported workflow: a stylized biped character built in Blender and validated for Godot.

Stages must run in order unless the Character Director explicitly creates a revision task that returns to an earlier stage.

| Stage ID | Stage Name | Primary Output | Required Gate |
|---|---|---|---|
| `concept_interpretation` | Concept interpretation | Character brief | Brief defines role, style, Godot target, platform, budgets, rig needs, and deliverables. |
| `reference_gathering` | Reference gathering | Curated reference records | References are classified, useful, non-contradictory, and sufficient for the next stage. |
| `proportion_planning` | Proportion planning | Proportion sheet or mannequin plan | Landmark proportions, stance, and silhouette intent are approved. |
| `blockout` | Blockout | Big-form blockout | Primary silhouette reads from front, side, back, 3/4, and gameplay distance. |
| `primary_forms` | Primary forms | Primary-form sculpt | Torso, pelvis, skull, limbs, and major masses are structurally sound. |
| `secondary_anatomy` | Secondary anatomy | Secondary-form sculpt | Muscles, fat, tension, and creature variations support the style without breaking structure. |
| `tertiary_detail` | Tertiary detail | High-resolution detail pass | Detail supports scale and material story without hiding landmarks or silhouette. |
| `clothing_hardsurface_hair` | Clothing, hard surface, and hair | Costume, gear, hair plan or production sculpt | Attachments, intersections, material IDs, hair strategy, and deformation zones are reviewable. |
| `retopology` | Retopology | Deformation-ready game mesh | Geometry is legal, edge flow supports deformation, and critical loops are present. |
| `uvs_and_baking` | UVs and baking | UV sets and baked utility maps | UVs, padding, seams, cages, and bakes are clean enough for texture work. |
| `texturing_materials` | Texturing and materials | Texture sets and material definitions | Materials are readable, correctly named, and compatible with the Godot export path. |
| `rigging_skinning` | Rigging and skinning | Rigged and weighted character | Skeleton, weights, influences, blend shapes, and required controls are present. |
| `deformation_testing` | Deformation testing | Pose battery report and corrective list | Critical joints, face shapes, and twist zones survive the pose tests. |
| `optimization_lods` | Optimization and LODs | LOD chain or documented Godot scene variants | Budgets, material slots, naming, and silhouette preservation are acceptable. |
| `export_godot_validation` | Export and Godot validation | Godot import package and validation log | The asset imports, previews, animates, and binds materials correctly in Godot. |

## Revision Rules

- A stage may return to an earlier stage only through a revision task card.
- A hard failure always blocks forward progression.
- Review notes may be deferred only if the QA audit records the risk and the next stage can safely proceed.
- Godot validation is required before any asset is considered done.
