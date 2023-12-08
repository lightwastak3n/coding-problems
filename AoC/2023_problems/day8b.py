from math import lcm


with open("AoC/2023_problems/day8.txt") as f:
    data = f.read()


def solve(text):
    instructions, nodes = text.split("\n\n")
    node_dict = {}
    for node in nodes.split("\n"):
        name, children = node.split(" = (")
        children = children.replace(")", "").split(", ")
        node_dict[name] = children

    a_nodes = list(filter(lambda x: x[-1] == "A", node_dict.keys()))
    nodes_steps = {k: 0 for k in a_nodes}
    while a_nodes:
        start_node = a_nodes.pop()
        node = start_node
        i = 0
        while node[-1] != "Z":
            if i == len(instructions):
                i = 0
            next_step = 0 if instructions[i] == "L" else 1
            node = node_dict[node][next_step]
            nodes_steps[start_node] += 1
            i += 1
    return nodes_steps["AAA"], lcm(*nodes_steps.values())

print(solve(data))
