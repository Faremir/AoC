from scripts import script_base


class Y22D02(script_base.ScriptBase):
    def __init__(self, gui):
        super().__init__(gui)
        self.has_input = True

    def compute(self):
        rounds = self.input_data.splitlines()

        part_1_data = {
            'HANDS': {
                'X': 1,  # ROCK
                'Y': 2,  # PAPER
                'Z': 3,  # SCISSORS
            },
            'RESULTS': {
                ('A', 'X'): 3,  # DRAW
                ('A', 'Y'): 6,  # WIN
                ('A', 'Z'): 0,  # LOSE
                ('B', 'X'): 0,  # LOSE
                ('B', 'Y'): 3,  # DRAW
                ('B', 'Z'): 6,  # WIN
                ('C', 'X'): 6,  # WIN
                ('C', 'Y'): 0,  # LOSE
                ('C', 'Z'): 3,  # DRAW
            },
        }

        part_2_data = {
            'RESULTS': {
                'X': 0,  # LOOSE
                'Y': 3,  # DRAW
                'Z': 6,  # WIN
            },
            'HANDS': {
                ('A', 'X'): 3,  # SCISSORS
                ('A', 'Y'): 1,  # ROCK
                ('A', 'Z'): 2,  # PAPER
                ('B', 'X'): 1,  # ROCK
                ('B', 'Y'): 2,  # PAPER
                ('B', 'Z'): 3,  # SCISSORS
                ('C', 'X'): 2,  # PAPER
                ('C', 'Y'): 3,  # SCISSORS
                ('C', 'Z'): 1,  # ROCK
            },
        }

        def get_round_p1(game_round):
            player_1, player_2 = game_round.split(" ")
            hand_score = part_1_data['HANDS'][player_2]
            round_score = part_1_data['RESULTS'][(player_1, player_2)]
            return hand_score + round_score

        def get_round_p2(game_round):
            player_1, result = game_round.split(" ")
            round_score = part_2_data['RESULTS'][result]
            hand_score = part_2_data['HANDS'][(player_1, result)]
            return hand_score + round_score

        part_1 = sum(get_round_p1(r) for r in rounds)
        part_2 = sum(get_round_p2(r) for r in rounds)
        self.result = f"Part 1: {str(part_1)} | Part 2 {str(part_2)}"
