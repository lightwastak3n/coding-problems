from os import path
from get_data import get_input
from copy import deepcopy

# Check if input file exists and if not download it and use it
if path.exists("day5.txt"):
    with open("day5.txt", "r") as f:
        day5 = f.read()
else:
    day5 = get_input(2022, 5)
day5 = day5.split('\n')
day5.pop() # Get rid of the last empty line

# Create empty stacks, find index row, get index of each box
index_row = 0
indexes = []
for row in day5:
    clean_row = row.split()
    if clean_row[0] == "1":
        stacks = {i: [] for i in clean_row}
        for item in clean_row:
            indexes.append(row.index(item))
        break
    index_row += 1

# Build stacks
for row in day5[:index_row]:
    for stack, index in zip(stacks.keys(), indexes):
        if row[index] != " ":
            stacks[stack].append(row[index])

# Reverse stacks because I'm an idiot and create starting stacks for the second part
for id in stacks:
    stacks[id].reverse()
stacks2 = deepcopy(stacks)

# Read instructions and move crates
for row in day5[index_row+2:]:
    to_move, source, dest = [x for x in row.split() if x.isnumeric()]
    for i in range(int(to_move)):
        stacks[dest].append(stacks[source].pop())
    # Second part of the problem
    stacks2[source], move = stacks2[source][:-int(to_move)], stacks2[source][-int(to_move):]
    stacks2[dest] += move

t1, t2 = "", ""
for id in stacks:
    t1 += stacks[id][-1]
    t2 += stacks2[id][-1]
print(t1, t2)
