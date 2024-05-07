# Title : GUIDE : Code Generator
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : 6 May 2024

import os
import pickle
import dearpygui.dearpygui as dpg
from Builder import Builder

class CodeGenerator:
    def __init__(self, dataman):
        self.dataman = dataman
        self.code_export_folder = "export"
        self.code_template_folder = "code template"
        self.builder = Builder()
        self.code = ""
        self.classCode = ""
        
        # Code Formats
        self.snippet_callback_function = """# $FUNCNAME$
        def $FUNCNAME$(self, sender, value, data):
        \tself.$VARNAME$ = value
        """

    def exportCode(self):
        dpg_UI_commands = ""
        for tag, component in self.dataman.data.items():
            command = self.builder.buildComponent(tag, component)