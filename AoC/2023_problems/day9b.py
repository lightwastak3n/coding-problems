with open("AoC/2023_problems/day9.txt") as f:
    data = f.read()

sequences = [list(map(int, x.split())) for x in data.split("\n")]


def find_element(seq):
    diff = []
    for i in range(len(seq)-1):
        diff.append(seq[i+1] - seq[i])
    if all(x == 0 for x in diff):
        return 0
    else:
        return diff[-1] + find_element(diff)


def solve():
    p1, p2 = 0, 0
    for seq in sequences:
        p1 += seq[-1] + find_element(seq)
        p2 += seq[0] + find_element(seq[::-1])
    return p1, p2


print(solve())
