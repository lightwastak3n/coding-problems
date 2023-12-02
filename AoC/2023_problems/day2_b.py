def solve(text):
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
