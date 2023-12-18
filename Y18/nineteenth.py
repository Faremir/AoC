from Y18.sixteenth import *


class Registers:
	def __init__(self, file = 'Y18/input'):
		self.register = [1,0,0,0,0,0]
		self.pointer_reg_id = 0
		self.inructions = []
		self.parse_instructions(file)

	def parse_instructions(self, file):
		with open(file) as f:
			for instruction in f.read().split('\n'):
				if instruction[0] == '#':
					self.pointer_reg_id = int(instruction[4])
				else:
					opcode, temp_reg = instruction.split(' ', 1)
					reg_manipulation = tuple(int(x) for x in temp_reg.split(' '))
					self.inructions.append([opcode, reg_manipulation])

	def run_instructions(self):
		instruction_pointer = 0
		opcodes = Opcodes()
		while 0 <= instruction_pointer < len(self.inructions):
			if instruction_pointer in (8,9,10):
				instruction_pointer = 11
				continue
			self.register[self.pointer_reg_id] = instruction_pointer
			opcode, params = self.inructions[instruction_pointer]
			str_old_reg = str(self.register)
			self.register = opcodes.__handler__(opcode, self.register, params)
			# if not self.register[3] % 100000:
			print(f"ip={instruction_pointer:2} "
				      f"{str_old_reg:40.35} {opcode} {params} "
				      f"{self.register}")
			instruction_pointer = self.register[self.pointer_reg_id]
			instruction_pointer += 1
		print(self.register)


reg = Registers('input')
reg.run_instructions()
