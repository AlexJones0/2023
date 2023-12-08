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
data = open("Day 05/data.txt", "r").readlines()

# Problem 1 approach: simulate all seeds, iterating through each map and calculating new mappings each time
seeds = [int(n) for n in data[0][7:].split()]
maps = [mapStr.split("\n")[1:] for mapStr in "".join(data[2:]).split("\n\n")]
maps = [[tuple(int(n) for n in line.split()) for line in mapLines] for mapLines in maps]

values = seeds.copy()
for valMap in maps:
    for i, val in enumerate(values):
        for (destStart, srcStart, rangeLen) in valMap:
            if srcStart <= val < (srcStart + rangeLen):
                values[i] = destStart + val - srcStart
                break
print("Problem 9:", min(values))


# Problem 2 approach: store all value intervals after every mapping. Iterate through the mappings, applying them each order.
# If an interval is entirely mapped within some range, perform the mapping.
# If an interval is split across multiple mapping ranges, map the part of the interval within the range and create a new interval for the remainder
# (to be mapped later on in this mapping iteration).
intervals = list(zip(seeds[0::2], seeds[1::2]))
for valMap in maps:
    for i, (valStart, valRange) in enumerate(intervals):
        for (destStart, srcStart, rangeLen) in valMap:
            srcEnd = srcStart + rangeLen - 1
            if srcStart <= valStart <= srcEnd:
                if (valStart + valRange - 1) <= srcEnd:
                    intervals[i] = (destStart + valStart - srcStart, valRange)
                else:
                    intervals[i] = (destStart + valStart - srcStart, srcEnd - valStart + 1)
                    intervals.append((srcEnd + 1, valRange - srcEnd + valStart - 1))
                break
print("Problem 10:", min(intervals)[0])
