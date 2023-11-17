# Title : GUI Designer : Panel Class
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Nov, 2023

import dearpygui.dearpygui as dpg

class Panel:
    def __init__(self):

        # Identifiers
        self.label = None
        self.tag = None

        # Functions

        # Parameters
        self.position = None
        self.width = None
        self.height = None

        # Theme
        self.theme = None
        self.color_background = None
        self.color_title = None
        self.color_title_active = None
        self.color_text = None

    def set_theme(self):
        self.theme = dpg.theme()
        self.theme_component = dpg.add_theme_component(dpg.mvAll, parent=self.theme)
        dpg.add_theme_color(dpg.mvThemeCol_TitleBg, self.color_title, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, self.color_title_active, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, self.color_background, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Text, self.text_color, category=dpg.mvThemeCat_Core, parent=self.theme_component)
 
    def add(self):
        self.set_theme()
        dpg.add_window(label=self.label, tag=self.tag)
        dpg.bind_item_theme(item=self.tag, theme=self.theme)
    
    def remove(self):
        dpg.delete_item(self.tag)
        if dpg.does_alias_exist(self.tag):
            dpg.remove_alias(self.tag)