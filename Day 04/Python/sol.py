"""
FILE: Day 04/sol.py
Author: Alex Jones
Desc: Solution to day 4 problems (7 & 8) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = [x.strip() for x in open("Day 04/data.txt", "r").read().split("\n") if len(x.strip()) > 0]

total = 0
for line in data:
    line = line.split(":")[1].split("|")
    winning = [int(n.strip()) for n in line[0].strip().split(" ") if len(n.strip()) > 0]
    yours = [int(n.strip()) for n in line[1].strip().split(" ") if len(n.strip()) > 0]
    intersect = set(winning).intersection(set(yours))
    if len(intersect) > 0:
        total += 2 ** (len(intersect) - 1)

print("Problem 7:", total)

total = 0
amount = []
for line in data:
    number_of_cards = 1
    if len(amount) > 0:
        number_of_cards += amount[0]
        amount = amount[1:]
    total += number_of_cards
    line = line.split(":")[1].split("|")
    winning = [int(n.strip()) for n in line[0].strip().split(" ") if len(n.strip()) > 0]
    yours = [int(n.strip()) for n in line[1].strip().split(" ") if len(n.strip()) > 0]
    intersect = set(winning).intersection(set(yours))
    for i in range(len(intersect)):
        if i < len(amount):
            amount[i] += number_of_cards
        else:
            amount.append(number_of_cards)


print("Problem 8:", total)
