# Title : GUI Designer : Viewport Class
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Nov, 2023

import dearpygui.dearpygui as dpg

class Viewport:
    def __init__(self):

        # Identifiers
        self.label = None

        # Parameters
        self.position = None
        self.width = None
        self.height = None

        # Theme
        self.theme = None
        self.color_background = None
