from os import path
from get_data import get_input

# Check if input file exists and if not download it and use it
if path.exists("day6.txt"):
    with open("day6.txt", "r") as f:
        s = f.read()
else:
    s = get_input(2022, 6)

for i in range(len(s)-4):
    if len(set(s[i:i+4])) == 4:
        print(i+4)
        break

for i in range(len(s)-14):
    if len(set(s[i:i+14])) == 14:
        print(i+14)
        break
