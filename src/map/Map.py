
from .Node import Node


class Map:
    dog = "cute"

    def __init__(self):
        self.node_array = self.setup()

    def print_dog(self):
        print(self.dog)

    def change_name(self, name):
        self.dog = name

    def setup(self):
        # width, arbitrary value
        cols = 3
        # height, arbitrary value
        rows = 3

        array = [[Node(True, 0, 0, "regular") for y in range(cols)] for x in range(rows)]

        self.fill_array(array, cols, rows)
        return array

    # Remember that we are looking at it from the point of (x, y) where (0, 0) is the top left corner of the grid
    def fill_array(self, array, cols, rows):
        for i in range(rows):
            for j in range(cols):
                array[i][j].x = j
                array[i][j].y = i

    def create_block(self, x, y):
        self.node_array[x][y].block_node()

    def free_block(self, x, y):
        self.node_array[x][y].free_node()

    def change_classification(self, x, y, classification):
        self.node_array[x][y].set_classification(classification)

    def get_array(self):
        return self.node_array
