from Y19.days.D02 import Computer as Computer


def get_diagnostic_code(mem, instruction_list):
    int_computer = Computer(mem, instruction_list)
    return int_computer.compute()


if __name__ == "__main__":
    import os

    file_path = os.path.abspath("../assignments/05.txt")
    with open(file_path, "r") as input_file:
        memory = [int(val) for val in input_file.read().split(",")]
    part_one = get_diagnostic_code(memory, [1, 2, 3, 4])
    part_two = get_diagnostic_code(memory, [1, 2, 3, 4, 5, 6, 7, 8])
    print(part_two)
