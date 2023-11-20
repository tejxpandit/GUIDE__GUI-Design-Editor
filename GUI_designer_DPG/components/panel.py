# Title : GUI Designer : Panel Class
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Nov, 2023

import dearpygui.dearpygui as dpg

default_pos = (0,0)
default_width = 100
default_height = 100

class Panel:
    def __init__(self, pos=default_pos, width=default_width, height=default_height):

        # Identifiers
        self.classname = "Panel"
        self.tag = dpg.generate_uuid()
        self.label = self.classname + " " + str(self.tag)

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
        dpg.add_window(label=self.label, tag=self.tag)

    def update(self):
        print(dpg.get_item_children(self.tag))
        dpg.delete_item(self.tag)
        dpg.add_window(label=self.label, tag=self.tag, width=self.width, height=self.height, pos=self.position)

    # def restore(self):
    #     #self.set_theme()
    #     dpg.add_window(label=self.label, tag=self.tag, on_close=self.remove, pos=self.position, width=self.width, height=self.height)
    #     #dpg.bind_item_theme(item=self.tag, theme=self.theme)
    
    # def remove(self):
    #     self.panels.pop(self.tag)
    #     dpg.delete_item(self.tag)
