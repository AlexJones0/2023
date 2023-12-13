"""
FILE: Day 13/sol.py
Author: Alex Jones
Desc: Solution to day 13 problems (25 & 26) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = open("Day 13/data.txt", "r").read().strip()

from typing import Callable
patterns = [[[c for c in line] for line in pattern.splitlines()] for pattern in data.split("\n\n")]

def findReflection(pattern: list[list[str]], limit: int, ignore: int, value: int, 
                      rowFunc: Callable[[list[str,str],int], list[str]]) -> int:
    for i in range(limit):
        left, right = i, i+1
        while 0 <= left and right <= limit and rowFunc(pattern, left) == rowFunc(pattern, right):
            left, right = left - 1, right + 1
        if (left < 0 or right > limit) and (value * (i+1)) != ignore:
            return value * (i+1)
    return -1

def findPatternReflection(pattern: list[list[str]], ignore: int = -1) -> int:
    res = findReflection(pattern, len(pattern)-1, ignore, 100, lambda xss, i: xss[i])
    if res != -1:
        return res
    return findReflection(pattern, len(pattern[0])-1, ignore, 1, lambda xss, i: [xs[i] for xs in xss])

reflections = [findPatternReflection(pattern) for pattern in patterns]
print("Problem 25:", sum(reflections))

def findSmudgedReflection(pattern: list[list[str]], ignore: int) -> int:
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            pattern[i][j] = "#" if pattern[i][j] == "." else "."
            reflection = findPatternReflection(pattern, ignore)
            pattern[i][j] = "#" if pattern[i][j] == "." else "."
            if reflection != -1:
                return reflection

print("Problem 26:", sum(findSmudgedReflection(*pattern) for pattern in zip(patterns, reflections)))
