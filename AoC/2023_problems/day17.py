import time
from heapq import heappush, heappop


test_data = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""


# with open("AoC/2023_problems/day17.txt", 'r') as f:
#     test_data = f.read()


def display_grid(grid):
    for row in grid:
        print(" ".join(row))


def color_node(grid, node, color):
    COLORS = {
        "RED": '\033[91m',
        "GREEN": '\033[92m',
        "YELLOW": '\033[93m',
        "BLUE": '\033[94m',
        "PURPLE": '\033[95m',
        "CYAN": '\033[96m',
        "RESET": '\033[0m'
    }
    grid[node[0]][node[1]] = COLORS[color] + grid[node[0]][node[1]] + COLORS["RESET"]
    return grid


def get_neighbors(height, width, node):
    neighbors= []
    if node[0] > 0:
        neighbors.append((node[0] - 1, node[1]))
    if node[0] < height - 1:
        neighbors.append((node[0] + 1, node[1]))
    if node[1] > 0:
        neighbors.append((node[0], node[1] - 1))
    if node[1] < width - 1:
        neighbors.append((node[0], node[1] + 1))
    return neighbors


def dijkstra(grid, goal):
    height, width = len(grid), len(grid[0])
    frontier = [(0, goal)]
    distance = {}
    distance[goal] = 0
    while len(frontier) > 0:
        current_node = heappop(frontier)[1]
        neighbors = get_neighbors(height, width, current_node)
        for neighbor in neighbors:
            weight = int(grid[neighbor[0]][neighbor[1]])
            tentative_distance = distance[current_node] + weight
            if neighbor not in distance or tentative_distance < distance[neighbor]:
                distance[neighbor] = tentative_distance
                heappush(frontier, (tentative_distance, neighbor))
    return distance


def heuristic(node, distance_map, came_from):
    past = []
    current = node
    for i in range(4):
        current = came_from[current]
        past.append(current)
    directions = []
    for i in range(len(past)-1):
        directions = (past[i][0] - past[i+1][0], past[i][1] - past[i+1][1])
    steps = directions.count(directions[0])
    return distance_map[node]*steps


def a_star(grid, start, goal):
    height, width = len(grid), len(grid[0])
    q = [(0, start)]
    cost_so_far = {start: 0}
    came_from = {start: None}
    steps = {start: None}
    while len(q) > 0:
        current = heappop(q)[1]
        if current == goal:
            break
        for node in get_neighbors(height, width, current):
            print("Checking", node)
            new_cost = cost_so_far[current] + int(grid[node[0]][node[1]])
            if node not in cost_so_far or new_cost < cost_so_far[node]:
                cost_so_far[node] = new_cost
                came_from[node] = current
                priority = new_cost + heuristic(node, cost_so_far, came_from)
                heappush(q, (priority, node))

    path = [goal]
    current = goal
    while current != start:
        current = came_from[current]
        path.append(current)

    return cost_so_far, path

grid = [list(x) for x in test_data.split("\n")]

bottom_right = (len(grid)-1, len(grid[0])-1)
distance_mapping = dijkstra(grid, bottom_right)
shortest_paths, end_path = a_star(grid, (0, 0), bottom_right)
print(shortest_paths[(12, 12)])
print(end_path)

for node in end_path:
    grid = color_node(grid, node, "GREEN")
display_grid(grid)



# with open("AoC/2023_problems/day17.txt", 'r') as f:
#     data = f.read()


# def cheapest_path(grid, start, end):



# def solve(data):
#     grid = [list(x) for x in data.split("\n")]
#     cur_pos = [0, 0]
#     goal = [len(grid) - 1, len(grid[0]) - 1]
#     total = 0
#     while cur_pos != (3, 3):
#         cur_pos = 
#         total += 1
#     return total
