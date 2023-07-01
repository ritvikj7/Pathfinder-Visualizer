class Node:

    def __init__(self, free, x, y, classification):
        self.free = free
        self.x = x
        self.y = y
        self.classification = classification

    def set_free(self, value):
        self.free = value

    # might not need
    def set_classification(self, classification):
        self.classification = classification;

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_free(self):
        return self.free

    def get_classification(self):
        return self.classification
