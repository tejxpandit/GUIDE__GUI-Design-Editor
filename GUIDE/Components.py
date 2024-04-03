# Title : GUIDE : Component Dictionary
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : 1 April 2024

import dearpygui.dearpygui as dpg

class Components:
    def __init__(self):
        self.components = None
        self.containers = None
        self.attr_func = None
        self.attr_types = None
        self.attr_defaults = None
        self.attr_mandatory = None
        self.attr_permenant = None
        self.Components()
        self.Components()
        self.Attributes()

    def Components(self):
            # Component Format
            # comp_id : {
            #     "name"          : "Display Name",
            #     "data_type"     : "Data Type",
            #     "function"      : "dpg add_function",
            #     "children"      : [] or None
            #     "attributes"    : {
            #         "attr_1"        : ["attr_1_label", "attr_1_type", attr_1_default_value],
            #         "attr_2"        : ["attr_2_label", "attr_2_type", attr_2_default_value],
            #         ....
            #     }
            # }
        pass