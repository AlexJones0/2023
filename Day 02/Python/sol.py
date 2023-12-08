"""
FILE: Day 02/sol.py
Author: Alex Jones
Desc: Solution to day 2 problems (3 & 4) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = [x.split(":") for x in open("Day 02/data.txt", "r").read().strip().split("\n")]

# For part 1 we assume that cubes of the same c olour do not appear in the same reveal (in the same game); this assumption holds
# for the input data, but if it was not true, we would need to track local amounts per reveal and update the max based on this.

from math import prod
from collections import defaultdict

def getGame(line: str) -> defaultdict[str,int]:
    gameData = defaultdict(int)
    for reveal in line.replace(";",",").split(","):
        (amount, colour) = reveal.split()
        gameData[colour] = max(gameData[colour], int(amount))
    return gameData

def isPossible(gameData: defaultdict[str,int], targets: dict[str,int]) -> bool:
    return all(gameData[colour] <= amount for colour, amount in targets.items())

targets = {"blue": 14, "red": 12, "green": 13}
print("Problem 3:", sum(int(id_.split()[-1]) for id_, line in data if isPossible(getGame(line), targets)))

# For part 2 we assume that only red, green and blue cubes are included in each game; which holds for the given data set.
print("Problem 4:", sum(prod(getGame(line).values()) for _, line in data))
