class Data:
	def __init__(self):
		self.data = [int(data) for data in open("day8").read().split(" ")]


class Tree:
	def __init__(self, child_count = 0, meta_count = 0):
		self.child_count = child_count
		self.meta_count = meta_count
		self.children = []
		self.metadata = []

	def add_child(self, child):
		self.children.append(child)

	def get_child(self):
		return self.children

	def add_meta(self, meta):
		self.metadata += meta

	def get_meta(self):
		return self.metadata


def build_tree(data):
	child_count = data[0]
	meta_count = data[1]
	root = Tree(child_count, meta_count)
	for _ in range(child_count):
		child, data_without_root = build_tree(data[2:])
		root.add_child(child)
		data = data[:2] + data_without_root
	root.add_meta(data[2:meta_count + 2])
	data = data[(meta_count + 2):]

	return root, data


def sum_tree_metadata(root):
	metadata_sum = sum(root.metadata)
	for child in root.children:
		metadata_sum += sum_tree_metadata(child)
	return metadata_sum


def sum_root_value(root):
	metadata_sum = 0
	if root.child_count == 0:
		return sum(root.metadata)

	for child_index in root.metadata:
		if child_index <= root.child_count:
			metadata_sum += sum_root_value(root.children[child_index - 1])
	return metadata_sum
