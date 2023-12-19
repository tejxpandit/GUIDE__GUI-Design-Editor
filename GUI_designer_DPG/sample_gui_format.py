# Title : GUI Builder Library : New GUI Data Format
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : Dec, 2023

# Make GUI Project Dictionary
project = dict()
census = dict()

# Component Numbering
census.update({"window" : 0})
census.update({"button" : 0})
census.update({"slider" : 0})

# Add to Windows to Project
name = "window " + census.get("window")
project.update({"Window 1" : "apple"})

# TODO : Finish template