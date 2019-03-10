import string


class Polymer:
    def __init__(self):
        self.hash = open("day 5.txt").read().strip()

    @staticmethod
    def truncate_hash(hash):
        new_string = ""
        i = 0
        hash2 = hash.swapcase()
        while i < len(hash) - 1:
            if hash[i] == hash2[i + 1]:
                i += 1
            elif new_string.endswith(hash2[i]):
                new_string = new_string[:-1]
            else:
                new_string += hash[i]
            i += 1
        return len(new_string)

    def get_most_reactant_char(self):
        alphabet = string.ascii_lowercase
        shortest_solved_hash = float('inf')
        for char in alphabet:
            shorted_hash = self.hash.replace(char, "").replace(char.upper(), "")
            length = self.truncate_hash(shorted_hash)
            if length < shortest_solved_hash:
                shortest_solved_hash = length
        return shortest_solved_hash


day_fifth = Polymer()
part_one = day_fifth.truncate_hash(day_fifth.hash)
part_two = day_fifth.get_most_reactant_char()
print(part_one, part_two)
# print(day_fifth.most_reactant_char + ": ", day_fifth.shortest_solved_hash)
