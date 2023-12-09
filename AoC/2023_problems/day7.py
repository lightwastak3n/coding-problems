from collections import defaultdict

test_case = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


with open("AoC/2023_problems/day7.txt") as f:
    data = f.read()


def convert_hand(hand, part=1):
    card_type = "AKQJT98765432"
    new_type = "abcdefghijklm"
    mapping = {card_type[i]: new_type[i] for i in range(len(card_type))}
    if part == 2:
        mapping["J"] = "z"
    new_hand = ""
    for c in hand:
        new_hand += mapping[c]
    return new_hand


def get_hand_val(hand):
    cards_set = list(set(hand))
    match len(cards_set):
        case 1:
            return 6
        case 2:
            if hand.count(cards_set[0]) in [2, 3]:
                return 4
            else:
                return 5
        case 3:
            if hand.count(cards_set[0]) * hand.count(cards_set[1]) * hand.count(cards_set[2]) == 4:
                return 2
            return 3
        case 4:
            return 1
        case 5:
            return 0


def joker_card_val(hand):
    cards = list(set(hand))
    if len(cards) == 1:
        return 6
    counts = [hand.count(card) for card in cards]
    jokers = hand.count("J")
    match len(cards), jokers:
        case 5, 1:
            # 2345J -> 23455
            return 1
        case 4, 1:
            # 2344J -> 23444
            return 3
        case 3, 1:
            if 2 in counts:
                # 2233J -> 22333
                return 4
            # 2333J -> 23333
            return 5
        case 2, 1:
            # 2222J -> 22222
            return 6
        case 4, 2:
            # 234JJ -> 23444
            return 3
        case 3, 2:
            # 233JJ -> 23333
            return 5
        case 2, 2:
            # 222JJ -> 22222
            return 6
        case 3, 3:
            # 23JJJ -> 23333
            return 5
        case 2, 3:
            # 22JJJ -> 22222
            return 6
        case 2, 4:
            # 2JJJJ -> 22222
            return 6


def solve(data):
    hands_bids = {line.split()[0]:int(line.split()[1]) for line in data.split("\n")}
    hand_values = defaultdict(list)
    joker_hand_values = defaultdict(list)
    for hand in hands_bids:
        hand_values[get_hand_val(hand)].append(hand)
        if "J" in hand:
            joker_hand_values[joker_card_val(hand)].append(hand)
        else:
            joker_hand_values[get_hand_val(hand)].append(hand)
    p1, p2 = 0, 0
    i, j= 1, 1
    for hand_val in [0, 1, 2, 3, 4, 5, 6]:
        if hand_val in hand_values:
            sorted_hands = sorted(hand_values[hand_val], key=lambda x: convert_hand(x), reverse=True)
            for hand in sorted_hands:
                p1 += i * hands_bids[hand]
                i += 1
        if hand_val in joker_hand_values:
            sorted_hands = sorted(joker_hand_values[hand_val], key=lambda x: convert_hand(x, 2), reverse=True)
            for hand in sorted_hands:
                p2 += j * hands_bids[hand]
                j += 1
    return p1, p2

print(solve(data))


import time
t1 = time.time()
for _ in range(100):
    solve(data)
t2 = time.time()
print(f"{(t2-t1)/100:.5f} seconds")