import math


with open("AoC/2023_problems/day8.txt") as f:
    data = f.read()


def lcm(nums):
    lcm = 1
    for num in nums:
        lcm = lcm * num // math.gcd(lcm, num)
    return lcm


def solve(text):
    instructions, nodes = text.split("\n\n")
    node_dict = {}
    for node in nodes.split("\n"):
        name, children = node.split(" = (")
        children = children.replace(")", "").split(", ")
        node_dict[name] = children
    current_node = "AAA"
    i, p1 = 0, 0
    while current_node != "ZZZ":
        if i == len(instructions):
            i = 0
        next_step = 0 if instructions[i] == "L" else 1
        current_node = node_dict[current_node][next_step]
        i += 1
        p1 += 1
    # part 2
    p2 = lcm(solve_p2(instructions, node_dict))
    print(p1, p2)


def solve_p2(instructions,  node_dict):
    current_nodes = list(filter(lambda x: x[-1] == "A", node_dict.keys()))
    substeps = []
    while current_nodes:
        node = current_nodes.pop()
        substeps.append(0)
        i = 0
        while node[-1] != "Z":
            if i == len(instructions):
                i = 0
            next_step = 0 if instructions[i] == "L" else 1
            node = node_dict[node][next_step]
            substeps[-1] += 1
            i += 1
    return substeps

solve(data)
