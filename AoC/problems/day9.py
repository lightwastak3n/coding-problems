from os import path
from get_data import get_input
import math


# Check if input file exists and if not download it and use it
if path.exists("day9.txt"):
    with open("day9.txt", "r") as f:
        s = f.read()
else:
    s = get_input(2022, 9)

s = s.split("\n")
s.pop()

# Get a list of moves like this "RRRDDDULLRRRRR..."
moves = ""
for line in s:
    direction, amount = line.split(" ")
    moves += direction * int(amount)


def move(dir, loc):
    match dir:
        case "R": loc[0] += 1
        case "L": loc[0] -= 1
        case "U": loc[1] += 1
        case "D": loc[1] -= 1
    return loc


def distance(head, tail):
    return math.sqrt((head[0] - tail[0]) ** 2 + (head[1] - tail[1]) ** 2)

# Tail will just follow the head if the distance is more than 1 "unit"
head, tail =  [0, 0], [0, 0]
visited = [[0, 0]]
for d in moves:
    phead = [head[0], head[1]]
    head = move(d, head)
    if distance(head, tail) >= 2:
        tail = phead
        if tail not in visited:
            visited.append([tail[0], tail[1]])
print(len(visited))

# :( rope doesn't move like I expected it. Need a different movement algorithm.
def get_moves(head, tail):
    movement = ""
    if head[0] > tail[0]:
        movement += "R"
    elif head[0] < tail[0]:
        movement += "L"
    if head[1] > tail[1]:
        movement += "U"
    elif head[1] < tail[1]:
        movement += "D"
    return movement


rope = [[0, 0] for _ in range(10)]
visited2 = [[0, 0]]
for d in moves:
    rope[9] = move(d, rope[9])
    for i in range(8, -1, -1):
        if distance(rope[i], rope[i+1]) >= 2:
            movement = get_moves(rope[i+1], rope[i])
            for p in movement:
                rope[i] = move(p, rope[i])
    if rope[0] not in visited2:
        visited2.append([rope[0][0], rope[0][1]])
print(len(visited2))
