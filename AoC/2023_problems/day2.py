import re


test = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


conditions = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def solve(text):
    total_p1 = 0
    total_p2 = 0
    for line in text.split("\n"):
        found = {"red": 0, "green": 0, "blue": 0}
        game_id = line.split()[1].split(":")[0]
        games = line.split(":")[1].split(";")
        games_stats = []
        for game in games:
            for color in conditions:
                if color in game:
                    #  Part 1
                    n = re.findall(rf'\d+ {color}', game)[0].split()[0]
                    games_stats.append(int(n) <= conditions[color])
                    # Part 2
                    if int(n) > found[color]:
                        found[color] = int(n)
        if all(games_stats):
            total_p1 += int(game_id)
        total_p2 += found["red"] * found["green"] * found["blue"]
    return total_p1, total_p2


if solve(test) == (8, 2286):
    with open("AoC/2023_problems/day2.txt") as f:
        data = f.read()
        p1, p2 = solve(data)
        print(p1, p2)
