from os import path
from get_data import get_input


# Check if input file exists and if not download it and use it
if path.exists("problems/day5.txt"):
    with open("problems/day5.txt", "r") as f:
        day5 = f.read()
else:
    day5 = get_input(2022, 4)
day5 = day5.split('\n')
day5.pop() # Get rid of the last empty line



