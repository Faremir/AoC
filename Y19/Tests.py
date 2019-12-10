from Y19.days import *


def day_01(file = ""):
    """
    Test: Day 2
    """
    part_one = D01.get_fuel_requirment(file)
    part_two = D01.get_fuel_req_rec_nolist(file)
    return part_one, part_two


def day_02(file = ""):
    """
    Test: Day 2
    """
    processor = D02.Computer()
    processor.parse_memory(file)
    part_one = processor.get_restored_noun()
    noun, verb = processor.get_valid_noun_verb(19690720)
    part_two = 100 * noun + verb
    return part_one, part_two


def day_03(file = ""):
    """
    Test: Day 3
    """
    panel = D03.Panel()
    panel.parse_wires(file)
    part_one = panel.get_closest_intxn()
    # print()
    part_two = panel.parse_steps_to_intxn()
    return part_one, part_two


def day_04(file = ""):
    """
    Test: Day 4
    """
    # TODO
    part_one = D04.count_combinations(file, "one")
    part_two = D04.count_combinations(file, "two")
    return part_one, part_two


def day_05(file = ""):
    """
    Test: Day 5
    """
    # TODO
    part_one, part_two = "#TODO", "#TODO"
    return part_one, part_two


def day_06(file = ""):
    """
    Test: Day 6
    """
    # TODO
    part_one, part_two = "#TODO", "#TODO"
    return part_one, part_two


def day_07(file = ""):
    """
    Test: Day 7
    """
    # TODO
    part_one, part_two = "#TODO", "#TODO"
    return part_one, part_two


def day_08(file = ""):
    """
    Test: Day 8
    """
    # TODO
    part_one, part_two = "#TODO", "#TODO"
    return part_one, part_two


def day_09(file = ""):
    """
    Test: Day 9
    """
    # TODO
    part_one, part_two = "#TODO", "#TODO"
    return part_one, part_two


def day_10(file = ""):
    """
    Test: Day 10
    """
    # TODO
    part_one, part_two = "#TODO", "#TODO"
    return part_one, part_two


def day_11(file = ""):
    """
    Test: Day 11
    """
    # TODO
    part_one, part_two = "#TODO", "#TODO"
    return part_one, part_two


def day_12(file = ""):
    """
    Test: Day 12
    """
    # TODO
    part_one, part_two = "#TODO", "#TODO"
    return part_one, part_two


def day_13(file = ""):
    """
    Test: Day 13
    """
    # TODO
    part_one, part_two = "#TODO", "#TODO"
    return part_one, part_two


def day_14(file = ""):
    """
    Test: Day 14
    """
    # TODO
    part_one, part_two = "#TODO", "#TODO"
    return part_one, part_two


def day_15(file = ""):
    """
    Test: Day 15
    """
    # TODO
    part_one, part_two = "#TODO", "#TODO"
    return part_one, part_two


def day_16(file = ""):
    """
    Test: Day 16
    """
    # TODO
    part_one, part_two = "#TODO", "#TODO"
    return part_one, part_two


def day_17(file = ""):
    """
    Test: Day 17
    """
    # TODO
    part_one, part_two = "#TODO", "#TODO"
    return part_one, part_two


def day_18(file = ""):
    """
    Test: Day 18
    """
    # TODO
    part_one, part_two = "#TODO", "#TODO"
    return part_one, part_two


def day_19(file = ""):
    """
    Test: Day 19
    """
    # TODO
    part_one, part_two = "#TODO", "#TODO"
    return part_one, part_two


def day_20(file = ""):
    """
    Test: Day 20
    """
    # TODO
    part_one, part_two = "#TODO", "#TODO"
    return part_one, part_two


def day_21(file = ""):
    """
    Test: Day 21
    """
    # TODO
    part_one, part_two = "#TODO", "#TODO"
    return part_one, part_two


def day_22(file = ""):
    """
    Test: Day 22
    """
    # TODO
    part_one, part_two = "#TODO", "#TODO"
    return part_one, part_two


def day_23(file = ""):
    """
    Test: Day 23
    """
    # TODO
    part_one, part_two = "#TODO", "#TODO"
    return part_one, part_two


def day_24(file = ""):
    """
    Test: Day 24
    """
    # TODO
    part_one, part_two = "#TODO", "#TODO"
    return part_one, part_two


def testing(default):
    print("\u2560" + "\u2550" * 13 + " 2019 " + "\u2550" * 13 + "\u2551")
    days = {"01": day_01, "02": day_02, "03": day_03, "04": day_04, "05": day_05, "06": day_06, "07": day_07, "08": day_08, "09": day_09, "10": day_10, "11": day_11, "12": day_12, "13": day_13, "14": day_14, "15": day_15, "16": day_16, "17": day_17, "18": day_18, "19": day_19, "20": day_20, "21": day_21, "22": day_22, "23": day_23, "24": day_24}
    for day, func in days.items():
        print_day(day, default, func)


def print_day(day, default, func):
    """
    Prints out formatted result of both parts of each day

    :param day: Day number
    :param default: Use default filesystem
    :param func:
    :return:
    """
    print("\u2551 \u2022 Day: " + day + " " * 22 + "\u2551")
    try:
        if default:
            file = "Y19/assignments/" + day + ".txt."
        else:
            file = input("Enter full path to file:")
        list(map(print_part, func(file), ("one", "two")))
    except FileNotFoundError:
        print("\u2560   \u25E6 " + "Input file not specified" + "   \u2551")
    print("\u2560" + ("\u2550" * 32) + "\u2551")


def print_part(result, num):
    """
    Prints out result of day part

    :param result: Result value
    :param num: part number: One | Two
    """
    part_string = " \t\u25E6 Part " + num + ": " + str(result)
    print("\u2551 " + part_string + " " * (31 - len(part_string)) + "\u2551")
