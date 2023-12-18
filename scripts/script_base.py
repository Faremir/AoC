from abc import abstractmethod, ABC


class ScriptBase(ABC):
    def __init__(self, gui):
        self.gui = gui
        self.has_input = False
        self.input_data = None
        self.result = ""

    def check_data(self):
        if not self.input_data and self.has_input:
            self.input_data = self.gui.data_handler[self.__class__.__name__]

    def run(self, year, day):
        print("Running year {} day {}".format(year, day))
        self.compute()
        print(self.result)
        return self.result

    @abstractmethod
    def compute(self):
        pass
