import pygame

class Node:

    def __init__(self, parent = None, position = None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


    def __lt__(self, other):
        return self.f < other.f

def astar_search(start, end, matrix, grid, show):
    start_node = Node(None, start)
    start_node.g=start_node.h=start_node.f=0
    end_node = Node(None, end)
    end_node.g=end_node.h=end_node.f=0

    open_list = []
    closed_list = []

    open_list.append(start_node)

    while len(open_list) > 0:

        open_list.sort()

        current_node = open_list.pop(0)

        closed_list.append(current_node)



        if current_node == end_node:
            path = []
            while current_node != start_node:
                path.append(current_node.position)
                current_node = current_node.parent
            path.append(start_node.position)
            return path[::-1]



        neighbors = get_neighbors((current_node.position))

        for pos in neighbors:
            if (pos[0] < 0 or
                    pos[1] < 0 or
                    pos[0] > len(matrix[len(matrix)-1])-1 or
                    pos[1] > (len(matrix)-1)):
                continue

            if matrix[pos[0]][pos[1]] == 1:
                continue

            neighbor = Node(current_node, pos)

            if neighbor in closed_list:
                continue

            generate_heuristic(neighbor, current_node, end_node)

            if add_to_open(open_list, neighbor) == True:
                open_list.append(neighbor)

        if show:
            for item in open_list:
                pygame.draw.polygon(grid, 'Green', box(item.position))
            for item in closed_list:
                pygame.draw.polygon(grid, 'Red', box(item.position))
            pygame.display.update()

    return None


def get_neighbors(tuple):
    x = tuple[0]
    y = tuple[1]
    neighbors = [(x-1, y-1), (x-1, y), (x, y-1),
                 (x+1, y+1), (x+1, y), (x, y+1),
                 (x-1, y+1, (x+1, (y-1)))]
    return neighbors

def generate_heuristic(node, current, end):
    node.g = current.g + 1
    node.h =((node.position[0] - end.position[0]) ** 2) + ((node.position[1] - end.position[1]) ** 2)
    node.f = node.g + node.h

def add_to_open(open, neighbor):
    for node in open:
        if (neighbor == node and neighbor.f >= node.f):
            return False
    return True

def box(tuple):
    x = tuple[0]
    y = tuple[1]
    new_tuple = [(x * 10, y * 10),
                (x * 10 + 10, y * 10),
                (x * 10 + 10, y* 10 + 10),
                (x * 10, y* 10 + 10)]
    return new_tuple
