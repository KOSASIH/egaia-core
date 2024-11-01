import heapq
from typing import List, Tuple, Dict

class Node:
    """Class representing a node in the grid for pathfinding."""
    
    def __init__(self, position: Tuple[int, int], parent: 'Node' = None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start to this node
        self.h = 0  # Heuristic cost to goal
        self.f = 0  # Total cost

    def __lt__(self, other: 'Node'):
        return self.f < other.f

def heuristic(a: Tuple[int, int], b: Tuple[int, int]) -> int:
    """Calculate the Manhattan distance heuristic."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(start: Tuple[int, int], goal: Tuple[int, int], grid: List[List[int]]) -> List[Tuple[int, int]]:
    """A* pathfinding algorithm."""
    open_list = []
    closed_list = set()

    start_node = Node(start)
    goal_node = Node(goal)

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)

        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 4 possible directions
        for new_position in neighbors:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if (0 <= node_position[0] < len(grid)) and (0 <= node_position[1] < len(grid[0])) and grid[node_position[0]][node_position[1]] == 0:
                if node_position in closed_list:
                    continue

                neighbor_node = Node(node_position, current_node)
                neighbor_node.g = current_node.g + 1
                neighbor_node.h = heuristic(neighbor_node.position, goal_node.position)
                neighbor_node.f = neighbor_node.g + neighbor_node.h

                if add_to_open(open_list, neighbor_node):
                    heapq.heappush(open_list, neighbor_node)

    return []  # Return empty path if no path is found

def add_to_open(open_list: List[Node], neighbor: Node) -> bool:
    """Check if the neighbor should be added to the open list."""
    for node in open_list:
        if neighbor.position == node.position and neighbor.g >= node.g:
            return False
    return True
