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

        # COMPONENT UI ELEMENTS
        dpg.add_text("Controls", parent="designer_tab")
        with dpg.group(parent="designer_tab", horizontal=True):
            dpg.add_button(label="Button", tag="designer_add_button_button", callback=self.newComponent)
        with dpg.group(parent="designer_tab", horizontal=True):
            dpg.add_button(label="Slider (Int)", tag="designer_add_slider_int_button", callback=self.newComponent)
            dpg.add_button(label="Slider (Float)", tag="designer_add_slider_float_button", callback=self.newComponent)
        with dpg.group(parent="designer_tab", horizontal=True):
            dpg.add_button(label="Input Text", tag="designer_add_input_text_button", callback=self.newComponent)
        dpg.add_spacer(parent="designer_tab")

        # DISPLAY UI ELEMENTS
        dpg.add_text("Display", parent="designer_tab")
        with dpg.group(parent="designer_tab", horizontal=True):
            dpg.add_button(label="Text", tag="designer_add_text_button", callback=self.newComponent)
            dpg.add_button(label="ListBox", tag="designer_add_listbox_button", callback=self.newComponent)
        dpg.add_spacer(parent="designer_tab")

        # GLOBAL CONTROLS
        dpg.add_text("Component Controls", parent="designer_tab")
        with dpg.group(parent="designer_tab", horizontal=True):
            dpg.add_button(label="Delete", callback=self.editor.deleteComponent)
            dpg.add_button(label="Move Up", user_data="up", callback=self.editor.movePosition)
            dpg.add_button(label="Move Down", user_data="down", callback=self.editor.movePosition)
        dpg.add_text("Project Controls", parent="designer_tab")
        with dpg.group(parent="designer_tab", horizontal=True):
            dpg.add_button(label="Export Code", callback=self.codegen.exportCode)