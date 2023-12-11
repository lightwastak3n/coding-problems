test_data = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""


with open("AoC/2023_problems/day11.txt", "r") as f:
    data = f.read()


def solve(data):
    grid = [list(x) for x in data.splitlines()]
    empty_rows = [i for i in range(len(grid)) if "#" not in grid[i]]
    empty_columns = [j for j in range(len(grid[0])) if "#" not in [grid[i][j] for i in range(len(grid))]]
    galaxies = []
    galaxies_1m = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "#":
                gi = i + sum([i > row for row in empty_rows])
                gj = j + sum([j > col for col in empty_columns])
                gi_1m = i + 999999*sum([i > row for row in empty_rows])
                gj_1m = j + 999999*sum([j > col for col in empty_columns])
                galaxies.append((gi, gj))
                galaxies_1m.append((gi_1m, gj_1m))
    p1, p2 = 0, 0
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            p1 += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
            p2 += abs(galaxies_1m[i][0] - galaxies_1m[j][0]) + abs(galaxies_1m[i][1] - galaxies_1m[j][1])
    return p1, p2

print(solve(data))
