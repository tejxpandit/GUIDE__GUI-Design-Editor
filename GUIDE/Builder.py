# Title : GUIDE : Builder
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : 8 April 2024

import dearpygui.dearpygui as dpg
from Components import Components

class Builder:
    def __init__(self):
        self.component_ref = Components()
        self.component = None

    def buildComponent(self, tag, component):
        arguments = ""
        for attr, attr_list in component["attributes"].items():
            argument = ""
            arg_val = attr_list[2]
            if not arg_val == None:
                if isinstance(arg_val, str):
                    arg_val = "'" + attr_list[2] + "'"
                else:
                    arg_val = str(attr_list[2])
                argument = attr + "=" + arg_val + ", "
            arguments += argument
        arguments = arguments.removesuffix(", ")
        command = "dpg." + component["function"] + "(" + arguments + ")"
        # print(command)
        exec(command)

    