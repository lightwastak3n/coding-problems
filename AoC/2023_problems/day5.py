test_data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


with open("AoC/2023_problems/day5.txt", "r") as f:
    pdata = f.read()


def solve(text):
    data = text.split("\n")
    seeds = [int(s) for s in data[0].split(": ")[1].split()]
    mappings = []
    i = 3
    while i < len(data):
        sub_map = []
        while i < len(data) and data[i] != "":
            dest, src, lng = [int(x) for x in data[i].split()]
            sub_map.append([src, dest, lng])
            i += 1
        mappings.append(sub_map)
        i += 2
    # Using seeds and generated mappings for part 2
    p2 = solve_p2(seeds.copy(), mappings)
    for mp in mappings:
        current = []
        for seed in seeds:
            found = seed
            for m in mp:
                if m[0] <= seed < m[0]+m[2]:
                    found = seed - m[0] + m[1]
                    break
            current.append(found)
        seeds = current
    return min(seeds), p2


def solve_p2(seeds, mappings):
    # Switch from seed, range -> seed_start, seed_end
    current_ranges = [[seeds[i], seeds[i] + seeds[i+1]] for i in range(0,len(seeds),2)]
    # Go through all the layers
    for layer in mappings:
        next_ranges = []
        while current_ranges:
            # We are pulling all the ranges through current layer conversion
            current_range = current_ranges.pop()
            for mp in layer:
                start, end = current_range
                src, dest, lng = mp
                if src <= start < (src + lng) or src < end <= (src + lng):
                    overlap = [max(start, src), min(end, src + lng)]
                    converted_range = [overlap[0] - src + dest, overlap[1] - src + dest]
                    # We are done with this move it to the next layer
                    next_ranges.append(converted_range)
                    if start < overlap[0]:
                        # left over on the left, keep it in the loop
                        current_ranges.append([start, overlap[0]])
                    if end > overlap[1]:
                        # left over on the right, keep it in the loop
                        current_ranges.append([overlap[1], end])
                    break
            else:
                # No overlap move it to the next layer
                next_ranges.append(current_range)
        current_ranges = next_ranges
    return sorted(current_ranges)[0][0]

print(solve(pdata))
