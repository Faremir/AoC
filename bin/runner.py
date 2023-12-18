import importlib

from bin import YEARS


class AOCRunner:
    def __init__(self, gui, year, day):
        self.gui = gui
        self.year = year
        self.day = str(day).zfill(2)
        self.script = self.get_script()

    def get_script(self):
        if self.year not in YEARS:
            raise ValueError("Invalid year")
        if int(self.day) not in range(1, 26):
            raise ValueError("Invalid day")
        module_name = f"scripts.{self.year}.{self.day}"
        try:
            module = importlib.import_module(module_name)
        except ImportError:
            raise ImportError(f"Module \"{module_name}\" does not exist.")

        class_name = f"Y{self.year[-2:]}D{self.day}"
        try:
            cls = getattr(module, class_name)
        except AttributeError:
            raise AttributeError(f"Class \"{class_name}\" does not exist in \"{module_name}\".")

        return cls(self.gui)

    def prepare(self):
        self.script.check_data()

    def run(self):
        return self.script.run(self.year, self.day)
