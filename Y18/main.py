from Y18.day_seventh import *
from Y18.day_eighth import *


def day_seventh_testing(workers):
	"""

	@param workers:
	"""
	graph = TaskManager(workers)

	time_to_complete = graph.process_tasks()
	print("Order: ")
	for task in graph.completed_tasks:
		print(task.marking, end = " ")
	print("\n\ttime: " + str(time_to_complete) + " seconds")


def day_eight_testing():
	"""

	"""
	root, _ = build_tree(data)
	print(sum_tree_metadata(root))
	print(sum_root_value(root))


# noinspection PyPep8
def day_ninth_testing():
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


def day_seventh():
	"""

	"""
	day_seventh_testing(1)
	day_seventh_testing(5)


def day_eight():
	"""

	"""
	day_eight_testing()
