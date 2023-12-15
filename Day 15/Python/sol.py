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

map_ = [{} for _ in range(256)]  # As of 3.6, Python dicts maintain insertion ordering by default! 
for s in data:
    (label, focus) = s.replace("-","=").split("=")
    if "=" in s:
        map_[hash_(label)][label] = int(focus)
    else:
        map_[hash_(label)].pop(label, None)
print("Problem 30:", sum(box*slot*focus for box, xs in enumerate(map_,1) for slot, focus in enumerate(xs.values(),1)))