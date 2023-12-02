"""
FILE: Day 02/sol.py
Author: Alex Jones
Desc: Solution to day 2 problems (3 & 4) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = [x.strip() for x in open("Day 02/data.txt", "r").read().split("\n") if len(x.strip()) > 0]

from functools import reduce


targetCubeAmounts = {
    "blue": 14,
    "red": 12,
    "green": 13
}


def getGameId(line: str) -> int:
    return int(line.split(":")[0].split(" ")[-1])


def getGameData(line: str) -> dict[str,int]:
    gameData = dict()
    for reveal in line.split(":")[1].split(";"):
        # Assume cubes of the same colour do not appear in the same reveal; this assumption holds for the input data
        # but if not true, we would need to track local amounts per reveal and update the max based on this.
        for cubeStr in reveal.split(", "):
            cubeStr = cubeStr.strip()
            if len(cubeStr) == 0:
                continue
            cubeInfo = cubeStr.split(" ")
            amount = int(cubeInfo[0])
            colour = cubeInfo[1].lower()
            prevAmount = gameData[colour] if colour in gameData else -1
            gameData[colour] = max(prevAmount, amount)
    return gameData


def isGamePossible(gameData: dict[str,int], targets: dict[str,int]) -> bool:
    for colour, amount in gameData.items():
        if colour not in targets or targets[colour] < amount:
            return False
    return True


print("Problem 3:", sum([getGameId(line) for line in data if isGamePossible(getGameData(line), targetCubeAmounts)]))

# For this we make an assumption that only red green and blue cubes are incldued in the set; this holds for the data
print("Problem 4:", sum([reduce(lambda x,y: (x*y), getGameData(line).values(), 1) for line in data]))
