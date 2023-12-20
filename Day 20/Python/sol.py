"""
FILE: Day 20/sol.py
Author: Alex Jones
Desc: Solution to day 20 problems (39 & 40) for Advent of Code 2023, solved in Python 3.
"""
NOT_IMPLEMENTED = "Not Yet Implemented"
data = [line.split(" -> ") for line in open("Day 20/data.txt", "r").read().strip().splitlines()]

from math import lcm

class Module:

    low_counter = 0
    high_counter = 0

    def __init__(self):
        self.destinations = []

    def reset(self):
        return

    def add_source(self, source: "Module"):
        return
    
    def pulse(self, highPulse: bool, source: "Module") -> list[tuple["Module",bool,"Module"]]:
        Module.high_counter += highPulse
        Module.low_counter += not highPulse
        return []

class FlipFlop(Module):

    def __init__(self):
        super(FlipFlop, self).__init__()
        self.state = False
    
    def reset(self):
        self.state = False

    def pulse(self, highPulse: bool, source: Module | None) -> list[tuple[Module,bool,Module]]:
        super(FlipFlop, self).pulse(highPulse, source)
        if highPulse:
            return []
        self.state = not self.state
        return [(module, self.state, self) for module in self.destinations]

class Conjunction(Module):
    
    def __init__(self):
        super(Conjunction, self).__init__()
        self.memory = {}
        self.gotLow = False

    def reset(self):
        self.memory = {source: False for source in self.memory.keys()}
        self.gotLow = False

    def add_source(self, source: "Module"):
        super(Conjunction, self).add_source(source)
        self.memory[source] = False

    def pulse(self, highPulse: bool, source: Module | None) -> list[tuple[Module,bool,Module]]:
        super(Conjunction, self).pulse(highPulse, source)
        if not highPulse:
            self.gotLow = True
        self.memory[source] = highPulse
        pulse = not all(pulse for pulse in self.memory.values())
        return [(module, pulse, self) for module in self.destinations]

class Broadcaster(Module):

    def __init__(self):
        super(Broadcaster, self).__init__()

    def pulse(self, highPulse: bool, source: Module | None) -> list[tuple[Module,bool,Module]]:
        super(Broadcaster, self).pulse(highPulse, source)
        return [(module, highPulse, self) for module in self.destinations]

class Button(Module):
    
    def __init__(self, broadcast: Broadcaster):
        super(Button, self).__init__()
        self.destinations.append(broadcast)

    def pulse(self, highPulse: bool, source: Module | None) -> list[tuple[Module,bool,Module]]:
        return [(self.destinations[0], False, self)]


class Rx(Module):

    def __init__(self):
        super(Rx, self).__init__()
        self.pulsed = False

    def reset(self):
        self.pulsed = False

    def pulse(self, highPulse: bool, source: Module | None) -> list[tuple[Module,bool,Module]]:
        super(Rx, self).pulse(highPulse, source)
        if not highPulse:
            self.pulsed = True
        return []

def simulatePulse(buttonModule: Button):
    frontier = [(buttonModule, False, None)]
    while frontier:
        (module, highPulse, source) = frontier.pop(0)
        frontier += module.pulse(highPulse, source)

def simulateUntil(buttonModule: Button, rxModule: Module, conjunctions: set[Conjunction]) -> int:
    cycle_counts = {}
    count = 0
    while len(cycle_counts) != len(conjunctions) and not rxModule.pulsed:
        simulatePulse(buttonModule)
        count += 1
        for module in conjunctions:
            if module.gotLow and module not in cycle_counts:
                cycle_counts[module] = count
    return count if rxModule.pulsed else lcm(*cycle_counts.values()) // 2

modules = {"output": Module(), "rx": Rx()}
for (moduleName, _) in data:
    match moduleName[0]:
        case "%": modules[moduleName[1:]] = FlipFlop()
        case "&": modules[moduleName[1:]] = Conjunction()
        case "b": modules[moduleName] = Broadcaster()
for (moduleName, dests) in data:
    moduleName = moduleName[1:] if moduleName != "broadcaster" else moduleName
    modules[moduleName].destinations = [modules[name] for name in dests.split(", ")]
    for module in modules[moduleName].destinations:
        module.add_source(modules[moduleName])
buttonModule = Button(modules["broadcaster"])
for i in range(1000):
    simulatePulse(buttonModule)
print("Problem 39:", Module.low_counter * Module.high_counter)

for module in modules.values():
    module.reset()
conjunctions = set(m for m in modules.values() if isinstance(m, Conjunction))
print("Problem 40:", simulateUntil(buttonModule, modules["rx"], conjunctions))
