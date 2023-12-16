"""
FILE: Day 16/sol.py
Author: Alex Jones
Desc: Solution to day 16 problems (31 & 32) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = open("Day 16/data.txt", "r").read().strip().splitlines()

def simulateEnergized(startPos: tuple[int,int], startDirection: tuple[int,int]) -> int:
    beams = [(startPos, startDirection)]
    energized = [[False] * len(data[0]) for _ in range(len(data))]
    prevSeen = set()
    while beams:
        newBeams = []
        for i, (beamPos, beamDirection) in enumerate(beams):
            nextPos = (beamPos[0]+beamDirection[0], beamPos[1]+beamDirection[1])
            if (beamPos, beamDirection) in prevSeen:
                beams[i] = None
                continue
            prevSeen.add((beamPos, beamDirection))
            if 0 <= nextPos[0] < len(data) and 0 <= nextPos[1] < len(data[0]):
                energized[nextPos[0]][nextPos[1]] = True
                nextSymbol = data[nextPos[0]][nextPos[1]]
            else:
                beams[i] = None
                continue
            if nextSymbol == '.':
                beams[i] = (nextPos, beamDirection)
            elif nextSymbol == '/':
                beamDirection = {(0,1):(-1,0), (-1,0):(0,1), (0,-1):(1,0), (1,0):(0,-1)}[beamDirection]
                beams[i] = (nextPos, beamDirection)
            elif nextSymbol == '\\':
                beamDirection = {(0,1):(1,0), (1,0):(0,1), (0,-1):(-1,0), (-1,0):(0,-1)}[beamDirection]
                beams[i] = (nextPos, beamDirection)
            elif nextSymbol == '|':
                if beamDirection[1] == 0:
                    beams[i] = (nextPos, beamDirection)
                else:
                    beams[i] = (nextPos, (-1,0))
                    newBeams.append((nextPos, (1,0)))
            elif nextSymbol == '-':
                if beamDirection[0] == 0:
                    beams[i] = (nextPos, beamDirection)
                else:
                    beams[i] = (nextPos, (0,-1))
                    newBeams.append((nextPos, (0,1)))
        beams += newBeams
        beams = [b for b in beams if b is not None]
    return len([1 for row in energized for state in row if state])

print("Problem 31:", simulateEnergized((0,-1), (0,1)))

starts = [((i,-1),(0,1)) for i in range(len(data))] + [((-1,j),(1,0)) for j in range(len(data[0]))] \
       + [((i,len(data)),(0,-1)) for i in range(len(data))] + [((len(data[0]),j),(-1,0)) for j in range(len(data[0]))]

print("Problem 32:", max(simulateEnergized(*info) for info in starts))
