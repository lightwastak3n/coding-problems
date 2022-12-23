from os import path
from get_data import get_input


# Check if input file exists and if not download it and use it
if path.exists("day10.txt"):
    with open("day10.txt", "r") as f:
        s = f.read()
else:
    s = get_input(2022, 10)

s = s.split("\n")
s.pop()


def draw_pixel(cycle, x, pixels):
    if (cycle - 1) % 40 in [x - 1, x, x + 1]:
        pixels[cycle-1] = "#"


x = 1
cycle = 1
total = 0
pixels = list(" " * 240)
for line in s:
    if line.startswith("ad"):
        p = int(line.split(" ")[1])
        cycle += 1
        draw_pixel(cycle, x, pixels)
        if cycle == 20 or (cycle-20) % 40 == 0:
            total += cycle * x
        x += p
        cycle += 1
    else:
        cycle += 1
    if cycle == 20 or (cycle-20) % 40 == 0:
            total += cycle * x
    draw_pixel(cycle, x, pixels)

print(total)
print("".join(pixels[:40]))
print("".join(pixels[40:80]))
print("".join(pixels[80:120]))
print("".join(pixels[120:160]))
print("".join(pixels[160:200]))
print("".join(pixels[200:240]))
