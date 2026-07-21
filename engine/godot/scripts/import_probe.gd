extends SceneTree

# Usage from a Godot project:
# godot --headless --script res://path/to/import_probe.gd -- --asset-id stylized_orc_bruiser --scene res://imports/character.glb --out user://godot_import_probe.json

func _initialize() -> void:
	var args := OS.get_cmdline_user_args()
	var asset_id := _arg_value(args, "--asset-id", "unknown_asset")
	var scene_path := _arg_value(args, "--scene", "")
	var out_path := _arg_value(args, "--out", "user://godot_import_probe.json")
	var result := {
		"asset_id": asset_id,
		"scene_path": scene_path,
		"import_succeeded": false,
		"scene_opens": false,
		"root_node_name": "",
		"mesh_instance_3d_count": 0,
		"skeleton_3d_count": 0,
		"animation_player_count": 0,
		"material_override_count": 0,
		"errors": []
	}
	if scene_path == "":
		result["errors"].append("Missing --scene path.")
		_write_json(out_path, result)
		quit(1)
		return
	var packed := load(scene_path)
	if packed == null or not packed is PackedScene:
		result["errors"].append("Scene could not be loaded as PackedScene.")
		_write_json(out_path, result)
		quit(1)
		return
	result["import_succeeded"] = true
	var root := packed.instantiate()
	if root == null:
		result["errors"].append("PackedScene could not instantiate.")
		_write_json(out_path, result)
		quit(1)
		return
	result["scene_opens"] = true
	result["root_node_name"] = root.name
	_count_nodes(root, result)
	root.free()
	_write_json(out_path, result)
	quit(0)


func _arg_value(args: PackedStringArray, key: String, default_value: String) -> String:
	for index in range(args.size()):
		if args[index] == key and index + 1 < args.size():
			return args[index + 1]
	return default_value


func _count_nodes(node: Node, result: Dictionary) -> void:
	if node is MeshInstance3D:
		result["mesh_instance_3d_count"] += 1
		var mesh_instance := node as MeshInstance3D
		if mesh_instance.material_override != null:
			result["material_override_count"] += 1
	if node is Skeleton3D:
		result["skeleton_3d_count"] += 1
	if node is AnimationPlayer:
		result["animation_player_count"] += 1
	for child in node.get_children():
		_count_nodes(child, result)


func _write_json(path: String, result: Dictionary) -> void:
	var file := FileAccess.open(path, FileAccess.WRITE)
	if file == null:
		push_error("Could not open output path: " + path)
		return
	file.store_string(JSON.stringify(result, "  "))
