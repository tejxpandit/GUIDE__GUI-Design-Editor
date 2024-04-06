# Title : GUIDE : Project Manager
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : 5 April 2024

import os
import pickle
import dearpygui.dearpygui as dpg
from Designer import Designer
from Editor import Editor
from Builder import Builder

class ProjectManager:
    def __init__(self, dataman):
        self.project_files = []
        self.project_filename = ""
        self.project_save_folder = "saved projects"
        self.dataman = dataman
        self.designer = Designer(dataman)
        self.editor = Editor(dataman)
        self.builder = Builder()
        self.designer.editor = self.editor
        self.editor.designer = self.designer

    # Project Manager
    def projectManagementWindow(self):
        with dpg.window(label="Project Manager", tag="project_manager_window", width=400, height=200):
            dpg.add_button(label="Load Project", callback=self.loadProject)
            dpg.add_button(label="New Project", callback=self.newProject)
    