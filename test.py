class Room:
    description = "Default description"
    exits = [ False, False, False, False ]

    def __init__(self, description, can_exit_north = False, can_exit_east = False, can_exit_south = False, can_exit_west = False):
        self.description = description
        self.exits = [ can_exit_north, can_exit_east, can_exit_south, can_exit_west ]

    def Log(self, printExits):
        print(self.description)
        if (printExits):
            print(self.exits)

# r1 = Room()
# r1.description = "Description of first room"
# r1.exits = [ True, False, True, False ]

# r2 = Room()
# r2.description = "Description of second room"
# r2.exits[2] = True

# r1.Log(False)
# r2.Log(True)

# r3 = r1

# r3.description = "Description of third room"
# r3.Log(False)
# r1.Log(False)

r4 = Room("This is the fourth room", can_exit_west = True)
r4.Log(True)