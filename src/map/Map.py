from .Node import Node
import random


class Map:

    def __init__(self):
        self.node_array = self.setup()

    def setup(self):
        random.seed(967)
        headx = random.randint(0, 9)
        heady = random.randint(0, 9)
        tailx = random.randint(0, 9)
        taily = random.randint(0, 9)

        # width, arbitrary value
        cols = 6
        # height, arbitrary value
        rows = 6

        array = [[Node(True, x, y, "head", 0) if x == headx and y == heady else Node(True, x, y, "tail",
                                                                                     0) if x == tailx and y == taily else Node(
            True, x, y, "block", 0)
                  for x in range(cols)] for y in range(rows)]

        return array

    def get_array(self):
        return self.node_array
