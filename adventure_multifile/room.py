from data.item_data import *

class Room:
    description = "Default description"
    exits = [ False, False, False, False ]
    position = (0,0)

    def __init__(self, description, can_exit_north = False, can_exit_east = False, can_exit_south = False, can_exit_west = False, position = (0,0)):
        self.description = description
        self.exits = [ can_exit_north, can_exit_east, can_exit_south, can_exit_west ]
        self.position = position

    def CanExit(self, direction_index):
        return self.exits[direction_index]

    def Look(self):
        global items

        print("-------------------------------------------------------")
        print(self.description)

        items_in_room = []
        for item in items:
            if (item.position == self.position):
                items_in_room.append(item)

        if (len(items_in_room) > 0):
            print("You see:")
            for item in items_in_room:
                print(item.name)
        print("-------------------------------------------------------")

    def Log(self, printExits):
        print(self.description)
        if (printExits):
            print(self.exits)
