from os import path
from get_data import get_input


# Check if input file exists and if not download it and use it
if path.exists("day2.txt"):
    with open("day2.txt", "r") as f:
        day2 = f.read()
else:
    day2 = get_input(2022, 4)

day2 = day2.split('\n')
day2.pop() # Get rid of the last empty line


# Solution 1
mapping = {
    "AX": 4, "AY": 8, "AZ":3,
    "BX": 1, "BY": 5, "BZ": 9,
    "CX": 7, "CY": 2, "CZ": 6
    }

score1 = 0
for match in day2:
    score1 += mapping[match[0] + match[2]]
print(score1)

op_move = ["", "A", "B", "C", ""]
my_move = ["Z", "X", "Y", "Z", "X"]
result_move = {"X": -1, "Y": 0, "Z": 1}

score2 = 0
for match in day2:
    op = match[0]
    result = match[2]
    me = my_move[op_move.index(op) + result_move[result]]
    score2 += mapping[op+me]
print(score2)
