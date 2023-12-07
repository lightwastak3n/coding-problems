test_input = """Time:      7  15   30
Distance:  9  40  200"""


with open("AoC/2023_problems/day6.txt", 'r') as f:
    s = f.read()


def solve(text):
    times, distances = [x.split(":")[1].split() for x in text.split("\n")]
    p1 = 1
    for i in range(len(times)):
        dt = [x*(int(times[i])-x) for x in range(0, int(times[i])+1)]
        p1 *= sum([x > int(distances[i]) for x in dt])
    t, d = [int("".join(x)) for x in [times, distances]]
    x1 = (t + (t**2 - 4*d)**0.5) / 2
    x2 = (t - (t**2 - 4*d)**0.5) / 2
    return p1, int(x1) - int(x2)

print(solve(s))
