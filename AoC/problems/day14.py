with open("day14.txt", 'r') as f:
    s = f.read()

pairs = []
bounds = [1000, 0, 0] # left, right, bottom
for line in s.split("\n"):
    line = line.split(" -> ")
    line = zip(line[:-1], line[1:])

    fix_point = lambda p: list(map(int, p.split(",")))
    for a,b in line:
        pair = [fix_point(a), fix_point(b)]
        bounds[0] = min(bounds[0], pair[0][0], pair[1][0])
        bounds[1] = max(bounds[1], pair[0][0], pair[1][0])
        bounds[2] = max(bounds[2], pair[0][1], pair[1][1])
        pairs.append(sorted(pair))

# Fix bounds so that it covers more (needed for part 2)
bounds = [bounds[0]-400, bounds[1]+400, bounds[2]+3]
# Create a cave - actually uses [y, x] instead of [x, y] oopsie
cave = [["." for i in range(bounds[0], bounds[1])] for j in range(bounds[2])]

# Add bottom floor
y = bounds[2]-1
for x in range(len(cave[0])):
    cave[y][x] = "#"

for pair in pairs:
    if pair[0][0] == pair[1][0]:
        # same x so vertical line
        for y in range(pair[0][1], pair[1][1]+1):
            cave[y][pair[0][0] - bounds[0]] = "#"
    else:
        # horizontal line same y
        for x in range(pair[0][0], pair[1][0]+1):
            cave[pair[0][1]][x-bounds[0]] = "#"


sand = [500, 0]
total1 = 0
while sand[1] < bounds[2]-2:
    x, y = sand
    if cave[y+1][x-bounds[0]] == ".":
        sand[1] += 1
    elif cave[y+1][x-1-bounds[0]] == ".":
        sand[0] -= 1
        sand[1] += 1
    elif cave[y+1][x+1-bounds[0]] == ".":
        sand[0] += 1
        sand[1] += 1
    else:
        cave[y][x-bounds[0]] = "o"
        sand = [500, 0]
        total1 += 1
print(total1)

# Part 2 - just continue on from part 1
sand = [500, 0]
total2 = total1
while cave[0][500-bounds[0]] != "o":
    x, y = sand
    if cave[y+1][x-bounds[0]] == ".":
        sand[1] += 1
    elif cave[y+1][x-1-bounds[0]] == ".":
        sand[0] -= 1
        sand[1] += 1
    elif cave[y+1][x+1-bounds[0]] == ".":
        sand[0] += 1
        sand[1] += 1
    else:
        cave[y][x-bounds[0]] = "o"
        sand = [500, 0]
        total2 += 1
print(total2)
