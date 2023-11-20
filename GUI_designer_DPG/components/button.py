# Title : GUI Designer : Button Class
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Nov, 2023

import dearpygui.dearpygui as dpg

# TODO : UPDATE Button Class to match Panel Class style

class Button:
    def __init__(self, name, parent, callback, components, width=0, height=0):

        # Identifiers
        self.label = name
        self.tag = None
        self.parent = parent

        # Component Collection
        self.components = components

        # Functions
        self.callback = callback

        # Parameters
        self.width = width
        self.height = height

        # Theme
        self.color = None
        self.color_hover = None
        self.color_active = None
        self.color_text = None
        self.rounding = None

        # Initialize
        # self.theme = dpg.theme()
        self.add()

    def set_name(self, name):
        self.label = name
        self.tag = name + "_tag"

    def set_parent(self, parent_tag):
        self.parent = parent_tag

    def set_params(self, w, h):
        self.width = w
        self.height = h

    def set_callback_func(self, func):
        self.callback = func

    def set_theme(self):
        with self.theme:
            with dpg.add_theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_Button, self.color, category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, self.color_hover, category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, self.color_active, category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_Text, self.color_text, category=dpg.mvThemeCat_Core)
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, self.rounding, category=dpg.mvThemeCat_Core)

    def add(self):
        #self.set_theme()
        self.tag = dpg.add_button(label=self.label, parent=self.parent, width=self.width, height=self.height, callback=self.callback)
        #dpg.bind_item_theme(item=self.tag, theme=self.theme)
        self.components.update({self.tag : self})
    
    def remove(self):
        self.components.pop(self.tag)
        dpg.delete_item(self.tag)
        # if dpg.does_alias_exist(self.tag):
        #     dpg.remove_alias(self.tag)