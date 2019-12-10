def part_one(file) -> int:
    """
    Calculating the resulting frequency after all of the changes in frequency have been applied.

    :returns: Resulting frequency
    """
    frequency = 0
    with open(file, "r") as input_file:
        for fr_change in input_file.readlines():
            frequency += int(fr_change)
    return frequency


def part_two(file):
    """
    Circulates list of changes in frequency until one frequency is reached twice.

    :param file: Assignment input file
    :return: First frequency value reached
    """
    with open(file, "r") as input_file:
        frequency_changes = [int(fr_change) for fr_change in input_file.readlines()]
    reached_frequency = []
    frequency = 0
    while True:
        for fr_change in frequency_changes:
            frequency += fr_change
            if frequency in reached_frequency:
                return frequency
            reached_frequency.append(frequency)
