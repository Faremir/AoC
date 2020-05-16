from Y19.classes.Computer import Computer


def get_restored_noun(memory):
    int_computer = Computer(memory, [1, 2])
    int_computer.memory[1], int_computer.memory[2] = 12, 2
    int_computer.compute()
    return int_computer.memory[0]


def get_valid_noun_verb(memory, valid_output):
    output = memory[0]
    noun, verb = 0, 0
    while output != valid_output:
        int_computer = Computer(memory, [1, 2])
        int_computer.memory[1], int_computer.memory[2] = noun, verb
        int_computer.compute()
        output = int_computer.memory[0]
        noun, verb = incr_noun_verb(noun, verb)
    return noun, verb - 1


def incr_noun_verb(noun, verb):
    verb += 1
    if verb == 100:
        verb = 0
        noun += 1
    return noun, verb


if __name__ == "__main__":
    import os

    file_path = os.path.abspath("../assignments/02.txt")
    with open(file_path, "r") as input_file:
        memory = [int(val) for val in input_file.read().split(",")]
    print(get_restored_noun(memory))
    noun, verb = get_valid_noun_verb(memory, 19690720)
    print(100 * noun + verb)
