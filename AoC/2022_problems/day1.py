from os import path
from get_data import get_input


# Check if input file exists and if not download it and use it
if path.exists("day1.txt"):
    with open("day1.txt", "r") as f:
        day1 = f.read()
else:
    day1 = get_input(2022, 4)

day1 = day1.split('\n')
day1.pop() # Get rid of the last empty line


# Solution 1: First try
elves = [0]
for cal in day1:
    if cal.isnumeric():
        elves[-1] += int(cal)
    else:
        elves.append(0)
elves.sort(reverse=True)

print(elves[0])
print(sum(elves[:3]))


####################################################################
# Solution 2: After some thinking - a bit shorter
with open("problems/day1.txt", "r") as f:
        day1 = f.read()
elves = [sum(map(int, package.split('\n'))) for package in day1.split("\n\n")[:-1]]
elves.sort(reverse=True)

print(elves[0])
print(sum(elves[:3]))
