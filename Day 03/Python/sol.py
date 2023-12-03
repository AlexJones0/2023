"""
FILE: Day 03/sol.py
Author: Alex Jones
Desc: Solution to day 3 problems (5 & 6) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = [x.strip() for x in open("Day 03/data.txt", "r").read().split("\n") if len(x.strip()) > 0]


# Problem 5 approach - iterate through data to find numbers, marking each number adjacent by checking neighbour
# cells for symbols while parsing. When finished parsing the number, record if next to some symbol. Sum these.

neighbours = lambda posY, posX: [(posY+y,posX+x) for x in [-1,0,1] for y in [-1,0,1] if x != y or x != 0]
inBounds = lambda posY, posX: 0 <= posY < len(data) and 0 <= posX < len(data[posY])
isSymbol = lambda posY, posX: not data[posY][posX].isdigit() and data[posY][posX] != "."

total = 0
for i, line in enumerate(data):
    num = ""
    isAdjacent = False
    for j, char in enumerate(line):
        if char.isdigit():
            num += char
            for pos in neighbours(i, j):
                if inBounds(*pos) and isSymbol(*pos):
                    isAdjacent = True
        elif num != "":
            if isAdjacent:
                total += int(num)
            num = ""
            isAdjacent = False
    if isAdjacent and num != "":
        total += int(num)
print("Problem 5:", total)


# Problem 6 approach - maintain a dict of gears, acting as a set of positions at first. Iterate through data to find
# numbers, and for each number parsed maintain a set of all gears the number is adjacent to by checking neighbours
# again. When finished parsing the number, record the number as next to each gear. Sum the gear ratio of all gears with
# exactly two adjacent numbers, no more and no less.

maybeGearNumbers = {
    (i, j): [] for i, line in enumerate(data) for j, char in enumerate(line) if char == "*"
}

for i, line in enumerate(data):
    num = ""
    adjacentGears = set()
    for j, char in enumerate(line):
        if char.isdigit():
            num += char
            for pos in neighbours(i, j):
                if pos in maybeGearNumbers:
                    adjacentGears.add(pos)
        elif num != "":
            for gear in adjacentGears:
                maybeGearNumbers[gear].append(num)
            adjacentGears = set()
            num = ""
    if num != "":
        for gear in adjacentGears:
            maybeGearNumbers[gear].append(num)

print("Problem 6:", sum(int(ns[0]) * int(ns[1]) for ns in maybeGearNumbers.values() if len(ns) == 2))
