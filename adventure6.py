class Room:
    description = "Default description"
    exits = [ False, False, False, False ]

    def __init__(self, description, can_exit_north = False, can_exit_east = False, can_exit_south = False, can_exit_west = False):
        self.description = description
        self.exits = [ can_exit_north, can_exit_east, can_exit_south, can_exit_west ]

    def CanExit(self, direction_index):
        return self.exits[direction_index]

    def Look(self):
        print("-------------------------------------------------------")
        print(self.description)
        print("-------------------------------------------------------")

    def Log(self, printExits):
        print(self.description)
        if (printExits):
            print(self.exits)

rooms = [
    [ 
        Room("Room description 0, 0", False, False, True, False ),
        Room("Room description 1, 0", False, True, False, False ),
        Room("Room description 2, 0", False, True, True, True ),
        Room("Room description 3, 0", False, True, True, True ),
        Room("Room description 4, 0", False, False, True, True )
    ],
    [ 
        Room("Room description 0, 1", True, False, True, False ),
        Room("Room description 1, 1", False, True, True, False ),
        Room("Room description 2, 1", True, True, True, True ),
        Room("Room description 3, 1", True, False, False, True ),
        Room("Room description 4, 1", True, False, True, False )
    ],
    [ 
        Room("Room description 0, 2", True, False, True, False ),
        Room("Room description 1, 2", True, False, False, False ),
        Room("You're on a dark path. A mansion looms in the distance to the north.", True, False, True, False ),
        Room("Room description 3, 2", False, True, False, False ),
        Room("Room description 4, 2", True, False, True, True )
    ],
    [ 
        Room("Room description 0, 3",  True, False, True, False ),
        Room("Room description 1, 3",  False, True, True, False ),
        Room("Room description 2, 3",  True, True, False, True ),
        Room("Room description 3, 3",  False, True, False, True ),
        Room("Room description 4, 3",  True, False, True, False )
    ],
    [ 
        Room("Room description 0, 4",  True, True, False, False ),
        Room("Room description 1, 4",  True, False, False, True ),
        Room("Room description 2, 4",  False, False, False, False ),
        Room("Room description 3, 4",  True, False, False, False ),
        Room("Room description 4, 4",  True, False, False, False )
    ]
]

def move_player(direction_index, x_inc, y_inc):
    global x, y
    global rooms

    current_room = rooms[y][x]

    if (current_room.CanExit(direction_index)):
        print("You move towards that direction!")
        x = x + x_inc
        y = y + y_inc

        current_room = rooms[y][x]
        current_room.Look()
    else:
        print("You can't move in that direction!")
    
    return True

command_processor = {
    "north" : lambda : move_player(0, 0, -1),
    "n" : lambda : move_player(0, 0, -1),
    "east" : lambda : move_player(1, 1, 0),
    "e" : lambda : move_player(1, 1, 0),
    "south" : lambda : move_player(2, 0, 1),
    "s" : lambda : move_player(2, 0, 1),
    "west" : lambda : move_player(3, -1, 0),
    "w" : lambda : move_player(3, -1, 0),
    "exit" : lambda : False
}

x, y = 2, 2

command = ""

rooms[y][x].Look()

while (command != "exit"):

    print("What now?")    
    command = input()
    command = command.strip()
    command = command.lower()

    if (command == ""):
        continue

    if (command in command_processor):
        func = command_processor[command]
        func()
    else:
        print("I don't understand " + command)

print("Goodbye!")
