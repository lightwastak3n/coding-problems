from os import path
from test_day import proceed

with open("day7.txt", "r") as f:
    s = f.read()

s = s.split("\n")
s.pop()

class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.files_size = 0
    
    def add_child(self, child):
        self.children.append(child)

    def add_file(self, file):
        fsize = file.split()[0]
        self.files_size += int(fsize)



current_dir = Dir("/", None)
dirs = [current_dir]
for line in s[1:]:
    if line == "$ ls":
        continue
    elif "$ cd" in line:
        if ".." in line:
            current_dir = current_dir.parent
        else:
            current_dir = [child for child in current_dir.children if child.name == line.split()[2]][0]
    elif "dir" in line:
        new_dir = Dir(line.split()[1], current_dir)
        current_dir.add_child(new_dir)
        dirs.append(new_dir)
    else:
        current_dir.add_file(line)


# Go through it and find all sizes
dir_size = []
for d in dirs:
    queue = [*d.children]
    total = d.files_size
    while queue:
        current = queue.pop()
        total += current.files_size
        queue.extend(current.children)
    dir_size.append(total)
# Find the part 1
part1 = sum([x for x in dir_size if x <= 100000])
# Find the part 2
unused_space = 70000000 - max(dir_size)
for d in sorted(dir_size):
    if unused_space + d >= 30000000:
        part2 = d
        break

print(part1)
print(part2)
