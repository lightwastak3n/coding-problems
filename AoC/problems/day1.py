from get_data import get_input

session_val = "redacted"
pr1 = get_input(session_val, 2022, 1)


# Solution 1: First try
elfs = [0]
for cal in pr1.split("\n"):
    if cal.isnumeric():
        elfs[-1] += int(cal)
    else:
        elfs.append(0)
elfs.sort(reverse=True)

print(elfs[0])
print(sum(elfs[:3]))


# Solution 2: After some thinking - a bit shorter
elfs = [sum(map(int, package.split('\n'))) for package in pr1.split("\n\n")[:-1]]
elfs.sort(reverse=True)

print(elfs[0])
print(sum(elfs[:3]))
