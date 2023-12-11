test_data = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJIF7FJ-
L---JF-JLJIIIIFJLJJ7
|F|F-JF---7IIIL7L|7|
|FFJF7L7F-JF7IIL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""

with open("AoC/2023_problems/day10.txt") as f:
    data = f.read()

move = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}

new_position_map = {
    "|": {"D": move["D"], "U": move["U"]},
    "-": {"L": move["L"], "R": move["R"]},
    "L": {"D": move["R"], "L": move["U"]},
    "J": {"D": move["L"], "R": move["U"]},
    "F": {"U": move["R"], "L": move["D"]},
    "7": {"U": move["L"], "R": move["D"]},
}

new_direction_map = {
    "|": {"D": "D", "U": "U"},
    "-": {"R": "R", "L": "L"},
    "L": {"D": "R", "L": "U"},
    "J": {"D": "L", "R": "U"},
    "F": {"U": "R", "L": "D"},
    "7": {"R": "D", "U": "L"},
}


def solve(data):
    grid = [list(x) for x in data.splitlines()]
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
    if cj + 1 < len(grid[0]) and grid[ci][cj + 1] in "-7J":
        possible_dirs.append("R")
    if ci + 1 < len(grid) and grid[ci + 1][cj] in "|LJ":
        possible_dirs.append("D")
    if cj > 0 and grid[ci][cj - 1] in "-FL":
        possible_dirs.append("L")
    if ci > 0 and grid[ci - 1][cj] in "|F7":
        possible_dirs.append("U")

    # Replace S with appropriate pipe for part 2
    s_replace = {"".join(new_direction_map[k].values()):k for k in new_direction_map}
    grid[s_loc[0]][s_loc[1]] = s_replace["".join(possible_dirs)]

    current_dir = possible_dirs[0]
    pipe_loop = [(ci, cj)]
    move_amount = move[current_dir]
    ci = ci + move_amount[0]
    cj = cj + move_amount[1]
    current_pipe = grid[ci][cj]
    while (ci, cj) != s_loc:
        pipe_loop.append((ci, cj))
        current_dir = new_direction_map[current_pipe][current_dir]
        move_amount = move[current_dir]
        ci = ci + move_amount[0]
        cj = cj + move_amount[1]
        current_pipe = grid[ci][cj]
    p1 = len(pipe_loop) // 2

    p2 = 0
    grid = ["".join(c if (i, j) in pipe_loop else "." for j, c in enumerate(row)) for i, row in enumerate(grid)]
    inside = False
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] in "F7|":
                inside = not inside
            elif grid[i][j] == "." and inside:
                p2 += 1
    return p1, p2

print(solve(data))
