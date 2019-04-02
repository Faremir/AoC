class ChocolateChart:
	def __init__(self, sequence):
		self.recipes = "37"
		self.current_recipes_count = 2
		self.recipeIDs = [0, 1]
		self.recipe_range = (sequence, sequence + 10)
		self.searched_sequence = str(sequence)
		self.sequence_length = self.get_sequence()

	def get_sequence(self):
		searched_seq_len = len(self.searched_sequence) + 1
		result_length = 2
		while self.searched_sequence not in self.recipes[-searched_seq_len:]:
			new_recipes = str(int(self.recipes[self.recipeIDs[0]]) + int(self.recipes[self.recipeIDs[1]]))
			result_length += len(new_recipes)
			self.recipes += new_recipes
			for i in range(2):
				steps = 1 + int(self.recipes[self.recipeIDs[i]])
				shift_index = self.recipeIDs[i] + steps
				self.recipeIDs[i] = shift_index % result_length
		return result_length - searched_seq_len

	def get_range(self):
		return ''.join(self.recipes[self.recipe_range[0]:self.recipe_range[1]])

	def get_recipes_count(self):
		return str(self.sequence_length)

	def __str__(self):
		return "Recipes scores = \"" + self.get_range() + "\"\n Count of recipes = " + self.get_recipes_count()


factory = ChocolateChart(880751)
print(factory)
