test = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""


test2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""


def solve(input, part):
    total = 0
    for line in input.split():
        if part == 2:
            line = fixline(line)
        for c in line:
            if c.isnumeric():
                total += int(c) * 10
                break
        for c in line[::-1]:
            if c.isnumeric():
                total += int(c)
                break
    print(total)


def fixline(line):
    nums = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    # check from front
    sub = ""
    for c in line:
        if c.isnumeric():
            break
        sub += c
        for n in nums:
            if n in sub:
                line = line.replace(n, str(nums[n]))
                break
    # check from back
    sub = ""
    for c in line[::-1]:
        if c.isnumeric():
            break
        sub = c + sub
        for n in nums:
            if n in sub:
                line = line.replace(n, str(nums[n]))
                break
    return line


with open("AoC/2023_problems/day1.txt", "r") as f:
    inpt = f.read()
    solve(inpt, 1)
    solve(inpt, 2)
