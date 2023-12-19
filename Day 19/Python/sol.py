"""
FILE: Day 19/sol.py
Author: Alex Jones
Desc: Solution to day 19 problems (37 & 38) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = [lines.splitlines() for lines in open("Day 19/data.txt", "r").read().strip().split("\n\n")]

def followsRule(partID: int, rule: str | bool) -> bool:
    if rule is True:
        return True
    op = ">" if ">" in rule else "<"
    attr, target = rule.split(op)
    return op == ">" and parts[partID][attr] > int(target) or op == "<" and parts[partID][attr] < int(target)

# Parse input data into workflows (dict of name: rules where rules are a sequential list of (condition, target workflow)
# and into parts, where each part is sequentially assigned an ID, and repreesnted as a dict of values.
workflowInfo = [line[:-1].split("{") for line in data[0]]
workflows = {name: [tuple(rule.split(":")) if ":" in rule else (True, rule) for rule in rules.split(",")] for name, rules in workflowInfo}
parts = {id_: {val.split("=")[0]: int(val.split("=")[1]) for val in line[1:-1].split(",")} for id_, line in enumerate(data[1])}

# For each part, starting from "in", process until "A" or "R" is reached according to workflow rules.
currentWorkflow = {part: "in" for part in parts.keys()}
processingList = [part for part in parts.keys()]
while processingList:
    for partID in processingList:
        for (rule, next_) in workflows[currentWorkflow[partID]]:
            if followsRule(partID, rule):
                currentWorkflow[partID] = next_
                break 
    processingList = [partID for partID in processingList if currentWorkflow[partID] not in ("A", "R")]
print("Problem 37:", sum(sum(parts[partID].values()) for partID, res in currentWorkflow.items() if res == "A"))



from functools import cache
from math import prod

Rule = tuple[str,str,int]
AttrRange = dict[str,tuple[int,int]]

def negateRule(rule: Rule) -> Rule:
    if rule[0] == "<":
        return (">", rule[1], rule[2]-1)
    return ("<", rule[1], rule[2]+1)

def ruleToRange(rule: Rule) -> AttrRange:
    return {c: (1,4000) if c != rule[1] else (1 if rule[0] == "<" else rule[2]+1, 4000 if rule[0] == ">" else rule[2]-1) for c in "xmas"}

def combineRanges(range1: AttrRange, range2: AttrRange) -> bool:
    for attr, (lower1, upper1) in range1.items():
        (lower2, upper2) = range2[attr]
        lower = max(lower1, lower2)
        upper = min(upper1, upper2)
        if upper < lower:
            return False
        range2[attr] = (lower, upper)
    return True

def applyRange(current: AttrRange, ranges: list[AttrRange]) -> list[AttrRange]: 
    result = []
    for attrRange in ranges:
        newRange = attrRange.copy()
        if combineRanges(current, newRange):
            result.append(newRange)
    return result

@cache
def acceptedRatings(workflowName: str) -> list[AttrRange]:
    currentConditions = {c: (1,4000) for c in "xmas"}
    if workflowName == "R":
        return []
    elif workflowName == "A":
        return [currentConditions]
    validRanges = []
    for rule, next_ in workflows[workflowName]:
        if rule is True:
            return validRanges + applyRange(currentConditions, acceptedRatings(next_))
        op = ">" if ">" in rule else "<"
        rule = (op, rule.split(op)[0], int(rule.split(op)[1]))
        ruleConditions = currentConditions.copy()
        if combineRanges(ruleToRange(rule), ruleConditions):
            validRanges += applyRange(ruleConditions, acceptedRatings(next_))
        if not combineRanges(ruleToRange(negateRule(rule)), currentConditions):
            break
    return validRanges

print("Problem 38:", sum(prod(u-l+1 for (l, u) in r.values()) for r in acceptedRatings("in")))
