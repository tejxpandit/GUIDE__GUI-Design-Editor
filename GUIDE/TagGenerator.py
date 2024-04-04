# Title : GUIDE : Tag Generator
# Project : GUI Designer DearPyGUI
# Author : Tej Pandit
# Date : 3 April 2024

class TagGenerator:
    def __init__(self):
        self.tag_id = 0
        self.list_id = []
        self.max_id = 10000
    
    def generateTag(self, name):
        self.addComponent()
        tag = name + "_" + str(self.tag_id)
        return tag
    
    def addComponent(self):
        self.tag_id += 1
        self.list_id.append(self.tag_id)

    def removeComponent(self, name_id):
        words = name_id.split("_")
        id = words[1]
        try:
            self.list_id.remove(id)
        except:
            print("no such component ID : " + str(id))

    # Clean-Up Unused IDs Later