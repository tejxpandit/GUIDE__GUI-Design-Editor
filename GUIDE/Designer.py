# Title : GUIDE : Designer
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : 10 April 2024

import copy as cpy
import dearpygui.dearpygui as dpg
from Components import Components
from Builder import Builder
from CodeGenerator import CodeGenerator

class Designer:
    def __init__(self, dataman):
        self.dataman = dataman
        self.editor = None
        self.taggen = dataman.taggen
        self.component_ref = Components()
        self.builder = Builder()
        self.codegen = CodeGenerator(dataman)
        self.selectionManager()
    
