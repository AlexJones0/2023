"""
FILE: Day 07/sol.py
Author: Alex Jones
Desc: Solution to day 7 problems (13 & 14) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = open("Day 07/data.txt", "r").read().strip().split("\n")

from functools import cmp_to_key
from collections import Counter

def get_type(counter):
    if len(counter) == 1:
        return 6
    elif len(counter) == 2 and 1 in counter.values():
        return 5
    elif len(counter) == 2 and 2 in counter.values():
        return 4
    elif len(counter) == 3 and 3 in counter.values():
        return 3
    elif len(counter) == 3 and len([x for x in counter.values() if x == 2]) == 2:
        return 2
    elif len(counter) == 4:
        return 1
    return 0

def get_card_value(card):
    if card in [str(i) for i in range(2,10)]:
        return int(card)
    elif card == "T":
        return 10
    elif card == "J":
        return 11
    elif card == "Q":
        return 12
    elif card == "K":
        return 13
    elif card == "A":
        return 14

def compare(item1, item2):
    hand1 = item1.split()[0]
    hand2 = item2.split()[0]
    h1counts = Counter(hand1)
    h2counts = Counter(hand2)
    h1type = get_type(h1counts)
    h2type = get_type(h2counts)
    if h1type != h2type:
        return 1 if h1type > h2type else -1
    for card1, card2 in zip(hand1, hand2):
        if card1 == card2:
            continue
        return 1 if get_card_value(card1) > get_card_value(card2) else -1
    return 0

hands = sorted(data, key=cmp_to_key(compare))

print("Problem 13:", sum([rank * int(hand.split()[1]) for rank, hand in list(enumerate([0] + hands))[1:]]))

def get_type2(counter):
    counterVals = {c: v for c, v in counter.items() if v != 0}
    if len(counterVals) == 1:
        cardval = 6
    elif len(counterVals) == 2 and 1 in counterVals.values():
        cardval = 5
    elif len(counterVals) == 2 and 2 in counterVals.values():
        cardval = 4
    elif len(counterVals) == 3 and 3 in counterVals.values():
        cardval = 3
    elif len(counterVals) == 3 and len([x for x in counterVals.values() if x == 2]) == 2:
        cardval = 2
    elif len(counterVals) == 4:
        cardval = 1
    else:
        cardval =  0
    if counter["J"] == 0:
        return cardval
    maxval = cardval
    counter["J"] -= 1
    for card in counter:
        if card == "J":
            continue
        counter[card] += 1
        maxval = max(maxval, get_type2(counter))
        counter[card] -= 1
    counter["J"] += 1
    return maxval

def get_card_value2(card):
    if card in [str(i) for i in range(2,10)]:
        return int(card)
    elif card == "T":
        return 10
    elif card == "J":
        return 1
    elif card == "Q":
        return 12
    elif card == "K":
        return 13
    elif card == "A":
        return 14

def compare2(item1, item2):
    hand1 = item1.split()[0]
    hand2 = item2.split()[0]
    h1counts = Counter(hand1)
    h2counts = Counter(hand2)
    h1type = get_type2(h1counts)
    h2type = get_type2(h2counts)
    if h1type != h2type:
        return 1 if h1type > h2type else -1
    for card1, card2 in zip(hand1, hand2):
        if card1 == card2:
            continue
        return 1 if get_card_value2(card1) > get_card_value2(card2) else -1
    return 0

hands = sorted(data, key=cmp_to_key(compare2))

print("Problem 14:", sum([rank * int(hand.split()[1]) for rank, hand in list(enumerate([0] + hands))[1:]]))
