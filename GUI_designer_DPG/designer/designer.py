# Title : GUI Designer : Designer Class
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Nov, 2023

import dearpygui.dearpygui as dpg

from utils.RepeatedTimer import RepeatedTimer
from .designer_theme import DesignerTheme

class Designer:
    def __init__(self):
        # Defaults
        self.window_position = (300, 50)
        self.window_width = 400
        self.window_height = 400

        # Variables
        self.panels = None
        self.components = None

        # Objects
        self.timer = RepeatedTimer()
        self.theme = DesignerTheme()

        # Tags
        self.editor_panel = "control_panel_editor_tab"

    ##########################################################
    ## COMPONENT CALLBACKS ##

    def new_gui_project_button_callback(self):
        self.delete_new_project_window()
        self.start_designer_window()
        self.start_window_polling_timer()

    def restore_gui_project_button_callback(self):
        self.delete_new_project_window()
        self.load_data()
        self.restore_panels()
        self.start_designer_window()

    def restore_gui_file_dropdown(self, s, file):
        global save_filename
        save_filename = file

    def add_panel_callback(self):
        components.add_component(components.component_types.get("Panel"))

    def component_selector_callback(self, s, component):
        selected_component_dropdown = component
        print(selected_component_dropdown)

    def add_component_callback(self):
        global components
        components.add_component(components.component_types.get(self.selected_component_dropdown))

    ##########################################################
    ## SYSTEM FUNCTIONS ##
    
    # Initialize GUI Components List
    def initialize_gui_components_list(self):
        global gui_components_list, components
        for c, v in components.component_types.items():
            gui_components_list.append(c)

    # Delete Project Window
    def delete_new_project_window(self):
        dpg.delete_item("new_project_win")

    # Window Identification Polling Function
    def start_window_polling_timer(self):
        self.timer.set_timer(interval=1.0, function=self.identify_active_window)
        self.timer.start()

    # Window Identification Function
    def identify_active_window(self):
        global components
        window_key = dpg.get_active_window()
        if window_key in self.panels:
            components.selected_panel = window_key
            dpg.set_value("selected_panel_text", "Selected Panel : " + str(self.panels.get(components.selected_panel).label))

    # Collect Window Data to Save
    def collect_panel_data(self):
        for panel_tag, panel in self.panels.items():
            panel.position = dpg.get_item_pos(panel_tag)
            panel.width = dpg.get_item_width(panel_tag)
            panel.height = dpg.get_item_height(panel_tag)

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
        dpg.add_combo(items=self.data_files_list, parent="new_project_win", callback=self.restore_gui_file_dropdown)
        dpg.add_button(label="Restore GUI Project", tag="restore_gui_project_button", parent="new_project_win", callback=self.restore_gui_project_button_callback)

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
        dpg.add_combo(items=self.gui_components_list, tag="component_selector", parent="control_panel_designer_tab", callback=self.component_selector_callback)
        dpg.add_button(label="Add Component", tag="add_component_button", parent="control_panel_designer_tab", callback=self.add_component_callback)

    # Designer Theme
    def bind_designer_theme(self):
        dpg.bind_item_theme(self.theme.get_designer_theme())