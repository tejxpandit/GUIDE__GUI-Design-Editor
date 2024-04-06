# Title : GUIDE : Data Manager
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : 1 April 2024

import dearpygui.dearpygui as dpg
from TagGenerator import TagGenerator
from Components import Components

class DataManager:
    def __init__(self):
        self.taggen = TagGenerator()
        self.data = {}
        self.window_data = {}
        self.project_name = ""
        self.selected_container = None
        self.selected_component = None
        self.active_window = None

    def updateComponent(self, tag, component):
        if tag in self.data:
            self.data[tag] = component
            print("Updated Component : " + str(tag))
        else:
            print("Failed to Find & Update Component! : " + str(tag))

