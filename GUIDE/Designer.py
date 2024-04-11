# Title : GUIDE : Designer
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : 10 April 2024

import copy as cpy
import dearpygui.dearpygui as dpg
from Components import Components
from Builder import Builder
from CodeGenerator import CodeGenerator

class Designer:
    def __init__(self, dataman):
        self.dataman = dataman
        self.editor = None
        self.taggen = dataman.taggen
        self.component_ref = Components()
        self.builder = Builder()
        self.codegen = CodeGenerator(dataman)
        self.selectionManager()
    
    def createDesignerTab(self):
        # SELECTION STATUS
        with dpg.group(parent="designer_tab"):
            dpg.add_text("Selected Container : ", tag="designer_selected_container_text")
            dpg.add_text("Selected Component : ", tag="designer_selected_component_text")
            dpg.add_tree_node(label="Hierarchy", tag="designer_selected_component_hierarchy")
            dpg.add_spacer()

        # CONTAINER UI ELEMENTS
        dpg.add_text("Containers", parent="designer_tab")
        with dpg.group(parent="designer_tab", horizontal=True):
            dpg.add_button(label="Window", tag="designer_add_window_button", callback=self.newComponent)
            dpg.add_button(label="Group", tag="designer_add_group_button", callback=self.newComponent)
            dpg.add_button(label="Tree Node", tag="designer_add_tree_node_button", callback=self.newComponent)
            dpg.add_spacer()

        