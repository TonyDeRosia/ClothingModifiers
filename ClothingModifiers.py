bl_info = {
    "name": "Clothing Modifiers",
    "author": "Tony DeRosia",
    "version": (1, 0),
    "blender": (4, 0, 2),
    "description": "Adds and applies clothing modifiers. Use at your own risk!",
    "category": "Object",
}

import bpy

class AddClothingModifiers(bpy.types.Operator):
    """Add clothing modifiers to the selected object"""
    bl_idname = "object.add_clothing_modifiers"
    bl_label = "Add Clothing Modifiers"

    def execute(self, context):
        obj = context.active_object
        if obj is not None and obj.type == 'MESH':
            # Add Shrinkwrap modifier
            obj.modifiers.new(name="Shrinkwrap", type='SHRINKWRAP')

            # Add Subdivision modifier
            subdivision_modifier = obj.modifiers.new(name="Subdivision", type='SUBSURF')
            subdivision_modifier.levels = 2

            # Add Solidify modifier
            solidify_modifier = obj.modifiers.new(name="Solidify", type='SOLIDIFY')
            solidify_modifier.thickness = 0.01

            # Add Multiresolution modifier and subdivide twice
            multires_modifier = obj.modifiers.new(name="Multiresolution", type='MULTIRES')
            bpy.ops.object.multires_subdivide(modifier="Multiresolution")
            bpy.ops.object.multires_subdivide(modifier="Multiresolution")
        return {'FINISHED'}

class ApplyModifiers(bpy.types.Operator):
    """Apply all modifiers to the selected object"""
    bl_idname = "object.apply_modifiers"
    bl_label = "Apply Modifiers"

    def execute(self, context):
        obj = context.active_object
        if obj is not None and obj.type == 'MESH':
            for modifier in obj.modifiers:
                bpy.ops.object.modifier_apply(modifier=modifier.name)
        return {'FINISHED'}

class ClothingModifierPanel(bpy.types.Panel):
    """Creates a Panel for Clothing Modifiers"""
    bl_label = "Clothing Modifier"
    bl_idname = "SCENE_PT_clothing_modifier"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "scene"

    def draw(self, context):
        layout = self.layout
        layout.operator(AddClothingModifiers.bl_idname)
        layout.operator(ApplyModifiers.bl_idname)

def register():
    bpy.utils.register_class(AddClothingModifiers)
    bpy.utils.register_class(ApplyModifiers)
    bpy.utils.register_class(ClothingModifierPanel)

def unregister():
    bpy.utils.unregister_class(ClothingModifierPanel)
    bpy.utils.unregister_class(ApplyModifiers)
    bpy.utils.unregister_class(AddClothingModifiers)

if __name__ == "__main__":
    register()