from get_data import get_input
from os import path


# Check if input file exists and if not download it and use it
if path.exists("day13.txt"):
    with open("day13.txt", "r") as f:
        s = f.read()
else:
    s = get_input(2022, 13)

s = s.split("\n")
s.pop()

t = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""


def parser(packet):
    

