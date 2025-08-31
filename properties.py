import bpy


class SBATCH_PR_script_entry(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(
        name = "Script Name",
    )
    filepath: bpy.props.StringProperty(
        name = "Script Path",
        subtype = "FILE_PATH",
    )

class SBATCH_PR_batch_entry(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(
    )
    entry_type: bpy.props.EnumProperty(
        name = "Entry Type",
        items = (
            ('FILE', "File", ""),
            ('FOLDER', "Folder", ""),
        ),
    )
    filepath: bpy.props.StringProperty(
        name = "File Path",
        subtype = "FILE_PATH",
    )
    folderpath: bpy.props.StringProperty(
        name = "Folder Path",
        subtype = "DIR_PATH",
    )

class SBATCH_PR_sbatch_preset(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(
    )
    scripts: bpy.props.CollectionProperty(
        type = SBATCH_PR_script_entry,
        name="Entries",
    )
    script_index: bpy.props.IntProperty(default = -1, min = -1)
    entries: bpy.props.CollectionProperty(
        type = SBATCH_PR_batch_entry,
        name="Entries",
    )
    entry_index: bpy.props.IntProperty(default = -1, min = -1)
    save_after: bpy.props.BoolProperty(
        name = "Save File",
        description = "Save file after scripts execution"),
        default = True,
    )
    custom_executable: bpy.props.StringProperty(
        name = "Custom Blender Executable",
        subtype = "FILE_PATH",
    )


### REGISTER ---
def register():
    bpy.utils.register_class(SBATCH_PR_script_entry)
    bpy.utils.register_class(SBATCH_PR_batch_entry)
    bpy.utils.register_class(SBATCH_PR_sbatch_preset)

def unregister():
    bpy.utils.unregister_class(SBATCH_PR_script_entry)
    bpy.utils.unregister_class(SBATCH_PR_batch_entry)
    bpy.utils.unregister_class(SBATCH_PR_sbatch_preset)
