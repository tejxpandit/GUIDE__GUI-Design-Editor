# Title : GUI Designer : Components Class
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Nov, 2023

import dearpygui.dearpygui as dpg

from gui_themes import Themes

from .panel import Panel
from .button import Button

class Components:
    def __init__(self):
        # GLOBAL VARIABLES
        self.panels = None
        self.components = None
        self.component = None # self.component = current active component
        self.editor_panel = None
        self.colors = Themes()

        # COMPONENT LIST
        self.component_types = ["Panel", "Tab Group", "New Tab", "Group", "Button", "Slider", "Input (Integer)", "Input (Float)", "Dropdown Menu", "Checkbox", "Table"]

        # COMPONENT PARAMETER / COLOR / STYLE LISTS
        self.component_params = dict()
        self.component_colors = dict()
        self.component_styles = dict()
        self.initialize_component_params()
        self.initialize_component_colors()
        self.initialize_component_styles()

        # COMPONENT PARAMETER / COLOR / STYLE TYPE REFERENCE LISTS
        self.parameter_reference = dict()
        self.color_reference = dict()
        self.style_reference = dict()
        self.initialize_parameter_reference()
        self.initialize_color_reference()
        self.initialize_style_reference()

    # COMPONENT FIELDS
    def initialize_component_params(self):
        self.component_params.update({"Panel" : ["label", "position", "width", "height"]})
        self.component_params.update({"Button" : ["label", "parent", "callback", "width", "height"]})

    def initialize_component_colors(self):
        self.component_colors.update({"Panel" : ["title background", "title background active", "window background", "text color"]})
        self.component_colors.update({"Button" : ["button color", "button hovered color", "button active color", "text color"]})

    def initialize_component_styles(self):
        self.component_styles.update({"Panel" : []})
        self.component_styles.update({"Button" : ["frame rounding"]})

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

    # COMPONENT EDITOR TYPE BUILDERS
    def build_editor_int_component(self, parameter):
        dpg.add_text(parameter + " :", color=self.colors.dark_green, parent=self.editor_panel)
        dpg.add_input_int(parent=self.editor_panel, callback=self.editor_change_parameter_callback, user_data=parameter)

    def build_editor_float_component(self, parameter):
        dpg.add_text(parameter + " :", color=self.colors.dark_green, parent=self.editor_panel)
        dpg.add_input_float(parent=self.editor_panel, callback=self.editor_change_parameter_callback, user_data=parameter)

    def build_editor_string_component(self, parameter):
        dpg.add_text(parameter + " :", color=self.colors.dark_green, parent=self.editor_panel)
        dpg.add_input_text(parent=self.editor_panel, callback=self.editor_change_parameter_callback, user_data=parameter)

    def build_editor_int2_component(self, parameter):
        dpg.add_text(parameter + " :", color=self.colors.dark_green, parent=self.editor_panel)
        dpg.add_input_intx(parent=self.editor_panel, size=2, callback=self.editor_change_parameter_callback, user_data=parameter)
    
    def build_editor_bool_component(self, parameter):
        dpg.add_text(parameter + " :", color=self.colors.dark_green, parent=self.editor_panel)
        dpg.add_checkbox(parent=self.editor_panel, callback=self.editor_change_parameter_callback, user_data=parameter)

    # COMPONENT EDITOR BUILD PARAMETER PARSER
    def add_editor_component_parameter_type(self, parameter, type):
        if type == "int":
            self.build_editor_int_component(parameter)
        elif type == "float":
            self.build_editor_float_component(parameter)
        elif type == "string":
            self.build_editor_string_component(parameter)
        elif type == "bool":
            self.build_editor_bool_component(parameter)
        elif type == "int2":
            self.build_editor_int2_component(parameter)

    def add_editor_component_parameter(self, parameter):
        type = self.parameter_reference.get(parameter)
        self.add_editor_component_parameter_type(parameter, type)
    
    # COMPONENT EDITOR PARAMETER BUILDER
    def add_editor_component(self, component):
        # Clear Editor Panel
        dpg.delete_item(item=self.editor_panel, children_only=True)
        # Get and add all Component Parameters
        params = self.component_params.get(component)
        for param in params:
            self.add_editor_component_parameter(param)
        # Add Update and Delete Buttons
        self.add_editor_component_update_button()
        self.add_editor_component_delete_button()

    # ADD COMPONENT UPDATE BUTTON
    def add_editor_component_update_button(self):
        dpg.add_button(label="UPDATE", parent=self.editor_panel, callback=self.component.update)

    # ADD COMPONENT DELETE BUTTON
    def add_editor_component_delete_button(self):
        dpg.add_button(label="DELETE", parent=self.editor_panel, callback=self.component.delete)

    # COMPONENT BUILDER
    def add_component(self, component): # component is a "string" here
        if component == "Panel":
            # Create Component Object
            panel = Panel()
            # Add Component to Components Dict with Tag as Key
            self.panels.update({panel.tag : panel})
            # Set Component as Active Component
            self.component = panel
            # Add Component to Editor Panel (along with all parameters)
            self.add_editor_component(panel.classname)
            
        # TODO : Add other components
        

    # COMPONENT CALLBACK : SET ACTIVE COMPONENT FOR EDITOR
    def set_active_component_callback(self, sender, value):
        # Set Component as Active Component
        self.component = self.components.get(sender)
        # Add Component to Editor Panel (along with all parameters)
        self.add_editor_component(self.component.classname)
