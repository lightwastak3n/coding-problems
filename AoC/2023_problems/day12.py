from itertools import combinations
from functools import cache

test_data = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


def get_groups(model):
    groups = []
    i = 0
    while i < len(model):
        s = 0
        if model[i] == "#":
            while i < len(model) and model[i] == "#":
                s += 1
                i += 1
            groups.append(s)
        i += 1
    return groups


def valid_combo(model, condition):
    if get_groups(model) == list(condition):
        return True
    return False


def create_combination(model, combo):
    new_model = []
    for i, char in enumerate(model):
        if i in combo:
            new_model.append("#")
        else:
            new_model.append(char)
    return new_model


# Cant brute force part 2 need something else. Could have used this for part 1.
@cache
def get_permutations(springs, condition):
    # No conditions and and no springs = 1 combo
    if not condition and (springs == "" or "#" not in springs):
        return 1
    # either empty springs but we expect some or we dont expect anything but have springs = 0 combinations
    if (condition and springs == "") or (not condition and "#" in springs):
        return 0
    total = 0
    # If the first char is . or ? (turn it into a dot) remove it and recurse
    if springs[0] in ".?":
        total += get_permutations(springs[1:], condition)
    # If the first char is # or ?
    if springs[0] in "#?":
        # we need to have space for current condition and no . so that we can fit everything
        if condition[0] <= len(springs) and "." not in springs[:condition[0]] and (condition[0] == len(springs) or springs[condition[0]] != "#"):
            total += get_permutations(springs[condition[0] + 1:], condition[1:])
    return total


def solve(data):
    p1, p2 = 0, 0
    for line in data.split("\n"):
        springs, condition = line.split()
        condition = tuple(map(int, condition.split(",")))

        slots_pos = []
        springs_present = 0
        for i,char in enumerate(springs):
            if char == "?":
                slots_pos.append(i)
            if char == "#":
                springs_present += 1
        inserts_needed = sum(condition) - springs_present

        combos = list(combinations(slots_pos, inserts_needed))
        model = tuple(springs)
        for combo in combos:
            new_model = create_combination(model, combo)
            if valid_combo(new_model, condition):
                p1 += 1
        p1 += get_permutations(springs, condition)
        # Part 2
        springs = "?".join([springs] * 5)
        condition *= 5
        p2 += get_permutations(springs, condition)
    return p1, p2


with open("AoC/2023_problems/day12.txt", "r") as f:
    data = f.read()

print(solve(data))
