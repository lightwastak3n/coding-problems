from os import path
from get_data import get_input
from string import ascii_lowercase, ascii_uppercase


# Check if input file exists and if not download it and use it
if path.exists("day3.txt"):
    with open("day3.txt", "r") as f:
        day3 = f.read()
else:
    day3 = get_input(2022, 4)

day3 = day3.split('\n')
day3.pop() # Get rid of the last empty line


# Solution 1: Tried to do it fast and this is the first thing that came to mind
## Setup for item priority
lookup = "*" + ascii_lowercase + ascii_uppercase
lookup_dict = {y:x for x, y in enumerate(lookup)}

## First part of the problem
total1 = 0
for rucksack in day3:
    for i in range(len(rucksack)//2):
        if rucksack[i] in rucksack[len(rucksack)//2:]:
            total1 += lookup_dict[rucksack[i]]
            break
print(total1)

## Second part of the problem
total2 = 0
group = []
for i in range(0, len(day3), 3):
    group = [day3[i], day3[i+1], day3[i+2]]
    for item in group[0]:
        if item in group[1] and item in group[2]:
            total2 += lookup_dict[item]
            break
    group = []
print(total2)


####################################################################
# Solution 2: sets?? and there's probably a way to use ord()
total1 = 0
total2 = 0
group = []
get_priority = lambda item : ord(item) - 96 if item.islower() else ord(item) - 38
for i in range(len(day3)):
    rucksack = day3[i]
    duplicate1 = set(rucksack[:len(rucksack)//2]) & set(rucksack[len(rucksack)//2:])
    total1 += get_priority(duplicate1.pop())

    # Collect groups of 3
    group.append(rucksack)
    if len(group) == 3:
        duplicate2 = set(group[0]) & set(group[1]) & set(group[2])
        total2 += get_priority(duplicate2.pop())
        group = []
    
print(total1)
print(total2)
