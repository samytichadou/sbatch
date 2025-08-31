import bpy
import os
import subprocess

# "blender --background --python script1.py --python script2.py"

def get_blend_files_from_folder(
    folderpath,
    recursive,
    include_pattern,
    exclude_pattern,
):
    blend_files = []
    return blend_files

def launch_command(
    executable,
    blend_file,
    scripts_list,
):
    cmd = f"{executable} --background"
    for script in scripts_list:
        cmd += f" --python {script}"

    subprocess.run(cmd)


class SBATCH_PR_execute_sbatch_preset(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "sbatch.execute_sbatch_preset"
    bl_label = "Execute Preset"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        addon = context.preferences.addons['bl_ext.user_default.sbatch'].preferences
        current_preset = addon.sbatchs[addon.sbatchs_enum]
        return {'FINISHED'}
