# Title : GUIDE : Editor
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : 25 April 2024

import copy as cpy
import dearpygui.dearpygui as dpg
from Components import Components
from Builder import Builder

class Editor:
    def __init__(self, dataman):
        self.dataman = dataman
        self.designer = None
        self.taggen = dataman.taggen
        self.component_ref = Components()
        self.builder = Builder()
        self.component = None
        self.tag = None