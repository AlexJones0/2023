"""
FILE: Day 13/sol.py
Author: Alex Jones
Desc: Solution to day 13 problems (25 & 26) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = [lines.splitlines() for lines in open("Day 13/data.txt", "r").read().strip().split("\n\n")]

def findReflection(pattern: list[list[str]], diffs: int) -> int:
    for i in range(len(pattern)-1):
        left, right = i, i+1
        diffsFound = 0
        while 0 <= left and right < len(pattern):
            diffsFound += sum([a != b for a, b in zip(pattern[left], pattern[right])])
            left, right = left - 1, right + 1
        if diffsFound == diffs:
            return i+1
    return -1

def findPatternReflection(pattern: list[list[str]], diffs: int) -> int:
    res = findReflection(pattern, diffs)
    return res * 100 if res != -1 else findReflection(list(zip(*pattern)), diffs)

print("Problem 25:", sum(findPatternReflection(pattern, diffs=0) for pattern in data))
print("Problem 26:", sum(findPatternReflection(pattern, diffs=1) for pattern in data))
