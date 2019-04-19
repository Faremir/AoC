class Acres:
	def __init__(self, size = 50, file = 'input'):
		self.area = []
		self.size = size
		self.parse_area(file)

	def parse_area(self, file):
		self.area = [list(line) for line in open(file).read().split('\n')]

	def neighbors(self, coords):
		y, x = coords
		neighbors = []
		for new_y in range(y - 1, y + 2):
			for new_x in range(x - 1, x + 2):
				if 0 <= new_y < self.size and 0 <= new_x < self.size and (new_y, new_x) != (y, x):
					neighbors.append((new_y, new_x))
		return neighbors

	def check_ground_tree(self, coords, check, old):
		count = 0
		neighbors = self.neighbors(coords)
		for y, x in neighbors:
			if self.area[y][x] == check:
				count += 1
		if count >= 3:
			return check
		return old

	def check_lumberyard(self, coords):
		lumberyards = 0
		trees = 0
		neighbors = self.neighbors(coords)
		for y, x in neighbors:
			if self.area[y][x] == '#':
				lumberyards += 1
			if self.area[y][x] == '|':
				trees += 1
		if lumberyards >= 1 and trees >= 1:
			return '#'
		return '.'

	def minute_flow(self):
		new_area = list(map(list, self.area))
		for y in range(0, self.size):
			for x in range(0, self.size):
				if self.area[y][x] == '.':
					new_area[y][x] = self.check_ground_tree((y, x), '|', '.')
				elif self.area[y][x] == '|':
					new_area[y][x] = self.check_ground_tree((y, x), '#', '|')
				elif self.area[y][x] == '#':
					new_area[y][x] = self.check_lumberyard((y, x))
		return new_area[:]

	def print_area(self, minute):
		print("After", minute, "minutes")
		for y in range(0, self.size):
			for x in range(0, self.size):
				print(self.area[y][x], end = "")
			print()

	def flow(self):
		old_area = list(map(list, self.area))
		for n in range(1000):
			self.area = self.minute_flow()
			if not (n - 19) % 28:
				if old_area == self.area:
					return self.result()
				else:
					old_area = list(map(list, self.area))

	def result(self):
		wood = 0
		yards = 0
		for y in range(0, self.size):
			for x in range(0, self.size):
				if self.area[y][x] == '|':
					wood += 1
				elif self.area[y][x] == '#':
					yards += 1

		return wood * yards
