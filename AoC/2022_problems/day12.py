from copy import deepcopy

with open(r"day12.txt", 'r') as f:
    s = f.read()


# I want mutable object.
s = [list(x) for x in s.split("\n")]

# Find start and end, replace entire map with numbers. Create a copy for part2.
for i in range(len(s)):
    for j in range(len(s[0])):
        if s[i][j] == "S":
            start = [i, j]
            s[i][j] = "a"
        elif s[i][j] == "E":
            end = [i, j]
            s[i][j] = "z"
        s[i][j] = ord(s[i][j])

s2 = deepcopy(s)

# Gets 4 neighbours
def get_four(a):
    i, j = a
    return [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]

# Checks if its within bounds
def check_valid(grid, a):
    if a[0] < 0 or a[0] >= len(grid) or a[1] < 0 or a[1] >= len(grid[0]):
        return False
    return True


# Walk through the map until you find the end coordinate. Change visited to 0.
visited = [[start], []]
step = 0
while end not in visited[-2]:
    for point in visited[-2]:
        nhbrs = get_four(point)
        for n in nhbrs:
            if check_valid(s, n) and s[n[0]][n[1]] != 0:
                if s[n[0]][n[1]] - s[point[0]][point[1]] < 2:
                    visited[-1].append(n)
        s[point[0]][point[1]] = 0
    visited.append([])
    step += 1
print(step)

# Part 2. Create an inverse of the graph and find any z aka biggest value?
start = end
target = ord("z") - ord("a") + 1 # Start from 1 since I'm setting visited nodes to 0
for i in range(len(s2)):
    for j in range(len(s2[0])):
         s2[i][j] = abs(ord("z")-s2[i][j])+1



visited = [[start], []]
visited_values = [] # Keep track of visited values
step = 0
while target not in visited_values:
    visited_values = [] # We only need last step 
    for point in visited[-2]:
        nhbrs = get_four(point)
        for n in nhbrs:
            if check_valid(s2, n) and s2[n[0]][n[1]] != 0:
                if s2[n[0]][n[1]] - s2[point[0]][point[1]] < 2:
                    visited[-1].append(n)
                    visited_values.append(s2[n[0]][n[1]])
        s2[point[0]][point[1]] = 0
    visited.append([])
    step += 1
print(step)
