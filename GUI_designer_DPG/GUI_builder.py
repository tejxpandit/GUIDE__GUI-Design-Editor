# Title : GUI Builder Library
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

class GUIBuilder:
    def __init__(self):
        # GUI Data
        self.viewport = Viewport()
        self.panels = dict()
        self.components = dict()

        # GUI Objects
        self.loader = Loader()
        self.saver = Saver()
        self.viewport = Viewport()
        self.new_project = NewProject()
        self.designer = Designer()
        self.component_manager = ComponentManager()

        # Initialize GUI Objects
        self.initialize()

    # Initialize GUI Objects
    def initialize(self):
        self.loader.initialize(self.viewport, self.panels, self.components)
        self.saver.initialize(self.viewport, self.panels, self.components)
        self.new_project.initialize(self.viewport, self.panels, self.components, self.loader, self.designer, self.component_manager)
        self.designer.initialize(self.viewport, self.panels, self.components, self.saver, self.component_manager)
        self.component_manager.initialize(self.viewport, self.panels, self.components)
        self.component_manager.editor_panel = self.designer.editor_panel

    # Run GUI
    def run(self):
        # DPG GUI
        dpg.create_context()
        self.viewport.add()
        dpg.setup_dearpygui()

        # Create New Project Window
        self.new_project.new_project_window()

        # Set Safe Exit
        dpg.set_exit_callback(self.saver.exit_callback)

        # DPG GUI Start and Cleanup
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()
