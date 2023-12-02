"""
FILE: Day 02/sol.py
Author: Alex Jones
Desc: Solution to day 2 problems (3 & 4) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = [x.strip() for x in open("Day 02/data.txt", "r").read().split("\n") if len(x.strip()) > 0]


CUBE_NUMS = {
    "blue": 14,
    "red": 12,
    "green": 13
}

possible = []
gameInfo = {}
for line in data:
    line = line.split(":")
    gameId = int(line[0].split(" ")[-1])
    gameInfo[gameId] = {}
    reveals = line[1].split(";")
    for reveal in reveals:
        cubes = reveal.split(", ")
        for cube in cubes:
            if len(cube.strip()) == 0:
                continue
            cube = cube.strip().split(" ")
            num = int(cube[0])
            colour = cube[1].lower().strip()
            if colour in gameInfo[gameId]:
                gameInfo[gameId][colour] = max(gameInfo[gameId][colour], num)
            else:
                gameInfo[gameId][colour] = num
    isPossible = True
    for colour, amount in gameInfo[gameId].items():
        if colour not in CUBE_NUMS or CUBE_NUMS[colour] < amount:
            isPossible = False
            break
    if isPossible:
        possible.append(gameId)

print("Problem 3:", sum(possible))

cumulativePower = 0
for gameId in gameInfo.keys():
    power = 1
    for amount in gameInfo[gameId].values():
        power *= amount
    cumulativePower += power

print("Problem 4:", cumulativePower)
