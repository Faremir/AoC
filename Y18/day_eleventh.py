from itertools import product
import numpy as np


class Grid:
	"""

	"""
	def __init__(self, serial_no):
		self.serial_no = serial_no
		self.grid = np.fromfunction(self.cell_value, (300, 300), dtype = int)

	def cell_value(self, x, y):
		"""

		@param x:
		@param y:
		@return:
		"""
		return ((((((x + 10) * y) + self.serial_no) * (x + 10)) % 1000) // 100) - 5

	# noinspection PyUnresolvedReferences
	def square_power_sum(self, y, x, square_size = 3):
		"""

		@param y:
		@param x:
		@param square_size:
		@return:
		"""
		# noinspection PyUnresolvedReferences
		submatrix = self.grid[np.ix_(range(x, x + square_size), range(y, y + square_size))]
		return submatrix.sum(axis = (1, 0))

	def parse_grid(self):
		"""

		@return:
		"""
		result = [[0, 0], float("-inf"), 0]
		for sub_size in range(3, 299):
			for y, x in product(range(300 - sub_size), range(300 - sub_size)):
				current = self.square_power_sum(y, x, sub_size)
				if result[1] < current:
					result = [[x, y], current, sub_size]
		return result


if __name__ == "__main__":
	grid = Grid(8141)
	print(grid.parse_grid())
