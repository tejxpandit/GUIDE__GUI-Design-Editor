# Title : GUI Designer : New Project Class
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Nov, 2023

import os
import dearpygui.dearpygui as dpg

from utils.RepeatedTimer import RepeatedTimer
from .designer_theme import DesignerTheme

class NewProject:
    def __init__(self):
        # Defaults
        self.window_position = (300, 50)
        self.window_width = 400
        self.window_height = 400

        # Variables
        self.viewport = None
        self.panels = None
        self.components = None
        self.save_filename = None

        # Objects
        self.timer = RepeatedTimer()
        self.theme = DesignerTheme()
        self.loader = None
        self.designer = None
        self.component_manager = None

        # Tags
        self.editor_panel = "control_panel_editor_tab"

    # Initialize New Project Panel Parameters
    def initialize(self, viewport, panels, components, loader, designer, component_manager):
        self.viewport = viewport
        self.panels = panels
        self.components = components
        self.loader = loader
        self.designer = designer
        self.component_manager = component_manager

    ##########################################################
    ## COMPONENT CALLBACKS ##

    def new_gui_project_button_callback(self):
        self.delete_new_project_window()
        self.designer.start_designer_window()
        self.start_window_polling_timer()

    def restore_gui_project_button_callback(self):
        self.delete_new_project_window()
        self.loader.load_data()
        self.restore_panels()
        self.designer.start_designer_window()
        self.start_window_polling_timer()

    def restore_gui_file_dropdown(self, s, file):
        self.save_filename = file

    ##########################################################
    ## SYSTEM FUNCTIONS ##

    # Delete Project Window
    def delete_new_project_window(self):
        dpg.delete_item("new_project_win")

    # Window Identification Polling Function
    def start_window_polling_timer(self):
        self.timer.set_timer(interval=1.0, function=self.identify_active_window)
        self.timer.start()

    # Window Identification Function
    def identify_active_window(self):
        window_key = dpg.get_active_window()
        if window_key in self.panels:
            self.component_manager.selected_panel = window_key
            dpg.set_value("selected_panel_text", "Selected Panel : " + str(self.panels.get(window_key).label))

    # Restore Saved Panels
    def restore_panels(self):
        # for panel_tag, panel in gui_panels.items():
        #     panel.restore()
        pass
    
    ##########################################################
    ## GUI SYSTEM ##

    # New Project Window
    def new_project_window(self):
        dpg.add_window(label="Save File Restore", tag="new_project_win", pos=self.window_position, width=self.window_width, height=self.window_height, no_close=True)
        dpg.add_text("Do you want to start a New GUI Project ?", color=self.theme.dark_green, parent="new_project_win")
        dpg.add_button(label="New GUI Project", tag="new_gui_project_button", parent="new_project_win", callback=self.new_gui_project_button_callback)
        dpg.add_text("Or do you want to restore a Previous GUI Project ?", color=self.theme.dark_green, parent="new_project_win")
        dpg.add_text("Choose File....", color=self.theme.dark_green, parent="new_project_win")
        dpg.add_combo(items=self.loader.data_files_list, parent="new_project_win", callback=self.restore_gui_file_dropdown)
        dpg.add_button(label="Restore GUI Project", tag="restore_gui_project_button", parent="new_project_win", callback=self.restore_gui_project_button_callback)

        self.bind_designer_theme()

    # Designer Theme
    def bind_designer_theme(self):
        # dpg.bind_item_theme(self.theme.get_designer_theme())
        dpg.bind_theme(self.theme.get_designer_theme())