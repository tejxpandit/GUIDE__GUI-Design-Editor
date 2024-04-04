# Title : GUIDE Launcher
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : 1 April 2024

import dearpygui.dearpygui as dpg
from ProjectManager import ProjectManager
from DataManager import DataManager

# DPG Context
dpg.create_context()

# DPG Viewport
dpg.create_viewport(title="GUIDE : GUI Design Editor", width=1200, height=400)

# Data Manager
dataman = DataManager()

# DPG Window
projectman = ProjectManager(dataman)
projectman.projectManagementWindow()
dpg.set_exit_callback(projectman.saveProjectOnExit)

# DPG Render Context
dpg.setup_dearpygui()
dpg.show_viewport()

# after "dpg.show_viewport()"
###### For DEBUGGING ######
dpg.configure_app(manual_callback_management=True)
while dpg.is_dearpygui_running():
    jobs = dpg.get_callback_queue()
    dpg.run_callbacks(jobs)
    dpg.render_dearpygui_frame()
##########################
# before "dpg.destroy_context()"
# comment out "dpg.start_dearpygui()"

#dpg.start_dearpygui()
dpg.destroy_context()