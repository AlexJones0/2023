"""
FILE: Day 16/sol.py
Author: Alex Jones
Desc: Solution to day 16 problems (31 & 32) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = open("Day 16/data.txt", "r").read().strip().splitlines()

def simulateEnergized(startPos: tuple[int,int], startDirection: tuple[int,int]) -> int:
    beams = [(startPos, startDirection)]
    seen = set()
    while beams:
        beamPos, beamDirection = beams.pop()
        if (beamPos, beamDirection) in seen:
            continue
        nextPos = (beamPos[0] + beamDirection[0], beamPos[1] + beamDirection[1])
        seen.add((beamPos, beamDirection))
        if not(0 <= nextPos[0] < len(data) and 0 <= nextPos[1] < len(data[0])):
            continue
        match data[nextPos[0]][nextPos[1]]:
            case  '.': beams.append((nextPos, beamDirection))
            case  '/': beams.append((nextPos, (-beamDirection[1], -beamDirection[0])))
            case '\\': beams.append((nextPos, (beamDirection[1], beamDirection[0])))
            case  '|': beams += [(nextPos, (-1,0)), (nextPos, (1,0))]
            case  '-': beams += [(nextPos, (0,-1)), (nextPos, (0,1))]
    return len(set(pos for (pos, _) in seen)) - 1

print("Problem 31:", simulateEnergized((0,-1), (0,1)))

starts = [((i,-1),(0,1)) for i in range(len(data))] + [((-1,j),(1,0)) for j in range(len(data[0]))] \
       + [((i,len(data)),(0,-1)) for i in range(len(data))] + [((len(data[0]),j),(-1,0)) for j in range(len(data[0]))]

print("Problem 32:", max(simulateEnergized(*info) for info in starts))