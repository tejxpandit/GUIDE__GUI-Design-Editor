# Title : GUI Designer : Saver Class
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Nov, 2023

import os
import pickle

class Saver:
    def __init__(self):
        self.gui_viewport
        self.gui_panels
        self.gui_components

        self.save_filename = "GUI_saved.pkl"
        self.data_files_list = []

    # Save GUI Components
    def save_data(self, ext=""):
        gui_all = []
        gui_all.append(self.gui_viewport)
        gui_all.append(self.gui_panels)
        gui_all.append(self.gui_components)
        pickle.dump(gui_all, open(ext + self.save_filename, 'wb'))