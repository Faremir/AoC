from scripts import script_base



class Y22D05(script_base.ScriptBase):
    def __init__(self, gui):
        super().__init__(gui)
        self.has_input = True

    def compute(self):
        part_1 = part_2 = 0
        res = self.input_data.splitlines()
        self.result = f"Part 1: {str(part_1)} | Part 2 {str(part_2)}"
