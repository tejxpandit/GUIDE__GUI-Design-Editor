# Title : GUI Designer : Designer Theme
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Nov, 2023

import dearpygui.dearpygui as dpg

class DesignerTheme:
    def __init__(self):

        # LIGHT COLORS
        self.white = (255,255,255)
        self.light_grey = (221,221,221)
        self.light_green = (29,120,116)

        # DARK COLORS
        self.black = (0,0,0)
        self.dark_green = (7,30,34)
        self.dark_grey = (100,100,100)
         
        # MEDIUM COLORS
        self.med_grey = (180,180,180)

        # GUI THEMES
        self.isDarkMode = True

        # GUI THEME PARAMETERS
        self.active_col = self.dark_green
        self.inactive_col = self.light_grey

    def enableDarkMode(self):
        self.isDarkMode = True

    def disableDarkMode(self):
        self.isDarkMode = False

    def get_designer_theme(self):
        # GUI Theme Colors
        with dpg.theme() as designer_theme:
            with dpg.theme_component(dpg.mvAll):
                # Window Colors
                dpg.add_theme_color(dpg.mvThemeCol_TitleBg, self.dark_green, category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_TitleBgActive, self.light_green, category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_WindowBg, self.white, category=dpg.mvThemeCat_Core)
                # Tab Colors
                dpg.add_theme_color(dpg.mvThemeCol_Tab, self.dark_green, category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_TabActive, self.light_green, category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_TabHovered, self.light_green, category=dpg.mvThemeCat_Core)
                # Slider Colors
                dpg.add_theme_color(dpg.mvThemeCol_FrameBg, self.dark_green, category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, self.black, category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, self.light_green, category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, self.light_green, category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, self.dark_green, category=dpg.mvThemeCat_Core)
                # Button Colors
                dpg.add_theme_color(dpg.mvThemeCol_Button, self.dark_green, category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, self.light_green, category=dpg.mvThemeCat_Core)
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, self.black, category=dpg.mvThemeCat_Core)
                # Component Styling
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 3, category=dpg.mvThemeCat_Core)
                # # Font Colors
                # dpg.add_theme_color(dpg.mvThemeCol_Text, theme.black, category=dpg.mvThemeCat_Core)
            
        return designer_theme
    