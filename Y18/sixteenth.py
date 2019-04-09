from collections import defaultdict


class Opcodes:
	def __init__(self):
		self.parsed_sample = {}
		self.register = [0, 0, 0, 0]

	def __parse_samples__(self, register, params):
		methods = [method for method in dir(self) if method[0] != '_']
		for method in methods:
			self.__handler__(method, register[:], params)

	def __handler__(self, method, register, params):
		if not hasattr(self, method):
			return
		callable_method = getattr(self, method)
		if not callable(callable_method):
			return
		self.register = register
		callable_method(*params)
		self.parsed_sample[callable_method] = register
		return self.register

	def addr(self, in_a, in_b, out_c):
		self.register[out_c] = self.register[in_a] + self.register[in_b]

	def addi(self, in_a, in_b, out_c):
		self.register[out_c] = self.register[in_a] + in_b

	def mulr(self, in_a, in_b, out_c):
		self.register[out_c] = self.register[in_a] * self.register[in_b]

	def muli(self, in_a, in_b, out_c):
		self.register[out_c] = self.register[in_a] * in_b

	def banr(self, in_a, in_b, out_c):
		self.register[out_c] = self.register[in_a] & self.register[in_b]

	def bani(self, in_a, in_b, out_c):
		self.register[out_c] = self.register[in_a] & in_b

	def borr(self, in_a, in_b, out_c):
		self.register[out_c] = self.register[in_a] | self.register[in_b]

	def borri(self, in_a, in_b, out_c):
		self.register[out_c] = self.register[in_a] | in_b

	def setr(self, in_a, in_b, out_c):
		self.register[out_c] = self.register[in_a]

	def seti(self, in_a, in_b, out_c):
		self.register[out_c] = in_a

	def gtir(self, in_a, in_b, out_c):
		self.register[out_c] = 1 if in_a > self.register[in_b] else 0

	def gtri(self, in_a, in_b, out_c):
		self.register[out_c] = 1 if self.register[in_a] > in_b else 0

	def gtrr(self, in_a, in_b, out_c):
		self.register[out_c] = 1 if self.register[in_a] > self.register[in_b] else 0

	def eqir(self, in_a, in_b, out_c):
		self.register[out_c] = 1 if in_a == self.register[in_b] else 0

	def eqri(self, in_a, in_b, out_c):
		self.register[out_c] = 1 if self.register[in_a] == in_b else 0

	def eqrr(self, in_a, in_b, out_c):
		self.register[out_c] = 1 if self.register[in_a] == self.register[in_b] else 0


class InstructionsEffet:
	def __init__(self, file = "input"):
		self.instruction_samples = defaultdict(list)
		self.instructions = []
		self.parse_input(file)
		self.opcodes = Opcodes()
		self.op_dict = defaultdict(list)
		self.has_3plus_opcodes = 0
		self.register = [0, 0, 0, 0]

	def parse_input(self, file):
		lines = [list(line) for line in open(file).read().split('\n')]
		i = 0
		while lines[i]:
			i = self.parse_samples(i, lines)
		while i < len(lines):
			i = self.parse_instructions(i, lines)

	def parse_instructions(self, i, lines):
		if lines[i]:
			instruction = [int(x) for x in ''.join(lines[i]).split(" ")]
			params = tuple(instruction[1:])
			self.instructions.append([instruction[0], params])
		i += 1
		return i

	def parse_samples(self, i, lines):
		if lines[i + 2][0] == 'A' and lines[i][0] == 'B':
			init_state = []
			result = []
			for k in range(9, 19, 3):
				init_state.append(int(lines[i][k]))
				result.append(int(lines[i + 2][k]))
			instruction = tuple(int(x) for x in ''.join(lines[i + 1]).split(" "))
			params = tuple(instruction[1:])
			self.instruction_samples[(instruction[0],params)].append([init_state, result])
		i += 4
		return i

	def process_samples(self):
		for instruction, register_results in self.instruction_samples.items():
			op_id, registers = instruction
			for register_state in register_results:
				init_state, result_state = register_state
				self.opcodes.__parse_samples__(init_state, registers)
				matching_opcodes = self.check_opcodes(result_state)

				self.op_dict[op_id] = self.filter_opcodes(matching_opcodes, op_id)

	def check_opcodes(self, result_state):
		matching = []
		count = 0
		for opcode, op_result in self.opcodes.parsed_sample.items():
			if op_result == result_state:
				count += 1
				matching.append(opcode.__name__)
		if count >= 3:
			self.has_3plus_opcodes += 1
		return matching

	def filter_opcodes(self, matching_opcodes, op_id):
		if self.op_dict[op_id]:
			return list(set(self.op_dict[op_id]) & set(matching_opcodes))
		return matching_opcodes

	def assign_instructions(self):
		assigned_opcodes = []
		while len(assigned_opcodes) < 16:
			for op_id, op_list in list(self.op_dict.items()):
				if len(op_list) == 1 and op_list[0] not in assigned_opcodes:
					assigned_opcodes.append(op_list[0])
				elif len(op_list) > 1:
					self.remove_already_assigned(assigned_opcodes, op_id)

	def remove_already_assigned(self, assigned_opcodes, op_id):
		new_id = 0
		while new_id < len(self.op_dict[op_id]):
			opcode = self.op_dict[op_id][new_id]
			if opcode in assigned_opcodes:
				self.op_dict[op_id].remove(opcode)
			else:
				new_id += 1

	def run_instructions(self):
		self.process_samples()
		self.assign_instructions()
		for instruction in self.instructions:
			op_id, params = instruction
			opcode = self.op_dict[op_id][0]
			self.register = self.opcodes.__handler__(opcode, self.register, params)

	def __str__(self):
		string = " samples with three or more opcodes.\n" \
		         "Final state of register after runing input instructions:\n\t"
		return str(self.has_3plus_opcodes) + string + str(self.register)
