from collections import Counter


def count_combinations(file, part):
    with open(file, "r") as input_f:
        pass_range = list(map(int, input_f.read().split("-")))
        return sum(count_possible_passwords(pass_range, part))


def count_possible_passwords(pass_range, part):
    for possible_pass in range(pass_range[0], pass_range[1]):
        if part == "one":
            yield 1 if part_one_validation(possible_pass) else 0
        if part == "two":
            yield 1 if part_two_validation(possible_pass) else 0


def part_one_validation(value):
    char_count = any(count > 1 for count in iter(Counter(str(value)).values()))
    ascending = sorted(str(value)) == list(str(value))
    return True if char_count and ascending else False


def part_two_validation(value):
    char_count = 2 in Counter(str(value)).values()
    ascending = sorted(str(value)) == list(str(value))
    return True if char_count and ascending else False
