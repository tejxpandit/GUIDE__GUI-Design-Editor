# Title : GUI Designer : Themes
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Nov, 2023

class Themes:
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
