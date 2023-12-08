"""
FILE: Day 01/sol.py
Author: Alex Jones
Desc: Solution to day 1 problems (1 & 2) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = [x for x in open("Day 01/data.txt", "r").read().split("\n")]

def solve(data: list[str]):
    # Find all digits, take the first and last, and work out the calibration values
    digits = [[c for c in line if c.isdigit()] for line in data]
    return sum([int(digitList[0] + digitList[-1]) for digitList in digits])

print("Problem 1:", solve(data))

# Replace all words with numberic occurrences (like one1one to consider overlap) and repeat
for i in range(len(data)):
    for n, word in enumerate(["one","two","three","four","five","six","seven","eight","nine"]):
        data[i] = data[i].replace(word, f"{word}{n+1}{word}")
print("Problem 2:", solve(data))
