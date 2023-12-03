"""
FILE: Day 03/sol.py
Author: Alex Jones
Desc: Solution to day 3 problems (5 & 6) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = [x.strip() for x in open("Day 03/data.txt", "r").read().split("\n") if len(x.strip()) > 0]

symbols = set([
    (i, j) for i, line in enumerate(data) for j, char in enumerate(line) if not (char.isdigit() or char == ".")
])

neighbours = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

total = 0
for i, line in enumerate(data):
    num = 0
    isAdjacent = False
    for j, char in enumerate(line):
        if char.isdigit():
            num = num * 10 + int(char)
            if not isAdjacent:
                for posI, posJ in neighbours:
                    if (i + posI, j + posJ) in symbols:
                        isAdjacent = True
                        break
        else:
            if isAdjacent and num != 0:
                total += num
            num = 0
            isAdjacent = False
    if isAdjacent and num != 0:
        total += num
print("Problem 5:", total)

gears = {
    (i, j): [] for i, line in enumerate(data) for j, char in enumerate(line) if char == "*"
}

for i, line in enumerate(data):
    num = 0
    adjacentGears = set()
    for j, char in enumerate(line):
        if char.isdigit():
            num = num * 10 + int(char)
            for posI, posJ in neighbours:
                pos = (i + posI, j + posJ)
                if pos in gears:
                    adjacentGears.add(pos)
                    break
        else:
            if num != 0:
                for gear in adjacentGears:
                    gears[gear].append(num)
                adjacentGears = set()
            num = 0
    if num != 0:
        for gear in adjacentGears:
            gears[gear].append(num)
            

total = 0
for gear, nums in gears.items():
    if len(nums) != 2:
        continue
    total += nums[0] * nums[1]
print("Problem 6:", total)
