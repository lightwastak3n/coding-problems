test = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def solve(text):
    lines = text.split("\n")
    p1 = 0
    p2 = [1] * len(lines)
    for i, line in enumerate(lines):
        data = line.split("|")
        winnings_nums = set(data[0].split(":")[1].split())
        draw = set(data[1].split())
        p1 += 2 ** (len(winnings_nums & draw) - 1) // 1
        for j in range(i+1, i+1+len(winnings_nums & draw)):
            p2[j] += p2[i]
    return int(p1), sum(p2)

with open("AoC/2023_problems/day4.txt") as f:
    if solve(test) == (13, 30):
        print(solve(f.read()))
