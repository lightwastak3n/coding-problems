from collections import defaultdict

test = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

with open("AoC/2023_problems/day3.txt") as f:
    test = f.read()

rows = [list(x) for x in test.split()]

def check_neighbours(locations):
    s = ".0123456789"
    if len(locations) > 2:
        locations = [locations[0], locations[2]]
    neighbours = []
    gear = set()
    for loc in locations:
        i, j = loc
        for m in range(i-1, i+2):
            for n in range(j-1, j+2):
                if (m < 0 or m >= len(rows)) or (n < 0 or n >= len(rows[0])):
                    continue
                if rows[m][n] not in s:
                    neighbours.append(True)
                    if rows[m][n] == "*":
                        gear.add((m, n))
    return any(neighbours), gear

total = 0
gears = defaultdict(list)
for i in range(len(rows)):
    num = ""
    locations = []
    for j in range(len(rows[0])):
        if rows[i][j].isdigit():
            num += rows[i][j]
            locations.append([i, j])
        elif num:
            add, gear = check_neighbours(locations)
            if add:
                total += int(num)
            if gear:
                for g in gear:
                    gears[g].append(int(num))
            num = ""
            locations = []
    # End of row check
    if num:
        add, gear = check_neighbours(locations)
        if gear:
            for g in gear:
                gears[g].append(int(num))
        if add:
            total += int(num)
print(total)
total_gears = 0
for gear in gears:
    if len(gears[gear]) > 1:
        total_gears += gears[gear][0] * gears[gear][1]
print(total_gears)
