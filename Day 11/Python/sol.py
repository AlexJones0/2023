"""
FILE: Day 11/sol.py
Author: Alex Jones
Desc: Solution to day 11 problems (21 & 22) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = open("Day 11/data.txt", "r").read().strip().split("\n")

from collections import defaultdict

def cosmicExpand(locs: list[str], scaleFactor: int) -> list[str]:
    copy = locs.copy()
    xVals, yVals = defaultdict(list), defaultdict(list)
    for i, (x, y) in enumerate(locs):
        xVals[x].append(i)
        yVals[y].append(i)
    xOffset, yOffset = 0, 0
    for x in range(min(xVals)+1, max(xVals)+1):
        if x not in xVals:
            xOffset += scaleFactor - 1
        for index in xVals[x]:
            copy[index] = (copy[index][0] + xOffset, copy[index][1])
    for y in range(min(yVals)+1, max(yVals)+1):
        if y not in yVals:
            yOffset += scaleFactor - 1
        for index in yVals[y]:
            copy[index] = (copy[index][0], copy[index][1] + yOffset)
    return copy

def findSumPairDists(locs: list[int]) -> int:
    return sum(abs(x1-x2)+abs(y1-y2) for i, (x1, y1) in enumerate(locs) for (x2, y2) in locs[(i+1):])

galaxies = [(i,j) for i, row in enumerate(data) for j, char in enumerate(row) if char == "#"]
print("Problem 21:", findSumPairDists(cosmicExpand(galaxies, 2)))
print("Problem 22:", findSumPairDists(cosmicExpand(galaxies, 1000000)))
