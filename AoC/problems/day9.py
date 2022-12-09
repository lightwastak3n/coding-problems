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

t_case = '''R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20'''

t_sol = 13

moves = ""
for line in t_case.split("\n"):
    direction, amount = line.split(" ")
    moves += direction * int(amount)


def move(dir, loc):
    match dir:
        case "R": loc[0] += 1
        case "L": loc[0] -= 1
        case "U": loc[1] += 1
        case "D": loc[1] -= 1
    return loc


def distance(hloc, tloc):
    return math.sqrt((hloc[0]-tloc[0])**2 + (hloc[1]-tloc[1])**2)


head, tail =  [0,0], [0,0]
visited = [[0, 0]]
for d in moves:
    phead = [head[0], head[1]]
    head = move(d, head)
    if distance(head, tail) >= 2:
        tail = phead
        if tail not in visited:
            visited.append([tail[0], tail[1]])
print(len(visited))

current_pos = [[0, 0] for i in range(10)]
visited = [[0,0]]
for d in moves:
    previous_position = [[node[0], node[1]] for node in current_pos]
    current_pos[9] = move(d, current_pos[9])
    for i in range(8,-1,-1):
        if distance(current_pos[i], current_pos[i+1]) >= 2:
            current_pos[i] = previous_position[i+1]
    if current_pos[0] not in visited:
        visited.append(current_pos[0])
print(len(visited))
