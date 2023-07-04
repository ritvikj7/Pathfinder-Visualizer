
from .Node import Node


class Map:

    def __init__(self):
        self.node_array = self.setup()


    def setup(self):
        # width, arbitrary value
        cols = 10
        # height, arbitrary value
        rows = 10
        #filling the array
        array = [[Node(True, x, y, "regular",0) for x in range(cols)] for y in range(rows)]


        return array

    # Remember that we are looking at it from the point of (x, y) where (0, 0) is the top left corner of the grid




    def get_array(self):
        return self.node_array
