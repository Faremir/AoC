from scripts import script_base


class Y22D01(script_base.ScriptBase):
    def __init__(self, gui):
        super().__init__(gui)
        self.has_input = True

    def compute(self):
        self.result = "Not implemented yet"
