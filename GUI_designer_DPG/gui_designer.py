# Title : GUI Designer App for DearPyGUI
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Nov, 2023

import dearpygui.dearpygui as dpg

from designer.new_project import NewProject
from designer.designer import Designer
from designer.loader import Loader
from designer.saver import Saver

from components.viewport import Viewport
from components.component_manager import ComponentManager

##########################################################
## PARAMETERS ##

##########################################################
## SYSTEM FUNCTIONS ##

##########################################################
## GUI DATA ##

viewport = Viewport()
panels = dict()
components = dict()

##########################################################
## GUI OBJECTS ##

loader = Loader()
saver = Saver()
viewport = Viewport()
new_project = NewProject()
designer = Designer()
component_manager = ComponentManager()

# Initialize GUI Objects
loader.initialize(viewport, panels, components)
saver.initialize(viewport, panels, components)
new_project.initialize(viewport, panels, components, loader, designer, component_manager)
designer.initialize(viewport, panels, components, saver, component_manager)
component_manager.initialize(viewport, panels, components)
component_manager.editor_panel = designer.editor_panel

##########################################################
## GUI SYSTEM ##

# DPG GUI
dpg.create_context()
viewport.add()
dpg.setup_dearpygui()

# Create New Project Window
new_project.new_project_window()

# Set Safe Exit
dpg.set_exit_callback(saver.exit_callback)

# DPG GUI Start and Cleanup
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

##########################################################