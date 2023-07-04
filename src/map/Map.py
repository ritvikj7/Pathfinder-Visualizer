
from .Node import Node
import random

class Map:

    def __init__(self):
        self.node_array = self.setup()


    def setup(self):
        # width, arbitrary value
        random.seed(967)
        headx = random.randint(0, 9)
        heady = random.randint(0, 9)
        tailx = random.randint(0, 9)
        taily = random.randint(0, 9)

        cols = 10
        # height, arbitrary value
        rows = 10
        #filling the array
        array = [[Node(True, x, y, "head",0) if x == headx and y==heady else Node(True, x, y, "tail",0) if x == tailx and y==taily else Node(True, x, y, "block",0)
                  for x in range(cols)] for y in range(rows)]

        for i in range(rows):
            for j in range(cols):
                print("("+str(array[i][j].x)+","+str(array[i][j].y)+")"+array[i][j].classification+" ")
            print("\n")




        return array

    # Remember that we are looking at it from the point of (x, y) where (0, 0) is the top left corner of the grid




    def get_array(self):
        return self.node_array
