from collections import defaultdict


class Claim:
    def __init__(self, data):
        self.is_invalid = False
        self.id = ""
        self.left = 0
        self.top = 0
        self.width = 0
        self.height = 0
        self.__parse__(data)

    def __parse__(self, data):
        self.id, _, offset, dimension = data.split()
        (self.left, self.top) = [int(s) for s in offset[:-1].split(",")]
        (self.width, self.height) = [int(s) for s in dimension.split("x")]


class Claims:
    def __init__(self, file = "input"):
        self.list_of_claims = []
        self.__parse__(file)
        self.claimed_indexes = defaultdict(int)
        self.get_used_coords()

    def __parse__(self, file):
        with open(file, "r") as input_file:
            for line in input_file.readlines():
                claim = Claim(line)
                self.list_of_claims.append(claim)

    def get_used_coords(self):
        for claim in self.list_of_claims:
            for h in range(claim.height):
                for w in range(claim.width):
                    self.claimed_indexes[(h + claim.top, w + claim.left)] += 1

    def get_overlapping_area(self):
        intersection_area = 0
        for (x, y), used_times in self.claimed_indexes.items():
            if used_times >= 2:
                intersection_area += 1
        return intersection_area

    def get_not_overlapping(self):
        for claim in self.list_of_claims:
            for h in range(claim.height):
                for w in range(claim.width):
                    if self.claimed_indexes[(h + claim.top, w + claim.left)] > 1:
                        claim.is_invalid = True
                        break
                if claim.is_invalid:
                    break
            if not claim.is_invalid:
                return claim.id
