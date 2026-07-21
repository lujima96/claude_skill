# Example Stylized Biped Brief

This example shows the kind of brief the Character Director should produce from: "stylized orc bruiser for a third-person game."

## Metadata

- `brief_id`: stylized_orc_bruiser-brief-001
- `character_name`: Stylized Orc Bruiser
- `created_by`: Character Director
- `created_at`: TBD
- `last_updated`: TBD
- `status`: draft
- `current_stage`: concept_interpretation

## Source Request

- `raw_prompt`: stylized orc bruiser for a third-person game
- `user_goals`: create a production-ready character pipeline brief for a Godot-targeted stylized biped
- `non_goals`: no sculpting, retopology, rigging, texturing, Blender MCP work, or Godot import work in this stage
- `open_questions`: target Godot version; target platform; poly budget; material slot budget; texture resolution; skeleton spec; animation list; facial animation needs; collision or attachment marker requirements

## Production Target

- `target_engine`: Godot
- `target_godot_version`: unknown
- `primary_dcc`: Blender
- `default_interchange_format`: GLB
- `target_platform`: unknown
- `camera_context`: third_person
- `expected_screen_size`: gameplay-distance readability required; exact screen size unknown

## Character Intent

- `role`: bruiser enemy or playable heavy archetype
- `narrative_function`: physically imposing fantasy combatant with readable strength and aggression
- `gameplay_function`: close-range melee threat with strong silhouette and readable attack poses
- `species`: orc
- `age_band`: adult
- `sex_or_body_type`: broad, muscular humanoid body type
- `body_type`: heroic stylized heavy build
- `personality_keywords`: intimidating, durable, blunt, aggressive, battle-worn
- `silhouette_priorities`: broad shoulders, thick neck, heavy jaw, large hands, strong forearms, readable tusks, clear weapon or gear profile if included

## Style Contract

- `style_family`: heroic_stylized
- `style_references`: pending reference gathering
- `proportion_rules`: exaggerate upper body mass while preserving pelvis, shoulder, elbow, wrist, hip, knee, neck, jaw, eyelid, and mouth deformation logic
- `shape_language`: large simple primary masses, angular jaw and brow, powerful taper from shoulders to waist, chunky hands and gear
- `detail_frequency`: low-to-medium until primary and secondary forms are approved; tertiary noise deferred
- `material_treatment`: readable leather, metal, cloth, skin, and hair material families under Godot lighting
- `color_readability_rules`: strong value separation between skin, armor, cloth, and weapon or gear silhouettes

## Asset Scope

- `required_body_regions`: full biped body, head, neck, torso, arms, hands, pelvis, legs, feet, eyes, mouth, nose, ears or orc ear variant
- `clothing_and_gear`: shoulder armor, bracers, belt kit, simple cloth or leather elements; exact gear pending references
- `hair_strategy`: sculpted or cards, pending style and platform constraints
- `facial_animation_required`: unknown
- `blend_shapes_required`: unknown
- `animation_requirements`: idle, locomotion, attack, hit reaction, and pose tests likely required; exact list unknown
- `collision_or_marker_requirements`: unknown

## Technical Budgets

- `poly_budget_lod0`: unknown
- `lod_count_target`: unknown
- `texture_sets`: unknown
- `texture_resolution_target`: unknown
- `material_slot_budget`: unknown
- `max_skin_influences`: unknown
- `skeleton_spec`: unknown

## Required Deliverables

- `source_blend`: required later
- `export_package`: `GLB` or `glTF` package required later
- `godot_import_package`: required later
- `screenshots`: required from blockout onward
- `validation_reports`: required once validators exist
- `qa_audit`: required at stage gates

## Acceptance Criteria

- `brief_completeness`: draft is usable for reference gathering; technical unknowns are clearly listed
- `style_readability`: heroic stylized fantasy direction is defined
- `production_constraints_defined`: Godot and Blender path defined; budgets remain blocking questions for later production stages
- `godot_target_defined`: yes
- `approval_required_from`: human art director or user

## Handoff

- `next_stage`: reference_gathering
- `handoff_summary`: gather references for orc silhouette, heroic stylized proportions, tusk and jaw construction, heavy neck and shoulder anatomy, hands, leather/metal/cloth material families, and Godot-friendly hair or card strategies
- `blocking_issues`: target platform, Godot version, budgets, skeleton spec, facial animation needs, and animation list must be answered before later production approval
- `approved_by`:
- `approved_at`:
