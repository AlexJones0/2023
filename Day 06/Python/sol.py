"""
FILE: Day 06/sol.py
Author: Alex Jones
Desc: Solution to day 6 problems (11 & 12) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = [x.split(":")[1] for x in open("Day 06/data.txt", "r").readlines()]

# Idea: the distance travelled is (race time - time waited) * speed
# But because we gain 1 speed per second waited, this makes our distance (time - speed) * speed = time * speed - speed^2
# This is a second order polynomial with a negative x^2 coeffcient - thus we can find all values where distance > record
# by examining the roots of the polynomial: -speed^2 + time * speed - record.
# We simply solve using the quadratic formula (simplifying, as a=-1 always), and find the number of discrete speeds/times
# in that closed range by calculating floor(upper root) - ceil(lower root) + 1.  

from math import prod, sqrt, floor, ceil

def getWays(time: int, record: int):
    det = sqrt(time ** 2 - 4 * record)
    return floor((time + det) / 2) - ceil((time - det) / 2) + 1

races = [[int(n) for n in line.split()] for line in data]
print("Problem 11:", prod([getWays(*race) for race in zip(*races)]))

print("Problem 12:", getWays(*[int(line.replace(" ","")) for line in data]))
