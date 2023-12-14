"""
FILE: Day 14/sol.py
Author: Alex Jones
Desc: Solution to day 14 problems (27 & 28) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = [[*line] for line in open("Day 14/data.txt", "r").read().strip().splitlines()]
dirs_ = {"NORTH": (0, -1), "EAST": (1, 0), "SOUTH": (0, 1), "WEST": (-1, 0)}

def tiltRocks(data: list[list[str]], dir_: tuple[int,int]) -> None:
    # This is all obviously the least readable thing ever but I love it so I'm leaving it in
    lastPosInRow = [dir_[0] if dir_[0] != 1 else len(data)] * len(data[0])
    lastPosInCol = [dir_[1] if dir_[1] != 1 else len(data[0])] * len(data)
    for i, row in list(enumerate(data))[::(dir_[1]<=0)*2-1]: 
        for j, char in list(enumerate(row))[::(dir_[0]<=0)*2-1]:
            if char == '#':
                lastPosInCol[j], lastPosInRow[i] = i, j
            elif char == 'O':
                data[i][j] = "."
                data[lastPosInCol[j]-dir_[1] if dir_[1] else i][lastPosInRow[i]-dir_[0] if dir_[0] else j] = "O"
                lastPosInCol[j], lastPosInRow[i] = (lastPosInCol[j] - dir_[1], lastPosInRow[i] - dir_[0])

def getNorthLoad(data: list[list[str]]) -> int:
    return sum(len(data)-i for i, row in enumerate(data) for char in row if char == "O")

copy = [line.copy() for line in data]
tiltRocks(copy, dirs_["NORTH"])
print("Problem 27:", getNorthLoad(copy))

states = []
while data not in states:
    states.append([line.copy() for line in data])
    for dir_ in (dirs_["NORTH"], dirs_["WEST"], dirs_["SOUTH"], dirs_["EAST"]):
        tiltRocks(data, dir_)
startPos = states.index(data)
states = states[startPos:]
print("Problem 28:", getNorthLoad(states[(1000000000-startPos) % len(states)]))
