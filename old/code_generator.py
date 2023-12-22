# Title : GUI Code Generator
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Nov, 2023

import random

# TODO : Maybe consider putting all the functions in a separate code file

class CodeGenerator():
    def __init__(self):
        self.components = None

        self.code_filename = "myGui.py"
        self.callback_component_list = ["Button", "Checkbox", "Slider"] # classnames with callbacks
        self.function_names_list = []

        self.code = ""
    
    # Initialize Loader Parameters
    def initialize(self, components):
        self.components = components

    # Generate All Callback Functions
    def add_functions(self):
        self.code += "# CALLBACK FUNCTIONS : \n\n"
        code = ""
        for tag, component in self.components.items():
            if component.classname in self.callback_component_list:
                label = component.label
                name = self.generate_func_name(label)
                
                func_code = "def " + name + "(component_id, value, special_value=\"optional\"):\n"
                func_code += "\t# Your Function Code\n"
                func_code += "\tpass\n\n"
                code += func_code
        self.code += code

    # Default callback function (for undefined callbacks in GUI)
    def add_default_callback(self):
        code = "# DEFAULT CALLBACK FUNCTION : \n\n"
        code += "def default_callback(component_id, value, special_value=\"nothing\"):\n"
        code += "\tprint(\"Component : \" + str(component_id) + \" has no callback\")\n"
        code += "\tprint(\"Value = \" + str(value))\n"
        code += "\tprint(\"Special Value = \" + str(special_value))\n"
        code += "\tpass\n\n"
        self.code += code

    # Generate function list connector
    def connect_functions(self):
        code = "# CONNECT FUNCTIONS TO DPG : \n\n"
        pass

    
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