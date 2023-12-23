"""
FILE: Day 23/sol.py
Author: Alex Jones
Desc: Solution to day 21 problems (45 & 46) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = open("Day 23/data.txt", "r").read().strip().splitlines()

from collections import defaultdict

start = (0,1)
goal = (len(data)-1, len(data[-1])-2)
DIRS = {
    ">": [(0, 1)],
    "<": [(0, -1)],
    "v": [(1, 0)],
    "^": [(-1, 0)],
    ".": [(1, 0), (-1, 0), (0, 1), (0, -1)]
}

def maxPathDFS(start: tuple[int,int], goal: tuple[int,int], graph: dict[tuple[int,int],dict[tuple[int,int],int]]):
    # DFS on a directed Digraph to find the maximum length path without cycles from the start to the goal.
    maxPathLength = 0
    stack = [(start, [])]
    while stack:
        (pos, path) = stack.pop()
        if pos == goal:
            path.append(pos)
            pathLen = sum(graph[fst][snd] for (fst, snd) in zip(path[:-1], path[1:]))
            maxPathLength = max(maxPathLength, pathLen)
            continue
        path.append(pos)
        neighbours = graph[pos].keys()
        for ngb in neighbours:
            if ngb in path:
                continue
            stack.append((ngb, path.copy()))
    return maxPathLength

def graphFromData(start: tuple[int,int], data: list[str]):
    # Construct an undirected Digraph (adjacency dict repr) from the graph data, contracting all edges to a minimal graph
    graph = defaultdict(dict)
    graph[start] = {}
    frontier = [(start, None, False, -1, start)]
    visited = set([])
    while frontier:
        prevNode, prevPos, slopeOnPath, pathLen, pos = frontier.pop(0)
        if pos in graph and prevNode != pos:
            if not slopeOnPath:
                graph[pos][prevNode] = pathLen + 1
            graph[prevNode][pos] = pathLen + 1
            if pos in visited:
                continue
        visited.add(pos)
        symbol = data[pos[0]][pos[1]]
        neighbours = [(pos[0]+r, pos[1]+c) for (r,c) in DIRS[symbol]]
        neighbours = [(r,c) for (r,c) in neighbours if 0 <= r < len(data) and 0 <= c < len(data[0]) 
                                                       and data[r][c] != "#" and (r,c) != prevPos]
        if len(neighbours) == 1: # Mid-path (pruned)
            ngb = [ngb for ngb in neighbours if ngb != prevPos][0]
            frontier.append((prevNode, pos, slopeOnPath or data[ngb[0]][ngb[1]] not in ".#", pathLen+1, ngb))
            continue
        # Dead-end or 3-/4-way junction (a node)
        if pos not in graph and symbol == "." and prevNode != pos:
            if not slopeOnPath:
                graph[pos][prevNode] = pathLen + 1
            graph[prevNode][pos] = pathLen + 1
        for ngb in neighbours:
            frontier.append((pos, pos, False, 0, ngb))
    return graph

print("Problem 45:", maxPathDFS(start, goal, graphFromData(start, data)))
noSlopeMap = ["".join(char if char in ".#" else "." for char in line) for line in data]
print("Problem 46:", maxPathDFS(start, goal, graphFromData(start, noSlopeMap)))
