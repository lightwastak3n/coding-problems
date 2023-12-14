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


with open("AoC/2023_problems/day14.txt") as f:
    data = f.read()


def display_grid(grid):
    for row in grid:
        print("|".join(row))


def tranpose_reverse(grid, reverse=False):
    transposed = list(map(list, zip(*grid)))
    if reverse:
        for row in transposed:
            row.reverse()
    return transposed


def tilt(grid):
    load = 0
    for row in grid:
        for i in range(len(row)):
            if row[i] == "O":
                load += len(row) - move_rock(row, i)
    return load

def move_rock(row, rock):
    while rock > 0 and row[rock-1] == ".":
        row[rock - 1], row[rock] = row[rock], row[rock - 1]
        rock -= 1
    return rock


def calculate_load(grid):
    load = 0
    for row in grid:
        for i in range(len(row)):
            if row[i] == "O":
                load += len(row) - i
    return load


def part1(data):
    grid = [list(x) for x in data.split("\n")]
    grid = tranpose_reverse(grid)
    return tilt(grid)


def part2(data):
    grid = [list(x) for x in data.split("\n")]
    cycle_end = []
    grid = tranpose_reverse(grid)
    for _ in range(200):
        # North
        tilt(grid)
        # West
        grid = tranpose_reverse(grid)
        tilt(grid)
        # South
        grid = tranpose_reverse(grid, True)
        tilt(grid)
        # East
        grid = tranpose_reverse(grid, True)
        tilt(grid)

        # Return back to facing north
        grid = tranpose_reverse(grid, reverse=True)
        grid = tranpose_reverse(grid, reverse=True)
        grid = tranpose_reverse(grid)
        # doing % 102600 since numbers are large and hard to see the pattern
        cycle_end.append(calculate_load(grid) % 102600)

    return cycle_end

# For my input it took 125 cycles until it started repeating in cycles of 21 so the part 2 is pattern[(1b - 125) % 21 - 1]
print(part2(data))
print("Part1:", part1(data))

