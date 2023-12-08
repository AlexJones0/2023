"""
FILE: Day 08/sol.py
Author: Alex Jones
Desc: Solution to day 8 problems (15 & 16) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = open("Day 08/data.txt", "r").read().strip().split("\n")

from math import lcm

dirs = data[0]
edges = {node: tuple([n for n in edge[1:-1].split(", ")]) for node, edge in [(line.split("=")[0].strip(), line.split("=")[1].strip()) for line in data[2:]]}

node = "AAA"
steps = 0
while node != "ZZZ":
    index = 0 if dirs[steps % len(dirs)] == "L" else 1
    node = edges[node][index]
    steps += 1

print("Problem 15:", steps)

nodes = [node for node in edges.keys() if node.endswith("A")]
encountered = {}
steps = 0
while len(encountered) != len(nodes):
    index = 0 if dirs[steps % len(dirs)] == "L" else 1
    for i, node in enumerate(nodes):
        if node.endswith("Z"):
            if i not in encountered:
                encountered[i] = steps
            continue
        nodes[i] = edges[node][index]
    steps += 1

print("Problem 16:", lcm(*[encountered[i] for i in range(len(nodes))]))
