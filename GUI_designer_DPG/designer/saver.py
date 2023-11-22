# Title : GUI Designer : Saver Class
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Nov, 2023

import os
import pickle

import dearpygui.dearpygui as dpg

class Saver:
    def __init__(self):
        self.viewport = None
        self.panels = None
        self.components = None

        self.save_filename = "GUI_saved.pkl"
        self.data_files_list = []

    # Initialize Loader Parameters
    def initialize(self, viewport, panels, components):
        self.viewport = viewport
        self.panels = panels
        self.components = components

    # Save GUI Components
    def save_data(self, ext=""):
        gui_data = []
        gui_data.append(self.viewport)
        gui_data.append(self.panels)
        gui_data.append(self.components)
        pickle.dump(gui_data, open(ext + self.save_filename, 'wb'))

    # Collect Window Data to Save
    def collect_panel_data(self):
        for panel_tag, panel in self.panels.items():
            panel.position = dpg.get_item_pos(panel_tag)
            panel.width = dpg.get_item_width(panel_tag)
            panel.height = dpg.get_item_height(panel_tag)

    # Handles Safe Exits
    def exit_callback(self):
        self.collect_panel_data()
        self.save_data("backup_")
        print("Safe Exit")