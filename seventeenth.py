class Node:
	def __init__(self, coords, mark):
		self.coords = coords
		self.mark = mark


class Water(Node):
	def __init__(self, coords, mark):
		Node.__init__(self, coords, mark)

	class Flowing(Node):
		def __init__(self, coords):
			Node.__init__(self, coords, "|")

	class Resting(Node):
		def __init__(self, coords):
			Node.__init__(self, coords, "~")

	class Spring(Node):
		def __init__(self, coords):
			Node.__init__(self, coords, "+")


class Sand(Node):
	def __init__(self, coords):
		Node.__init__(self, coords, ".")


class Clay(Node):
	def __init__(self, coords):
		Node.__init__(self, coords, "#")
