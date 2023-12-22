# Title : GUI Designer : Slider Class
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Nov, 2023

import dearpygui.dearpygui as dpg

default_width = 0
default_height = 0
default_min = 0
default_max = 100

class Slider:
    def __init__(self, parent, callback, width=default_width, height=default_height, min_value=default_min, max_value=default_max):

        # Identifiers
        self.classname = "Slider"
        self.tag = dpg.generate_uuid()
        self.label = self.classname + " " + str(self.tag)
        self.parent = parent
        self.children = []

        # Parameters
        self.width = width
        self.height = height
        self.min = min_value
        self.max = max_value

        # Theme
        self.color_background = None
        self.color_text = None

        # Functions
        self.callback = callback

        # Initialize
        self.add()

    def add(self):
        dpg.add_slider_int(label=self.label, tag=self.tag, width=self.width, height=self.height, min_value=self.min, max_value=self.max, parent=self.parent, callback=self.callback)
    