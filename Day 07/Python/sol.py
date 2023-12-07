"""
FILE: Day 07/sol.py
Author: Alex Jones
Desc: Solution to day 7 problems (13 & 14) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = open("Day 07/data.txt", "r").read().strip().split("\n")

from functools import cmp_to_key
from collections import Counter

def getHandType(hand: str) -> int:
    # Given a hand (e.g. 23JJK), determine the "type" of the hand, where stronger types are assigned higher numbers.
    cardCounts = tuple(sorted(Counter(hand).values()))
    typeValue = {
        (5,): 6,
        (1, 4): 5,
        (2, 3): 4,
        (1, 1, 3): 3,
        (1, 2, 2): 2,
        (1, 1, 1, 2): 1,
        (1, 1, 1, 1, 1): 0
    }
    return typeValue[cardCounts]

def getCardValue(card: str) -> int:
    # Given a card (e.g. "Q"), determine the "value" of the card, where stronger cards are assigned higher numbers.
    return {c: i for i, c in enumerate("23456789TJQKA")}[card]

def compare(item1: str, item2: str) -> int:
    # Compare two hand strings (including hands and bids, e.g. "3958K 683") based on appropriate hand ordering rules.
    hand1, hand2 = item1.split()[0], item2.split()[0]
    hand1Type, hand2Type = getHandType(hand1), getHandType(hand2)
    if hand1Type != hand2Type:
        return 1 if hand1Type > hand2Type else -1
    for card1, card2 in zip(hand1, hand2):
        if card1 == card2:
            continue
        return 1 if getCardValue(card1) > getCardValue(card2) else -1
    return 0

hands = sorted(data, key=cmp_to_key(compare))
print("Problem 13:", sum([rank * int(handBid.split()[1]) for rank, handBid in enumerate(hands, start=1)]))

def getCardValueWithJoker(card: str) -> int:
    # Get the card value where "J" is now a joker with the weakest value.
    return {c: i for i, c in enumerate("J23456789TQKA")}[card]

def bestJokerHand(hand: str) -> str:
    # Given a hand (e.g. 23JJK), determine (one of) the strongest possible hand(s) that could be made by substituting jokers.
    if all(c == "J" for c in hand):
        return hand
    cardCounts = Counter(hand)
    return hand.replace("J", max(cardCounts.keys(), key=lambda k: cardCounts[k] if k != "J" else -1))

def compareWithJoker(item1: str, item2: str) -> int:
    # Compare two hand strings (including hand and bids, e.g. "3958K 683") based on hand ordering rules, accounting for jokers.
    hand1, hand2 = item1.split()[0], item2.split()[0]
    hand1Type, hand2Type = getHandType(bestJokerHand(hand1)), getHandType(bestJokerHand(hand2))
    if hand1Type != hand2Type:
        return 1 if hand1Type > hand2Type else -1
    for card1, card2 in zip(hand1, hand2):
        if card1 == card2:
            continue
        return 1 if getCardValueWithJoker(card1) > getCardValueWithJoker(card2) else -1
    return 0

hands = sorted(data, key=cmp_to_key(compareWithJoker))
print("Problem 14:", sum([rank * int(handBid.split()[1]) for rank, handBid in enumerate(hands, start=1)]))
