# Title : GUI Designer : Designer Class
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Nov, 2023

import os
import dearpygui.dearpygui as dpg

from .designer_theme import DesignerTheme

class Designer:
    def __init__(self):
        # Defaults
        self.window_position = (300, 50)
        self.window_width = 400
        self.window_height = 400

        # Variables
        self.viewport = None
        self.panels = None
        self.components = None
        self.components_list = []
        self.selected_component_dropdown = None

        # Objects
        self.theme = DesignerTheme()
        self.saver = None
        self.component_manager = None

        # Tags
        self.editor_panel = "control_panel_editor_tab"

    # Initialize Designer Parameters
    def initialize(self, viewport, panels, components, saver, component_manager):
        self.viewport = viewport
        self.panels = panels
        self.components = components
        self.saver = saver
        self.component_manager = component_manager
        self.initialize_gui_components_list()

    ##########################################################
    ## COMPONENT CALLBACKS ##

    def add_panel_callback(self):
        # self.component_manager.component_types.get("Panel")
        self.component_manager.add_component("panel") 

    def component_selector_callback(self, s, component):
        self.selected_component_dropdown = component

    def add_component_callback(self):
        self.component_manager.add_component(self.component_manager.component_types.get(self.selected_component_dropdown))

    ##########################################################
    ## SYSTEM FUNCTIONS ##
    
    # Initialize GUI Components List
    def initialize_gui_components_list(self):
        for c, v in self.component_manager.component_types.items():
            self.components_list.append(c)
        print(self.components_list)
    
    ##########################################################
    ## GUI SYSTEM ##

    # Designer Window
    def start_designer_window(self):
        dpg.add_window(label="GUI Designer", tag="designer_win", pos=self.window_position, width=self.window_width, height=self.window_height, no_close=True)

        # Control Panel
        dpg.add_tab_bar(tag="designer_tabs", parent="designer_win")
        dpg.add_tab(label="Designer", tag="control_panel_designer_tab", parent="designer_tabs")
        dpg.add_tab(label="Editor", tag="control_panel_editor_tab", parent="designer_tabs")

        # Designer Panel
        dpg.add_button(label="Add Panel", tag="add_panel_button", parent="control_panel_designer_tab", callback=self.add_panel_callback)
        dpg.add_separator(parent="control_panel_designer_tab")
        dpg.add_text("Selected Panel : None", tag="selected_panel_text", color=self.theme.dark_green, parent="control_panel_designer_tab")
        dpg.add_combo(items=self.components_list, tag="component_selector", parent="control_panel_designer_tab", callback=self.component_selector_callback)
        dpg.add_button(label="Add Component", tag="add_component_button", parent="control_panel_designer_tab", callback=self.add_component_callback)
        
        self.bind_designer_theme()

    # Designer Theme
    def bind_designer_theme(self):
        # dpg.bind_item_theme(self.theme.get_designer_theme())
        dpg.bind_theme(self.theme.get_designer_theme())