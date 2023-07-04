# Dijkstra's algorithm allows users to find the path from a vertex s to all the vertex in a graph g
# This implementation of the algorithm will be targeted for unweighted graphs.
# The representation of the graph is an adjacency matrix.

# need to consider acyclic, cyclic, and no solution graphs
from src.map.Node import Node
import heapq


class Dijkstras:

    def __init__(self, x, y, grid):
        self.start_x = x
        self.start_y = y
        self.grid = grid

    # Will need to initialize a few arrays: visited nodes, distance from node
    # Lets implement it the typical way, where we have to visit each node
    def dijkstras(self):
        num_rows = len(self.grid)
        num_cols = len(self.grid[0])

        distances = [[float('inf') for _ in range(num_cols)] for _ in range(num_rows)]

        distances[self.start_x][self.start_y] = 0

        priority_queue = []
        heapq.heappush(priority_queue, Node(False, self.start_x, self.start_y, 'regular', 0))

        movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while priority_queue:
            current_node = heapq.heappop(priority_queue)

            for dx, dy in movements:
                new_x = current_node.x + dx
                new_y = current_node.y + dy

                if 0 <= new_x < num_rows and 0 <= new_y < num_cols:
                    new_distance = current_node.distance + 1

                    if new_distance < distances[new_x][new_y]:
                        distances[new_x][new_y] = new_distance
                        heapq.heappush(priority_queue, Node(False, new_x, new_y, "regular", new_distance))

        return distances