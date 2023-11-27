# Title : GUI Designer : Panel Class
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Nov, 2023

import dearpygui.dearpygui as dpg

default_pos = (0,0)
default_width = 100
default_height = 100

class Panel:
    def __init__(self, on_close_func, pos=default_pos, width=default_width, height=default_height):

        # Identifiers
        self.classname = "Panel"
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
        self.position = pos
        self.width = width
        self.height = height

        # Functions
        self.on_close = on_close_func

        # Theme
        self.color_background = None
        self.color_title = None
        self.color_title_active = None
        self.color_text = None

        # Initialize
        self.add()

    def add(self):
        dpg.add_window(label=self.label, tag=self.tag, width=self.width, height=self.height, pos=self.position, on_close=self.on_close, user_data=self.tag)

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

    def delete(self):
        # Get All Children
        for child in self.children:
            # Recursive Deletion of Children
            self.components.get(child).delete()
        # Deletion of Panel from Panel Dict (after deleting all children)
        self.panels.pop(self.tag)
        for panel_tag, panel in self.panels.items():
            self.set_active_panel_callback(panel_tag, 0)
            return
    
    def editor_callback(self, sender, value, parameter_name):
        setattr(self, parameter_name, value)

    def editor_controls(self):
        dpg.delete_item(item=self.editor_panel, children_only=True)
        # Get and add all Component Parameters

        # TODO : Add all parameters from component manager

        # Add Update and Delete Buttons
        dpg.add_button(label="UPDATE", parent=self.editor_panel, callback=self.update, user_data=self.tag)
        dpg.add_button(label="DELETE", parent=self.editor_panel, callback=self.delete, user_data=self.tag)