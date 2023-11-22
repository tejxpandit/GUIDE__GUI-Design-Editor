# Title : GUI Designer : Panel Class
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Nov, 2023

import dearpygui.dearpygui as dpg

default_pos = (0,0)
default_width = 100
default_height = 100

class Panel:
    def __init__(self, on_close_func, pos=default_pos, width=default_width, height=default_height):

        # Identifiers
        self.classname = "Panel"
        self.tag = dpg.generate_uuid()
        self.label = self.classname + " " + str(self.tag)
        self.parent = None
        self.children = []

        # Parameters
        self.position = pos
        self.width = width
        self.height = height

        # Functions
        self.on_close = on_close_func

        # Theme
        self.color_background = None
        self.color_title = None
        self.color_title_active = None
        self.color_text = None

        # Initialize
        self.add()

    def add(self):
        dpg.add_window(label=self.label, tag=self.tag, width=self.width, height=self.height, pos=self.position, on_close=self.on_close, user_data=self.tag)
    