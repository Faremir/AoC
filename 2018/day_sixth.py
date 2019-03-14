
class Area:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_finite = True
        self.size = 0


class Grid:
    def __init__(self, file = "input", distance = 10000):
        self.Areas = []
        self.__parser__(file)
        self.bottom = max(area.y for area in self.Areas)
        self.right = max(area.x for area in self.Areas)
        self.size_shared_region = 0
        self.manhatan_dist = distance

    def __parser__(self, file):
        with open(file, "r") as input_file:
            for line in input_file.readlines():
                x, y = (int(x) for x in line.split(", "))
                self.Areas.append(Area(x, y))

    def get_finite_sizes(self):
        for y in range(self.bottom):
            for x in range(self.right):
                infinite_area = None
                closest_distance = 1000
                for area in self.Areas:
                    if abs(abs(area.x - x) + abs(area.y - y)) < closest_distance:
                        closest_distance = abs(abs(area.x - x) + abs(area.y - y))
                        infinite_area = area
                    elif abs(abs(area.x - x) + abs(area.y - y)) == closest_distance:
                        infinite_area = None
                if infinite_area:
                    infinite_area.size += 1
                    if y == 0 or x == 0 or x == self.right or y == self.bottom:
                        infinite_area.is_finite = False

    def get_shared_size(self):

        for y in range(self.bottom + 1):
            for x in range(self.right + 1):
                self.size_shared_region += int(sum(abs(area.x - x) + abs(area.y - y) for area in self.Areas) < self.manhatan_dist)

    def print_grid(self):

        print(max(area.size for area in self.Areas if area.is_finite))
        print(self.size_shared_region)


day_sixth = Grid()
day_sixth.get_finite_sizes()
day_sixth.get_shared_size()
day_sixth.print_grid()
