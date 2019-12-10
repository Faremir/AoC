from collections import defaultdict


class Claim:
    """
    Claim class containing information of single claim
    """

    def __init__(self, data):
        self.is_invalid = False
        self.id, _, offset, dimension = data.split()
        (self.left, self.top) = [int(s) for s in offset[:-1].split(",")]
        (self.width, self.height) = [int(s) for s in dimension.split("x")]

    def __str__(self):
        return str(self.id) + "("+ str(self.width) + "x" + str(self.height)+") : [" + str(self.left) + ";" + str(self.top) + "]"


class Claims:
    """
    Object containing all objects :py:class:`Claim`
    """

    def __init__(self, file):
        with open(file, "r") as input_file:
            self.list_of_claims = [Claim(claim_info) for claim_info in input_file.readlines()]
        self.claimed_indexes = defaultdict(int)
        for claim in self.list_of_claims:
            for h in range(claim.height):
                for w in range(claim.width):
                    self.claimed_indexes[(h + claim.top, w + claim.left)] += 1

    def get_overlapping_area(self):
        """
        Count square inches which are within two or more claims

        :rtype: int
        :return: number of square inches of overlapping area
        """
        intersection_area = 0
        for _, used_times in self.claimed_indexes.items():
            if used_times >= 2:
                intersection_area += 1
        return intersection_area

    def get_not_overlapping(self):

        """
        Get :py:class:`Claim` object which area doesn't overlap with any of others Claims.

        :rtype: :py:class:`Claim`
        :returns: Claim object
        """
        for claim in self.list_of_claims:
            for h in range(claim.height):
                for w in range(claim.width):
                    if self.claimed_indexes[(h + claim.top, w + claim.left)] > 1:
                        claim.is_invalid = True
                        break
                if claim.is_invalid:
                    break
            if not claim.is_invalid:
                return claim
