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
