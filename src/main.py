# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from .Screen import screen

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# x = Node(False, 2, 3, "Regular")
# print(x.get_y())

map_obj = Map()

# print(map_obj.get_array())

# print("x: " + map_obj.get_array()[i][j].x + " " + "y: " + map_obj.get_array()[i][j].y)

for i in range(9):
    for j in range(9):
        print("("+str(map_obj.get_array()[i][j].x)+" "+str(map_obj.get_array()[i][j].y)+")")


map_obj.create_block(0, 2);

print(map_obj.get_array()[0][2].get_state())
