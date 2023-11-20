# Title : GUI Designer : Panel Class
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Nov, 2023

import dearpygui.dearpygui as dpg

default_pos = (0,0)
default_width = 100
default_height = 100

class Panel:
    def __init__(self, pos=default_pos, width=default_width, height=default_height):

        # Identifiers
        self.classname = "Panel"
        self.tag = dpg.generate_uuid()
        self.label = self.classname + " " + str(self.tag)

        # Parameters
        self.position = pos
        self.width = width
        self.height = height

        # Theme
        self.color_background = None
        self.color_title = None
        self.color_title_active = None
        self.color_text = None

        # Initialize
        self.add()

    def add(self):
        dpg.add_window(label=self.label, tag=self.tag, width=self.width, height=self.height, pos=self.position)

    # TODO : Maybe move delete and update functions to components.py if they are generic. Especially since they need to access all components, panels, children and parents. 
    def update(self):
        print(dpg.get_item_children(self.tag, 1))
        # TODO : Get all children, and their children
        dpg.delete_item(self.tag)
        self.add()
        # TODO : Implement recursive update of children, when parent is updated
        # Actually, if you implement a immidiate child update function, where an "update function" is called in the immidiate children, and if this update function is in all children, then all children will be automatically updated recursively anyways!
        # TODO : The update needs to actually delete and re-add the parent, because if the child is removed and added, the order of components will change. The entire structure need to be readded in order

    def delete(self):
        dpg.delete_item(self.tag)
        # RECURSIVE DELETION OF CHILDREN IS AUTOMATIC IN DPG!
        # TODO : Recursive Deletion of Children from Component Lists
