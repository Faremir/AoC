from collections import defaultdict


class Garden:
    def __init__(self, initial_stage, generations = 20, file = "input"):
        self.initial_stage = [i for i in initial_stage]
        self.progress_combinations = defaultdict(str)
        self.parse_progress(file)
        self.generations = generations

    def parse_progress(self, file):
        with open(file) as progresses:
            for line in progresses.readlines():
                progress = line.split(" ")
                self.progress_combinations[progress[0]] = progress[2]
        progresses.close()

    def check_next_generation(self, pot_index, current_generation):

        return '-'

    def aging(self):
        result = 0
        current_generation = self.initial_stage
        print(''.join(current_generation))
        for age in range(1, self.generations + 1):
            new_gen = [i for i in current_generation]
            for pot_index in range(2, len(current_generation) - 3):

                new_gen[pot_index] = '.'
                for progress, new_plant in self.progress_combinations.items():
                    match_count = 0
                    for progress_range in range(-2, 3):
                        check_index = pot_index + progress_range
                        progress_index = progress_range + 2
                        if progress[progress_index] == current_generation[check_index]:
                            match_count += 1
                        elif progress[progress_index] != current_generation[check_index]:
                            break

                        if match_count == 5:
                            #print(progress, progress[progress_index], current_generation[check_index], progress_index, check_index, end = " ")
                            pass
                    if match_count == 5:
                        #print(current_generation[pot_index], result[0])
                        new_gen[pot_index] = new_plant[0]
            current_generation = new_gen

        for index in range(len(current_generation)-1):
            if current_generation[index] == '#':
                result += index-5
        return result


zero = "#.#####.#.#.####.####.#.#...#.......##..##.#.#.#.###..#.....#.####..#.#######.#....####.#....##....#"
test = "#..#.#..##......###...###"
initial = "....." + zero + "..................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................."
garden = Garden(initial, 50000000000)
next_gen = garden.aging()
print(next_gen)
