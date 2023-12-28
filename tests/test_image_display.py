# Title : GUI Builder Library : Testing Displaying Images
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : 28 Dec 2023

import dearpygui.dearpygui as dpg

# DPG GUI
dpg.create_context()
dpg.create_viewport(title="Test")
dpg.setup_dearpygui()

# Image Window
parent_tag = dpg.add_window(label="Image", autosize=True)

width, height, channels, data = dpg.load_image("./tests/plot.jpg")

with dpg.texture_registry():
    dpg.add_static_texture(width=width, height=height, default_value=data, tag="texture_tag")

resize = 0.2
resize_w = width*resize
resize_h = height*resize
dpg.add_image("texture_tag", parent=parent_tag, width=resize_w, height=resize_h, uv_min=(0.1,0.1), uv_max=(0.9, 0.9))

# TODO : Dynamic Image Update

# DPG GUI Start and Cleanup
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()