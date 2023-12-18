from scripts import script_base


class Y22D01(script_base.ScriptBase):
    def __init__(self, gui):
        super().__init__(gui)
        self.has_input = True

    def compute(self):
        groups = self.input_data.split("\n\n")

        def split_to_int(group):
            block = group.splitlines()
            return sum(int(x) for x in block)

        data = [split_to_int(group) for group in groups]
        max_1 = data.pop(data.index(max(data)))
        max_2 = data.pop(data.index(max(data)))
        max_3 = data.pop(data.index(max(data)))
        max_sum = max_1 + max_2 + max_3
        self.result = f"Part 1: {str(max_1)} | Part 2 {str(max_sum)}"
