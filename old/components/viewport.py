# Title : GUI Designer : Viewport Class
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Nov, 2023

import dearpygui.dearpygui as dpg

default_title = "GUI Designer DPG"
default_width = 1000
default_height = 600

class Viewport:
    def __init__(self, title=default_title, width=default_width, height=default_height):

        # Identifiers
        self.classname = "Viewport"
        self.tag = None
        self.label = title
        self.parent = None
        self.children = None

        # Parameters
        self.width = width
        self.height = height

        # Theme
        self.color_background = None

        # Initialize
        # self.add()

    def add(self):
        dpg.create_viewport(title=self.label, width=self.width, height=self.height)    
