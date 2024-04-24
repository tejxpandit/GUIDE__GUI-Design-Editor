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

        # Add Starter Window --> REMOVE LATER
        # self.newComponent("designer_add_window_button")

        def newComponent(self, sender):
            component_type = sender.removeprefix("designer_add_").removesuffix("_button")
            self.addComponent(component_type)

        def addComponent(self, component_type):
            component = cpy.deepcopy(self.component_ref.components[component_type])
            tag = self.taggen.generateTag(component_type)
            component["attributes"]["tag"][2] = tag
            if not component_type=="window":
                component["attributes"]["parent"][2] = self.dataman.selected_container
            if component["data_type"] == "container":
                self.dataman.selected_container = tag
                self.dataman.selected_component = tag
            else:
                self.dataman.selected_component = tag
            self.builder.buildComponent(tag, component)
            self.dataman.addComponent(tag, component)
            self.updateSelectionText()
            if not component["data_type"] == "container":
                dpg.bind_item_handler_registry(tag, "selection_handler")
        
        def deleteComponent(self, tag):
            self.builder.removeComponent(tag)
            self.dataman.deleteComponent(tag)

        def selectionManager(self):
            # Window Selection
            with dpg.handler_registry():
                dpg.add_mouse_down_handler(callback=self.getActiveWindow)
                dpg.add_key_down_handler()

            # Component Selection
            with dpg.item_handler_registry(tag="selection_handler") as handler:
                dpg.add_item_clicked_handler(callback=self.selectionHandler)

        def getActiveWindow(self):
            tag_id = dpg.get_active_window()
            tag = dpg.get_item_alias(tag_id)
            if tag in self.dataman.data:
                if not tag == self.dataman.active_window:
                    self.dataman.active_window = tag
                    self.dataman.selected_container = tag
                    self.updateSelectionText()
                    print("Selected Window : " + tag)

        def selectionHandler(self, registryID, sender):
            tag = dpg.get_item_alias(sender[1])
            if self.dataman.selected_component == tag:
                if not self.isWindow(self.dataman.selected_container):
                    self.dataman.selected_container = self.getParent(self.dataman.selected_container)
            else:
                if self.isContainer(tag):
                    self.dataman.selected_component = tag
                    self.dataman.selected_container = tag
                else:
                    self.dataman.selected_component = tag
                    self.dataman.selected_container = self.getParent(self.dataman.selected_component)
            self.updateSelectionText()
            print("Selected Item : " + tag)

        def updateSelectionHierarchy(self):
            dpg.delete_item("designer_selected_component_hierarchy", children_only=True)
            with dpg.group(parent="designer_selected_component_hierarchy"):
                component = self.dataman.selected_component
                level = 0
                max_level = 10
                while not self.isWindow(component):
                    parent = self.getParent(component)
                    dpg.add_button(label=parent, user_data=parent, callback=self.selectComponent)
                    component = parent
                    level += 1
                    if level >= max_level:
                        break

        def selectComponent(self, sender, value, tag):
            if self.isContainer(tag):
                self.dataman.selected_container = tag
                self.dataman.selected_component = tag
            else:
                self.dataman.selected_container = self.getParent(tag)
                self.dataman.selected_component = tag
            self.updateSelectionText()
            
        def updateSelectionText(self):
            dpg.set_value("designer_selected_container_text", "Selected Container : " + self.dataman.selected_container)
            dpg.set_value("designer_selected_component_text", "Selected Component : " + self.dataman.selected_component)
            self.updateSelectionHierarchy()
            self.editor.updateEditorTab()

        def getParent(self, child):
            return self.dataman.data[child]["attributes"]["parent"][2]
        
        def isWindow(self, tag):
            return self.dataman.data[tag]["name"] == "Window"