# Title : GUI Designer : Checkbox Class
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Nov, 2023

import dearpygui.dearpygui as dpg

default_width = 0
default_height = 0

class Checkbox:
    def __init__(self, parent, callback, width=default_width, height=default_height):

        # Identifiers
        self.classname = "Checkbox"
        self.tag = dpg.generate_uuid()
        self.label = self.classname + " " + str(self.tag)
        self.parent = parent
        self.children = []

        # Parameters

        # Theme
        self.color_background = None
        self.color_text = None

        # Functions
        self.callback = callback

        # Initialize
        self.add()

    def add(self):
        dpg.add_checkbox(label=self.label, tag=self.tag, parent=self.parent, callback=self.callback)
    