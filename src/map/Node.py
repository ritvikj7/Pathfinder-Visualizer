class Node:

    # The basic idea is that the map will be  made up of a list of nodes
    # There will be 4 classification to a node: regular nodes, start node, end node, and blocked node
    # Do we possibly want to change free to state?
    # If state is false, then the node is free otherwise it is blocked
    def __init__(self, state, x, y, classification):
        self.state = state
        self.x = x
        self.y = y
        self.classification = classification

    def free_node(self):
        self.state = False

    def block_node(self):
        self.state = True

    # might not need
    def set_classification(self, classification):
        self.classification = classification

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_state(self):
        return self.state

    def get_classification(self):
        return self.classification
