# Title : Calculator App Example
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Nov, 2023

import math
import time
import dearpygui.dearpygui as dpg
from gui_themes import themes

####################

def update_output():
    dpg.set_value("output", output_display)

def update_output_live():
    dpg.set_value("output_live", str(output))

def bnumber(s, d, user_data):
    global output_display
    num = user_data
    if output_display == "0":
        output_display = str(num)
    elif output_display[-1] == "+" or output_display[-1] == "-" or output_display[-1] == "x" or output_display[-1] == "/":
        output_display = output_display + " " + str(num)
    else:
        output_display = output_display + str(num)
    parse_equation()
    update_output()
    update_output_live()

def bAC():
    global output, output_display, prev_output
    output = 0
    prev_output = 0
    output_display = "0"
    update_output()
    update_output_live()

def divide_by_zero_error():
    global output, output_display, prev_output
    output = 0
    prev_output = 0
    dpg.set_value("output_live", "Error : Cannot Divide by 0")
    time.sleep(2)
    output_display = "0"

def parse_equation():
    global output_display, output
    commands = output_display.split(' ')
    print(commands)
    output = prev_output
    prev_c = None
    num = 0
    for c in commands:
        if c == "+" or c == "-" or c == "x" or c == "/":
            prev_c = c
        else:
            if "." in c:
                num = float(c)
            else:
                num = int(c)

            if prev_c == "+":
                output = output + num
            elif prev_c == "-":
                output = output - num
            elif prev_c == "x":
                output = output * num
            elif prev_c == "/":
                if float(num) == float(0):
                    print("Error: Divide by Zero")
                    divide_by_zero_error()
                    return
                else:
                    output = output / num
            else:
                output = num

def bcommand(s, d, key):
    global output_display
    if output_display == "0":
        pass
    elif output_display[-1] == "+" or output_display[-1] == "-" or output_display[-1] == "x" or output_display[-1] == "/":
        pass
    else:
        output_display = output_display + " " + key
    parse_equation()
    update_output()
    update_output_live()
    
def bdecimal():
    global output_display
    if output_display[-1] == "+" or output_display[-1] == "-" or output_display[-1] == "x" or output_display[-1] == "/":
        pass
    else:
        output_display = output_display + "."
    update_output()
    pass

def bDEL():
    global output, output_display
    output_display = output_display[:-1]
    parse_equation()
    update_output()
    update_output_live()

def bequals():
    global output, output_display, prev_output
    parse_equation()
    output_display = str(output)
    prev_output = output
    output = 0 # CHECK
    update_output()
    update_output_live()

####################

theme = themes()
prev_output = 0
output = 0
output_display = "0"

# DPG GUI
dpg.create_context()
dpg.create_viewport(title="Calculator App", width=400, height=450, clear_color=theme.dark_green)
dpg.setup_dearpygui()

# CODE
dpg.add_window(label="Calculator", tag="main", no_close=True, pos=(0,0), width=400, height=450)
dpg.add_text("0", color=theme.dark_green, tag="output", parent="main", wrap=0)
dpg.add_text("", color=theme.dark_green, tag="output_live", parent="main")

dpg.add_group(tag="line0", parent="main", horizontal=True)
dpg.add_button(label="AC", callback=bAC, parent="line0", width=255, height=50)
dpg.add_button(label=chr(247), callback=bcommand, parent="line0", width=80, height=50, user_data="/")

dpg.add_group(tag="line1", parent="main", horizontal=True)
dpg.add_button(label="7", callback=bnumber, parent="line1", width=80, height=50, user_data=7)
dpg.add_button(label="8", callback=bnumber, parent="line1", width=80, height=50, user_data=8)
dpg.add_button(label="9", callback=bnumber, parent="line1", width=80, height=50, user_data=9)
dpg.add_button(label="x", callback=bcommand, parent="line1", width=80, height=50, user_data="x")

dpg.add_group(tag="line2", parent="main", horizontal=True)
dpg.add_button(label="4", callback=bnumber, parent="line2", width=80, height=50, user_data=4)
dpg.add_button(label="5", callback=bnumber, parent="line2", width=80, height=50, user_data=5)
dpg.add_button(label="6", callback=bnumber, parent="line2", width=80, height=50, user_data=6)
dpg.add_button(label="-", callback=bcommand, parent="line2", width=80, height=50, user_data="-")

dpg.add_group(tag="line3", parent="main", horizontal=True)
dpg.add_button(label="1", callback=bnumber, parent="line3", width=80, height=50, user_data=1)
dpg.add_button(label="2", callback=bnumber, parent="line3", width=80, height=50, user_data=2)
dpg.add_button(label="3", callback=bnumber, parent="line3", width=80, height=50, user_data=3)
dpg.add_button(label="+", callback=bcommand, parent="line3", width=80, height=50, user_data="+")

dpg.add_group(tag="line4", parent="main", horizontal=True)
dpg.add_button(label="0", callback=bnumber, parent="line4", width=80, height=50, user_data=0)
dpg.add_button(label=".", callback=bdecimal, parent="line4", width=80, height=50)
dpg.add_button(label="DEL", callback=bDEL, parent="line4", width=80, height=50)
dpg.add_button(label="=", callback=bequals, parent="line4", width=80, height=50)


####################

# GUI Theme Colors
with dpg.theme() as global_theme:
    with dpg.theme_component(dpg.mvAll):
        # Window Colors
        dpg.add_theme_color(dpg.mvThemeCol_TitleBg, theme.dark_green, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, theme.light_green, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_WindowBg, theme.white, category=dpg.mvThemeCat_Core)
        # Tab Colors
        dpg.add_theme_color(dpg.mvThemeCol_Tab, theme.dark_green, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TabActive, theme.light_green, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_TabHovered, theme.light_green, category=dpg.mvThemeCat_Core)
        # Slider Colors
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, theme.dark_green, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, theme.black, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, theme.light_green, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, theme.light_green, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, theme.dark_green, category=dpg.mvThemeCat_Core)
        # Button Colors
        dpg.add_theme_color(dpg.mvThemeCol_Button, theme.dark_green, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, theme.light_green, category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, theme.black, category=dpg.mvThemeCat_Core)
        # Component Styling
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 3, category=dpg.mvThemeCat_Core)
        dpg.set_global_font_scale(2)

        # # Font Colors
        # dpg.add_theme_color(dpg.mvThemeCol_Text, theme.black, category=dpg.mvThemeCat_Core)

dpg.bind_theme(global_theme)

# DPG GUI Start and Cleanup
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()




