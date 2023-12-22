# Title : GUI Builder Library : New GUI Data Format
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Dec, 2023

from components import panel
from components import component

# CENSUS
# Make GUI Project Census Dictionary
census = dict()

# Component Numbering
census.update({"window" : 0})
census.update({"button" : 0})
census.update({"slider" : 0})

# Add or Remove Component from Census
census["window"] = census.get("window") + 1
census["window"] = census.get("window") - 1

#############################################

# WINDOWS
# Make GUI Project Window Dictionary
windows = dict()

# Add a Window to the Project
default_window_name = panel.type + "_" + census.get(panel.type)
windows.update({default_window_name : []})

#############################################

# COMPONENTS
# Make GUI Project Component Dictionary
components = dict()

# Add a Component to a Window
default_component_name = component.type + "_" + census.get(component.type)
components.update({default_component_name : []})

#############################################

# TODO : Finish template