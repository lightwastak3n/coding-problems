from get_data import get_input

from os import path
from copy import deepcopy
from functools import reduce
import math

# Check if input file exists and if not download it and use it
if path.exists("day11.txt"):
    with open("day11.txt", "r") as f:
        s = f.read()
else:
    s = get_input(2022, 11)

s = s.split("\n\n")

# Calculate new worry based on old worry, operation given and divisor (3 in part1, 1 in part2)
def new_worry(old_worry, operation, d):
    new_worry = []
    do = lambda x: math.floor(x/d)
    for w in old_worry:
        if "old * old" == operation:
            new_worry.append(do(w * w))
        elif "*" in operation:
            new_worry.append(do(w * int(operation.split("* ")[1])))
        elif "+" in operation:
            new_worry.append(do(w + int(operation.split("+ ")[1])))
        else:
            print(f"wtf is this {operation}")
    return new_worry


# Collect all monkeys and build data list and create a copy for the second part since you are going to mutate it.
ms1 = [[] for _ in range(len(s))]
for i, monkey in enumerate(s):
    d = monkey.split("\n")
    for l in d:
        if l.startswith("  Starting items:"):
            worry_lvl = [int(x.strip()) for x in l.split(": ")[1].split(",")]
            ms1[i].append(worry_lvl)
        elif l.startswith("  Operation"):
            ms1[i].append(l.split("= ")[1])
        elif l.startswith("  Test"):
            ms1[i].append(int(l.split("by ")[1]))
        elif l.startswith("    If true:"):
            ms1[i].append(int(l.split("monkey ")[1]))
        elif l.startswith("    If false:"):
            ms1[i].append(int(l.split("monkey ")[1]))
    ms1[i].append(0)

ms2 = deepcopy(ms1)

# Monkey business part 1
for _ in range(20):
    for i in range(len(ms1)):
        nw = new_worry(ms1[i][0], ms1[i][1], 3)
        ms1[i][0] = []
        for w in nw:
            if w % ms1[i][2]:
                ms1[ms1[i][4]][0].append(w)
            else:
                ms1[ms1[i][3]][0].append(w)
            ms1[i][-1] += 1

# Collect all inspections
inspections = sorted([m[-1] for m in ms1])
print(inspections[-1] * inspections[-2])

# Monkey business part 2
# Huge numbers but x % y = 0 and x % z = 0 means x % (y * z) = 0 so lets collect all mods
dd = reduce(lambda a, b: a * b, [m[2] for m in ms2])
for _ in range(10000):
    for i in range(len(ms2)):
        nw = new_worry(ms2[i][0], ms2[i][1], 1)
        ms2[i][0] = []
        for w in nw:
            w = w % dd
            if w % ms2[i][2]:
                ms2[ms2[i][4]][0].append(w)
            else:
                ms2[ms2[i][3]][0].append(w)
            ms2[i][-1] += 1

# Collect all inspections
inspections = sorted([m[-1] for m in ms2])
print(inspections[-1] * inspections[-2])
