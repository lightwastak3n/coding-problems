test_input = """Time:      7  15   30
Distance:  9  40  200"""


with open("AoC/2023_problems/day6.txt", 'r') as f:
    s = f.read()


def part1(text):
    lines = text.split("\n")
    td = zip(lines[0].split(":")[1].split(), lines[1].split(":")[1].split())
    total = 1
    for r in td:
        distances = [x*(int(r[0])-x) for x in range(0, int(r[0])+1)]
        total *= sum([x > int(r[1]) for x in distances])
    return total


def part2(text):
    text = text.replace(" ", "")
    t = int(text.split("\n")[0].split(":")[1])
    d = int(text.split("\n")[1].split(":")[1])
    x1 = (t + (t**2 - 4*d)**0.5) / 2
    x2 = (t - (t**2 - 4*d)**0.5) / 2
    return int(x1) - int(x2)


if part1(test_input) == 288:
    print(part1(s))
if part2(test_input) == 71503:
    print(part2(s))
