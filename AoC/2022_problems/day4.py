from os import path
from get_data import get_input


# Check if input file exists and if not download it and use it
if path.exists("day4.txt"):
    with open("day4.txt", "r") as f:
        day4 = f.read()
else:
    day4 = get_input(2022, 4)

day4 = day4.split('\n')
day4.pop() # Get rid of the last empty line

t1, t2 = 0, 0
for pair in day4:
    a1, a2, b1, b2 = map(int, pair.replace(',', '-').split('-'))
    if (a1 <= b1 and a2 >= b2) or (b1 <= a1 and b2 >= a2):
        t1 += 1
    if (a2 >= b1) and (a1 <= b2):
        t2 += 1
print(t1, t2)
