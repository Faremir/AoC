import itertools
from collections import Counter


class Product:
    def __init__(self):
        self.id = ""
        self.letter_count = {}
        self.two_same_indexes = False
        self.three_same_indexes = False

    def parse_letters(self):
        self.letter_count = Counter(self.id)
        for _, count in self.letter_count.items():
            if count == 2 and not self.two_same_indexes:
                self.two_same_indexes = True
            if count == 3 and not self.three_same_indexes:
                self.three_same_indexes = True


class Products:
    def __init__(self):
        self.product_list = []
        self.file = "day 2.txt"
        self.parse_products()

    def parse_products(self):
        with open(self.file, "r") as input_file:
            for line in input_file.readlines():
                product = Product()
                product.id = line
                self.product_list.append(product)

    def get_correct_products(self):
        for product_A, product_B in itertools.combinations(self.product_list, 2):
            count_of_differences = 0
            index_of_letter = 0
            for i in range(len(product_A.id)):
                if product_A.id[i] != product_B.id[i]:
                    count_of_differences += 1
                    index_of_letter = i
            if count_of_differences == 1:
                return product_A.id[:index_of_letter] + product_A.id[(index_of_letter + 1):]

    def get_correct_hash(self):
        doubled_chars = 0
        tripled_chars = 0
        for product in self.product_list:
            product.parse_letters()
            if product.two_same_indexes:
                doubled_chars += 1
            if product.three_same_indexes:
                tripled_chars += 1
        return doubled_chars * tripled_chars


x = Products()
print(x.get_correct_products())
print(x.get_correct_hash())
