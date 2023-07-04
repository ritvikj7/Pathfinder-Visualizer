# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from Screen import Screen
from map.Map import Map
from PyQt5.QtWidgets import QApplication

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# x = Node(False, 2, 3, "Regular")
# print(x.get_y())
app = QApplication([])

map_obj = Map()

screen = Screen(map_obj)
screen.show()
app.exec()


# from map.Map import Map
# from algorithms.Dijkstras import Dijkstras
# from algorithms.Astar import Astar
#
# map_obj = Map()
#
# astar_obj = Astar(3, 3, map_obj.get_array())
# distance1 = astar_obj.astar(4, 4)
# print(distance1)
#
# d_obj = Dijkstras(3, 3, map_obj.get_array())
# distance2 = d_obj.dijkstras()
# print(distance2)


