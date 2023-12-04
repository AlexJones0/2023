"""
FILE: Day 04/sol.py
Author: Alex Jones
Desc: Solution to day 4 problems (7 & 8) for Advent of Code 2023, solved in Python 3.
Rank: 252/110
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = [x.strip() for x in open("Day 04/data.txt", "r").read().split("\n") if len(x.strip()) > 0]


# Problem 7 approach: parse line into a set of winning numbers and our numbers, perform set intersection,
# and get scores by summing 2 to the power of the size of the intersection minus 1 (unless it is 0).

def parseNumbers(numberStr: str) -> set[str]:
    return set([n.strip() for n in numberStr.strip().split(" ") if n != ""])

data = [line.split(":")[1].split("|") for line in data]
matches = [len(parseNumbers(line[0]).intersection(parseNumbers(line[1]))) for line in data]

print("Problem 7:", sum(2 ** (n-1) if n > 0 else 0 for n in matches))


# Problem 8 approach: using the prev calculated num of matches, construct a list of the number of each
# card by traversing the list in order, and sum the resulting list at the end. We could optimise to O(1) 
# space using the fact that there is only ever <= 10 winning numbers, but this is not a problem here and 
# we are trying to make a general solution, so we don't bother.

numOfCards = [1 for _ in range(len(data))]
for i, card in enumerate(matches):
    maxFollowIndex = min(len(matches),i+1+matches[i])
    for j in range(i+1, maxFollowIndex):
        numOfCards[j] += numOfCards[i]

print("Problem 8:", sum(numOfCards))
