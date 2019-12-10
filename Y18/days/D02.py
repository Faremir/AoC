import itertools
from collections import Counter


class Box:
    """
    Box class containing information of single box
    """

    def __init__(self, box_id):
        self.id = box_id
        self.two_same_indexes = False
        self.three_same_indexes = False
        self.letter_count = self.parse_box_id(box_id)

    def parse_box_id(self, box_id):
        """
        Parsing box id into class

        :param box_id: Sting representing ID of box
        :return: dictionary containing Dict => {Letter: Count}
        """
        letter_count = Counter(box_id)
        for _, count in letter_count.items():
            if count == 2 and not self.two_same_indexes:
                self.two_same_indexes = True
            if count == 3 and not self.three_same_indexes:
                self.three_same_indexes = True
        return letter_count


class Boxes:
    """
    Class containing list of :py:class:`Box` objects
    """

    def __init__(self, file):
        self.box_list = []
        self.parse_boxes(file)

    def parse_boxes(self, file):
        """
        Parse boxes from input file

        :param file: Assignment input file
        """
        with open(file, "r") as input_file:
            for line in input_file.readlines():
                box = Box(line)
                self.box_list.append(box)

    def get_correct_hash(self):
        """
        Calculating hash of boxes by multiplying number of boxes containing two and three identical characters.

        :return: Checksum of boxes
        """
        doubled_chars = 0
        tripled_chars = 0
        for box in self.box_list:
            if box.two_same_indexes:
                doubled_chars += 1
            if box.three_same_indexes:
                tripled_chars += 1
        return doubled_chars * tripled_chars

    def get_correct_boxes(self):
        """
        Find two matching boxes with one character difference at same position.

        :return: Matching characters sequence of correct boxes
        """
        for box_A, box_B in itertools.combinations(self.box_list, 2):
            count_of_differences = 0
            index_of_letter = 0
            for i in range(len(box_A.id)):
                if box_A.id[i] != box_B.id[i]:
                    count_of_differences += 1
                    index_of_letter = i
            if count_of_differences == 1:
                return box_A.id[:index_of_letter] + box_A.id[(index_of_letter + 1):]
