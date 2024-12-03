test_input = """3   4
4   3
2   5
1   3
3   9
3   3"""


with open("AoC/2024_problems/day1.txt", "r") as f:
    data = f.read()


def solve(text):
    list1 = []
    list2 = []
    for line in text.split("\n"):
        a, b = line.split()
        list1.append(int(a))
        list2.append(int(b))
    list1.sort()
    list2.sort()
    first_part = 0
    second_part = 0
    for i in range(len(list1)):
        first_part += abs(list1[i] - list2[i])
        second_part += list1[i] * list2.count(list1[i])
    print(first_part)
    print(second_part)

solve(data)
