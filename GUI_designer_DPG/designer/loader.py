# Title : GUI Designer : Loader Class
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Nov, 2023

import os
import pickle

class Loader:
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
        self.get_data_filenames()

    # Load Saved GUI Components
    def load_data(self):
        if os.path.isfile(os.getcwd() + '\\' + self.save_filename):    
            with open(self.save_filename, 'rb') as file: 
                gui_all = pickle.load(file)
                self.viewport = gui_all[0]
                self.panels = gui_all[1]
                self.components = gui_all[2]
                print("Loaded : " + self.save_filename)
        else:
            print("No such data file")
            quit()

    # Get all GUI data filenames
    def get_data_filenames(self):
        for filename in os.listdir(os.getcwd()):
            if filename.endswith(".pkl"):
                self.data_files_list.append(filename)
        # print(self.data_files_list)
