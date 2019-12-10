from utils import globals
from utils import func
from collections import defaultdict


class WireParser:
    def __init__(self, moves):
        self.coords = []
        self.parse_wire(moves)

    def parse_wire(self, moves):
        directions = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
        path = (0, 0)
        for movement in moves.split(","):
            for _ in range(int(movement[1:])):
                self.coords.append(path := tuple(map(sum, zip(path, directions[movement[0]]))))

    def get_wire(self):
        return self.coords


class Panel:
    def __init__(self):
        self.wires = []
        self.base = (0, 0)

    def parse_wires(self, file):
        with open(file, "r") as input_file:
            self.wires = [WireParser(moves).get_wire() for moves in input_file.readlines()]

    def get_intxns(self):
        return set.intersection(*map(set, self.wires))

    def get_closest_intxn(self):
        intxn_list = self.get_intxns()
        dist = globals.inf
        for intxn in intxn_list:
            if (new_dist := func.count_manhattan(self.base, intxn)) < dist:
                dist = new_dist
        return dist

    def calc_steps_to_intxn(self):
        intxn_list = self.get_intxns()
        intxn_list_dist = defaultdict(lambda: [0, 0])
        wire_id = 0
        for wire_path in self.wires:
            steps = 1
            for coords in wire_path:
                if coords in intxn_list and not ((coords in intxn_list_dist) and ((value := intxn_list_dist[coords][wire_id]) != 0)):
                    intxn_list_dist[coords][wire_id] = steps
                steps += 1
            wire_id += 1
        return intxn_list_dist

    def parse_steps_to_intxn(self):
        steps_to_intxn = self.calc_steps_to_intxn()
        steps = defaultdict(int)
        for coords, (wire_1, wire_2) in steps_to_intxn.items():
            steps[coords] = wire_1 + wire_2
        return steps[min(steps, key = steps.get)]
