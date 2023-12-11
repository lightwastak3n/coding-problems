test_data = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""


MOVE = {
"R": (0, 1),
"D": (1, 0),
"L": (0, -1),
"U": (-1, 0)
}

NEW_DIRECTION = {
    "|": {"U": "U", "D": "D"},
    "-": {"R": "R", "L": "L"},
    "L": {"D": "R", "L": "U"},
    "J": {"D": "L", "R": "U"},
    "F": {"U": "R", "L": "D"},
    "7": {"U": "L", "R": "D"}
}

with open("AoC/2023_problems/day10.txt") as f:
    data = f.read()


def move_pipe(grid, cur_pos, cur_dir):
    # Get next direction and position based on current position and direction
    current_pipe = grid[cur_pos[0]][cur_pos[1]]
    next_dir = NEW_DIRECTION[current_pipe][cur_dir]
    offset = MOVE[next_dir]
    next_position = (cur_pos[0] + offset[0], cur_pos[1] + offset[1])
    return next_position, next_dir


def solve(data):
    grid = [list(x) for x in data.splitlines()]

    # Find the start location
    s_loc = None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                s_loc = (i, j)
                break
        if s_loc:
            break
    ci, cj = s_loc
    possible_dirs = []

    # Check if S in corner and check all 4 directions
    if cj + 1 < len(grid[0]) and grid[ci][cj + 1] in "-7J":
        possible_dirs.append("R")
    if ci + 1 < len(grid) and grid[ci + 1][cj] in "|LJ":
        possible_dirs.append("D")
    if cj > 0 and grid[ci][cj - 1] in "-FL":
        possible_dirs.append("L")
    if ci > 0 and grid[ci - 1][cj] in "|F7":
        possible_dirs.append("U")

    # Keep track of pipes that make the loop
    pipe_loop = [(ci, cj)]
    # Choose first available direction and move to the next pipe
    cur_dir = possible_dirs[0]
    cur_pos = (s_loc[0] + MOVE[cur_dir][0], s_loc[1] + MOVE[cur_dir][1])
    cur_pipe = grid[cur_pos[0]][cur_pos[1]]
    # Keep moving until we find S again
    while cur_pipe != "S":
        pipe_loop.append(cur_pos)
        cur_pos, cur_dir = move_pipe(grid, cur_pos, cur_dir)
        cur_pipe = grid[cur_pos[0]][cur_pos[1]]

    # The half of the length of the loop is the solution to part 1
    p1 = len(pipe_loop) / 2

    # Shocelace formula https://en.wikipedia.org/wiki/Shoelace_formula
    area = 0
    for i in range(len(pipe_loop)-1):
        area += 0.5 * (pipe_loop[i][1] + pipe_loop[i+1][1]) * (pipe_loop[i][0] - pipe_loop[i+1][0])
    area = abs(area)
    # Picks theorem https://en.wikipedia.org/wiki/Pick%27s_theorem
    p2 = area - len(pipe_loop)/2 + 1
    return p1, p2


print(solve(data))
