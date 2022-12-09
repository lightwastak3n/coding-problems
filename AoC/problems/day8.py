from os import path
from get_data import get_input


# Check if input file exists and if not download it and use it
if path.exists("day8.txt"):
    with open("day8.txt", "r") as f:
        s = f.read()
else:
    s = get_input(2022, 8)

s = s.split("\n")
s.pop()


def visible(f, i, j):
    # Check the row
    if max(f[i][0:j]) < f[i][j]:
        return True
    elif max(f[i][j+1:]) < f[i][j]:
        return True
    # Build and check the column
    column = [f[r][j] for r in range(len(f))]
    if max(column[:i]) < f[i][j]:
        return True
    elif max(column[i+1:]) < f[i][j]:
        return True
    return False


s = [list(map(int,x)) for x in s]

d = len(s)
total1 = d*4 - 4

for i in range(1, d-1):
    for j in range(1, d-1):
        if visible(s, i, j):
            total1 += 1
print(total1)


def number_visible(f, i, j):
    row = f[i]
    column = [f[r][j] for r in range(len(f))]

    def check_list(lst, tree):
        subtotal = 0
        for val in lst:
            if val < tree:
                subtotal += 1
            else:
                subtotal += 1
                return subtotal
        return subtotal

    # Check the row
    left_total = check_list(row[j-1::-1], row[j])
    right_total = check_list(row[j+1:], row[j])
    # Check the column
    top_total = check_list(column[i-1::-1], column[i])
    bottom_total = check_list(column[i+1:], column[i])
    score = left_total * right_total * top_total * bottom_total
    return score
    

scenic_score = 0
for i in range(1, d-1):
    for j in range(1, d-1):
        score = number_visible(s, i, j)
        scenic_score = max(scenic_score, score)
print(scenic_score)
