from scripts import script_base


class Y22D03(script_base.ScriptBase):
    def __init__(self, gui):
        super().__init__(gui)
        self.has_input = True

    def compute(self):
        res = self.input_data.splitlines()
        part_1 = 0
        part_2 = 0
        group = []

        def get_letter_value(letter):
            res = ord(letter) - 96
            if res < 0:
                res += 58
            return res

        for line in res:
            # split line in two same size halves of original string
            group.append(line)
            if len(group) == 3:
                group = [set(g) for g in group]
                intersect = group[0].intersection(group[1], group[2])
                part_2 += get_letter_value(intersect.pop())
                group = []

            p1, p2 = line[: len(line) // 2], line[len(line) // 2:]
            intersect = set(p1).intersection(set(p2))
            part_1 += get_letter_value(intersect.pop())

        self.result = f"Part 1: {str(part_1)} | Part 2 {str(part_2)}"
