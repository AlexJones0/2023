"""
FILE: Day 25/sol.py
Author: Alex Jones
Desc: Solution to day 25 problems (49 & 50) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = [line.split(": ") for line in open("Day 25/data.txt", "r").read().strip().splitlines()]

import networkx
from math import prod

graph = networkx.Graph({wire: other.split() for wire, other in data})
networkx.set_edge_attributes(graph, {e:{'capacity':1} for e in graph.edges()})
cutValue, components = 0, tuple()
for source, sink in [(a,b) for a in graph.nodes() for b in graph.nodes() if a != b]:
    cutValue, components = networkx.minimum_cut(graph, source, sink)
    if cutValue == 3:
        break
print("Problem 49:", prod(len(component) for component in components))
print("Problem 50:", "Freebie :)")
