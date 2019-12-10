import operator


class Instruction:
    def __init__(self, code):
        self.code = code
        self.params_count = 2
        self.params_id = [None for x in range(self.params_count)]
        self.out_id = None

    def halt(self):
        return self.code != 1 and self.code != 2

    def get_params_indexes(self, current_state, opcode_index):
        for incr in range(1, self.params_count + 1):
            self.params_id[incr - 1] = current_state[opcode_index + incr]

    def get_action(self):
        ops = {
            1: operator.add,
            2: operator.mul
            }
        return ops[self.code]

    def write_action(self, memory):
        action = self.get_action()
        action_result = action(memory[self.params_id[0]], memory[self.params_id[1]])
        memory[self.out_id] = action_result


class Computer:
    def __init__(self):
        self.memory = []

    def parse_memory(self, file):
        with open(file, "r") as input_file:
            self.memory = [int(val) for val in input_file.read().split(",")]

    def get_restored_noun(self):
        current_state = self.memory.copy()
        current_state[1], current_state[2] = 12, 2
        current_state = self.compute(current_state)
        return current_state[0]

    def get_valid_noun_verb(self, valid_output):
        output = self.memory[0]
        noun, verb = 0, 0
        while output != valid_output:
            current_state = list(self.memory)
            current_state[1], current_state[2] = noun, verb
            current_state = self.compute(current_state)
            output = current_state[0]
            noun, verb = self.incr_noun_verb(noun, verb)
        return noun, verb - 1

    @staticmethod
    def incr_noun_verb(noun, verb):
        verb += 1
        if verb == 100:
            verb = 0
            noun += 1
        return noun, verb

    @staticmethod
    def compute(current_state):
        instr = None
        for opcode_index in range(0, len(current_state), 4):
            instr = Instruction(current_state[opcode_index])
            if instr.halt(): break
            instr.get_params_indexes(current_state, opcode_index)
            instr.out_id = current_state[opcode_index + instr.params_count + 1]
            instr.write_action(current_state)
        return current_state
