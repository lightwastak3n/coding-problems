test_data = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""


with open("AoC/2023_problems/day14.txt", "r") as f:
    data = f.read()

# We will rotate the grid so that moving rocks up is equivalent to moving them left
def move_rocks_left(grid):
    for row in grid:
        for j in range(len(row)):
            if row[j] == "O":
                while j > 0 and row[j - 1] == ".":
                    row[j - 1], row[j] = row[j], row[j - 1]
                    j -= 1


def get_load(grid):
    load = 0
    for row in grid:
        for i in range(len(row)):
            if row[i] == "O":
                load += len(row) - i
    return load


def rotate_right(grid):
    grid = list(map(list, zip(*grid)))
    for row in grid:
        row.reverse()
    return grid


def rotate_left(grid):
    for row in grid:
        row.reverse()
    grid = list(map(list, zip(*grid)))
    return grid


def grid_hash(grid):
    return tuple(tuple(row) for row in grid)


def solve_part1(data):
    grid = [list(x) for x in data.split("\n")]
    # Rotate grid so north is left
    grid = rotate_left(grid)
    move_rocks_left(grid)
    return get_load(grid)


def solve_part2(data):
    grid = [list(x) for x in data.split("\n")]
    grid = rotate_left(grid)
    cycles = 0
    grids_set = {grid_hash(grid)}
    seen_grids = [grid_hash(grid)]
    seen_loads = [get_load(grid)]
    while True:
        for _ in range(4):
            move_rocks_left(grid)
            grid = rotate_right(grid)
        cycles += 1
        ghash = grid_hash(grid)
        seen_grids.append(ghash)
        seen_loads.append(get_load(grid))
        if ghash in grids_set:
            break
        grids_set.add(ghash)

    pattern_start = seen_grids.index(ghash)
    pattern_length = cycles - pattern_start

    return seen_loads[pattern_start + (1_000_000_000 - pattern_start) % pattern_length]


print(solve_part1(data))
print(solve_part2(data))
