# Title : GUI Designer App for DearPyGUI
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Nov, 2023

import os
import pickle
import dearpygui.dearpygui as dpg

from utils.RepeatedTimer import RepeatedTimer

from designer.designer import Designer
from designer.loader import Loader
from designer.saver import Saver

from gui_themes import Themes
from components.components import Components
from components.viewport import Viewport


##########################################################
## PARAMETERS ##

viewport_width = 1000
viewport_height = 600

new_panel_position = (0, 0)

##########################################################
## SYSTEM FUNCTIONS ##

# Handles Safe Exits
def exit_callback():
    collect_panel_data()
    save_data("backup_")
    print("Safe Exit")

##########################################################
## GUI DATA ##

gui_all = []
gui_viewport = Viewport()
gui_panels = dict()
gui_components = dict()

##########################################################
## GUI COMPONENTS ##

designer = Designer()
loader = Loader()
saver = Saver()

theme = Themes()
components = Components()

components.panels = gui_panels
components.components = gui_components
components.editor_panel = "control_panel_editor_tab"

##########################################################
## GUI SYSTEM ##

# DPG GUI
dpg.create_context()
dpg.create_viewport(title="GUI Designer DPG", width=viewport_width, height=viewport_height, clear_color=theme.dark_green)
dpg.setup_dearpygui()

# Create Designer Window
designer.new_project_window()

# Set Safe Exit
dpg.set_exit_callback(exit_callback)

# DPG GUI Start and Cleanup
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()