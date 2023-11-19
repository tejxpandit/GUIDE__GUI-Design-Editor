# Title : GUI Designer : Components Class
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Nov, 2023

import dearpygui.dearpygui as dpg

from gui_themes import Themes
from components.viewport import Viewport
from components.panel import Panel
from components.button import Button

class Components:
    def __init__(self):
        self.type = None
        self.component = None
        self.parameter = None
        self.editor_panel = None

        self.component_types = ["Panel", "Tab Group", "New Tab", "Group", "Button", "Slider", "Integer Input", "Float Input", "Dropdown Menu", "Checkbox", "Table"]
        
        self.component_params = dict()
        self.component_colors = dict()
        self.component_styles = dict()
        self.parameter_reference = dict()
        
        
        self.initialize_parameter_reference()
        self.initialize_component_params()
        self.initialize_component_colors()
        self.initialize_component_styles()

    def initialize_component_params(self):
        self.component_params.update({"Panel" : ["label", "position", "width", "height"]})
        self.component_params.update({"Panel" : ["label", "position", "width", "height"]})

    def initialize_component_colors(self):
        self.component_params.update({"Panel" : [dpg.mvThemeCol_TitleBg, dpg.mvThemeCol_TitleBgActive, dpg.mvThemeCol_WindowBg, dpg.mvThemeCol_Text]})

    def initialize_component_styles(self):
        self.component_params.update({"Panel" : [""]})

    def initialize_parameter_reference(self):
        self.parameter_reference.update({"label" : "string"})
        self.parameter_reference.update({"position" : "tuple2"})
        self.parameter_reference.update({"width" : "int"})
        self.parameter_reference.update({"height" : "int"})
        self.parameter_reference.update({"max" : "float"})
        self.parameter_reference.update({"min" : "float"})

        self.parameter_reference.update({"isFixed" : "bool"})
        self.parameter_reference.update({"isResizable" : "bool"})
        self.parameter_reference.update({"isHidden" : "bool"})
        self.parameter_reference.update({"isEnabled" : "bool"})

    def editor_change_parameter_callback(self, value):
        setattr(self.component, self.parameter, value)

    def build_editor_int_component(self, name):
        dpg.add_text(name + " :", parent=self.editor_panel)
        dpg.add_input_int(parent=self.editor_panel, callback=self.editor_change_parameter_callback)
