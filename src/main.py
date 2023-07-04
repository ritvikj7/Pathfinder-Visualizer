# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from map.Node import Node
from map.Map import Map
from algorithms.Dijkstras import Dijkstras


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# x = Node(False, 2, 3, "Regular")
# print(x.get_y())

map_obj = Map()

dijkstras_obj = Dijkstras(2, 2, map_obj.get_array())

distances = dijkstras_obj.dijkstras()
print(distances)

