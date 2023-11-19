# Title : GUI Designer : Panel Class
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Nov, 2023

import dearpygui.dearpygui as dpg

class Panel:
    def __init__(self, pos, width, height, panels):

        # Identifiers
        self.tag = dpg.generate_uuid()
        self.label = "Panel " + str(self.tag)

        # Parameters
        self.position = pos
        self.width = width
        self.height = height

        # Theme
        self.color_background = None
        self.color_title = None
        self.color_title_active = None
        self.color_text = None

        # Initialize
        self.add()

    def add(self):
        #self.set_theme()
        dpg.add_window(label=self.label, tag=self.tag, on_close=self.remove)
        #dpg.bind_item_theme(item=self.tag, theme=self.theme)
        self.panels.update({self.tag : self})

    def restore(self):
        #self.set_theme()
        dpg.add_window(label=self.label, tag=self.tag, on_close=self.remove, pos=self.position, width=self.width, height=self.height)
        #dpg.bind_item_theme(item=self.tag, theme=self.theme)
    
    def remove(self):
        self.panels.pop(self.tag)
        dpg.delete_item(self.tag)
