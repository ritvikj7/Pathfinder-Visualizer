# Dijkstra's algorithm allows users to find the path from a vertex s to all the vertex in a graph g
# need to consider acyclic, cyclic, and no solution graphs

import heapq
from src.map.Node import Node


class Dijkstras:
    def __init__(self, start_x, start_y, target_x, target_y, grid):
        self.start_x = start_x
        self.start_y = start_y
        self.target_x = target_x
        self.target_y = target_y
        self.grid = grid

    def calculate_distance(self, current_distance):
        return current_distance + 1

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
            print(current_node.x, current_node.y)

            if current_node.x == self.target_x and current_node.y == self.target_y:
                break

            for dx, dy in movements:
                new_x = current_node.x + dx
                new_y = current_node.y + dy

                if 0 <= new_x < num_rows and 0 <= new_y < num_cols:
                    new_distance = self.calculate_distance(current_node.distance)

                    # Need to think deeply about what is actually happening here, that is leading us to having
                    # the same results
                    if new_distance < distances[new_x][new_y]:
                        distances[new_x][new_y] = new_distance
                        heapq.heappush(priority_queue, Node(False, new_x, new_y, "regular", new_distance))

        return distances
