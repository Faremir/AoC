from Y19.classes.Instruction import Instruction


class Computer:
    def __init__(self, memory, opcodes):
        self.memory = list(memory)
        self.instructions = set(opcodes)
        self.instruction_pointer = 0
        self.manual_move = False

    def compute(self):
        result = None
        while self.instruction_pointer < len(self.memory):
            instr = Instruction(self)
            if instr.halt:
                break
            if (output := instr.process_opcode()) is not None:
                result = output
            self.move_instructor_pointer(instr.params_count)
        return result

    def move_instructor_pointer(self, shift):
        if not self.manual_move:
            self.instruction_pointer += shift + 1
        self.manual_move = False
