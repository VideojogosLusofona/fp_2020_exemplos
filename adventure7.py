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

class Item:
    position = (2,2)
    name = "Default item name"
    description = "Default item description"
    in_inventory = False

    def __init__(self, name, description, position):
        self.name = name
        self.description = description
        self.position = position

rooms = [
    [ 
        Room("Room description 0, 0", False, False, True, False, (0, 0) ),
        Room("Room description 1, 0", False, True, False, False, (1, 0) ),
        Room("Room description 2, 0", False, True, True, True, (2, 0) ),
        Room("Room description 3, 0", False, True, True, True, (3, 0)),
        Room("Room description 4, 0", False, False, True, True, (4, 0))
    ],
    [ 
        Room("Room description 0, 1", True, False, True, False, (0,1)),
        Room("Room description 1, 1", False, True, True, False, (1,1)),
        Room("Room description 2, 1", True, True, True, True, (2,1)),
        Room("Room description 3, 1", True, False, False, True, (3, 1)),
        Room("Room description 4, 1", True, False, True, False, (4, 1))
    ],
    [ 
        Room("Room description 0, 2", True, False, True, False, (0, 2) ),
        Room("Room description 1, 2", True, False, False, False, (1, 2)),
        Room("You're on a dark path. A mansion looms in the distance to the north.", True, False, True, False, (2, 2) ),
        Room("Room description 3, 2", False, True, False, False, (3, 2) ),
        Room("Room description 4, 2", True, False, True, True, (4, 2) )
    ],
    [ 
        Room("Room description 0, 3",  True, False, True, False, (0, 3) ),
        Room("Room description 1, 3",  False, True, True, False, (1, 3)),
        Room("Room description 2, 3",  True, True, False, True, (2, 3)),
        Room("Room description 3, 3",  False, True, False, True, (3, 3)),
        Room("Room description 4, 3",  True, False, True, False, (3, 4))
    ],
    [ 
        Room("Room description 0, 4",  True, True, False, False, (0, 4)),
        Room("Room description 1, 4",  True, False, False, True, (1, 4)),
        Room("Room description 2, 4",  False, False, False, False, (2, 4)),
        Room("Room description 3, 4",  True, False, False, False, (3, 4)),
        Room("Room description 4, 4",  True, False, False, False, (4, 4))
    ]
]

items = [
    Item("Candle", "This is an ordinary wax candle", (2,2)),
    Item("Shovel", "A worn down shovel", (2,2)),
    Item("Apple", "An apple. It is rotten", (2, 3))
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

def examine_item(command_items):
    global items
    global x,y

    print()

    if (len(command_items) <= 1):
        print("Examine what?\n")
        return

    item_name = command_items[1]

    for item in items:
        if (item.name.lower() == item_name):
            if (item.position == (x,y)):
                print(item.description)
                print()
                return

    print("Can't see " + item_name)
    print()

command_processor = {
    "north" : lambda x: move_player(0, 0, -1),
    "n" : lambda x: move_player(0, 0, -1),
    "east" : lambda x: move_player(1, 1, 0),
    "e" : lambda x: move_player(1, 1, 0),
    "south" : lambda x: move_player(2, 0, 1),
    "s" : lambda x: move_player(2, 0, 1),
    "west" : lambda x: move_player(3, -1, 0),
    "w" : lambda x: move_player(3, -1, 0),
    "examine" : lambda x: examine_item(x),
    "exit" : lambda x: False
}

x, y = 2, 2

command = ""

rooms[y][x].Look()

while (command != "exit"):

    print("What now?")    
    command = input()
    command = command.strip()
    command = command.lower()

    command_items = command.split(" ")

    if (len(command_items) == 0):
        continue

    verb = command_items[0]

    if (verb in command_processor):
        func = command_processor[verb]
        func(command_items)
    else:
        print("I don't understand " + verb)

print("Goodbye!")
