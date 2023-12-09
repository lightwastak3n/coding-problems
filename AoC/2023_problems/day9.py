test_data = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
10 9 8 7 6 5
22 18 13 7 0 -8"""


with open("AoC/2023_problems/day9.txt") as f:
    data = f.read()


def solve(data):
    sequences = [list(map(int, x.split())) for x in data.split("\n")]
    p1, p2 = 0, 0
    for seq in sequences:
        current_seq = seq
        n_rows = []
        while not all([x == 0 for x in current_seq]):
            new_row = [current_seq[i] - current_seq[i-1] for i in range(1, len(current_seq))]
            n_rows.append(new_row)
            current_seq = new_row
        last_one = 0
        before_first = 0
        for i in range(len(n_rows)-2, -1, -1):
            last_one += n_rows[i][-1]
            before_first = n_rows[i][0] - before_first
        p1 += last_one + seq[-1]
        p2 += seq[0] - before_first
    return p1, p2


print(solve(data))
