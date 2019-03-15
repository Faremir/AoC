from collections import defaultdict


class Pot:
    def __init__(self):
        self.plant = False
        self.prev = None
        self.next = None


class Garden:
    def __init__(self, initial_stage, file = "input"):
        self.initial_stage = initial_stage
        self.first_Pot = Pot()
        self.generat_inital_stage(self.first_Pot, 0)
        self.progress_combinations = defaultdict(str)
        self.parse_progress(file)
        self.generations = 20

    def generat_inital_stage(self, current_pot, index):
        if self.initial_stage[index] == '#':
            current_pot.plant = True

        if index + 1 < len(self.initial_stage) - 1:
            current_pot.next = Pot()
            current_pot.next.prev = current_pot
            current_pot = current_pot.next
        if index + 1 <= len(self.initial_stage) - 1:
            self.generat_inital_stage(current_pot, index + 1)

    def parse_progress(self, file):
        with open(file) as progresses:
            for line in progresses.readlines():
                progress = line.split(" ")
                self.progress_combinations[progress[0]] = progress[2]
        progresses.close()

    def aging(self):
        for age in range(self.generations):
            for pot_index in range(2, len(self.initial_stage)-3):
                for progress in self.progress_combinations:





zero = "#.#####.#.#.####.####.#.#...#.......##..##.#.#.#.###..#.....#.####..#.#######.#....####.#....##....#"
garden = Garden(zero)
pot = garden.first_Pot
while pot:
    if pot.plant:
        print("#", end = "")
    else:
        print(".", end = "")
    pot = pot.next
print("\n")
for progress, result in garden.progress_combinations.items():
    print(progress, " => ", result)
