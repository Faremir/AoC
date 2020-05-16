class Instruction:
    params_count = 0
    op_code = 0
    param_modes = [0, 0, 0]  # A,B,C
    ops = {}

    def __init__(self, computer):
        self.computer = computer
        self.parse_instr()
        self.set_operations()

    def parse_instr(self):
        value = self.computer.memory[self.computer.instruction_pointer]
        self.op_code = value % 100
        params = str(value // 100).zfill(3)
        self.param_modes = [int(d) for d in params][::-1]

    def set_operations(self):
        self.ops = {
            1: self.__addi__,
            2: self.__mull__,
            3: self.__uinp__,
            4: self.__vout__,
            5: self.__jont__,
            6: self.__jonf__,
            7: self.__cmpl__,
            8: self.__cmpe__
            }
        self.ops = {k: self.ops[k] for k in (self.ops.keys() & self.computer.instructions)}

    def get_params_count(self):
        params_count = {
            1: 3,
            2: 3,
            3: 1,
            4: 1,
            5: 2,
            6: 2,
            7: 3,
            8: 3
            }
        self.params_count = params_count[self.op_code] if self.op_code in params_count else 0

    def get_action(self):
        return self.ops[self.op_code] if self.op_code in self.ops else None

    def get_params(self):
        self.get_params_count()
        for i in range(1, self.params_count + 1):
            if not self.param_modes[i - 1]:
                yield self.computer.memory[self.computer.instruction_pointer + i]
            else:
                yield self.computer.instruction_pointer + i

    def process_opcode(self):
        action = self.get_action()
        params_index = list(self.get_params())
        return action(*params_index)

    ## ACTIONS ###
    @property
    def halt(self):
        return self.op_code not in self.ops

    def __addi__(self, in_a, in_b, out_c):
        self.computer.memory[out_c] = self.computer.memory[in_a] + self.computer.memory[in_b]

    def __mull__(self, in_a, in_b, out_c):
        self.computer.memory[out_c] = self.computer.memory[in_a] * self.computer.memory[in_b]

    def __uinp__(self, out_a):
        message = "\u2551 \t\t\u25E6 Enter ID:  " + " " * 12 + "\u2560\u2550 "
        while not (user_input := input(message)).isdigit():
            pass
        self.computer.memory[out_a] = int(user_input)

    def __vout__(self, in_a):
        return self.computer.memory[in_a]

    def __jont__(self, in_a, out_b):
        if self.computer.memory[in_a] != 0:
            self.computer.instruction_pointer = self.computer.memory[out_b]
            self.computer.manual_move = True

    def __jonf__(self, in_a, out_b):
        if not self.computer.memory[in_a]:
            self.computer.instruction_pointer = self.computer.memory[out_b]
            self.computer.manual_move = True

    def __cmpl__(self, in_a, in_b, out_c):
        if self.computer.memory[in_a] < self.computer.memory[in_b]:
            self.computer.memory[out_c] = 1
        else:
            self.computer.memory[out_c] = 0

    def __cmpe__(self, in_a, in_b, out_c):
        if self.computer.memory[in_a] == self.computer.memory[in_b]:
            self.computer.memory[out_c] = 1
        else:
            self.computer.memory[out_c] = 0
