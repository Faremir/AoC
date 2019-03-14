from collections import defaultdict
import re


class Point:
    def __init__(self, x, y, shift_x, shift_y):
        self.x_pos = x
        self.y_pos = y
        self.velocity = [shift_x, shift_y]

    def move_point(self):
        self.x_pos += self.velocity[0]
        self.y_pos += self.velocity[1]


class Plane:
    def __init__(self, file):
        self.points = []
        self.parse_input(file)

    @staticmethod
    def parse_point(line):
        _, point, _, velocity, _ = re.split(r"<|>", line)
        x, y = [int(n) for n in point.split(", ")]
        shift_x, shift_y = [int(n) for n in velocity.split(", ")]
        return x, y, shift_x, shift_y

    def parse_input(self, file):
        with open(file) as inputF:
            for line in inputF.readlines():
                x, y, shift_x, shift_y = self.parse_point(line)
                self.points.append(Point(x, y, shift_x, shift_y))

    def get_min_max(self, attribute):
        minimum = min(self.points, key = lambda point: getattr(point, attribute))
        maximum = max(self.points, key = lambda point: getattr(point, attribute))
        return getattr(minimum, attribute), getattr(maximum, attribute)

    def print_plane(self):
        y_min, y_max = self.get_min_max("y_pos")
        x_min, x_max = plane.get_min_max("x_pos")
        for height in range(y_min-1, y_max+1):
            for width in range(x_min-1, x_max+1):
                if any((point.y_pos == height and point.x_pos == width) for point in self.points):
                    print("#", end = "")
                else:
                    print(".", end = "")

            print("\n")

    def aging(self):
        time = 0
        min_diff = float("inf")
        while True:
            time += 1
            for point in self.points:
                point.x_pos += point.velocity[0]
                point.y_pos += point.velocity[1]
            y_min, y_max = self.get_min_max("y_pos")
            if y_max - y_min < min_diff:
                min_diff = y_max - y_min
            else:
                for point in self.points:
                    point.x_pos -= point.velocity[0]
                    point.y_pos -= point.velocity[1]
                self.print_plane()
                return time-1



