# Title : GUI Designer App for DearPyGUI
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Nov, 2023

import os
import pickle
import dearpygui.dearpygui as dpg

from gui_themes import themes

from components.viewport import Viewport
from components.panel import Panel
from components.button import Button


##########################################################
## PARAMETERS ##

viewport_width = 1000
viewport_height = 600

designer_window_position = (300, 50)
designer_window_width = 400
designer_window_height = 400

new_panel_position = (0, 0)

##########################################################
## SYSTEM FUNCTIONS ##

# Handles Safe Exits
def exit_callback():
    save_data("backup_")
    print("Safe Exit")

# Save GUI Components
def save_data(ext=""):
    gui_all.append(gui_viewport)
    gui_all.append(gui_panels)
    gui_all.append(gui_components)
    with open(ext + save_filename, 'wb') as file: 
        pickle.dump(gui_all, file)

# Load Saved GUI Components
def load_data():
    global gui_all, gui_viewport, gui_panels, gui_components
    if os.path.isfile(os.getcwd() + '\\' + save_filename):    
        with open(save_filename, 'rb') as file: 
            gui_all = pickle.load(file)
            gui_viewport = gui_all[0]
            gui_panels = gui_all[1]
            gui_components = gui_all[2]
            print("Loaded : " + save_filename)
    else:
        print("No such data file")
        quit()

# Get all GUI data filenames
def get_data_filenames():
    global data_files_list
    data_files_list = []
    for filename in os.listdir(os.getcwd()):
        if filename.endswith(".pkl"):
            data_files_list.append(filename)
    print(data_files_list)

# Delete Project Window
def delete_new_project_window():
    dpg.delete_item("new_project_win")

##########################################################
## COMPONENT CALLBACKS ##

def new_gui_project_button_callback():
    delete_new_project_window()
    start_designer_window()

def restore_gui_project_button_callback():
    delete_new_project_window()
    load_data()
    start_designer_window()

def restore_gui_file_dropdown(s, file):
    global save_filename
    save_filename = file

def add_panel_callback():
    dpg.add_window(label="New Panel", pos=new_panel_position)

def component_selector_callback(s, component):
    selected_component_dropdown = component
    print(selected_component_dropdown)

def add_component_callback():
    # add_component(selected_component_dropdown, selected_parent)
    pass

##########################################################
## GUI DATA ##

gui_all = []
gui_viewport = Viewport()
gui_panels = dict()
gui_components = dict()

##########################################################
## GUI COMPONENTS ##

gui_components_list = ["Button", "Slider", "Dropdown Menu", "New Tab", "Tab Group", "Group"]

active_panel = None
active_component = None
selected_parent = None
selected_component_dropdown = None

theme = themes()

##########################################################
## GUI VARIABLES ##

##########################################################
## GUI SYSTEM ##

# New Project Window
def new_project_window():
    dpg.add_window(label="Save File Restore", tag="new_project_win", pos=designer_window_position, width=designer_window_width, height=designer_window_height, no_close=True)
    dpg.add_text("Do you want to start a New GUI Project ?", color=theme.dark_green, parent="new_project_win")
    dpg.add_button(label="New GUI Project", tag="new_gui_project_button", parent="new_project_win", callback=new_gui_project_button_callback)
    dpg.add_text("Or do you want to restore a Previous GUI Project ?", color=theme.dark_green, parent="new_project_win")
    dpg.add_text("Choose File....", color=theme.dark_green, parent="new_project_win")
    dpg.add_combo(items=data_files_list, parent="new_project_win", callback=restore_gui_file_dropdown)
    dpg.add_button(label="Restore GUI Project", tag="restore_gui_project_button", parent="new_project_win", callback=restore_gui_project_button_callback)

# Designer Window
def start_designer_window():
    dpg.add_window(label="GUI Designer", tag="designer_win", pos=designer_window_position, width=designer_window_width, height=designer_window_height, no_close=True)

    # Control Panel
    dpg.add_tab_bar(tag="designer_tabs", parent="designer_win")
    dpg.add_tab(label="Designer", tag="control_panel_designer_tab", parent="designer_tabs")
    dpg.add_tab(label="Editor", tag="control_panel_editor_tab", parent="designer_tabs")

    # Designer Panel
    dpg.add_button(label="Add Panel", tag="add_panel_button", parent="control_panel_designer_tab", callback=add_panel_callback)
    dpg.add_separator(parent="control_panel_designer_tab")
    dpg.add_text("Selected Window : " +  "None", color=theme.dark_green, parent="control_panel_designer_tab")
    dpg.add_combo(items=gui_components_list, tag="component_selector", parent="control_panel_designer_tab", callback=component_selector_callback)

# DPG GUI
dpg.create_context()
dpg.create_viewport(title="GUI Designer DPG", width=viewport_width, height=viewport_height, clear_color=theme.dark_green)
dpg.setup_dearpygui()

# Intial Windows
data_files_list = []
save_filename = "GUI_saved.pkl"
get_data_filenames()
new_project_window()

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

# Set Safe Exit
dpg.set_exit_callback(exit_callback)

# DPG GUI Start and Cleanup
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()