t = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""

t = t.split("\n\n")
 
# Conditions - we are looking for either first fail or pass
# 1. If both values are integers the first one should be smaller. If they are the same continue.
# 2. If both values are lists compare the values 1 by 1. If first runs out of items its correct, 
# if the second first runs out its not the right order. If same length and same digits then continue.
# 3. If exactly one value is an integer convert the other to a list

# c = 0
# for pair in t:
#     l, r = pair.split("\n")
#     l = eval(f"list({l})")
#     r = eval(f"list({r})")
#     i, j = 0, 0
#     while i < len(l) and j < len(r):
#         if type(l[i]) == type(r[j]) == int:
#             if l[i] < r[j]:
#                 c += 1
#                 i = len(l)
#             elif l[i] > r[j]:
#                 i = len(l)
#             i += 1
#             j += 1
#         elif type(l[i]) == type(r[j]) == list:
#             subi, subj = 0, 0
#             while subi < len(l[i]) and subj < len(r[j]):
#                 if l[i][subi] < r[j][subj]:
#                     c += 1
#                     subi = len(l[i])
#                 elif l[i][subi] > r[j][subj]:
#                     subi = len(l[i])
#                 subi += 1
#                 subj += 1

# Conditions - we are looking for either first fail or pass
# 1. If both values are integers the first one should be smaller. If they are the same continue.
# 2. If both values are lists compare the values 1 by 1. If first runs out of items its correct, 
# if the second first runs out its not the right order. If same length and same digits then continue.
# 3. If exactly one value is an integer convert the other to a list

def check(a, b):
    if type(a) == type(b) == int:
        if a < b:
            return True
        elif a > b:
            return False
    else:
        a  = list(a) if type(a) != int else [a]
        b  = list(b) if type(b) != int else [b]
        i = 0
        while i < len(a) and i < len(b):
            return check(a[i], b[i])




c = 0
counter = 1
for pair in t:
    l, r = pair.split("\n")
    l = eval(f"list({l})")
    r = eval(f"list({r})")
    checks = []
    for p in zip(l, r):
        if type(p[0]) == type(p[1]) == int:
            if p[0] < p[1]:
                checks.append(1)
            elif p[0] > p[1]:
                checks.append(-1)
        else:
            pa = list(p[0]) if type(p[0]) != int else [p[0]]
            pb = list(p[1]) if type(p[1]) != int else [p[1]]
            i = 0
            while i < len(pa) and i < len(pb):
                if pa[i] < pb[i]:
                    checks.append(1)
                elif pa[i] > pb[i]:
                    checks.append(-1)
                i += 1
            if i < len(pb):
                checks.append(1)
            elif i < len(pa):
                checks.append(-1)
        if -1 not in checks:
            print(counter)
            c += counter
            break
    counter += 1

print(c)