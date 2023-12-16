"""
FILE: Day 16/sol.py
Author: Alex Jones
Desc: Solution to day 16 problems (31 & 32) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = open("Day 16/data.txt", "r").read().strip().splitlines()

def simulateEnergized(startPos: complex, startDirection: complex) -> int:
    beams = [(startPos, startDirection)]
    seen = set()
    while beams:
        beamPos, beamDirection = beams.pop()
        if (beamPos, beamDirection) in seen:
            continue
        seen.add((beamPos, beamDirection))
        beamPos += beamDirection
        if not(0 <= beamPos.real < len(data) and 0 <= beamPos.imag < len(data[0])):
            continue
        match data[int(beamPos.real)][int(beamPos.imag)]:
            case  '.': beams.append((beamPos, beamDirection))
            case  '/': beams.append((beamPos, -1j/beamDirection))
            case '\\': beams.append((beamPos, 1j/beamDirection))
            case  '|': beams += [(beamPos, -1), (beamPos, 1)]
            case  '-': beams += [(beamPos, -1j), (beamPos, 1j)]
    return len(set(pos for (pos, _) in seen)) - 1

print("Problem 31:", simulateEnergized(-1j, 1j))

starts = [(complex(i,-1),1j) for i in range(len(data))] + [(complex(-1,j),1) for j in range(len(data[0]))] \
       + [(complex(i,len(data)),-1j) for i in range(len(data))] + [(complex(len(data[0]),j),-1) for j in range(len(data[0]))]

print("Problem 32:", max(simulateEnergized(*info) for info in starts))