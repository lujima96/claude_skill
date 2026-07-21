# Stage Order

This reference defines the Director's default routing for the first workflow: stylized biped character, Blender source, Godot target, `GLB`/`glTF` interchange.

| Order | Stage ID | Required Inputs | Required Outputs | Primary Specialist |
|---:|---|---|---|---|
| 1 | `concept_interpretation` | Raw idea, known game constraints | Character brief | Character Director |
| 2 | `reference_gathering` | Approved or draft brief | Reference records and coverage summary | Reference Librarian |
| 3 | `proportion_planning` | Brief, reference records, style constraints | Proportion plan or mannequin plan | Anatomy Reviewer |
| 4 | `blockout` | Proportion plan, references | Blockout artifacts and silhouette screenshots | Anatomy Reviewer, Style Keeper |
| 5 | `primary_forms` | Approved blockout | Primary-form sculpt and review screenshots | Anatomy Reviewer |
| 6 | `secondary_anatomy` | Approved primary forms | Secondary-form sculpt and anatomy review | Anatomy Reviewer |
| 7 | `tertiary_detail` | Approved secondary anatomy | High-resolution detail pass | Anatomy Reviewer, Style Keeper |
| 8 | `clothing_hardsurface_hair` | Approved body forms, costume refs | Costume, gear, hair plan or sculpt | Style Keeper, Anatomy Reviewer |
| 9 | `retopology` | Approved high-resolution sculpt | Deformation-ready game mesh | Topology Reviewer |
| 10 | `uvs_and_baking` | Final game mesh, high-resolution source | UVs and baked maps | UV Bake Reviewer |
| 11 | `texturing_materials` | UVs, bakes, material IDs | Texture sets and material definitions | Materials Reviewer |
| 12 | `rigging_skinning` | Game mesh, skeleton spec, facial spec | Rigged and weighted character | Rigging Reviewer |
| 13 | `deformation_testing` | Rigged character, pose library | Deformation report and corrective list | Rigging Reviewer |
| 14 | `optimization_lods` | Approved LOD0, platform budgets | LOD chain or Godot scene-variant policy | Optimization Reviewer |
| 15 | `export_godot_validation` | Export package, textures, animations | Godot import package and validation log | Godot Export Reviewer |

## Stage Selection

- If no character brief exists, select `concept_interpretation`.
- If a brief exists but is not approved, continue `concept_interpretation`.
- If the latest handoff is approved, select its `to_stage`.
- If the latest QA audit says `revise_current_stage`, stay on the same stage.
- If the latest QA audit says `return_to_previous_stage`, create a revision task for the named previous stage.
- If hard failures are present, select the stage responsible for fixing the hard failure.

## Routing Constraints

- Do not route Blender MCP work before `blockout`.
- Do not route topology work before the sculpt stages are approved unless creating a planning note.
- Do not route rigging work before retopology is approved unless creating skeleton requirements.
- Do not route Godot validation before export artifacts exist.
- Do not mark an asset complete before `export_godot_validation` passes.
