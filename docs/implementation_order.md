# Implementation Order for the AI Assisted Character Pipeline Framework

## Purpose

This document turns the blueprint in `docs/plan.md` into a build sequence. The goal is to avoid building the exciting parts first and ending up with an untestable pile of prompts, scripts, and half-connected tools.

The correct order is:

1. Define the pipeline contracts.
2. Build the repository skeleton and durable project rules.
3. Implement the director workflow.
4. Add specialist skills one at a time.
5. Add validators before automation gets ambitious.
6. Prove the system on one narrow vertical slice.
7. Expand stage coverage only after the loop is observable and repeatable.
8. Add Blender MCP and engine adapters behind explicit gates.

The system should be useful before it is complete. The first milestone is not a finished character generator. The first milestone is a reliable stage-gated review loop that can take a character brief through reference, blockout review, validation, and handoff without losing context or skipping approvals.

## Godot Target Assumptions

Targeting Godot does not change the character-production stages. It changes the engine adapter, export format, import checks, and runtime validation criteria.

The initial implementation should assume:

- Blender remains the primary DCC and automation target.
- Godot is the first supported engine.
- `glTF`/`GLB` is the default interchange format from Blender to Godot.
- Engine validation means opening and previewing the imported asset in a Godot project, not only exporting a file from Blender.
- The Godot adapter must check imported scene structure, `Skeleton3D`, skin weights, material resources, texture references, animation clips, blend shapes when used, collision or marker nodes when required, and preview-scene rendering.
- Unreal, Unity, MetaHuman, Control Rig, and humanoid-avatar assumptions are future adapter concerns, not part of the first build path.

## Build Principles

- Build contracts before capabilities.
- Keep each stage independently testable.
- Prefer small specialist skills over one large prompt.
- Make every handoff machine-readable.
- Add validators before adding destructive automation.
- Treat Blender and engine integrations as adapters, not the core system.
- Keep human approval gates mandatory until the workflow has proven itself.
- Use one target workflow first: stylized biped character for Blender, with Godot export deferred until the Blender loop is stable.

## Phase 0: Repository Foundation

### Objective

Create the project shape that every later phase will depend on.

### Build

Create the top-level structure:

```text
game-character-system/
├── AGENTS.md
├── CLAUDE.md
├── skills/
├── prompts/
├── knowledge/
├── workflows/
├── blender_scripts/
├── validators/
├── engine/
├── templates/
├── examples/
├── reports/
└── docs/
```

Inside `engine/`, create the first adapter folder: `godot/`. Inside `workflows/`, create the first workflow folder: `stylized-biped-godot/`.

### Deliverables

- Repository folders exist.
- `AGENTS.md` defines the non-negotiable production rules.
- `CLAUDE.md` mirrors equivalent durable guidance if Claude will be supported.
- `README.md` explains the project purpose, current status, and first supported workflow.
- `docs/glossary.md` defines pipeline terms such as stage, gate, artifact, validator, handoff, hard failure, and review loop.

### Exit Gate

Do not move on until the repo has a stable vocabulary and a durable rule file that says the system must advance one validated stage at a time.

## Phase 1: Pipeline Contracts

### Objective

Define the data contracts before writing any specialist skills or Blender scripts.

### Build

Create schema files or markdown templates for:

- Character brief.
- Reference record.
- Stage task card.
- Stage handoff.
- Review report.
- Validation report.
- QA audit report.
- Asset manifest.

Recommended folder:

```text
templates/
├── character_brief.md
├── reference_record.md
├── stage_task_card.md
├── stage_handoff.md
├── review_report.md
├── validation_report.md
├── qa_audit_report.md
└── asset_manifest.md
```

The stage task card should use this common schema:

```text
goal:
current_stage:
allowed_tools:
known_constraints:
input_refs:
output_contract:
acceptance_tests:
stop_conditions:
handoff_format:
```

The validation report should separate hard failures from weighted score issues. Hard failures block progression regardless of total score.

### Deliverables

- Template files for every major artifact.
- A documented stage list matching the production pipeline.
- A documented list of hard failures.
- A documented scoring rubric based on the plan.

### Exit Gate

Do not implement automation until a human can fill out the templates manually and the next stage would know exactly what input it received.

## Phase 2: Character Director Skill

### Objective

Build the orchestration layer first. The director owns stage order, gate checks, handoff completeness, and stop conditions.

### Build

Create:

```text
skills/character-director/
├── SKILL.md
├── references/
│   ├── stage_order.md
│   ├── hard_failures.md
│   └── handoff_rules.md
└── scripts/
```

The Character Director should be able to:

- Convert a raw character idea into a production brief.
- Select the current stage.
- Generate a stage task card.
- Check whether required inputs are missing.
- Stop at approval gates.
- Route work to the correct specialist.
- Reject attempts to skip topology, deformation, or engine validation.

### Deliverables

- `SKILL.md` with clear invocation rules.
- Stage order reference.
- Gate and hard-failure reference.
- Example task card for a stylized biped.

### Exit Gate

The director can take the prompt "stylized orc bruiser for a third-person game" and produce a complete brief plus the first stage task card without invoking Blender or specialist skills.

## Phase 3: Knowledge Base Skeleton

### Objective

Create a retrieval-ready knowledge structure, but keep the initial content small and high-signal.

### Build

Create:

```text
knowledge/
├── anatomy/
├── style-library/
├── topology/
├── rigging/
├── materials/
├── engine-standards/
├── critique-patterns/
└── examples/
```

Add metadata requirements to `knowledge/README.md`:

```text
domain:
body_region:
species:
sex_or_body_type:
age_band:
style_family:
deformation_criticality:
target_engine:
target_platform:
source_quality:
last_reviewed:
linked_docs:
```

Seed only the knowledge needed for the first workflow:

- Stylized biped proportion notes.
- Head and face construction notes.
- Shoulder, elbow, hip, knee, and neck deformation notes.
- Silhouette and gameplay readability notes.
- Basic topology loop notes for eyes, mouth, shoulders, elbows, knees, and hips.

### Deliverables

- Knowledge folder structure.
- Metadata rules.
- Minimal first-pass documents for stylized biped review.

### Exit Gate

Specialist skills can cite or load small, targeted knowledge files instead of relying on one giant background document.

## Phase 4: First Specialist Skills

### Objective

Add the minimum specialist set needed to review a pre-production character before any mesh automation exists.

### Build Order

1. `reference-librarian`
2. `style-keeper`
3. `anatomy-review`
4. `qa-audit`

Recommended structure:

```text
skills/
├── reference-librarian/
├── style-keeper/
├── anatomy-review/
└── qa-audit/
```

The Reference Librarian should produce reference requirements and metadata checks. It does not need web access for the first version; it can operate on local reference records.

The Style Keeper should enforce style-family rules as controlled dials: proportion, plane simplification, feature emphasis, material treatment, and detail frequency.

The Anatomy Reviewer should review proportions, landmarks, asymmetry, construction order, and pose risks.

The QA Auditor should aggregate reports and distinguish hard failures from weighted scoring issues.

### Deliverables

- Four specialist skills.
- One sample report from each specialist.
- One combined QA audit report.

### Exit Gate

The director can route a stylized biped concept through brief creation, reference requirements, style review, anatomy review, and QA summary without any Blender automation.

## Phase 5: Manual Vertical Slice

### Objective

Prove the workflow manually before connecting external tools.

### Build

Create one example project:

```text
examples/stylized_orc_bruiser/
├── brief.md
├── references/
├── task_cards/
├── handoffs/
├── reviews/
├── validations/
└── audit.md
```

Run the workflow by hand:

1. Character Director creates the brief.
2. Reference Librarian defines required reference coverage.
3. Style Keeper sets style constraints.
4. Anatomy Reviewer reviews the proportion and blockout plan.
5. QA Auditor produces the first audit.
6. Human approval gate decides whether to proceed.

### Deliverables

- A complete example folder.
- Filled templates for the first stages.
- A visible decision trail from idea to approved blockout plan.

### Exit Gate

A new user can inspect the example and understand what each stage consumed, produced, approved, or rejected.

## Phase 6: Core Validators Without Blender MCP

### Objective

Build validators as local scripts before letting an agent control Blender interactively.

### Build

Create:

```text
validators/
├── README.md
├── validate_manifest.py
├── validate_stage_handoff.py
├── validate_review_report.py
├── validate_qa_audit.py
└── rules/
```

Start with document and manifest validation:

- Required fields exist.
- Stage names are valid.
- Handoff source and target stages match.
- Hard failures are explicit.
- QA scores add up correctly.
- Asset manifest references existing files.

Then add Blender-file-adjacent validators that can operate on exported data or generated reports:

- Polycount report parser.
- Material-slot report parser.
- Naming report parser.
- Screenshot manifest checker.

### Deliverables

- CLI validation scripts.
- Example passing reports.
- Example failing reports.
- Documentation showing how to run validation.

### Exit Gate

The QA Auditor can consume validator output instead of relying only on narrative review.

## Phase 7: Blender Script Pack

### Objective

Add controlled Blender automation as scripts that can be run intentionally, reviewed, and tested.

### Build

Create:

```text
blender_scripts/
├── README.md
├── mesh_report.py
├── scene_report.py
├── naming_report.py
├── material_report.py
├── screenshot_set.py
├── pose_battery.py
└── export_package.py
```

Start with read-only reporting scripts:

1. Scene report.
2. Mesh geometry report.
3. Polycount and material-slot report.
4. Naming and transform report.
5. Screenshot set generation.

Only after reporting is stable should you add controlled cleanup operations such as merge-by-distance or unused data-block removal.

### Deliverables

- Blender scripts that generate JSON or markdown reports.
- A screenshot manifest format.
- Sample reports committed under the example project.

### Exit Gate

The system can open or process a Blender character file, produce reports and screenshots, and feed those reports into QA without modifying the source file.

## Phase 8: Topology and Rigging Specialists

### Objective

Add the specialists whose reviews depend on mesh and deformation reports.

### Build

Create:

```text
skills/topology-review/
skills/rigging-review/
```

The Topology Reviewer should evaluate:

- Edge flow around eyes, mouth, shoulders, elbows, hips, knees, neck, fingers, and cloth.
- Pole placement.
- Triangle hot spots.
- Loop density by deformation zone.
- Bake readiness risks.

The Rigging Reviewer should evaluate:

- Skeleton naming.
- Joint placement.
- Max influences per vertex.
- Unweighted vertices.
- Twist zones.
- Corrective shape needs.
- Pose battery results.

### Deliverables

- Topology review skill.
- Rigging review skill.
- Report templates for topology and deformation.
- Example reviews against the stylized orc project.

### Exit Gate

The director can block progression when topology or deformation reports show hard failures.

## Phase 9: Bounded Blender MCP Loop

### Objective

Connect MCP only after the workflow, validators, and Blender reports are already useful.

### Build

Implement a strict operating policy:

- One bounded microtask per MCP loop.
- No broad "finish the character" instructions.
- Screenshot after every meaningful structural change.
- Validator run before the next modeling pass.
- Source files are copied before modification.
- Destructive operations require explicit approval.
- Every MCP action is logged.

Recommended loop:

1. Director selects one microtask.
2. Specialist defines acceptance tests.
3. Blender MCP executes a short edit burst.
4. Screenshot set is captured.
5. Validators run.
6. Specialist reviews output.
7. QA Auditor scores result.
8. Human approves, rejects, or requests revision.

### Deliverables

- MCP usage policy.
- Action log format.
- One successful microtask example.
- One rollback or rejected-change example.

### Exit Gate

The MCP loop can make a small, reviewable change without damaging source assets or bypassing approval.

## Phase 10: Materials, UV, Baking, and Optimization

### Objective

Expand from form and deformation into production-readiness.

### Build

Add or extend skills:

```text
skills/materials-review/
skills/uv-bake-review/
skills/optimization-review/
```

Add validators for:

- Missing UVs.
- UV overlaps where disallowed.
- Texture naming and size.
- Material slot count.
- Channel packing rules.
- LOD naming.
- LOD polycount budgets.
- Godot export texture paths.
- `glTF`/`GLB` package completeness.

### Deliverables

- Review skills for UVs, baking, materials, and optimization.
- Validation reports for texture and LOD readiness.
- Updated QA rubric that includes these reports.

### Exit Gate

The example character can pass from approved mesh to texture and LOD readiness without relying on subjective visual review alone.

## Phase 11: Engine Export Adapters

### Objective

Treat Godot readiness as a first-class validation stage.

### Build

Create:

```text
engine/
└── godot/
    ├── README.md
    ├── import_checklist.md
    ├── validation_report.md
    ├── preview_scene_checklist.md
    └── scripts/
```

Godot should be the first and primary engine adapter. Unreal, Unity, and other engines should be treated as future adapters, not as requirements for the initial build.

The default interchange target should be `glTF`/`GLB` from Blender unless a specific Godot project requirement proves that another format is better. The exporter should preserve scale, object names, material assignments, skeleton hierarchy, skin weights, animations, shape keys when needed, and texture references.

The adapter should validate:

- Import succeeds.
- The imported scene opens cleanly in Godot.
- Skeleton, `Skeleton3D`, skin weights, and bone names are present when expected.
- Meshes, surfaces, and material slots match the asset manifest.
- Materials bind to the expected imported resources or project material overrides.
- Textures are present, correctly referenced, and imported with expected flags.
- Animation clips import and can play through the preview scene.
- Shape keys or blend shapes import when expected.
- LOD policy is documented, even if the first Godot workflow uses manual LOD scenes rather than engine-side automatic LOD.
- Collision, attachment sockets, hitboxes, or marker nodes exist when required by the game.
- Preview scene renders under known lighting and camera distance.
- Test animation or pose preview works.

### Deliverables

- Godot adapter.
- Godot import checklist.
- Godot preview scene checklist.
- Godot validation report.
- Example successful `GLB` or `glTF` import package.

### Exit Gate

The framework can prove that an asset is Godot-ready, not merely Blender-ready.

## Phase 12: Full Stylized Biped Workflow

### Objective

Run the first complete workflow from prompt to Godot validation.

### Build

Use `examples/stylized_orc_bruiser/` as the acceptance project.

Required stages:

1. Concept interpretation.
2. Reference gathering.
3. Proportion planning.
4. Blockout.
5. Primary forms.
6. Secondary anatomy.
7. Tertiary detail.
8. Clothing, hard surface, and hair.
9. Retopology.
10. UVs and baking.
11. Texturing and materials.
12. Rigging and skinning.
13. Deformation testing.
14. Optimization and LODs.
15. Export and engine validation.

### Deliverables

- Complete stage history.
- All task cards and handoffs.
- All specialist reviews.
- All validation reports.
- Final QA audit.
- Godot validation report.

### Exit Gate

The workflow is considered complete only when every stage has an artifact, every handoff is explicit, hard failures are absent, and the final package imports and previews correctly in Godot.

## Phase 13: Second Workflow

### Objective

Prove the framework generalizes without rewriting the core.

### Build

Choose one second workflow:

- Realistic biped.
- Creature biped.
- Quadruped.
- Low-poly mobile character.

Add only the knowledge, validators, and specialist rules required by that workflow. Do not rewrite the director unless the stage contract itself is wrong.

### Deliverables

- New workflow folder.
- Workflow-specific knowledge files.
- One example project.
- Delta notes explaining what changed from stylized biped.

### Exit Gate

The second workflow should reuse the director, task cards, handoffs, QA audit format, and validator interfaces.

## Recommended First Milestone

The first useful milestone should be:

```text
Milestone 1: Manual stage-gated pre-production workflow
```

Scope:

- Repo foundation.
- Pipeline templates.
- Character Director skill.
- Reference Librarian skill.
- Style Keeper skill.
- Anatomy Reviewer skill.
- QA Auditor skill.
- Stylized orc example through approved blockout plan.

Do not include Blender MCP in Milestone 1. The goal is to prove the workflow brain before adding tool hands.

## Recommended Second Milestone

```text
Milestone 2: Validator-backed Blender reporting
```

Scope:

- Document validators.
- Asset manifest validators.
- Read-only Blender report scripts.
- Screenshot set generation.
- QA audit consuming script outputs.

This milestone proves observability. The system should be able to say what exists, what is missing, and what blocks progression.

## Recommended Third Milestone

```text
Milestone 3: Bounded Blender edit loop
```

Scope:

- Blender MCP policy.
- Microtask execution loop.
- Action logs.
- Source-file backup rule.
- Screenshot and validation after each meaningful edit.
- One approved microtask and one rejected microtask.

This milestone proves controlled automation. It should still be narrow.

## Recommended Fourth Milestone

```text
Milestone 4: Full character asset pipeline
```

Scope:

- Topology, rigging, UV, material, optimization, and Godot export specialists.
- Full stylized biped workflow.
- Godot adapter.
- Final QA audit with hard-failure blocking.

This is the first point where the system can honestly claim to produce or supervise a game-ready character asset.

## Dependency Map

| Build Item | Depends On | Should Not Depend On |
|---|---|---|
| Repository foundation | Nothing | Blender MCP |
| Pipeline templates | Repository foundation | Specialist skills |
| Character Director | Pipeline templates | Blender automation |
| Knowledge skeleton | Repository foundation | Full knowledge library |
| Reference, style, anatomy skills | Director and templates | Mesh validators |
| QA Auditor | Review and validation templates | Engine adapters |
| Document validators | Templates | Blender MCP |
| Blender report scripts | Validator format | Blender MCP edit permissions |
| Topology and rigging skills | Blender reports | Engine import |
| Blender MCP loop | Director, validators, reports | Engine adapters |
| Materials and optimization | Mesh and manifest reports | Second workflow |
| Godot adapter | Export package format | Multiple engines |
| Second workflow | Completed first workflow | Rewriting the core |

## Things to Delay

Delay these until the core loop works:

- Multi-engine support.
- MetaHuman integration.
- Marvelous Designer integration.
- Substance Painter automation.
- Houdini procedural generation.
- Photogrammetry cleanup.
- NPC batch generation.
- Large-scale retrieval infrastructure.
- Fully automated character creation.

Each of these should eventually plug into the same stage contracts, validator hooks, artifact manifests, and approval gates.

## Definition of Done

The framework is working when:

- A raw idea becomes a structured character brief.
- Every stage has a task card and handoff.
- Specialist reviews stay inside their domain.
- Validators produce machine-readable reports.
- Hard failures block progression.
- Blender automation is bounded, logged, and reversible.
- Screenshots and reports exist for meaningful asset changes.
- QA can explain both score and blocking issues.
- Godot validation proves the asset works outside Blender.
- A second workflow can be added without redesigning the system.

The end state is not a magic character generator. The end state is a production framework where AI workers can help advance a character asset one validated stage at a time.
