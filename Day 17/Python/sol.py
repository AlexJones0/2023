"""
FILE: Day 17/sol.py
Author: Alex Jones
Desc: Solution to day 17 problems (33 & 34) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = open("Day 17/data.txt", "r").read().strip().splitlines()

from heapq import *

def AStarSearch(start: tuple[int,int], end: tuple[int,int], minMoves: int, maxMoves: int) -> int:
    h = lambda pos, goal: goal[0] - pos[0] + goal[1] - pos[1]  # Manhattan distance (admissable heuristic)
    left = lambda x, y: (-y, x if y==0 else -x)
    right = lambda x, y: (y, -x)
    distance, frontier = {}, []
    startState = (start, (0,1), maxMoves-1)
    distance[startState] = 0
    heappush(frontier, (h(start, end), startState))
    while frontier:
        state = heappop(frontier)[1]
        (pos, dir_, moves) = state
        if pos == end:
            return distance[state]
        
        neighbours = []
        nextPos = (pos[0] + dir_[0], pos[1] + dir_[1])
        if 0 < moves and 0 <= nextPos[0] < len(data) and 0 <= nextPos[1] < len(data[0]):
            neighbours.append(((nextPos, dir_, moves-1), int(data[nextPos[0]][nextPos[1]])))
        for f in (left, right):
            nextDir = f(*dir_)
            nextPos = (pos[0] + nextDir[0] * minMoves, pos[1] + nextDir[1] * minMoves)
            if 0 <= nextPos[0] < len(data) and 0 <= nextPos[1] < len(data[0]):
                cost = sum(int(data[pos[0]+nextDir[0]*i][pos[1]+nextDir[1]*i]) for i in range(1,minMoves+1))
                neighbours.append(((nextPos, nextDir, maxMoves-minMoves), cost))

        for (nextState, cost) in neighbours:
            nextDistance = distance[state] + cost
            if nextState not in distance or nextDistance < distance[nextState]:
                distance[nextState] = nextDistance
                heappush(frontier, (nextDistance + h(nextState[0], end), nextState))
    return -1

start, end = (0,0), (len(data)-1, len(data[0])-1)
print("Problem 33:", AStarSearch(start, end, 1, 3))
print("Problem 34:", AStarSearch(start, end, 4, 10))
