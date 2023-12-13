test_data = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""


with open("AoC/2023_problems/day13.txt", "r") as f:
    data = f.read()


def find_reflection(grid):
    part1, part2 = 0, 0
    for i in range(1, len(grid)):
        top = grid[:i][::-1]
        bottom = grid[i:]
        # Limit both to same size
        size = min(len(top), len(bottom))
        top = top[:size]
        bottom = bottom[:size]
        # If no difference then part 1, if 1 difference part 2
        if find_difference(top, bottom) == 0:
            part1 += i
        if find_difference(top[:size], bottom[:size]) == 1:
            part2 += i
    return part1, part2


def find_difference(grid1, grid2):
    diff = 0
    for i in range(len(grid1)):
        row1 = grid1[i]
        row2 = grid2[i]
        for j in range(len(row1)):
            if row1[j] != row2[j]:
                diff += 1
    return diff


def process_grid(grid):
    orig_p1, orig_p2 = find_reflection(grid)
    transpose_p1, transpose_p2 = find_reflection(list(map(list, zip(*grid))))
    part1 = 100*orig_p1 or transpose_p1
    part2 = 100*orig_p2 or transpose_p2
    return part1, part2


def solve(data):
    grids = data.split("\n\n")
    p1, p2 = 0, 0
    for g in grids:
        grid = [list(x) for x in g.split()]
        part1, part2 = process_grid(grid)
        p1 += part1
        p2 += part2
        
    return p1, p2

print(solve(data))
