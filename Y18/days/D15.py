class Unit:
	HP = 200
	AP = 3

	def __init__(self, coords, race, hp: int = HP, ap: int = AP):
		self.coords = coords
		self.race = race
		self.HP = hp
		self.AP = ap

	def __attack__(self, other):
		other.HP -= self.AP
		return not other.check_lives()

	def __move__(self, coords):
		self.coords = coords

	def is_target(self, other):
		return not self.race == other.race

	def check_lives(self):
		if self.HP > 0:
			return True
		return False

	def __eq__(self, coords):
		return self.coords == coords

	def __repr__(self):
		return str(self.coords) + str(self.race)

	def __hash__(self):
		return self.coords

	def is_attackable(self, other):
		return self.is_target(other) and self.distance(other) == 1

	def distance(self, other):
		return abs(self.coords[0] - other.coords[0]) + abs(self.coords[1] - other.coords[1])


def get_shortest_path(paths):
	return min(sorted(paths.values()), key = len)


class Game:
	def __init__(self, file = 'Y18/input', debug = False):
		self.file = file

		self.debug = debug
		self.units = []
		self.board = None
		self.board_size = None

	def __clear_board__(self):
		self.board = [list(line) for line in open(self.file).read().split('\n')]
		self.board_size = len(self.board[0])
		self.units = []

	def __generate_game__(self):
		self.__clear_board__()
		for y in range(self.board_size):
			for x in range(self.board_size):
				if self.board[y][x] == 'G' or self.board[y][x] == 'E':
					self.units.append(Unit([y, x], self.board[y][x]))
					self.board[y][x] = '.'

	def is_accesible(self, node):
		y, x = node
		return self.board[y][x] not in ['G', 'E'] and [y, x] not in self.units

	def neighbors(self, node):
		y, x = node
		possible_neighbors = [[y - 1, x], [y, x - 1], [y, x + 1], [y + 1, x]]
		return [nbr for nbr in possible_neighbors if self.board[nbr[0]][nbr[1]] != "#"]

	def generate_path(self, start, goal):
		explored = []
		queue = [[start]]
		while queue:
			path = queue.pop(0)
			current = path[-1]
			if current not in explored:
				for nbr in self.neighbors(current):
					new_path = list(path)
					if nbr == goal:
						return new_path[1:]
					if self.is_accesible(nbr):
						new_path.append(nbr)
						queue.append(new_path)
				explored.append(current)
		return []

	def get_paths(self, unit):
		paths = {}
		for goal in self.units:
			if unit.is_target(goal) and not unit == goal.coords:
				if unit.distance(goal) == 1:
					paths = {}
					break
				path = self.generate_path(unit.coords, goal.coords)
				if path:
					paths[tuple(goal.coords)] = path
		return paths

	def get_attackable_target(self, unit):
		attackable_targets = []
		for target in self.units:
			if target.is_attackable(unit):
				attackable_targets.append(target)
		attackable_targets.sort(key = lambda x: (x.HP, x.coords))
		return attackable_targets

	def unit_actions(self, unit, unit_index):
		self.unit_move(unit)
		return self.unit_attack(unit, unit_index) - 1

	def remove_dead_target(self, next_target, unit_index):
		if not next_target.check_lives():
			target_index = self.units.index(next_target)
			self.units.remove(next_target)
			if target_index < unit_index:
				return 1
		return 0

	def unit_attack(self, unit, unit_index):
		targets = self.get_attackable_target(unit)
		if targets:
			next_target = targets[0]
			unit.__attack__(next_target)
			return self.remove_dead_target(next_target, unit_index)
		return 0

	def unit_move(self, unit):
		possible_paths = self.get_paths(unit)
		if possible_paths:
			shortest_path = min(sorted(possible_paths.values()), key = len)
			next_step: [int, int] = shortest_path[0]
			unit.__move__(next_step)

	def check_game_end(self):
		elves, goblins = 0, 0
		for unit in self.units:
			if unit.race == "G":
				goblins += 1
			else:
				elves += 1
		return elves == 0 or goblins == 0

	def get_result(self, completed_rounds):
		remaining_hp = 0
		for unit in self.units:
			remaining_hp += unit.HP
		return remaining_hp * completed_rounds

	def increment_elves_attack(self, increment):
		for unit in self.units:
			if unit.race == "E":
				unit.AP += increment

	def check_alive_elves(self):
		dead_elves = 0
		for unit in self.units:
			if unit.race == "E":
				dead_elves += 1
		return dead_elves

	@staticmethod
	def elves_total(board):
		elves = 0
		for node in board:
			if node == 'E':
				elves += 1
		return elves

	def make_turn(self, index, one_race_left):
		self.units.sort(key = lambda x: x.coords)
		unit_index = 0
		turn_finihed = False
		while unit_index < len(self.units):
			turn_finihed = False
			unit = self.units[unit_index]
			unit_index -= self.unit_actions(unit, unit_index)
			if self.check_game_end():
				one_race_left = True
				if unit_index < len(self.units):
					break
			turn_finihed = True
		index += 1 if turn_finihed else 0
		if self.debug:
			self.print_board(index)
		return index, one_race_left

	def run_game(self):
		one_race_left = False
		index = 0
		while not one_race_left:
			index, one_race_left = self.make_turn(index, one_race_left)
		return self.get_result(index), index

	def prevent_dead_elves(self):
		board = open(self.file).read()
		alive_elves = self.elves_total(board)
		dead_elves = float('inf')
		increment, result, index = 0, 0, 0
		while dead_elves > 0:
			increment += 1
			self.__generate_game__()
			self.increment_elves_attack(increment)
			result, index = self.run_game()
			dead_elves = alive_elves - self.check_alive_elves()
			print(result, increment + 3, index, dead_elves)
		return result, increment + 3, index

	def print_board(self, index):
		print("\nAfter", index, "turns:")
		for y in range(self.board_size):
			units_hp = []
			for x in range(self.board_size):
				unit = next((unit for unit in self.units if unit == [y, x]), None)
				if unit:
					units_hp.append(unit.HP)
					print(unit.race, end = "")
				else:
					print(self.board[y][x], end = "")
			if units_hp:
				print(" ", units_hp)
			else:
				print()
