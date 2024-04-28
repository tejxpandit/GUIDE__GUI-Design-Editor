# Title : GUIDE : Editor
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : 25 April 2024

import copy as cpy
import dearpygui.dearpygui as dpg
from Components import Components
from Builder import Builder

class Editor:
    def __init__(self, dataman):
        self.dataman = dataman
        self.designer = None
        self.taggen = dataman.taggen
        self.component_ref = Components()
        self.builder = Builder()
        self.component = None
        self.tag = None

    def updateEditorTab(self):
        self.tag = self.dataman.selected_component
        self.component = cpy.deepcopy(self.dataman.data[self.tag])
        dpg.delete_item("editor_tab", children_only=True)
        with dpg.group(parent="editor_tab"):
            for attr, attr_list in self.component["attributes"].items():
                attr_label = attr_list[0]
                attr_type = attr_list[1]
                attr_default = attr_list[2]

                raw_command = self.component_ref.attr_func[attr_type]
                command = raw_command.replace("$LABEL", str(attr_label)).replace("$ATTR", str(attr))

                if attr_default == None:
                    command = command.replace("default_value=$DEFAULT,", "")
                    command = command.replace("default_value='$DEFAULT',", "")
                else:
                    command = command.replace("$DEFAULT", str(attr_default))
                # print(command)
                exec(command)

            dpg.add_separator()
            dpg.add_button(label="DELETE", callback=self.deleteComponent)

    def deleteComponent(self):
        dpg.delete_item("editor_tab", children_only=True)
        dpg.delete_item(self.tag)
        self.dataman.deleteComponent(self.tag)
        self.resetSelections()

    def resetSelections(self):
        NoWindows = True
        for tag, component in self.dataman.data.items():
            if component["name"] == "Window":
                self.dataman.active_window = tag
                self.dataman.selected_container = tag
                self.dataman.selected_component = tag
                self.tag = tag
                self.component = component
                self.designer.updateSelectionText()
                NoWindows = False
                break
        if NoWindows:
            self.designer.addComponent("window")
    
    def movePosition(self, sender, data, direction):
        if not self.dataman.data[self.tag]["name"] == "Window":
            parent_tag = self.dataman.data[self.tag]["attributes"]["parent"][2]
            if direction == "up":
                dpg.move_item_up(self.tag)
            elif direction == "down":
                dpg.move_item_down(self.tag)
            self.dataman.data[parent_tag]["children"] = dpg.get_item_children(parent_tag)[1]

    