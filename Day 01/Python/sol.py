"""
FILE: Day 01/sol.py
Author: Alex Jones
Desc: Solution to day 1 problems (1 & 2) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = [x for x in open("Day 01/data.txt", "r").read().split("\n")]


digits = [[c for c in line if c.isdigit()] for line in data]
print("Problem 1:", sum([int(digitList[0] + digitList[-1]) for digitList in digits if len(digitList) > 0]))


words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
digitIndexes = [{i: c for i, c in enumerate(line) if c.isdigit()} for line in data]
for i, line in enumerate(data):
    line = line.lower()
    for n, word in enumerate(words):
        digitPos = 0
        while digitPos != -1:
            digitPos = line.find(word, digitPos)
            if digitPos != -1:
                digitIndexes[i][digitPos] = str(n + 1)
                digitPos += 1
firstDigit = [lineDict[min(lineDict.keys())] for lineDict in digitIndexes if len(lineDict) > 0]
lastDigit = [lineDict[max(lineDict.keys())] for lineDict in digitIndexes if len(lineDict) > 0]
print("Problem 2:", sum([int(f + l) for f, l in zip(firstDigit, lastDigit)]))
