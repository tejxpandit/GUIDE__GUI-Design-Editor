# Title : GUIDE : Project Manager
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : 7 April 2024

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
    
    def newProject(self):
        dpg.delete_item("project_manager_window")
        self.newProjectWindow()

    def loadProject(self):
        dpg.delete_item("project_manager_window")
        self.getProjectFiles()
        self.loadProjectWindow()

    # Load Project
    def loadProjectWindow(self):
        with dpg.window(label="Load Project", tag="load_project_window"):
            dpg.add_listbox(label="Saved Projects", tag="projects_listbox", callback=self.selectProject)
            dpg.add_button(label="Load Project", callback=self.loadProjectFile)
        dpg.configure_item("projects_listbox", items=self.project_files)

    def selectProject(self, sender, file_name):
        self.project_filename = file_name

    def getProjectFiles(self):
        for f in os.listdir(path=os.path.join(os.getcwd(), self.project_save_folder)):
            if f.endswith(".guide"):
                self.project_files.append(f)

    def loadProjectFile(self):
        with open(os.path.join(os.getcwd(), self.project_save_folder, self.project_filename), 'rb') as f:
            self.dataman.data, self.dataman.window_data, self.dataman.taggen.tag_id = pickle.load(f)
        self.reloadProject()

    def reloadProject(self):
        self.dataman.project_name = self.project_filename.removesuffix(".guide")
        dpg.delete_item("load_project_window")
        dpg.set_viewport_title(self.dataman.project_name)
        self.createGUIDEWindow()
        self.rebuildProject()

    # New Project
    def newProjectWindow(self):
        with dpg.window(label="New Project", tag="new_project_window"):
            dpg.add_input_text(label="Project Name", tag="project_name_text", default_value="Project_X", callback=self.newProjectName)
            dpg.add_button(label="Create New Project", callback=self.createNewProject)

    def newProjectName(self, sender, value):
        self.dataman.project_name = value

    def createNewProject(self):
        self.dataman.project_name = dpg.get_value("project_name_text")
        dpg.delete_item("new_project_window")
        dpg.set_viewport_title(self.dataman.project_name)
        self.createGUIDEWindow()

    # GUIDE Designer & Editor
    def createGUIDEWindow(self):
        dpg.add_window(label="GUI Design Editor", tag="guide", width=400, height=400)
        dpg.add_tab_bar(parent="guide", tag="guide_tabs")
        dpg.add_tab(label="Designer", parent="guide_tabs", tag="designer_tab")
        dpg.add_tab(label="Editor", parent="guide_tabs", tag="editor_tab")
        self.designer.createDesignerTab()

    # Rebuild Project
    def rebuildProject(self):
        for tag, component in self.dataman.data.items():
            self.builder.buildComponent(tag, component)
            if not component["data_type"] == "container":
                dpg.bind_item_handler_registry(tag, "selection_handler")
            if component["name"] == "Window":
                window_data = self.dataman.window_data[tag]
                dpg.configure_item(tag, width=window_data[0], height=window_data[1], pos=window_data[2])
            self.designer.selectComponent(0, 0, tag)
        self.designer.updateSelectionText()

    # Get Window [Width, Height and Position]
    def getWindowData(self):
        for tag, component in self.dataman.data.items():
            if component["name"] == "Window":
                window_data = [dpg.get_item_width(tag), dpg.get_item_height(tag), dpg.get_item_pos(tag)]
                self.dataman.window_data[tag] = window_data

    # Save Project --> On Exit
    def saveProjectOnExit(self):
        print("Saving Project : " + self.dataman.project_name)
        filename = self.dataman.project_name + '.guide'
        self.getWindowData()
        with open(os.path.join(os.getcwd(), self.project_save_folder, filename), 'wb') as f:
            pickle.dump([self.dataman.data, self.dataman.window_data, self.dataman.taggen.tag_id], f)
            print("Project Saved!")