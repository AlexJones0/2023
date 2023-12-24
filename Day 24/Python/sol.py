"""
FILE: Day 24/sol.py
Author: Alex Jones
Desc: Solution to day 24 problems (47 & 48) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = [tuple(tuple(int(num.strip()) for num in part.split(",")) 
        for part in line.split("@")) 
        for line in open("Day 24/data.txt", "r").read().strip().splitlines()]
testMinPos, testMaxPos = (7, 27) if len(data) == 5 else (200000000000000, 400000000000000)

Vector2, Vector3 = tuple[float,float], tuple[float,float,float]
SlopeIntercept = tuple[float,float]
ParametricLine = tuple[Vector3,Vector3]

def getIntersection2D(line1: SlopeIntercept, line2: SlopeIntercept) -> Vector2 | None:
    (grad1, intersect1) = line1
    (grad2, intersect2) = line2
    if grad1 == grad2:
        return None  # Count the same line as having "no intersections"
    if grad1 == float("inf"):
        meetX = intersect1
        meetY = grad2 * meetX + intersect2
    elif grad2 == float("inf"):
        meetX = intersect2
        meetY = grad1 * meetX + intersect1
    else:
        meetX = (intersect2 - intersect1) / (grad1 - grad2)
        meetY = grad1 * meetX + intersect1
    return (meetX, meetY)

def isInFuture(nextPos: Vector2, lineInfo: ParametricLine) -> bool:
    return all((vel == 0 and (nextVal - pos) == 0) or (vel != 0 and (nextVal - pos) / vel > 0) 
               for (nextVal, pos, vel) in zip(nextPos, *lineInfo))

part1 = []
for lineInfo in data:
    ((px, py, _), (vx, vy, _)) = lineInfo
    grad = vy/vx if vx != 0 else float('inf')
    intersect = (py - grad * px) if vx != 0 else px
    line = (grad, intersect)
    part1.append((line, lineInfo))

result = 0
for i, (line1, line1Info) in enumerate(part1):
    for (line2, line2Info) in part1[(i+1):]:
        intersect = getIntersection2D(line1, line2)
        if (intersect is not None and \
            all(testMinPos <= val <= testMaxPos for val in intersect) and \
            isInFuture(intersect, line1Info) and isInFuture(intersect, line2Info)
        ):
            result += 1
print("Problem 47:", result)

import z3
(px, py, pz, vx, vy, vz) = [z3.Real(var) for var in ("px", "py", "pz", "vx", "vy", "vz")]
solver = z3.Solver()
for i, hailInfo in enumerate(data):
    t = z3.Real(f't{i}')
    for p, v, hp, hv in zip((px,py,pz),(vx,vy,vz), *hailInfo):
        solver.add(p + v * t == hp + hv * t)
    solver.add(t >= 0)
assert solver.check() == z3.sat
model = solver.model()
print("Problem 48:", sum(model.eval(var).as_long() for var in (px, py, pz)))
