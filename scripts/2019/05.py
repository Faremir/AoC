from .libs import Computer as Cmp


def get_diagnostic_code(mem, instruction_list):
    int_computer = Cmp.Computer(mem, instruction_list)
    return int_computer.compute()
