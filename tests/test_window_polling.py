# Title : GUI Builder Library : Can we poll windows by using global listners ?
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Dec, 2023

import dearpygui.dearpygui as dpg

# Functions
def test_callback(sender):
    print(sender)

def window_handler_callback(sender):
    window_key = dpg.get_active_window()
    print("Window Selected : " + str(window_key))

# DPG GUI
dpg.create_context()
dpg.create_viewport(title="Test")
dpg.setup_dearpygui()

# DPG Window
dpg.add_window(label="Test", tag="test_window")
dpg.add_group(tag="test_group", parent="test_window")

# Handler
with dpg.handler_registry(tag="window_handler") as handler:
    dpg.add_mouse_click_handler(callback=window_handler_callback)

# Component
dpg.add_button(label="Hello", tag="test_button", parent="test_group", callback=test_callback)
dpg.add_slider_int(label="Slider", tag="test_slider", parent="test_group", callback=test_callback)

# DPG GUI Start and Cleanup
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
