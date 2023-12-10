"""
FILE: Day 10/sol.py
Author: Alex Jones
Desc: Solution to day 10 problems (19 & 20) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = open("Day 10/data.txt", "r").read().strip().split("\n")

def getDirs(char: str) -> list[tuple[int,int]]:
    match char:
        case "S": return [(1, 0),  (-1, 0), (0, 1), (0, -1)]
        case "|": return [(1, 0),  (-1, 0)]
        case "-": return [(0, 1),  (0, -1)]
        case "L": return [(-1, 0), (0, 1) ]
        case "J": return [(-1, 0), (0, -1)]
        case "7": return [(1, 0),  (0, -1)]
        case "F": return [(1, 0),  (0, 1) ]
        case ".": return []

start = [(i,j) for i, line in enumerate(data) for j, char in enumerate(line) if char == 'S'][0]
pos = start
dirs = getDirs("S")
cycle = set([pos])
cyclePath = [pos]
while pos != start or len(cycle) == 1:
    for dir_ in dirs:
        ngb = (pos[0] + dir_[0], pos[1] + dir_[1])
        opp = (-dir_[0], -dir_[1])
        ngbDirs = getDirs(data[ngb[0]][ngb[1]])
        if opp in ngbDirs and (ngb not in cycle or ngb == start and len(cycle) > 2):
            pos = ngb
            cycle.add(ngb)
            cyclePath.append(ngb)
            dirs = ngbDirs
            break

print("Problem 19:", len(cycle) // 2)

inside = 0
out = ""
last = None
for i, line in enumerate(data):
    inLoop = False
    for j, char in enumerate(line):
        if (i, j) in cycle and char in "|JL" or char == "S":  # AND S behaves like J or L (which it does for my input) - need to figure out how to implement this rather than hard coding
            out += char
            inLoop = not inLoop
            continue
        if (i, j) in cycle or not inLoop:
            out += char
            if char == "F" or char == "L":
                last = char
            elif char != "-":
                last = None
            continue
        inside += 1
        out += "@"
    out += "\n"
print(out)

print("Problem 20:", inside)
