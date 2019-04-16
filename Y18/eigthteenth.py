class Acres:
	def __init__(self, file):
		self.area = []
		self.parse_area(file)

	def parse_area(self, file):
		self.area = [list(line) for line in open(file).read().split('\n')]
