"""
FILE: Day 13/sol.py
Author: Alex Jones
Desc: Solution to day 13 problems (25 & 26) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = [lines.splitlines() for lines in open("Day 13/data.txt", "r").read().strip().split("\n\n")]

from typing import Callable

def findReflection(pattern: list[list[str]], limit: int, diffs: int, value: int, 
                   rowFunc: Callable[[list[str,str],int], list[str]]) -> int:
    for i in range(limit):
        left, right = i, i+1
        diffsFound = 0
        while 0 <= left and right <= limit:
            diffsFound += len([1 for a, b in zip(rowFunc(pattern, left), rowFunc(pattern, right)) if a != b])
            left, right = left - 1, right + 1
        if diffsFound == diffs:
            return value * (i+1)
    return -1

def findPatternReflection(pattern: list[list[str]], diffs: int = 0) -> int:
    res = findReflection(pattern, len(pattern)-1, diffs, 100, lambda xss, i: xss[i])
    columnFunc = lambda xss, i: [xs[i] for xs in xss]
    return res if res != -1 else findReflection(pattern, len(pattern[0])-1, diffs, 1, columnFunc)

print("Problem 25:", sum(findPatternReflection(pattern) for pattern in data))
print("Problem 26:", sum(findPatternReflection(pattern, diffs=1) for pattern in data))
