from scripts import script_base


class Pair:
    def __init__(self, regions):
        start, stop = regions.split("-")
        self.range_start = int(start)
        self.range_stop = int(stop)

    def __eq__(self, other):
        return (self.range_start <= other.range_start <= other.range_stop <= self.range_stop) or \
            (other.range_start <= self.range_start <= self.range_stop <= other.range_stop)

    def __and__(self, other):
        return not (self.range_stop < other.range_start or self.range_start > other.range_stop)

    def __str__(self):
        return f"{self.range_start}-{self.range_stop}"


class Y22D04(script_base.ScriptBase):
    def __init__(self, gui):
        super().__init__(gui)
        self.has_input = True

    def compute(self):
        part_1 = part_2 = 0
        res = self.input_data.splitlines()

        for p1, p2 in ((Pair(regions) for regions in line.split(",")) for line in res):
            part_1 += int(p1 == p2)
            part_2 += int(p1 & p2)
        self.result = f"Part 1: {str(part_1)} | Part 2 {str(part_2)}"
