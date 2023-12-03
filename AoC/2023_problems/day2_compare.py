import time
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


def time_function(func, runs=500):
    def wrapper(text):
        t1 = time.time()
        for _ in range(runs):
            result = func(text)
        t2 = time.time()
        print(f"{func.__name__} took {t2-t1} seconds")
        return result
    return wrapper


@time_function
def original_solution(text):
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


@time_function
def nore_solution(text):
    total_p1 = 0
    total_p2 = 0
    for line in text.split("\n"):
        found = {"red": [0, 12], "green": [0, 13], "blue": [0, 14]}
        game_id = line.split()[1].split(":")[0]
        games = line.split(":")[1].split(";")
        for game in games:
            for dice in game.split(","):
                val, color = dice.split()
                if int(val) > found[color][0]:
                    found[color][0] = int(val.strip())
        if all(found[color][0] <= found[color][1] for color in found):
            total_p1 += int(game_id)
        total_p2 += found["red"][0] * found["green"][0] * found["blue"][0]
    return total_p1, total_p2


with open("AoC/2023_problems/day2.txt", "r") as f:
    test = f.read()

print(original_solution(test))
print(nore_solution(test))
