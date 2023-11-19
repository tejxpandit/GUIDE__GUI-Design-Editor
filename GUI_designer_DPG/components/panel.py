# Title : GUI Designer : Panel Class
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Nov, 2023

import dearpygui.dearpygui as dpg

class Panel:
    def __init__(self, name, pos, width, height, panels):

        # Identifiers
        self.label = name
        self.tag = None

        # Component Collection
        self.panels = panels

        # Functions

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
        # self.theme = dpg.theme()
        self.add()

    def set_name(self, name):
        self.label = name

    def set_params(self, pos, w, h):
        self.position = pos
        self.width = w
        self.height = h

    def set_theme(self):
        with self.theme:
            with dpg.add_theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_TitleBg, self.color_title, category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, self.color_title_active, category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_WindowBg, self.color_background, category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_Text, self.text_color, category=dpg.mvThemeCat_Core)
 
    def add(self):
        #self.set_theme()
        self.tag = dpg.add_window(label=self.label, on_close=self.remove)
        self.label = "Panel " + str(self.tag)
        dpg.set_item_label(self.tag, self.label)
        #dpg.bind_item_theme(item=self.tag, theme=self.theme)
        self.panels.update({self.tag : self})

    def restore(self):
        #self.set_theme()
        dpg.add_window(label=self.label, tag=self.tag, on_close=self.remove, pos=self.position, width=self.width, height=self.height)
        #dpg.bind_item_theme(item=self.tag, theme=self.theme)
    
    def remove(self):
        self.panels.pop(self.tag)
        dpg.delete_item(self.tag)
        # if dpg.does_alias_exist(self.tag):
        #     dpg.remove_alias(self.tag)
