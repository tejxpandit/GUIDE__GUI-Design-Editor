# Title : GUI Designer App for DearPyGUI
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Nov, 2023

import os
import dearpygui.dearpygui as dpg

from gui_themes import themes

##########################################################
## PARAMETERS ##

viewport_width = 1000
viewport_height = 600
designer_window_position = (300, 50)
designer_window_width = 400
designer_window_height = 400

new_panel_position = (0, 0)
active_panel = None

gui_components_list = ["Button", "Slider", "Dropdown Menu", "New Tab", "Tab Group", "Group"]
active_component = None

selected_parent = None
selected_component_dropdown = None



##########################################################
## COMPONENT CALLBACKS ##

def add_panel_callback():
    dpg.add_window(label="New Panel", pos=new_panel_position)

def component_selector_callback(s, component):
    selected_component_dropdown = component
    print(selected_component_dropdown)

def add_component_callback():
    # add_component(selected_component_dropdown, selected_parent)
    pass

##########################################################
## GUI COMPONENTS ##

theme = themes()

##########################################################
## GUI VARIABLES ##

##########################################################
## GUI SYSTEM ##

# DPG GUI
dpg.create_context()
dpg.create_viewport(title="GUI Designer DPG", width=viewport_width, height=viewport_height, clear_color=theme.dark_green)
dpg.setup_dearpygui()

# Designer Window
designer_win = dpg.add_window(label="GUI Designer", pos=designer_window_position, width=designer_window_width, height=designer_window_height)

# Control Panel
dpg.add_tab_bar(tag="designer_tabs", parent=designer_win)
dpg.add_tab(label="Designer", tag="control_panel_designer_tab", parent="designer_tabs")
dpg.add_tab(label="Editor", tag="control_panel_editor_tab", parent="designer_tabs")

# Designer Panel
dpg.add_button(label="Add Panel", tag="add_panel_button", parent="control_panel_designer_tab", callback=add_panel_callback)
dpg.add_separator(parent="control_panel_designer_tab")
dpg.add_text("Window : " +  "None", color=theme.dark_green, parent="control_panel_designer_tab")
dpg.add_combo(items=gui_components_list, tag="component_selector", parent="control_panel_designer_tab", callback=component_selector_callback)
dpg.add_group

# GUI Theme Colors
with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        # Window Colors
        dpg.add_theme_color(dpg.mvThemeCol_TitleBg, theme.dark_green, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, theme.light_green, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, theme.white, category=dpg.mvThemeCat_Core)
        # Tab Colors
        dpg.add_theme_color(dpg.mvThemeCol_Tab, theme.dark_green, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TabActive, theme.light_green, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TabHovered, theme.light_green, category=dpg.mvThemeCat_Core)
        # Slider Colors
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, theme.dark_green, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, theme.black, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, theme.light_green, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, theme.light_green, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, theme.dark_green, category=dpg.mvThemeCat_Core)
        # Button Colors
        dpg.add_theme_color(dpg.mvThemeCol_Button, theme.dark_green, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, theme.light_green, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, theme.black, category=dpg.mvThemeCat_Core)
        # Component Styling
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 3, category=dpg.mvThemeCat_Core)
        # # Font Colors
        # dpg.add_theme_color(dpg.mvThemeCol_Text, theme.black, category=dpg.mvThemeCat_Core)

dpg.bind_theme(global_theme)

dpg.show_style_editor()

# DPG GUI Start and Cleanup
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()