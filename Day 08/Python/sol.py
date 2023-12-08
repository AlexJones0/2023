"""
FILE: Day 08/sol.py
Author: Alex Jones
Desc: Solution to day 8 problems (15 & 16) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = [line.split(" = ") for line in open("Day 08/data.txt", "r").read().strip().split("\n")]

from math import lcm

# Part 1 approach - represent the input as a list of directions and an adjacency list representation of a graph,
# simulate the steps taken until the end is found and output the counted steps.

instrs = data[0][0]
edges = {node.strip(): edges[1:-1].split(", ") for node, edges in data[2:]}

node, steps = "AAA", 0
while node != "ZZZ":
    index = instrs[steps % len(instrs)] == "R"
    node = edges[node][index]
    steps += 1
print("Problem 15:", steps)

# Part 2 approach - based on the fact that the problem description means that each start node must eventually
# hit some cycle involving the end node, we can simply find the number of steps required to hit the end
# node for each input, and then apply Chinese Remainder Theorem. In this case it turns out that
# cycles regularly occur such that each cycle hits Z at some multiple of a cycle length, meaning that
# the problem reduces to just taking the Lowest Common Multiple (LCM) of the steps at which end nodes are encountered.


nodes = [node for node in edges.keys() if node.endswith("A")]
steps, counts = 0, []
while nodes:
    index = instrs[steps % len(instrs)] == "R"
    for i, node in enumerate(nodes):
        nodes[i] = edges[node][index]
        if nodes[i].endswith("Z"):
            counts.append(steps+1)
    nodes = [node for node in nodes if not node.endswith("Z")]
    steps += 1
print("Problem 16:", lcm(*counts))
