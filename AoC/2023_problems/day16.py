with open("AoC/2023_problems/day16.txt", 'r') as f:
    data = f.read()

grid = [list(x) for x in data.split("\n")]


def part1(grid, initial_conditions):
    limits = (len(grid), len(grid[0]))
    visited = set()
    queue = [initial_conditions]
    # queue.append((start, direction))
    while queue:
        beam_pos, beam_dir = queue.pop()
        beam_pos = (beam_pos[0] + beam_dir[0], beam_pos[1] + beam_dir[1])
        if not 0 <= beam_pos[0] < limits[0] or not 0 <= beam_pos[1] < limits[1] or (beam_pos, beam_dir) in visited:
            continue
        visited.add((beam_pos, beam_dir))
        if grid[beam_pos[0]][beam_pos[1]] == "/":
            beam_dir = (-beam_dir[1], -beam_dir[0])
        elif grid[beam_pos[0]][beam_pos[1]] == "\\":
            beam_dir = (beam_dir[1], beam_dir[0])
        elif grid[beam_pos[0]][beam_pos[1]] == "|" and beam_dir in [(0, 1), (0, -1)]:
            beam_dir = (1, 0)
            queue.append((beam_pos, (-1, 0)))
        elif grid[beam_pos[0]][beam_pos[1]] == "-" and beam_dir in [(1, 0), (-1, 0)]:
            beam_dir = (0, 1)
            queue.append((beam_pos, (0, -1)))
        queue.append((beam_pos, beam_dir))
    unique = set() 
    for node in visited:
        unique.add(node[0])
    return len(unique)


def part2(grid):
    results = []
    all_sides = []
    for i in range(len(grid)):
        all_sides.append(((-1, i), (1, 0))) # top
        all_sides.append(((i, -1), (0, 1))) # left
        all_sides.append(((i, len(grid)), (0, -1))) # right
        all_sides.append(((len(grid), i), (-1, 0))) # bottom
    for start in all_sides:
        results.append(part1(grid, start))
    return max(results)


part1_start = ((0, -1), (0, 1))
print(part1(grid, part1_start))
print(part2(grid))
