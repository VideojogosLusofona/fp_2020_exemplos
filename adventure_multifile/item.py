from room import *

class Item:
    position = (2,2)
    name = "Default item name"
    description = "Default item description"
    in_inventory = False

    def __init__(self, name, description, position):
        self.name = name
        self.description = description
        self.position = position

