class Point:
    def __init__(self, x, y):
        self.x_pos = x
        self.y_pos = y
        self.velocity = (0, 0)

    def move_point(self):
        self.x_pos += self.velocity[0]
        self.y_pos += self.velocity[1]
