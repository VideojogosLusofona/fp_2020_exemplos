import random
import time

#Lists 
# print("Lists")

# my_list = [ 12, 23, 34, 54, 676, 4, 32, 32, 43 ]

# print(my_list[4])

# for e in my_list:
#     print(e)

#Tuples
# print("Tuples")

# tuple_value = (1,2)
# x,y = tuple_value

# print(x,y)

#Dictionaries
# print("Dictionaries")

# release_year = { }
# release_year["God of War"] = 2018
# release_year["Subnautica"] = 2018
# release_year["Asteroids"] = 1979
# release_year["Super Mario Bros"] = 1984

# if ("God of War" in release_year):
#     print("Found it!")
# else:
#     print("Where is it?")

# for key in release_year:
#     print("Key=" + str(key))

# for key,value in release_year.items():
#     print("Key=" + str(key) + " | Value=" + str(value))

# for value in release_year.values():
#     print("Value=" + str(value))

# room_descriptions = {
#     (1,1) : "Description of room (1,1)",
#     (1,2) : "Description of room (1,2)",
#     (1,3) : "Description of room (1,3)",
#     (2,1) : "Description of room (2,1)"
# }

# print(room_descriptions[(1,3)])

# for key,value in room_descriptions.items():
#     print("Key=" + str(key) + " | Value=" + str(value))

# print("Sets")

# arenas_played = { "Blood Bowl", "Graveyard" }

# arenas_played.add("Trial of Champions")
# arenas_played.remove("Blood Bowl")

# if ("Spires of Destiny" in arenas_played):
#     arenas_played.remove("Spires of Destiny")

# for arena in arenas_played:
#     print(arena)

# a = { 1, 2, 3 }
# b = { 2, 3, 1, 1 }

# if (a == b):
#     print("Sets are the same")
# else:
#     print("Sets are different")

# for elem in b:
#     print(elem)

# Profile code
# list_of_values = []
# dictionary_of_value = { }
# for i in range(0, 1000):
#     val = random.randint(0, 1000)

#     list_of_values.append(val)
#     dictionary_of_value[val] = i

# value_to_search = list_of_values[random.randint(0, 1000)]

# t0 = time.time()

# for i in range(0, 10000):
#     index = -1
#     for j in range(0, len(list_of_values)):
#         if (list_of_values[index] == value_to_search):
#             index = j
#             break        

# t1 = time.time()

# print("Time elapsed = " + str(t1 - t0))

# t0 = time.time()

# for i in range(0, 10000):
#     index = -1
#     if (value_to_search in dictionary_of_value):
#         index = dictionary_of_value[value_to_search]  

# t1 = time.time()

# print("Time elapsed = " + str(t1 - t0))

