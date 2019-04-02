class ChocolateChart:
	"""

	"""

	def __init__(self, sequence):
		"""

		@param sequence:
		"""
		self.recipes = "37"

		self.recipe_range = (int(sequence), int(sequence) + 10)
		self.searched_sequence = sequence
		self.sequence_length = self.get_sequence()

	def get_sequence(self):
		"""

		@return:
		"""
		searched_seq_len = len(self.searched_sequence)
		result_length = 2
		indexes = [0, 1]
		while self.searched_sequence not in self.recipes[-(searched_seq_len+1):]:
			result_length = self.update_recipes(result_length, indexes)
			self.shift_indexes(result_length, indexes)
		return result_length - searched_seq_len


	def update_recipes(self, length, indexes):
		"""

		@param length:
		@param indexes:
		@return:
		"""
		new_recipes = str(int(self.recipes[indexes[0]]) + int(self.recipes[indexes[1]]))
		length += len(new_recipes)
		self.recipes += new_recipes
		return length

	def shift_indexes(self, result_length, indexes):
		"""

		@param result_length:
		@param indexes:
		"""
		for i in range(2):
			steps = 1 + int(self.recipes[indexes[i]])
			shift_index = indexes[i] + steps
			indexes[i] = shift_index % result_length

	def get_range(self):
		"""

		@return:
		"""
		return ''.join(self.recipes[self.recipe_range[0]:self.recipe_range[1]])

	def get_recipes_count(self):
		"""

		@return:
		"""
		return str(self.sequence_length)


	def __str__(self):
		return "Recipes scores = \"{0}\"\n Count of recipes = {1}".format(self.get_range(), self.get_recipes_count())


factory = ChocolateChart('880751')
print(factory)
