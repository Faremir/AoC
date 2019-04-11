class ChocolateChart:
	"""

	"""

	def __init__(self, sequence):
		"""

		@param sequence:
		"""
		self.recipes = [3, 7]
		self.recipe_range = int(sequence)
		self.searched_sequence = sequence
		self.first_elf = 0
		self.second_elf = 1
		self.sequence_length = self.next_recipes()

	def next_recipes(self):
		"""

		@return:
		"""
		searched_seq_len = len(self.searched_sequence)
		result_length = 2
		while not self.check_recipes_sequence(searched_seq_len):
			result_length += self.add_new_recipes()
			self.shift_elves(result_length)
		return result_length - searched_seq_len

	def check_recipes_sequence(self, length):
		"""

		@param length:
		@return:
		"""
		if self.searched_sequence == ''.join(str(i) for i in self.recipes[-length:]):
			return True
		elif self.searched_sequence == ''.join(str(i) for i in self.recipes[-length - 1:-1]):
			return True
		return False

	def add_new_recipes(self):
		"""

		@return:
		"""
		new_recipes = self.recipes[self.first_elf] + self.recipes[self.second_elf]
		for recipe in str(new_recipes):
			self.recipes.append(int(recipe))
		return 2 if new_recipes >= 10 else 1

	def shift_elves(self, length):
		"""

		@param length:
		"""
		self.first_elf += 1 + self.recipes[self.first_elf]
		self.second_elf += 1 + self.recipes[self.second_elf]
		self.first_elf %= length
		self.second_elf %= length

	def get_range(self):
		"""

		@return:
		"""
		return str(self.recipes[self.recipe_range:self.recipe_range + 10])

	def get_recipes_count(self):
		"""

		@return:
		"""
		return str(self.sequence_length)

	def __str__(self):
		return "\nRecipes scores = \"{0}\"\nCount of recipes = {1}".format(self.get_range(), self.get_recipes_count())



