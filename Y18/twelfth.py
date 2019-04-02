from collections import defaultdict


def change_state(state):
	"""

	@param state:
	@return:
	"""
	if state == '#':
		return True
	else:
		return False


class Pot:
	"""

	"""

	def __init__(self):
		self.plant = False
		self.next_generation = False
		self.prev = None
		self.next = None
		self.index = 0

	def set_plant(self, state):
		"""

		@param state:
		"""
		self.plant = change_state(state)

	def get_plant(self):
		"""

		@return:
		"""
		if self.plant:
			return '#'
		return '.'

	def set_atr(self, index, plant = None):
		"""

		@param index:
		@param plant:
		"""
		self.index = index
		self.set_plant(plant)

	def add_next(self, other, plant = None):
		"""

		@param other:
		@param plant:
		"""
		self.next = other
		other.prev = self
		other.set_atr(self.index + 1, plant)

	def add_prev(self, other, plant = None):
		"""

		@param other:
		@param plant:
		"""
		self.prev = other
		other.next = self
		other.set_atr(self.index - 1, plant)

	def check_plant(self, plant):
		"""

		@param plant:
		@return:
		"""
		if self.get_plant() != plant:
			return False
		return True

	def set_next_gen(self, state):
		"""

		@param state:
		"""
		self.next_generation = change_state(state)

	def update(self):
		"""

		"""
		self.plant = self.next_generation
		self.next_generation = False

	def get_index(self):
		"""

		@return:
		"""
		return self.index


def check_progress(current_plant, next_gen):
	"""

	@param current_plant:
	@param next_gen:
	@return:
	"""
	first = current_plant.prev.prev
	for i in range(5):
		if not first.check_plant(next_gen[i]):
			return False
		first = first.next
	return True


class Garden:
	"""

	"""

	def __init__(self, initial_stage, generations, debug = False, file = "input"):
		self.next_generations = defaultdict(str)
		self.gen_stage_changes(file)
		self.generations = generations
		self.debug = debug

		self.initial_stage = initial_stage
		self.head = None
		self.tail = None

		self.result = 0

	def gen_init_stage(self, current_pot = None, index = 1):
		"""

		@param current_pot:
		@param index:
		@return:
		"""
		if index == len(self.initial_stage):
			self.tail = current_pot
			return
		current_pot.add_next(Pot(), self.initial_stage[index])
		self.gen_init_stage(current_pot.next, index + 1)

	def gen_stage_changes(self, file):
		"""

		@param file:
		"""
		with open(file) as progresses:
			for line in progresses.readlines():
				state, _, state_result = line.split(" ")
				self.next_generations[state] = state_result[0]
		progresses.close()

	def add_to_top(self, first, num = 0):
		"""

		@param first:
		@param num:
		@return:
		"""
		if num == 5:
			self.head = first
			return
		first.add_prev(Pot())
		self.add_to_top(first.prev, num + 1)

	def add_to_end(self, last, num = 0):
		"""

		@param last:
		@param num:
		@return:
		"""
		if num == 5:
			self.tail = last
			return
		last.add_next(Pot())
		self.add_to_end(last.next, num + 1)

	def remove_tail(self):
		"""

		"""
		tail = self.tail
		while tail:
			if not tail.plant:
				tail = tail.prev
			else:
				self.tail = tail
				break

	def remove_head(self):
		"""

		"""
		head = self.head
		while head:
			if not head.plant:
				head = head.next
			else:
				self.head = head
				break

	def del_excess_pots(self):
		"""

		"""
		self.remove_head()
		self.remove_tail()
		self.add_to_top(self.head)
		self.add_to_end(self.tail)

	def count_flowers(self):
		"""

		"""
		curr_plant = self.head
		while curr_plant:
			if curr_plant.check_plant('#'):
				self.result += curr_plant.get_index()
			curr_plant = curr_plant.next

	def generate_pattern(self):
		"""

		@return:
		"""
		string = ""
		curr_plant = self.head
		while curr_plant:
			string + str(curr_plant.get_index())
			curr_plant = curr_plant.next
		return string, self.head.get_index()

	# def check_pattern(self, str1, str2, id1, id2):
	# 	if str1 == str2:
	# 		return id2 - id1
	# 	return -1

	def aging(self):
		"""

		@return:
		"""
		self.head = Pot()
		self.head.set_plant(self.initial_stage[0])
		self.gen_init_stage(self.head)
		if self.debug:
			self.print_generation()

		for age in range(self.generations):
			self.del_excess_pots()
			self.check_next_gen()
			self.update_next_gen()

			if self.debug:
				self.print_generation()

		# pattern, id = self.generate_pattern()
		# index_diff = self.check_pattern()
		# if index_diff != -1:
		# 	print(index_diff)

		self.count_flowers()
		return self.result

	def check_next_gen(self):
		"""

		"""
		curr_plant = self.head.next.next
		while curr_plant.next.next:
			for state, state_result in self.next_generations.items():
				if check_progress(curr_plant, state):
					curr_plant.set_next_gen(state_result)

			curr_plant = curr_plant.next

	def update_next_gen(self):
		"""

		"""
		curr_plant = self.head
		while curr_plant:
			curr_plant.update()
			curr_plant = curr_plant.next

	def print_generation(self):
		"""

		"""
		pot = self.head
		while pot:
			if pot.plant:
				print("#", end = "")
			else:
				print(".", end = "")
			pot = pot.next
		print("\n")

