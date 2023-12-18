from .libs import Computer as Cmp


def get_restored_noun(memory):
    int_computer = Cmp.Computer(memory, [1, 2])
    int_computer.memory[1], int_computer.memory[2] = 12, 2
    int_computer.compute()
    return int_computer.memory[0]


def get_valid_noun_verb(memory, valid_output):
    output = memory[0]
    noun, verb = 0, 0
    while output != valid_output:
        int_computer = Cmp.Computer(memory, [1, 2])
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
