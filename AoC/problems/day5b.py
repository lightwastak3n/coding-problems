from os import path
from get_data import get_input


# Get the input data as a list
if path.exists("day5.txt"):
    with open("day5.txt", "r") as f:
        data = f.read()
else:
    data = get_input(2022, 5)
data = data.split('\n')
data.pop() # Get rid of the last empty line

# Just looking at the input
index_row = 8

# The letters in crates are actually every 4th character in the input
stacks = [[] for _ in range(18)] # create empty stacks for both parts
for row in data[index_row-1::-1]:
    for i, crate in enumerate(row[1::4]):
        if crate != " ":
            stacks[i].append(crate)
            stacks[i+9].append(crate)

# Read instructions and move crates
for row in data[index_row+2:]:
    q, a, b = [int(x) for x in row.split() if x.isnumeric()] # q = quantity, a = source, b = destination
    for i in range(q):
        stacks[b-1].append(stacks[a-1].pop())
    stacks[b+8].extend(stacks[a+8][-q:])
    stacks[a+8] = stacks[a+8][:-q]

print("".join(x[-1] for x in stacks[:9]), "".join(x[-1] for x in stacks[9:]))
