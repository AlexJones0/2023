"""
FILE: Day 22/sol.py
Author: Alex Jones
Desc: Solution to day 22 problems (43 & 44) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = [[tuple(int(val) for val in coord.split(",")) for coord in line.split("~")] for line in open("Day 22/data.txt", "r").read().strip().splitlines()]

# Initialise all brick positions
falling = {brickID: [(i,j,k) for i in range(start[0], end[0]+1) 
                             for j in range(start[1], end[1]+1) 
                             for k in range(start[2], end[2]+1) ] 
           for brickID, (start, end) in enumerate(data)}

# Simulate bricks falling until all bricks are at rest, create a bidirectional map describing supporting / supported by relationships
brickCubes, supporting, supportedBy = {}, {i: set() for i in range(len(data))}, {i: set() for i in range(len(data))}
while falling:
    for brickID, positions in sorted(falling.items(), key=lambda pair: max(z for (_,_,z) in pair[1])):
        onGround = any(z <= 1 for (_,_,z) in positions)
        nextPositions = [(x,y,z-1) for (x,y,z) in positions]
        for supportingID in [brickCubes[pos] for pos in nextPositions if pos in brickCubes]:
            supportedBy[brickID].add(supportingID)
            supporting[supportingID].add(brickID)
        if onGround or supportedBy[brickID]:
            falling.pop(brickID)
            brickCubes |= {pos: brickID for pos in positions}
        else:
            falling[brickID] = nextPositions

# Calculate the number of bricks that only support bricks supported by some *other* brick, and hence are safe to disintegrate
print("Problem 43:", len([1 for brickID in range(len(data)) if all(len(supportedBy[supportID]) > 1 for supportID in supporting[brickID])]))

# For each brick, perform a BFS through the support maps to determine which bricks would fall in order, and sum these.
total = 0
for brickID in range(len(data)):
    fell, queue = set([brickID]), list(supporting[brickID].copy())
    while queue:
        supportedID = queue.pop(0)
        if supportedID in fell or len(supportedBy[supportedID] - fell) > 0:
            continue
        fell.add(supportedID)
        queue += supporting[supportedID]
    total += len(fell) - 1
print("Problem 44:", total)
