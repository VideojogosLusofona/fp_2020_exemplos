
command = ""

while (command != "exit"):
    print("What now?")    
    command = input()

    if (command == "north"):
        print("You move north...")
    elif (command == "south"):
        print("You move south...")
    elif (command == "east"):
        print("You move east...")
    elif (command == "west"):
        print("You move west...")
    elif (command == "exit"):
        pass
    else:
        print("I don't understand " + command)

print("Goodbye!")
