# Title : GUI Designer : Components Class
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Nov, 2023

import dearpygui.dearpygui as dpg

from viewport import Viewport
from panel import Panel
from button import Button

class Components:
    def __init__(self):
        self.component = None
        self.editor_panel = None

        self.component_types = ["Panel", "Tab Group", "New Tab", "Group", "Button", "Slider", "Input (Integer)", "Input (Float)", "Dropdown Menu", "Checkbox", "Table"]
        
        self.parameter_reference = dict()
        self.color_reference = dict()
        self.style_reference = dict()
        self.initialize_parameter_reference()
        self.initialize_color_reference()
        self.initialize_style_reference()

        self.component_params = dict()
        self.component_colors = dict()
        self.component_styles = dict()
        self.initialize_component_params()
        self.initialize_component_colors()
        self.initialize_component_styles()

    # COMPONENT FIELDS
    def initialize_component_params(self):
        self.component_params.update({"Panel" : ["label", "position", "width", "height"]})
        self.component_params.update({"Button" : ["label", "parent", "callback", "width", "height"]})

    def initialize_component_colors(self):
        self.component_params.update({"Panel" : ["title background", "title background active", "window background", "text color"]})
        self.component_params.update({"Button" : ["button color", "button hovered color", "button active color", "text color"]})

    def initialize_component_styles(self):
        self.component_params.update({"Panel" : []})
        self.component_params.update({"Button" : ["frame rounding"]})

    # COMPONENT TYPES
    def initialize_parameter_reference(self):
        self.parameter_reference.update({"label" : "string"})
        self.parameter_reference.update({"position" : "int2"})
        self.parameter_reference.update({"width" : "int"})
        self.parameter_reference.update({"height" : "int"})
        self.parameter_reference.update({"max" : "float"})
        self.parameter_reference.update({"min" : "float"})

        self.parameter_reference.update({"parent" : "int"}) # or "string"
        self.parameter_reference.update({"calllback" : "string"})

        self.parameter_reference.update({"isFixed" : "bool"})
        self.parameter_reference.update({"isResizable" : "bool"})
        self.parameter_reference.update({"isHidden" : "bool"})
        self.parameter_reference.update({"isEnabled" : "bool"})

    def initialize_color_reference(self):
        self.color_reference.update({"text color" : dpg.mvThemeCol_Text})

        self.color_reference.update({"title background" : dpg.mvThemeCol_TitleBg})
        self.color_reference.update({"title background active" : dpg.mvThemeCol_TitleBgActive})
        self.color_reference.update({"window background" : dpg.mvThemeCol_WindowBg})
        
        self.color_reference.update({"button color" : dpg.mvThemeCol_Button})
        self.color_reference.update({"button hovered color" : dpg.mvThemeCol_ButtonHovered})
        self.color_reference.update({"button active color" : dpg.mvThemeCol_ButtonActive})

    def initialize_style_reference(self):
        self.style_reference.update({"frame rounding" : dpg.mvStyleVar_FrameRounding})

    # COMPONENT EDITOR CALLBACKS
    def editor_change_parameter_callback(self, sender, value, parameter):
        setattr(self.component, parameter, value) # parameter is user_data (string) passed from editor component. 

    # COMPONENT TYPE BUILDERS
    def build_editor_int_component(self, name):
        dpg.add_text(name + " :", parent=self.editor_panel)
        dpg.add_input_int(parent=self.editor_panel, callback=self.editor_change_parameter_callback, user_data=name)

    def build_editor_float_component(self, name):
        dpg.add_text(name + " :", parent=self.editor_panel)
        dpg.add_input_float(parent=self.editor_panel, callback=self.editor_change_parameter_callback, user_data=name)

    def build_editor_string_component(self, name):
        dpg.add_text(name + " :", parent=self.editor_panel)
        dpg.add_input_text(parent=self.editor_panel, callback=self.editor_change_parameter_callback, user_data=name)

    def build_editor_int2_component(self, name):
        dpg.add_text(name + " :", parent=self.editor_panel)
        dpg.add_input_intx(parent=self.editor_panel, size=2, callback=self.editor_change_parameter_callback, user_data=name)
    
    def build_editor_bool_component(self, name):
        dpg.add_text(name + " :", parent=self.editor_panel)
        dpg.add_checkbox(parent=self.editor_panel, callback=self.editor_change_parameter_callback, user_data=name)

    # COMPONENT BUILD PARSER
        # TODO : Build Editor for all parameters of a selected component. 