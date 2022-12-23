from get_data import get_input
from os import path


# Check if input file exists and if not download it and use it
if path.exists("day18txt"):
    with open("day18.txt", "r") as f:
        s = f.read()
else:
    s = get_input(2022, 18)

s = s.split("\n")
s.pop()
