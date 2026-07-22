# Hard Failures

Hard failures block progression regardless of weighted QA score. A hard failure must be fixed or explicitly converted into a scoped revision task by the Character Director.

## Global Hard Failures

- Missing character brief after `concept_interpretation`.
- Missing stage task card for the current stage.
- Missing stage handoff before starting the next stage.
- Missing required artifact listed in the task card.
- Missing validation report for a required validator.
- Any artifact path in the asset manifest points to a missing file.
- A specialist reports a critical issue inside the current stage scope.
- Human approval is required but absent.
- The stage attempts to skip topology, rigging, deformation, or Godot validation.
- Blender MCP execution starts without a validated current-stage authorization envelope and an exact runtime target receipt, compatible capability preflight, isolated workspace, or verified source-protection receipt. A schema-0.3 active-session task card plus its hash-chained iteration record satisfies the task-card requirement; legacy task cards remain valid.
- Blender MCP evidence claims screenshots or reports that are missing, invalid, or inconsistent with the protected working file.
- A Blender MCP loop changes the source `.blend` or operates outside its named targets and allowed change types.

## Concept and Reference Hard Failures

- Target engine is not set to Godot or explicitly documented as engine-agnostic pre-production.
- Target platform, camera context, or style family is unknown after brief approval.
- Poly, material, texture, skeleton, or animation requirements are missing when they affect later stages.
- Reference set is contradictory without a documented decision.
- Reference records are missing source or usage notes.

## Form and Anatomy Hard Failures

- Proportion plan lacks front, side, or 3/4 evaluation.
- Character silhouette fails the required gameplay-distance read.
- Primary forms contain unresolved structural defects in skull, torso, pelvis, limbs, hands, or feet.
- Deformation-critical landmarks are missing or misplaced in a way that affects rigging.
- Tertiary detail is added before primary and secondary forms are approved.

## Mesh and Topology Hard Failures

- Mesh has invalid geometry that blocks export, bake, or import.
- Non-manifold geometry exists where manifold geometry is required.
- Critical deformation loops are missing around eyes, mouth, shoulders, elbows, hips, knees, neck, fingers, or cloth bend zones.
- Pole or triangle placement creates visible or predictable deformation failure in a critical zone.
- Mesh density is so uneven that baking, weighting, or LOD work cannot proceed.
- Retopology is approved only for still images rather than deformation.

## UV, Bake, Material, and Texture Hard Failures

- Required UV set is missing.
- UV overlap exists where overlap is disallowed.
- Padding is insufficient for the declared texture resolution and mip usage.
- Bake artifacts obscure deformation-critical or high-visibility areas.
- Required texture files are missing.
- Material slots exceed the declared budget without approval.
- Texture or material naming prevents reliable Godot import or binding.

## Rigging and Deformation Hard Failures

- Required skeleton is missing.
- Bone naming does not match the project skeleton spec.
- Joint placement causes immediate pose-test failure.
- Vertices are unweighted.
- Skin influences exceed the declared maximum.
- Required blend shapes are missing.
- Shoulder, elbow, wrist, hip, knee, neck, jaw, eyelid, lip, or twist-zone tests fail in a way that cannot be deferred safely.

## Optimization and LOD Hard Failures

- LOD0 exceeds the approved performance budget without explicit approval.
- LOD or Godot scene-variant policy is missing when required by the target platform.
- Lower LODs destroy primary silhouette or face readability.
- Material or draw-call count exceeds budget without a recorded exception.

## Godot Export Hard Failures

- `GLB` or `glTF` package is missing or incomplete.
- Godot import fails.
- Imported scene cannot open in the target Godot project.
- Expected `Skeleton3D` hierarchy is missing.
- Skin weights do not survive import.
- Materials or textures are missing after import.
- Required animation clips do not import or cannot play in the preview scene.
- Required blend shapes do not import.
- Required collision, hitbox, attachment, or marker nodes are missing.
- Preview scene cannot render the asset under known lighting.
