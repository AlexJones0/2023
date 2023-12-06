"""
FILE: Day 06/sol.py
Author: Alex Jones
Desc: Solution to day 6 problems (11 & 12) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = open("Day 06/data.txt", "r").read().split("\n")

# Idea: the distance travelled is (race time - time waited) * speed
# But because we gain 1 speed per second waited, this makes our distance (time - speed) * speed = time * speed - speed^2
# This is a second order polynomial with a negative x^2 coeffcient - thus we can find all values where distance > record
# by examining the roots of the polynomial: -speed^2 + time * speed - record.
# We simply solve using the quadratic formula (simplifying, as a=-1 always), and find the number of discrete speeds/times
# in that closed range by calculating floor(upper root) - ceil(lower root) + 1.  

from math import prod, sqrt, floor, ceil

def getWays(time, record):
    det = sqrt(time * time - 4 * record)
    return floor((time + det) / 2) - ceil((time - det) / 2) + 1

times = [int(n) for n in data[0].split(":")[1].split()]
records = [int(n) for n in data[1].split(":")[1].split()]
print("Problem 11:", prod([getWays(time, record) for time, record in zip(times, records)]))

time = int(data[0].split(":")[1].replace(" ",""))
record = int(data[1].split(":")[1].replace(" ",""))
print("Problem 12:", getWays(time, record))
