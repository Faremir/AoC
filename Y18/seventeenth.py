import math
import re
import sys
from itertools import chain

sys.setrecursionlimit(3000)


class Reservoir:
	def __init__(self, file = "input"):
		self.clay = []
		self.spring = (0, 500)
		self.flowing_water = []
		self.resting_water = []
		self.current_nodes = [self.under(self.spring)]
		self.min_y, self.min_x = [math.inf] * 2
		self.max_y, self.max_x = [-math.inf] * 2
		self.parse_resrevoir(file)

	def parse_resrevoir(self, file):
		with open(file) as in_file:
			index = 0
			for line in in_file.read().split('\n'):
				first_coord_axis = line[0]
				_, first_coord, _, second_coord_s, second_coord_e = re.split("[=,. ]+", line)

				for n in range(int(second_coord_s), int(second_coord_e) + 1):
					if first_coord_axis == 'x':
						clay = (int(n), int(first_coord))
					else:
						clay = (int(first_coord), int(n))

					self.get_min_max(clay)
					self.clay.append(clay)
					index += 1
		in_file.close()

	def get_min_max(self, clay):
		self.min_y = clay[0] if clay[0] < self.min_y else self.min_y
		self.max_y = clay[0] if clay[0] > self.max_y else self.max_y
		self.min_x = clay[1] if clay[1] < self.min_x else self.min_x
		self.max_x = clay[1] if clay[1] > self.max_x else self.max_x

	def side_nbrs(self, coords):
		y, x = coords
		return [(y, x - 1), (y, x + 1)]

	def under(self, coords):
		y, x = coords
		return y + 1, x

	def over(self, coords):
		y, x = coords
		return y - 1, x

	def update_waters(self, new_resting_water):
		self.resting_water.extend(new_resting_water)
		for rest_water in new_resting_water:
			if rest_water in self.flowing_water:
				self.flowing_water.remove(rest_water)

	def check_nbrs(self, node, new_resting_water, should_rest = 0):
		under = self.under(node)
		if node in self.clay:
			should_rest += 1
			if should_rest == 2:
				return should_rest
		if node not in chain(self.clay, new_resting_water) and under in chain(self.clay, self.resting_water):
			# print("\t\t\t", node)
			new_resting_water.append(node)
			for nbr in self.side_nbrs(node):
				if nbr not in new_resting_water:
					should_rest = self.check_nbrs(nbr, new_resting_water, should_rest)
		if under not in chain(self.clay, self.resting_water):
			# print("\t\t\tNew_origin:", node)
			self.current_nodes.append(node)
		return should_rest

	def flow_to_sides(self, node):
		new_resting_water = []
		# print("\n\t\tSide nodes:")
		closure = self.check_nbrs(node, new_resting_water)
		if closure == 2:
			self.update_waters(new_resting_water)
			self.current_nodes.append(self.over(new_resting_water[0]))
		else:
			self.flowing_water = list(set(self.flowing_water + new_resting_water))
		# print("\t\tPop:", self.current_nodes[0])
		self.current_nodes.pop(0)

	# print("\t\tNew origins:", self.current_nodes)

	def flow_down(self, node):
		if self.under(node) not in chain(self.clay, self.resting_water):
			if node not in self.flowing_water:
				self.flowing_water.append(node)
			return True
		return False

	def water_drop(self, current_node):
		# print(current_node, end = "; ")
		if current_node[0] > self.max_y:
			return True
		if current_node[0] <= self.max_y:
			if self.flow_down(current_node):
				return self.water_drop(self.under(current_node))
			else:
				self.flow_to_sides(current_node)
		return False

	def remove_duplicates(self):
		if len(self.current_nodes) >= 2:
			self.current_nodes = list(dict.fromkeys(self.current_nodes))

	def flow(self):
		while self.current_nodes:
			self.remove_duplicates()
			for current_node in self.current_nodes[:]:
				at_bottom = self.water_drop(current_node)
				if at_bottom:
					self.current_nodes.remove(current_node)
		self.calc_remaining_water()

	def calc_remaining_water(self):
		all_water = list(set(self.resting_water + self.flowing_water))
		index = 0
		while index < len(all_water):
			if all_water[index][0] < self.min_y:
				all_water.pop(index)
			else:
				index += 1
		resting_water = list(set(self.resting_water))
		return len(all_water), len(resting_water)
