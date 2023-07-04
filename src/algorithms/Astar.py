# A* is basically an informed variation of Dijkstra.
# A* is considered a "best first search" because it greedily chooses which vertex to explore next,
# according to the value of f(v) [f(v) = h(v) + g(v)] - where h is the heuristic and g is the cost so far.

# need to consider acyclic, cyclic, and no solution graphs
from src.map.Node import Node
import heapq


class Astar:

    def __init__(self, start_x, start_y, grid):
        self.start_x = start_x
        self.start_y = start_y
        self.grid = grid

    def calulate_heuristic(self, current_x, current_y, target_x, target_y):
        return abs(current_x-target_x) + abs(current_y-target_y)

    def astar(self, target_x, target_y):
        num_rows = len(self.grid)
        num_cols = len(self.grid[0])

        distances = [[float('inf') for _ in range(num_cols)] for _ in range(num_rows)]

        distances[self.start_x][self.start_y] = 0

        priority_queue = []
        heapq.heappush(priority_queue, Node(False, self.start_x, self.start_y, 'regular', 0))

        movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while priority_queue:
            current_node = heapq.heappop(priority_queue)

            if current_node.x == target_x and current_node.y == target_y:
                break

            for dx, dy in movements:
                new_x = current_node.x + dx
                new_y = current_node.y + dy

                if 0 <= new_x < num_rows and 0 <= new_y < num_cols:
                    new_distance = current_node.distance + 1
                    heuristic = self.calulate_heuristic(new_x, new_y, target_x, target_y)
                    total_cost = new_distance + heuristic

                    if total_cost < distances[new_x][new_y]:
                        distances[new_x][new_y] = new_distance
                        heapq.heappush(priority_queue, Node(False, new_x, new_y, "regular", new_distance))

        return distances
