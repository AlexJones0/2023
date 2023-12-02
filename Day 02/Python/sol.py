"""
FILE: Day 02/sol.py
Author: Alex Jones
Desc: Solution to day 2 problems (3 & 4) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = [x.strip() for x in open("Day 02/data.txt", "r").read().split("\n") if len(x.strip()) > 0]


# For part 1 we assume that cubes of the same c olour do not appear in the same reveal (in the same game); this assumption holds
# for the input data, but if it was not true, we would need to track local amounts per reveal and update the max based on this.

# For part 2 we assume that only red, green and blue cubes are included in each game; which holds for the given data set.


from math import prod
from collections import defaultdict


def getGameId(line: str) -> int:
    return int(line.split(":")[0].split(" ")[-1])


def getGameData(line: str) -> defaultdict[str,int]:
    gameData = defaultdict(int)
    for reveal in line.split(":")[1].split(";"):
        for cubeStr in reveal.split(", "):
            (amount, colour) = cubeStr.strip().split(" ")
            gameData[colour] = max(gameData[colour], int(amount))
    return gameData


def isGamePossible(gameData: defaultdict[str,int], targets: dict[str,int]) -> bool:
    return all(gameData[colour] <= amount for colour, amount in targets.items())


def getGamePower(line: str) -> int:
    return prod(getGameData(line).values())


targetCubeAmounts = {"blue": 14, "red": 12, "green": 13}
print("Problem 3:", sum(getGameId(line) for line in data if isGamePossible(getGameData(line), targetCubeAmounts)))

print("Problem 4:", sum(getGamePower(line) for line in data))
