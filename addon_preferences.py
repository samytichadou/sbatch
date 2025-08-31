import bpy
import os

from .properties import SBATCH_PR_sbatch_preset

def sbatch_items_callback(self, context):
    items = []
    coll = self.sbatchs
    for s in coll:
        items.append(
            (s.name, s.name, ""),
        )
    return items

class SBATCH_UL_batch_entries(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        icon2="NOT_FOUND"

        if item.entry_type == "FILE":
            prop="filepath"
            icon="FILE"
            if os.path.isfile(item.filepath):
                if item.filepath.endswith(".blend"):
                    icon2=None
        else:
            prop="folderpath"
            icon="FILE_FOLDER"
            if os.path.isdir(item.folderpath):
                icon2=None

        layout.label(text="", icon=icon)
        layout.prop(item, prop, text="")
        if icon2 is not None:
            layout.label(text="", icon=icon2)

class SBATCH_PF_addon_prefs(bpy.types.AddonPreferences) :
    bl_idname = __package__

    sbatchs: bpy.props.CollectionProperty(
        type = SBATCH_PR_sbatch_preset,
        name="SBatch Presets",
    )
    sbatchs_enum: bpy.props.EnumProperty(
        name = "Sbatch Presets",
        items = sbatch_items_callback,
    )

    def draw(self, context) :
        layout = self.layout
        layout.prop(self, "sbatchs_enum", text="")
        current = self.sbatchs[self.sbatchs_enum]
        layout.template_list(
            "SBATCH_UL_batch_entries",
            "",
            current,
            "entries",
            current,
            "entry_index",
            rows=5,
        )


# get addon preferences
def get_addon_preferences():
    addon = bpy.context.preferences.addons.get(__package__)
    return getattr(addon, "preferences", None)


### REGISTER ---
def register():
    bpy.utils.register_class(SBATCH_UL_batch_entries)
    bpy.utils.register_class(SBATCH_PF_addon_prefs)

def unregister():
    bpy.utils.unregister_class(SBATCH_UL_batch_entries)
    bpy.utils.unregister_class(SBATCH_PF_addon_prefs)
