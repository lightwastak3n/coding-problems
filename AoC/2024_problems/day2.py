test_input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""


with open("AoC/2024_problems/day2.txt", "r") as f:
    data = f.read()


def valid_report(report):
    sign = 1 if report[1] - report[0] >= 0 else -1
    for i in range(0, len(report) - 1):
        diff = report[i+1] - report[i]
        if diff * sign > 3 or diff * sign <= 0:
            return False
    return True


def solve(text):
    reports = text.split("\n")
    safe = 0
    could_be_safe = 0
    for report in reports:
        nums = [int(x) for x in report.split()]
        safe += valid_report(nums)
        if not safe:
            could_be_safe += any(valid_report(nums[:i] + nums[i+1:]) for i in range(0, len(nums)))
    print(safe)
    print(safe + could_be_safe)


solve(data)
