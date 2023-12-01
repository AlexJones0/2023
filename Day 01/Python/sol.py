"""
FILE: Day 01/sol.py
Author: Alex Jones
Desc: Solution to day 1 problems (1 & 2) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = [x for x in open("Day 01/data.txt", "r").read().split("\n")]

# Find all digits, take the first and last, and work out the calibration values
digits = [[c for c in line if c.isdigit()] for line in data]
print("Problem 1:", sum([int(digitList[0] + digitList[-1]) for digitList in digits]))


digitIndexes = [{i: int(c) for i, c in enumerate(line) if c.isdigit()} for line in data]

# In addition to the above, we now store the indexes of our digits to allow easy comparison
# and search for occurrences of all words in each line, marking these accordingly
words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for i, line in enumerate(data):
    line = line.lower()
    for valuePos, word in enumerate(words):
        digitPos = 0
        while digitPos != -1:
            digitPos = line.find(word, digitPos)
            if digitPos != -1:
                digitIndexes[i][digitPos] = valuePos + 1
                digitPos += 1
# Again we combine the first and last digits to get calibration values, this time searching by min/max index
calibrationValues = [lineDict[min(lineDict.keys())] * 10 + lineDict[max(lineDict.keys())] for lineDict in digitIndexes]
print("Problem 2:", sum(calibrationValues))
