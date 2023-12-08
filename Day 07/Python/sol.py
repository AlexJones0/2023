"""
FILE: Day 07/sol.py
Author: Alex Jones
Desc: Solution to day 7 problems (13 & 14) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = [x.split() for x in open("Day 07/data.txt", "r").read().strip().split("\n")]

from functools import cmp_to_key, partial
from collections import Counter

getValue      = lambda card: "23456789TJQKA".index(card)
getJokerValue = lambda card: "J23456789TQKA".index(card)
id_           = lambda hand: hand

def getHandType(hand: str) -> int:
    # Given a hand (e.g. 23JJK), determine the "type" of the hand, where stronger types are assigned higher numbers.
    cardCounts = Counter(hand).values()
    return max(cardCounts) - len(cardCounts)

def compare(item1: list[str], item2: list[str], valueFunc=getValue, processFunc=id_) -> int:
    # Compare two hand strings (including hands and bids, e.g. "3958K 683") based on appropriate hand ordering rules.
    hand1, hand2 = item1[0], item2[0]
    hand1Type, hand2Type = getHandType(processFunc(hand1)), getHandType(processFunc(hand2))
    if hand1Type != hand2Type:
        return 1 if hand1Type > hand2Type else -1
    for card1, card2 in zip(hand1, hand2):
        if card1 == card2:
            continue
        return 1 if valueFunc(card1) > valueFunc(card2) else -1
    return 0

hands = sorted(data, key=cmp_to_key(compare))
print("Problem 13:", sum(rank * int(bid[1]) for rank, bid in enumerate(hands, start=1)))

def bestHand(hand: str) -> str:
    # Given a hand (e.g. 23JJK), determine (one of) the strongest possible hand(s) that could be made by substituting jokers.
    if all(c == "J" for c in hand):
        return hand
    counts = Counter(hand)
    return hand.replace("J", max(counts.keys(), key=lambda k: counts[k] if k != "J" else -1))

hands = sorted(data, key=cmp_to_key(partial(compare, valueFunc=getJokerValue, processFunc=bestHand)))
print("Problem 14:", sum(rank * int(bid[1]) for rank, bid in enumerate(hands, start=1)))
