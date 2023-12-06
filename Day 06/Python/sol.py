"""
FILE: Day 05/sol.py
Author: Alex Jones
Desc: Solution to day 5 problems (9 & 10) for Advent of Code 2023, solved in Python 3.
Rank: 463/77
Comments: I ran into so many issues on part 1 because of a bug in my boilerplate that I stopped trying for speed (as is evident in my part 1 rank),
  but unexpectedly after realising a brute force wouldn't work for part 2 I managed to code up the relevant interval tracking solution very quickly
  with no bugs and put myself on the leaderboard for the first time. I'm guessing most people found either the algorithm or the small details
  of implementing part 2 difficult.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = open("Day 06/data.txt", "r").read().split("\n")

from math import prod, sqrt, floor, ceil

times = [int(n) for n in data[0].split(":")[1].split()]
distances = [int(n) for n in data[1].split(":")[1].split()]

raceWays = []
for time, record in zip(times, distances):
    ways = 0
    for speed in range(1, time):
        distance = (time - speed) * speed
        if distance > record:
            ways += 1
    raceWays.append(ways)

print("Problem 11:", prod(raceWays))

time = int(data[0].split(":")[1].replace(" ",""))
record = int(data[1].split(":")[1].replace(" ",""))

a = -1
b = time
c = -record
determinant = sqrt(b * b - 4 * a * c)
roots = [(-b - determinant) / (2 * a), (-b + determinant) / (2 * a)]
maxDist = floor(min(time, max(roots)))
minDist = ceil(max(min(roots), 1))

print("Problem 12:", maxDist - minDist + 1)
