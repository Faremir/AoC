from Y18.fifteenth import *
from Y18.seventeenth import *
from Y18.sixteenth import *
from Y18.thirteenth import *
from Y18.twelfth import *


def day_1():
	"""

	"""
	part_one()
	part_two()
	pass


def day_2():
	"""

	"""
	pass


def day_3():
	"""

	"""
	pass


def day_4():
	"""

	"""
	pass


def day_5():
	"""

	"""
	pass


def day_6():
	"""

	"""
	day_sixth = Plane()
	day_sixth.get_finite_sizes()
	day_sixth.get_shared_size()
	day_sixth.print_grid()


def day_7():
	"""

	"""
	workers = 5
	graph = TaskManager(workers)

	time_to_complete = graph.process_tasks()
	print("Order: ")
	for task in graph.completed_tasks:
		print(task.marking, end = " ")
	print("\n\ttime: " + str(time_to_complete) + " seconds")


def day_8():
	"""

	"""
	root, _ = build_tree(data)
	print(sum_tree_metadata(root))
	print(sum_root_value(root))


def day_9():
	"""

	"""
	# noinspection PyUnusedLocal
	test_cases = {"10 players; last marble is worth 1618 points": "high score is 8317",
	              "13 players; last marble is worth 7999 points": "high score is 146373",
	              "17 players; last marble is worth 1104 points": "high score is 2764",
	              "21 players; last marble is worth 6111 points": "high score is 54718",
	              "30 players; last marble is worth 5807 points": "high score is 37305"}
	# noinspection PyUnusedLocal
	test_input = "405 players; last marble is worth 70953 points"


def day_10():
	"""

	"""
	pass


def day_11():
	"""

	"""
	grid = Grid(8141)
	print(grid.parse_grid())
	pass


def day_12():
	"""

	"""
	zero = "#.#####.#.#.####.####.#.#...#.......##..##.#.#.#.###..#.....#.####..#.#######.#....####.#....##....#"
	garden = Garden(zero, 20, False, "Y18/input")
	print("Part one: ", garden.aging())
	garden = Garden(zero, 50000000000, False, "Y18/input")
	print("Part two: ", garden.aging())


def day_13():
	track = Track("Y18/input")
	print(track.run_track())


def day_14():
	factory = ChocolateChart("880751")
	print(factory)


def day_15():
	# print("\nAfter 0 round:")

	game = Game()
	print(game.prevent_dead_elves())


def day_16():
	neco = InstructionsEffet('Y18\input')
	neco.run_instructions()
	print(neco)


def day_17():
	reservoir = Reservoir('Y18/input')
	reservoir.flow()



if __name__ == "__main__":
	# day_12()
	day_17()
