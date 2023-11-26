# Title : GUI Code Generator
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Nov, 2023

import random

class CodeGenerator():
    def __init__(self):
        self.components = None

        self.code_filename = "myGui.py"
        self.callback_component_list = ["Button", "Checkbox", "Slider"] # classnames with callbacks
        self.function_names_list = []

        self.code = "# CALLBACK FUNCTIONS : \n\n"
    
    # Initialize Loader Parameters
    def initialize(self, components):
        self.components = components

    # Generate All Callback Functions
    def add_functions(self):
        code = ""
        for tag, component in self.components.items():
            if component.classname in self.callback_component_list:
                label = component.label
                name = self.generate_func_name(label)
                
                func_code = "def " + name + "(component_id, value, special_value=\"optional\"):\n"
                func_code += "\t# Your Function Code"
                func_code += "\tpass\n\n"
                code += func_code
        self.code += code
    
    # Generate Callback Function Names
    def generate_func_name(self, label):
        name = ""
        word = word.replace("!@#$%^&*()_+:;[]", "")
        words = label.split()
        for word in words:
            name += word + "_"
        name.pop()

        if name not in self.function_names_list:
            self.function_names_list.append(name)
        else:
            name += "_" + random.randint(0,99)
        return name
    
    # Save Code to File
    def save_code(self):
        with open(self.code_filename, 'w') as f:
            f.write(self.code)