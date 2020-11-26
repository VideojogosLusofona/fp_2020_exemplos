

room_desc = [
    [ "Room description 0, 0", "Room description 1, 0", "Room description 2, 0", "Room description 3, 0", "Room description 4, 0" ],
    [ "Room description 0, 1", "Room description 1, 1", "Room description 2, 1", "Room description 3, 1", "Room description 4, 1" ],
    [ "Room description 0, 2", "Room description 1, 2", "You're in a dark path, in front of you the mansion rises in the distance", "Room description 3, 2", "Room description 4, 2" ],
    [ "Room description 0, 3", "Room description 1, 3", "Room description 2, 3", "Room description 3, 3", "Room description 4, 3" ],
    [ "Room description 0, 4", "Room description 1, 4", "Room description 2, 4", "Room description 3, 4", "Room description 4, 4" ],
]

room_exits = [
    [ 
        [ False, False, True, False ],
        [ False, True, False, False ],
        [ False, True, True, True ],
        [ False, True, True, True ],
        [ False, False, True, True ]
    ],
    [ 
        [ True, False, True, False ],
        [ False, True, True, False ],
        [ True, True, True, True ],
        [ True, False, False, True ],
        [ True, False, True, False ]
    ],
    [ 
        [ True, False, True, False ],
        [ True, False, False, False ],
        [ True, False, True, False ],
        [ False, True, False, False ],
        [ True, False, True, True ]
    ],
    [ 
        [ True, False, True, False ],
        [ False, True, True, False ],
        [ True, True, False, True ],
        [ False, True, False, True ],
        [ True, False, True, False ]
    ],
    [ 
        [ True, True, False, False ],
        [ True, False, False, True ],
        [ False, False, False, False ],
        [ True, False, False, False ],
        [ True, False, False, False ]
    ]
]

def show_current_room_description():
    global x, y
    print("-------------------------------------------------------")
    print(room_desc[y][x])
    print("-------------------------------------------------------")


def move_player(direction_index, x_inc, y_inc):
    global x, y

    if (room_exits[y][x][direction_index]):
        print("You move towards that direction!")
        x = x + x_inc
        y = y + y_inc

        show_current_room_description()
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

show_current_room_description()

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
