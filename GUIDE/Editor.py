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