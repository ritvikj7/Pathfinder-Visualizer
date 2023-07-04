from .Node import Node
import random


class Map:

    def __init__(self):
        self.node_array = self.setup()

    def setup(self):
        # random.seed(967)
        # headx = random.randint(0, 9)
        # heady = random.randint(0, 9)
        # tailx = random.randint(0, 9)
        # taily = random.randint(0, 9)

        # width, arbitrary value
        cols = 5
        # height, arbitrary value
        rows = 5

        # array = [[Node(True, x, y, "head", 0) if x == headx and y == heady else Node(True, x, y, "tail",
        #                                                                              0) if x == tailx and y == taily else Node(
        #     True, x, y, "block", 0)
        #           for x in range(cols)] for y in range(rows)]

        # filling the array
        array = [[Node(True, 0, 0, "regular", 0) for y in range(cols)] for x in range(rows)]
        self.fill_array(array, cols, rows)

        return array

    def fill_array(self, array, cols, rows):
        for i in range(rows):
            for j in range(cols):
                array[i][j].x = j
                array[i][j].y = i

    def get_array(self):
        return self.node_array
