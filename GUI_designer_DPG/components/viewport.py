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

    def set_theme(self):
        self.theme = dpg.theme()
        self.theme_component = dpg.add_theme_component(dpg.mvAll, parent=self.theme)
        dpg.add_theme_color(dpg.mvThemeCol_Button, self.color, category=dpg.mvThemeCat_Core, parent=self.theme_component)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, self.color_hover, category=dpg.mvThemeCat_Core, parent=self.theme_component)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, self.color_active, category=dpg.mvThemeCat_Core, parent=self.theme_component)
        dpg.add_theme_color(dpg.mvThemeCol_Text, self.color_text, category=dpg.mvThemeCat_Core, parent=self.theme_component)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, self.rounding, category=dpg.mvThemeCat_Core, parent=self.theme_componen)

    def add(self):
        self.set_theme()
        dpg.add_button(label=self.label, tag=self.tag, parent=self.parent, callback=self.callback)
        dpg.bind_item_theme(item=self.tag, theme=self.theme)
    
    def remove(self):
        dpg.delete_item(self.tag)
        if dpg.does_alias_exist(self.tag):
            dpg.remove_alias(self.tag)
