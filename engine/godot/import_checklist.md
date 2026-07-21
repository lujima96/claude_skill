# Godot Import Checklist

Use this checklist for `export_godot_validation`.

## Package

- `GLB` or `glTF` package exists.
- Exported package path is listed in the asset manifest.
- Package opens in Godot without import errors.
- Texture paths resolve from the Godot project or import package.
- Scale and orientation match the project convention.
- Object and mesh names are stable after import.

## Scene Structure

- Imported root node is named as expected.
- Mesh nodes are present.
- Surface and material slot counts match the manifest.
- Required marker, socket, hitbox, or collision nodes exist.
- LOD policy is documented, even when LODs are separate scenes.

## Rig And Animation

- `Skeleton3D` exists when the asset is skinned.
- Bone names remain stable after import.
- Skin weights survive import.
- Max influence policy is respected.
- Required animation clips import.
- Required clips can play in the preview scene.
- Blend shapes import when required.

## Materials And Textures

- Imported materials bind to the expected resources or documented overrides.
- Texture resources exist.
- Texture import flags match project expectations.
- Alpha materials have explicit handling.
- Normal, roughness, metallic, AO, and packed maps are interpreted correctly.

## Preview

- Preview scene opens.
- Character renders under known light and camera distance.
- Pose or test animation can be viewed.
- No blocking visual, material, rig, or missing-resource errors appear.
