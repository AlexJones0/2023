"""
FILE: Day 09/sol.py
Author: Alex Jones
Desc: Solution to day 9 problems (17 & 18) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = [[int(n) for n in line.split()] for line in open("Day 09/data.txt", "r").read().strip().split("\n")]


diffs = [(i, hist.copy()) for i, hist in enumerate(data)]
histories = [[hist.copy()] for hist in data]
while len(diffs) != 0:
    diffs = [(i, [snd - fst for fst, snd in zip(seq[:-1], seq[1:])]) for (i, seq) in diffs]
    for i, seq in diffs:
        histories[i].append(seq)
    diffs = [(i, seq) for i, seq in diffs if not all(n == 0 for n in seq)]
for seq in histories:
    seq[-1].append(0)
for seqHist in histories:
    for i in range(len(seqHist) - 2, -1, -1):
        seqHist[i].append(seqHist[i][-1] + seqHist[i+1][-1])
print("Problem 17:", sum(hist[0][-1] for hist in histories))

for seq in histories:
    seq[-1] = [0] + seq[-1]
for seqHist in histories:
    for i in range(len(seqHist) - 2, -1, -1):
        seqHist[i] = [seqHist[i][0] - seqHist[i+1][0]] + seqHist[i]
print("Problem 18:", sum(hist[0][0] for hist in histories))
