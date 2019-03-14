from collections import defaultdict


class Marble:
    def __init__(self, score):
        self.value = score
        self.prev = None
        self.next = None


class Game:
    """Trida Game reprezentuje probíhající hru.

    Atributy:
        first   reference na prvni prvek seznamu
    """

    def __init__(self, file):
        self.players = defaultdict(int)
        players_count, _, _, _, _, _, turns, _ = [int(data) for data in open(file).read().split(" ")]
        self.marble_value = 0
        self.current_player = 0
        self.players_count = players_count
        self.last_marble_value = turns

    def turn(self):
        self.marble_value += 1
        self.current_player += 1
        if self.current_player > self.players_count:
            self.current_player = 1

    def add_score(self, score):
        self.players[self.current_player] += score

    def new_marble(self, current):
        new = Marble(self.marble_value)
        last = current.next.next
        middle = current.next
        middle.next = new
        last.prev = new
        new.prev = middle
        new.next = last
        return new

    @staticmethod
    def remove_marble(current):
        prev = current.prev
        nextt = current.next
        prev.next = nextt
        nextt.prev = prev
        return nextt

    @staticmethod
    def skip_marble(current):
        for _ in range(7):
            current = current.prev
        return current

    @staticmethod
    def init_first_marble():
        current = Marble(0)
        current.next = current
        current.prev = current
        return current

    def start_game(self):
        current = self.init_first_marble()
        while self.marble_value <= self.last_marble_value:
            self.turn()
            if self.marble_value % 23 == 0:
                self.add_score(self.marble_value)
                current = self.remove_marble(current)
            else:
                current = self.skip_marble(current)
                self.add_score(current.value)
                current = self.new_marble(current)

    def game_score(self):
        maximum = 0
        for key, player in self.players.items():
            if maximum < player:
                maximum = player
        return maximum
