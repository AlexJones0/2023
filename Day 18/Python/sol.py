"""
FILE: Day 18/sol.py
Author: Alex Jones
Desc: Solution to day 18 problems (35 & 36) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = [line.split() for line in open("Day 18/data.txt", "r").read().strip().splitlines()]
DIRS = {"U": (-1,0), "R": (0,1), "D": (1,0), "L": (0,-1)}
RIGHT = {(-1,0): (0,1), (0,1): (1,0), (1,0):(0,-1), (0,-1):(-1,0)}
rotLeft = lambda xs, n: xs[n:] + xs[0:n]
adjPairs = lambda xs: zip(xs, rotLeft(xs, 1))

def shoelaceArea(coords: list[tuple[int,int]]) -> int: 
    # https://en.wikipedia.org/wiki/Shoelace_formula
    return abs(sum(x1*y2 - y1*x2 for (y1,x1), (y2,x2) in adjPairs(coords))) // 2

def picksCoords(area: int, boundaries: int) -> int: 
    # https://en.wikipedia.org/wiki/Pick's_theorem
    # A = i + (b/2) -1       =>     A + 1 + (b/2) = i + b
    return area + 1 + boundaries // 2

def decodeHex(code: str) -> tuple[int, tuple[int,int]]:
    return (DIRS["RDLU"[int(code[-2])]], int(code[2:-2], base=16))

def findVolume(instrs: list[tuple[int,tuple[int,int]]]) -> int:
    current = (0,0)
    coords = [current]
    boundaryCoords = 0
    dirs = []
    for dir_, moves in instrs:
        current = (current[0] + dir_[0] * moves, current[1] + dir_[1] * moves)
        coords.append(current)
        boundaryCoords += moves
        dirs.append(dir_)
    clockwise = sum(1 if dir2 == RIGHT[dir1] else -1 for dir1, dir2 in adjPairs(dirs))
    if clockwise:
        coords = coords[::-1]
    return picksCoords(shoelaceArea(coords), boundaryCoords)

print("Problem 35:", findVolume([(DIRS[dir_], int(move)) for (dir_, move, _) in data]))
print("Problem 36:", findVolume([decodeHex(hexCode) for (_, _, hexCode) in data]))
