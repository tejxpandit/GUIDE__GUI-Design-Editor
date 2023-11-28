# Title : GUI Designer : Component Class (Inheritance Parent for all Components)
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Nov, 2023

import dearpygui.dearpygui as dpg

class Component:
    def __init__(self, callback, parent):

        # Identifiers
        self.classname = "Component"
        self.tag = dpg.generate_uuid()
        self.label = self.classname + " " + str(self.tag)
        self.parent = None
        self.children = []

        # Objects
        self.panels = None
        self.components = None
        self.component_manager = None
        self.parent_panel = None
        self.editor_panel = None

        # Parameters
        self.position = None
        self.width = None
        self.height = None

        # Functions
        self.callback = None
        self.edit_callback = None

        # Theme
        self.color_background = None
        self.color_title = None
        self.color_title_active = None
        self.color_text = None

        # Initialize
        self.add()

    def initialize(self, panels, components, component_manager, parent_panel, editor_panel):
        self.panels = panels
        self.components = components
        self.component_manager = component_manager
        self.parent_panel = parent_panel
        self.editor_panel = editor_panel
    
    def add(self):
        pass

    def restore(self):
        self.add()
        for child in self.children:
            self.panels.get(child).restore()

    def update_panel_data(self):
        self.position = dpg.get_item_pos(self.tag)
        self.width = dpg.get_item_width(self.tag)
        self.height = dpg.get_item_height(self.tag)

    def update(self):
        self.update_panel_data()
        dpg.delete_item(self.parent_panel)
        self.restore(self.parent_panel)

    def delete_parent_relation(self):
        if self.parent != None:
            if self.parent in self.panels:
                self.panels.get(self.parent).children.remove(self.tag)
                self.component_manager.set_active_panel_callback(self.parent, 0)
            elif self.parent in self.components:
                self.components.get(self.parent).children.remove(self.tag)
                self.component_manager.set_active_component_callback(self.parent, 0)

    def delete_child(self):
        for child in self.children:
            self.components.get(child).delete()
        self.components.pop(self.tag)

    def delete(self):
        self.delete_child()
        self.delete_parent_relation()
    
    def editor_callback(self, sender, value, parameter_name):
        setattr(self, parameter_name, value)

    def editor_parameters(self):
        pass

    def editor_colors(self):
        pass

    def editor_styles(self):
        pass

    def editor_controls(self):
        # Clear all previous editor controls
        dpg.delete_item(item=self.editor_panel, children_only=True)

        # Get and add all Component Parameters, Colors and Styles
        self.editor_parameters()
        self.editor_colors()
        self.editor_styles()

        # Add Update and Delete Buttons
        dpg.add_button(label="UPDATE", parent=self.editor_panel, callback=self.update, user_data=self.tag)
        dpg.add_button(label="DELETE", parent=self.editor_panel, callback=self.delete, user_data=self.tag)