"""
FILE: Day 21/sol.py
Author: Alex Jones
Desc: Solution to day 21 problems (41 & 42) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = open("Day 21/data.txt", "r").read().strip().splitlines()
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ngbs4 = lambda x, y: [(x+i, y+j) for i, j in DIRS]

from functools import cache

@cache
def reachedInSteps(start: tuple[int,int], steps:int, cycle=False) -> set[tuple[int,int]]:
    if steps <= 0:
        return set([start])
    result = set()
    for pos in reachedInSteps(start, steps-1, cycle):
        for (r, c) in ngbs4(*pos):
            if not cycle and 0 <= r < len(data) and 0 <= c < len(data[0]) and data[r][c] != "#":
                result.add((r, c))
            elif cycle and data[r%len(data)][c%len(data[0])] != "#":
                result.add((r, c))
    return result

start = [(i, j) for i, row in enumerate(data) for j, char in enumerate(row) if char == "S"][0]
print("Problem 41:", len(reachedInSteps(start, 64)))

def reachedInStepsInfinite(start: tuple[int,int], steps:int) -> int:
    rows, n = len(data), steps // len(data)
    f1 = len(reachedInSteps(start, rows // 2, cycle=True))
    f2 = len(reachedInSteps(start, rows + rows // 2, cycle=True))
    f3 = len(reachedInSteps(start, 2*rows + rows // 2, cycle=True))
    diff1, diff2 = f2-f1, f3-f2
    secondDiff = diff2 - diff1
    return (n * (n - 1) // 2) * secondDiff + n * diff1 + f1 

print("Problem 42:", reachedInStepsInfinite(start, 26501365))
