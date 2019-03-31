class Cart:
    def __init__(self, direct):
        self.direction = direct
        self.coords = [0, 0]
        self.alive = True
        self.turn_count = 0

    def move(self, next_path):
        if next_path == '+':
            self.turn()
        # move TODO
        pass

    def turn(self):
        # [left:0, straight:1,tight:2, left:3, straight:4, right:5]
        # [
        if self.turn_count == 0 or self.turn_count % 3 == 0:
            self.turn_left()
            pass
        elif self.turn_count % 3 == 1:
            # straight TODO
            pass
        elif self.turn_count % 3 == 2:
            # right TODO
            pass
        pass

    def turn_left(self):
        if self.direction == '<':
            self.direction = 'v'
        elif self.direction == 'v':
            self.direction = '>'
        elif self.direction == '>':
            self.direction = '^'
        elif self.direction == '^':
            self.direction = '<'


class Track:
    def __init__(self, file):
        self.track = [str(line) for line in open(file).read().split('\n')]
        self.carts = self.parse_carts()

    def parse_carts(self):
        x = 0
        y = 0
        cart_list = []
        for line in self.track:
            for path in line:
                if path == 'v' or path == '>' or path == '<' or path == '^':
                    cart = Cart(path)
                    cart.coords = [y, x]
                    cart_list += [cart]
                x += 1
            x = 0
            y += 1

        return cart_list


track = Track("input")
# for line in track.track:
# 	print(line)

for cart_ in track.carts:
    print(cart_.direction, " = [", cart_.coords[0], ",", cart_.coords[1], "]")
