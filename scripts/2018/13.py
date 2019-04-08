from itertools import combinations
class Cart:
	def __init__(self, direct):
		self.direction = direct
		self.coords = [0, 0]
		self.alive = True
		self.turn_count = 0

	def move(self, next_path):
		"""

		@param next_path:
		"""
		self.update_coords()
		self.turn(next_path)
		if next_path == '+':
			self.crossroad_turn()

	def turn(self, next_path):
		if next_path == '\\':  # FROM  - TO
			if self.direction == '>':  # right  - bottom
				self.direction = 'v'
			elif self.direction == '<':  # left  - top
				self.direction = '^'
			elif self.direction == '^':  # top   - left
				self.direction = '<'
			elif self.direction == 'v':  # botoom- right
				self.direction = '>'
		elif next_path == '/':
			if self.direction == '>':  # right  - top
				self.direction = '^'
			elif self.direction == '<':  # left - botom
				self.direction = 'v'
			elif self.direction == '^':  # top   - right
				self.direction = '>'
			elif self.direction == 'v':  # bottom- left
				self.direction = '<'

	def update_coords(self):
		if self.direction == '<':
			self.coords[1] -= 1
		elif self.direction == '>':
			self.coords[1] += 1
		elif self.direction == '^':
			self.coords[0] -= 1
		elif self.direction == 'v':
			self.coords[0] += 1

	def crossroad_turn(self):
		if self.turn_count % 3 == 0:
			self.turn_left()
		elif self.turn_count % 3 == 1:
			pass
		elif self.turn_count % 3 == 2:
			# right TODO
			self.turn_right()
		self.turn_count += 1
		pass

	def turn_left(self):
		if self.direction == '<':
			self.direction = 'v'
		elif self.direction == 'v':
			self.direction = '>'
		elif self.direction == '>':
			self.direction = '^'
		elif self.direction == '^':
			self.direction = '<'

	def turn_right(self):
		if self.direction == '<':
			self.direction = '^'
		elif self.direction == 'v':
			self.direction = '<'
		elif self.direction == '>':
			self.direction = 'v'
		elif self.direction == '^':
			self.direction = '>'

	def get_next_coords(self):
		if self.direction == '<':
			return [self.coords[0], self.coords[1] - 1]
		elif self.direction == '>':
			return [self.coords[0], self.coords[1] + 1]
		elif self.direction == '^':
			return [self.coords[0] - 1, self.coords[1]]
		elif self.direction == 'v':
			return [self.coords[0] + 1, self.coords[1]]

	def __eq__(self, other):
		if self.coords == other.coords:
			self.alive = False
			other.alive = False
			return True
		return False


class Track:
	def __init__(self, file = 'Y18/input'):
		self.track = [list(line) for line in open(file).read().split('\n')]
		self.carts = self.parse_carts()
		self.remove_carts()

	def parse_carts(self):
		"""

		@return:
		"""
		x = 0
		y = 0
		cart_list = []
		for line in self.track:
			for path in line:
				if path == 'v' or path == '>' or path == '<' or path == '^':
					cart = Cart(path)
					cart.coords = [y, x]
					cart_list += [cart]
				x += 1
			x = 0
			y += 1

		return cart_list

	def remove_carts(self):
		for cart in self.carts:
			if cart.direction == "<" or cart.direction == ">":
				self.track[cart.coords[0]][cart.coords[1]] = '-'
			elif cart.direction == "^" or cart.direction == "v":
				self.track[cart.coords[0]][cart.coords[1]] = '|'

	def check_collision(self, first, second):
		if first.alive and second.alive and first.__eq__(second):
			coords = [first.coords[1], first.coords[0]]
			self.carts.remove(second)
			return coords
		return None


	def move_carts(self, cart):
		y, x = cart.get_next_coords()
		cart.move(self.track[y][x])

	def run_track(self):
		last_alive = len(self.carts)
		print(last_alive)
		while last_alive != 1:
			self.carts.sort(key = lambda h: (h.coords[0], h.coords[1]))
			for cart in self.carts:
				if cart.alive:
					self.move_carts(cart)
				for first, second in combinations(self.carts, 2):
					collision_coords = self.check_collision(first, second)
					if collision_coords:
						last_alive -= 2
						break
		return [self.carts[0].coords[1], self.carts[0].coords[0]]

