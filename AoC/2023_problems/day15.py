test_data = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

with open("AoC/2023_problems/day15.txt") as f:
    data = f.read()

# Alg 0 -> + ASCII (char) -> *= 17 -> %= 256
def hash_alg(seq):
    hash = 0
    for s in seq:
        hash = ((hash + ord(s)) * 17) % 256
    return hash


def part1(data):
    instructions = data.split(",")
    hash = 0
    for ins in instructions:
        hash += hash_alg(ins)
    return hash


def part2(data):
    instructions = data.split(",")
    boxes = {k: dict() for k in range(256)}
    for ins in instructions:
        if "=" in ins:
            letters, focal_len = ins.split("=")
            box_num = hash_alg(letters)
            boxes[box_num][letters] = int(focal_len)
        else:
            letters = ins.split("-")[0]
            box_num = hash_alg(letters)
            if letters in boxes[box_num]:
                del boxes[box_num][letters]
    total_focus = 0
    for box in boxes:
        box_mul = box + 1
        for i, lens in enumerate(boxes[box].values()):
            total_focus += box_mul * (i+1) * lens
    return total_focus


print(part1(data))
print(part2(data))
