"""
FILE: Day 12/sol.py
Author: Alex Jones
Desc: Solution to day 12 problems (23 & 24) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = [line.split() for line in open("Day 12/data.txt", "r").read().strip().split("\n")]

from functools import cache

@cache
def findNumArrangements(row: str, damages: tuple[int], mustBeDamaged: bool = False) -> int:
    cannotBeDamaged = damages and damages[-1] == 0
    if cannotBeDamaged:
        damages = damages[:-1]
        mustBeDamaged = False
    cannotBeDamaged = cannotBeDamaged or len(damages) == 0
    if len(row) == 0:
        return len(damages) == 0
    elif row.endswith("#") or row.endswith("?") and mustBeDamaged:
        if cannotBeDamaged:
            return 0
        newDamages = tuple(d if (i+1) != len(damages) else (d-1) for i, d in enumerate(damages))
        return findNumArrangements(row[:-1], newDamages, True)
    elif row.endswith(".") or cannotBeDamaged:
        return 0 if mustBeDamaged else findNumArrangements(row[:-1], damages)
    newDamages = tuple(d if (i+1) != len(damages) else (d-1) for i, d in enumerate(damages))
    return findNumArrangements(row[:-1], damages) + findNumArrangements(row[:-1], newDamages, True)

def unfold(row: str, damages: tuple[int], n: int) -> tuple[str,tuple[int]]:
    return ("?".join([row] * n), tuple(sum([list(damages)] * n, [])))

data = [(row, tuple(int(n) for n in damages.split(","))) for row, damages in data]
print("Problem 23:", sum(findNumArrangements(*info) for info in data))
print("Problem 24:", sum(findNumArrangements(*unfold(*info, 5)) for info in data))
