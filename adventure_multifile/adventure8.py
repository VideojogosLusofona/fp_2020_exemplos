
from room import *
from item import *
from data.room_data import *
from data.item_data import *

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
