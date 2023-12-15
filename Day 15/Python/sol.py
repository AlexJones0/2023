"""
FILE: Day 15/sol.py
Author: Alex Jones
Desc: Solution to day 15 problems (29 & 30) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = open("Day 15/data.txt", "r").read().strip().split(",")

from functools import reduce

hash_ = lambda string: reduce(lambda val, char: (val + ord(char)) * 17 % 256, string, 0)
print("Problem 29:", sum(hash_(s) for s in data))

map_ = [[] for _ in range(256)]
for s in data:
    isAdd, (label, focus) = "=" in s, s.replace("-","=").split("=")
    box = hash_(label)
    if isAdd and any(lbl == label for (lbl, _) in map_[box]):
        map_[box] = [v if v[0] != label else (v[0], int(focus)) for v in map_[box]]
    elif isAdd:
        map_[box].append((label, int(focus)))
    else:
        map_[box] = [v for v in map_[box] if v[0] != label]
print("Problem 30:", sum(sum((box+1) * slot * focus for slot, (_, focus) in enumerate(xs,start=1)) for box, xs in enumerate(map_)))
