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
        self.components = {
            # Button
            "button" : {
                "name"          : "Button",
                "data_type"     : "trigger",
                "function"      : "add_button",
                "children"      : None,
                "attributes"    : {
                    "label"         : ["Label", "identifier", "Button"],
                    "tag"           : ["Tag", "identifier", None],
                    "parent"        : ["Parent", "identifier", None],
                    "callback"      : ["Function", "function", None],

                    "user_data"     : ["User Data", "any", None],
                    "width"         : ["Width", "int", None],
                    "height"        : ["Height", "int", None],
                    "pos"           : ["Position", "tuple2", None],
                    "show"          : ["Visible", "bool", True],
                    "enabled"       : ["Enabled", "bool", True]
                }
            },
            # CheckBox
            "checkbox" : {
                "name"          : "CheckBox",
                "data_type"     : "bool",
                "function"      : "add_checkbox",
                "children"      : None,
                "attributes"    : {
                    "label"         : ["Label", "identifier", "CheckBox"],
                    "tag"           : ["Tag", "identifier", None],
                    "parent"        : ["Parent", "identifier", None],
                    "callback"      : ["Function", "function", None],
                    "default_value" : ["Default Value", "bool", False],
                    
                    "user_data"     : ["User Data", "any", None],
                    "width"         : ["Width", "int", None],
                    "height"        : ["Height", "int", None],
                    "pos"           : ["Position", "tuple2", None],
                    "show"          : ["Visible", "bool", True],
                    "enabled"       : ["Enabled", "bool", True]
                }
            },
            # Slider (Int)
            "slider_int" : {
                "name"          : "Slider (Int)",
                "data_type"     : "int",
                "function"      : "add_slider_int",
                "children"      : None,
                "attributes"    : {
                    "label"         : ["Label", "identifier", "Slider Int"],
                    "tag"           : ["Tag", "identifier", None],
                    "parent"        : ["Parent", "identifier", None],
                    "callback"      : ["Function", "function", None],
                    "default_value" : ["Default Value", "int", 20],
                    "min_value"     : ["Minimum", "int", 0],
                    "max_value"     : ["Maximum", "int", 100],

                    "user_data"     : ["User Data", "any", None],
                    "width"         : ["Width", "int", None],
                    "height"        : ["Height", "int", None],
                    "pos"           : ["Position", "tuple2", None],
                    "vertical"      : ["Vertical", "bool", False],
                    "show"          : ["Visible", "bool", True],
                    "enabled"       : ["Enabled", "bool", True]
                }
            },
            # Slider (Float)
            "slider_float" : {
                "name"          : "Slider (Float)",
                "data_type"     : "float",
                "function"      : "add_slider_float",
                "children"      : None,
                "attributes"    : {
                    "label"         : ["Label", "identifier", "Slider Float"],
                    "tag"           : ["Tag", "identifier", None],
                    "parent"        : ["Parent", "identifier", None],
                    "callback"      : ["Function", "function", None],
                    "default_value" : ["Default Value", "int", 0.2],
                    "min_value"     : ["Minimum", "float", 0.0],
                    "max_value"     : ["Maximum", "float", 1.0],

                    "user_data"     : ["User Data", "any", None],
                    "width"         : ["Width", "int", None],
                    "height"        : ["Height", "int", None],
                    "pos"           : ["Position", "tuple2", None],
                    "vertical"      : ["Vertical", "bool", False],
                    "show"          : ["Visible", "bool", True],
                    "enabled"       : ["Enabled", "bool", True]
                }
            },
            # Input (Int)
            "input_int" : {
                "name"          : "Input (Int)",
                "data_type"     : "int",
                "function"      : "add_input_int",
                "children"      : None,
                "attributes"    : {
                    "label"         : ["Label", "identifier", "Input Int"],
                    "tag"           : ["Tag", "identifier", None],
                    "parent"        : ["Parent", "identifier", None],
                    "callback"      : ["Function", "function", None],
                    "default_value" : ["Default Value", "int", 0],
                    "min_value"     : ["Minimum", "int", 0],
                    "max_value"     : ["Maximum", "int", 100],

                    "user_data"     : ["User Data", "any", None],
                    "width"         : ["Width", "int", None],
                    "height"        : ["Height", "int", None],
                    "pos"           : ["Position", "tuple2", None],
                    "step"          : ["Step", "float", 1], # TODO: Reconsider : Make Step Default Value = None
                    "show"          : ["Visible", "bool", True],
                    "enabled"       : ["Enabled", "bool", True],
                    "readonly"      : ["Read-Only", "bool", False]
                }
            },
            # Input (Float)
            "input_float" : {
                "name"          : "Input (Float)",
                "data_type"     : "float",
                "function"      : "add_input_float",
                "children"      : None,
                "attributes"    : {
                    "label"         : ["Label", "identifier", "Input Float"],
                    "tag"           : ["Tag", "identifier", None],
                    "parent"        : ["Parent", "identifier", None],
                    "callback"      : ["Function", "function", None],
                    "default_value" : ["Default Value", "float", 0.0],
                    "min_value"     : ["Minimum", "float", 0.0],
                    "max_value"     : ["Maximum", "float", 1.0],
                    
                    "user_data"     : ["User Data", "any", None],
                    "width"         : ["Width", "int", None],
                    "height"        : ["Height", "int", None],
                    "pos"           : ["Position", "tuple2", None],
                    "step"          : ["Step", "float", 0.1], # TODO: Reconsider : Make Step Default Value = None
                    "show"          : ["Visible", "bool", True],
                    "enabled"       : ["Enabled", "bool", True],
                    "readonly"      : ["Read-Only", "bool", False]
                }
            },
            # Input (Text)
            "input_text" : {
                "name"          : "Input (Text)",
                "data_type"     : "string",
                "function"      : "add_input_text",
                "children"      : None,
                "attributes"    : {
                    "label"         : ["Label", "identifier", "Input Text"],
                    "tag"           : ["Tag", "identifier", None],
                    "parent"        : ["Parent", "identifier", None],
                    "callback"      : ["Function", "function", None],
                    "default_value" : ["Default Value", "string", None],
                    "multiline"     : ["Multi-Line", "bool", False],

                    "user_data"     : ["User Data", "any", None],
                    "width"         : ["Width", "int", None],
                    "height"        : ["Height", "int", None],
                    "pos"           : ["Position", "tuple2", None],
                    "show"          : ["Visible", "bool", True],
                    "enabled"       : ["Enabled", "bool", True],
                    "readonly"      : ["Read-Only", "bool", False],
                    "password"      : ["Password", "bool", False],
                    "uppercase"     : ["Uppercase", "bool", False],
                    "scientific"    : ["Scientific", "bool", False],
                    "hexadecimal"   : ["Hexadecimal", "bool", False]
                }
            },
            # Text
            "text" : {
                "name"          : "Text",
                "data_type"     : "string",
                "function"      : "add_text",
                "children"      : None,
                "attributes"    : {
                    "tag"           : ["Tag", "identifier", None],
                    "parent"        : ["Parent", "identifier", None],
                    "default_value" : ["Text", "string", "Text"],

                    "user_data"     : ["User Data", "any", None],
                    "pos"           : ["Position", "tuple2", None],
                    "show"          : ["Visible", "bool", True],
                    "wrap"          : ["Wrap Text Distance", "int", -1],
                    "bullet"        : ["Bullet Point", "bool", False],
                    "label"         : ["Additional Label", "identifier", None]
                }
            },
            # ListBox
            "listbox" : {
                "name"          : "ListBox",
                "data_type"     : "string",
                "function"      : "add_listbox",
                "children"      : None,
                "attributes"    : {
                    "label"         : ["Label", "identifier", "ListBox"],
                    "tag"           : ["Tag", "identifier", None],
                    "parent"        : ["Parent", "identifier", None],
                    "callback"      : ["Function", "function", None],
                    "items"         : ["Python List", "list(string)", None],
                    "default_value" : ["Default Value", "string", None],
                    "num_items"     : ["# Rows Visible", "int", 3],

                    "user_data"     : ["User Data", "any", None],
                    "width"         : ["Width", "int", None],
                    "pos"           : ["Position", "tuple2", None],
                    "show"          : ["Visible", "bool", True],
                    "enabled"       : ["Enabled", "bool", True]
                }
            },
            # Tree Node
            "tree_node" : {
                "name"          : "TreeNode",
                "data_type"     : "container",
                "function"      : "add_tree_node",
                "children"      : [],
                "attributes"    : {
                    "label"         : ["Label", "identifier", "TreeNode"],
                    "tag"           : ["Tag", "identifier", None],
                    "parent"        : ["Parent", "identifier", None],

                    "default_open"  : ["Default Open", "bool", False],
                    "open_on_double_click" : ["Double Click to Open", "bool", False],
                    "open_on_arrow" : ["Click Arrow (Only) to Open", "bool", False],
                    "leaf"          : ["Always Open", "bool", False],
                    "bullet"        : ["Bullet Point", "bool", False],
                    "selectable"    : ["Highlight when Open", "bool", False],
                    "pos"           : ["Position", "tuple2", None],
                    "show"          : ["Visible", "bool", True],
                    "user_data"     : ["User Data", "any", None]
                }
            },
            # Group
            "group" : {
                "name"          : "Group",
                "data_type"     : "container",
                "function"      : "add_group",
                "children"      : [],
                "attributes"    : {
                    "tag"           : ["Tag", "identifier", None],
                    "parent"        : ["Parent", "identifier", None],
                    "horizontal"    : ["Horizontal Layout", "bool", False],

                    "horizontal_spacing" : ["Horizontal Spacing", "float", None],
                    "pos"           : ["Position", "tuple2", None],
                    "show"          : ["Visible", "bool", True],
                    "label"         : ["Invisible Label", "identifier", "Group"],
                    "user_data"     : ["User Data", "any", None]
                }
            },
            # Window
            "window" : {
                "name"          : "Window",
                "data_type"     : "container",
                "function"      : "add_window",
                "children"      : [],
                "attributes"    : {
                    "label"         : ["Label", "identifier", "Window"],
                    "tag"           : ["Tag", "identifier", None],

                    "width"         : ["Width", "int", None],
                    "height"        : ["Height", "int", None],
                    "pos"           : ["Position", "tuple2", None],
                    "show"          : ["Visible", "bool", True], 
                    "on_close"      : ["Function When Closed", "function", None],
                    "no_title_bar"  : ["Hide Title Bar", "bool", False],
                    "menubar"       : ["Show Menu Bar", "bool", True],
                    "collapsed"     : ["Window Minimized", "bool", False],
                    "no_collapse"   : ["Disallow Minimize", "bool", False],
                    "autosize"      : ["Autosize", "bool", False],
                    "no_resize"     : ["Disallow Resizing", "bool", False],
                    "no_move"       : ["Disallow Moving", "bool", False],
                    "no_close"      : ["Disallow Closing", "bool", False],
                    "no_scrollbar"  : ["Disallow Scrolling", "bool", False],
                    "no_background" : ["Remove Background", "bool", False],
                    "modal"         : ["Block Other Windows", "bool", False],
                    "popup"         : ["Popup", "bool", False],
                    "no_focus_on_appearing" : ["No Focus on Spawn", "bool", False],
                    "user_data"     : ["User Data", "any", None],
                }
            }
        }
    
    def Containers(self):
        self.containers = {
        }

    def Attributes(self):
        # self.attr_all = {
        #         "label",
        #         "tag",
        #         "callback",
        #         "on_close",

        #         "width",
        #         "height",
        #         "pos",
        #         "show",
        #         "no_title_bar",
        #         "menubar",
        #         "collapsed",
        #         "no_collapse",
        #         "autosize",
        #         "no_resize",
        #         "no_move",
        #         "no_close",
        #         "no_scrollbar",
        #         "no_background",
        #         "modal",
        #         "popup",
        #         "no_focus_on_appearing",
        #         "readonly",
        #         "password",
        #         "uppercase",
        #         "scientific",
        #         "hexadecimal",
        #         "user_data"
        # }
        self.attr_permenant = [
            "name", "data_type"
        ]
        self.attr_mandatory = [
            "label", "tag", "parent", "callback", "items", "default_value", "min_value", "max_value"
        ]
        # self.attr_optional --> All other attributes are by default optional
        self.attr_types = {
            "identifier"        : "input_text",
            "int"               : "input_int",
            "tuple2"            : "input_intx", # Limit inputs to 2
            "float"             : "input_float",
            "bool"              : "checkbox",
            "string"            : "input_text",
            "list(string)"      : "input_text", # Special Handling
            "function"          : "input_text", # RECHECK THIS <-- Maybe Function Names should be auto generated
            "any"               : "input_text"  # Limited to a string currently
        }