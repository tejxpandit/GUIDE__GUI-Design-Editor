# Title : GUI Designer : Button Class
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Nov, 2023

import dearpygui.dearpygui as dpg
from .component import Component

default_width = 0
default_height = 0

class Button(Component):
    def __init__(self, parent, callback, width=default_width, height=default_height):
        super().__init__()
        
        # Identifiers
        self.classname = "Button"
        self.tag = dpg.generate_uuid()
        self.label = self.classname + " " + str(self.tag)
        self.parent = parent
        self.children = []

        # Parameters
        self.width = width
        self.height = height

        # Theme
        self.color_background = None
        self.color_text = None

        # Functions
        self.callback = callback

        # Initialize
        self.add()

    def add(self):
        dpg.add_button(label=self.label, tag=self.tag, width=self.width, height=self.height, parent=self.parent, callback=self.callback)
    