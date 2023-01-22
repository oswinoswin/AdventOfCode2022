import math
import re
from collections import deque


class Valve:
    def __init__(self, name: str, flow_rate: int):
        self.name: str = name
        self.flow_rate: int = flow_rate
        self.neighbours = []

    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)

    def __str__(self):
        return f"{{'name': '{self.name}', 'flow_rate': {self.flow_rate}, 'opened': {self.opened}, " \
               f"'neighbours':{[n.name for n in self.neighbours]}}} "

    def traverse(self, minutes_left, prev, gain, open_valves):
        # print(f"Minutes left: {minutes_left}, gain: {gain} valve: {self.name}, from: {prev.name} open: {open_valves}")
        if minutes_left == 0 or minutes_left == 1:
            return gain, open_valves.copy()

        if len(self.neighbours) == 1:
            gain_if_not_opened, valves_if_not_opened = prev.traverse(minutes_left - 1, self, gain, open_valves.copy())
            if self.flow_rate != 0 and self.name not in open_valves:
                gain_if_opened, valves_if_opened = prev.traverse(minutes_left - 2, self,
                                                                 gain + (minutes_left - 1) * self.flow_rate,
                                                                 open_valves.union({self.name}))
                if gain_if_opened > gain_if_not_opened:
                    return gain_if_opened, valves_if_opened.copy()
            return gain_if_not_opened, valves_if_not_opened.copy()

        updated_gain = gain
        updated_valves = open_valves.copy()

        for neighbour in self.neighbours:
            if neighbour == prev:
                continue
            neighbour_gain, neighbour_valves = neighbour.traverse(minutes_left - 1, self, gain, open_valves.copy())
            if neighbour_gain > updated_gain:
                updated_gain = neighbour_gain
                updated_valves = neighbour_valves

        if self.name not in open_valves and self.flow_rate != 0:
            tmp_gain = gain + self.flow_rate * (minutes_left - 1)
            for neighbour in self.neighbours:
                if neighbour == prev:
                    continue
                neighbour_gain, neighbour_valves = neighbour.traverse(minutes_left - 2, self, tmp_gain,
                                                                      open_valves.union({self.name}))
                if neighbour_gain > updated_gain:
                    updated_gain = neighbour_gain
                    updated_valves = neighbour_valves

        return updated_gain, updated_valves.copy()


def first(filename):
    valves = dict()
    neighbours_dict = dict()
    with open(filename, "r") as f:
        for line in f:
            flow_rate = re.findall(r'-?[0-9]+', line)
            flow_rate = int(flow_rate[0])
            name = line[6:8]
            neighbours = line.strip().split('to valve')
            neighbours = re.findall(r'[A-Z][A-Z]', neighbours[-1])
            valves[name] = Valve(name, flow_rate)
            neighbours_dict[name] = neighbours

    for key, nb in neighbours_dict.items():
        for n in nb:
            valves[key].add_neighbour(valves[n])
        print(valves[key])

    # valves["AA"].traverse(0)
    source = valves["AA"]
    open_valves = frozenset()
    return source.traverse(30, source, 0, open_valves)


def second(filename):
    with open(filename, "r") as f:
        for line in f:
            print(line)


if __name__ == "__main__":
    print(first("example.txt"))
    print(first("input.txt"))
    # print(second("example.txt"))
    # print(second("input.txt"))

#
#
# def bfs(source):
#     to_visit = deque([source])
#     minute = 0
#     source.steps_from_source = 0
#     while to_visit:
#         current = to_visit.popleft()
#         current.visited = True
#         print(f"{minute} Visiting: {current.name} steps from source = {current.steps_from_source}")
#         minute += 1
#         for neighbour in current.neighbours:
#             if not neighbour.visited:
#                 neighbour.steps_from_source = current.steps_from_source + 1
#                 to_visit.append(neighbour)
#
#
# def bfs2(source):
#     to_visit = source
#     minute = 0
#
#     while to_visit and minute < 10:
#         current = to_visit
#         current.visited = True
#         print(f"{minute} Visiting: {current.name}")
#         minute += 1
#         #where to go next?
#
#         current.neighbours.sort(key=lambda n: n.flow_rate, reverse=True)
#         print([(n.name, n.flow_rate) for n in current.neighbours])
#         for neighbour in current.neighbours:
#             if not neighbour.visited:
#                 to_visit = neighbour
#                 break
