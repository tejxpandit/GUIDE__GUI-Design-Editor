# Title : GUI Builder Library : Can we attach listners to all components ?
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Dec, 2023

import dearpygui.dearpygui as dpg

# Functions
def test_callback(sender):
    print(sender)

def handler_callback(sender):
    print("Item Clicked")

# DPG GUI
dpg.create_context()
dpg.create_viewport(title="Test")
dpg.setup_dearpygui()

# DPG Window
dpg.add_window(label="Test", tag="test_window")
dpg.add_group(tag="test_group", parent="test_window")

# Handler
with dpg.item_handler_registry(tag="click_handler") as handler:
    dpg.add_item_clicked_handler(callback=handler_callback)

# Component
dpg.add_button(label="Hello", tag="test_button", parent="test_group", callback=test_callback)
dpg.add_slider_int(label="Slider", tag="test_slider", parent="test_group", callback=test_callback)

# Bind Component to Handler
dpg.bind_item_handler_registry("test_slider", "click_handler")

# Bind Group to Handler
dpg.bind_item_handler_registry("test_group", "click_handler")

# DPG GUI Start and Cleanup
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
