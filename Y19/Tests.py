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
    with open(file, "r") as input_file:
        memory = [int(val) for val in input_file.read().split(",")]
    yield D02.get_restored_noun(memory)
    noun, verb = D02.get_valid_noun_verb(memory, 19690720)
    yield 100 * noun + verb


def day_03(file = ""):
    """
    Test: Day 3
    """
    panel = D03.Panel()
    panel.parse_wires(file)
    yield panel.get_closest_intxn()
    yield panel.parse_steps_to_intxn()


def day_04(file = ""):
    """
    Test: Day 4
    """
    yield D04.count_combinations(file, "one")
    yield D04.count_combinations(file, "two")


def day_05(file = ""):
    """
    Test: Day 5
    """
    with open(file, "r") as input_file:
        memory = [int(val) for val in input_file.read().split(",")]
    yield D05.get_diagnostic_code(memory, [1, 2, 3, 4])
    yield D05.get_diagnostic_code(memory, [1, 2, 3, 4, 5, 6, 7, 8])


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


def day_25(file = ""):
    """
    Test: Day 25
    """
    # TODO
    part_one, part_two = "#TODO", "#TODO"
    return part_one, part_two


def testing(default, string_vars):
    print(('\u2554{horizontal_line}\u2557\n'
           '\u2551{spaces}2019{spaces}\u2551\n'
           '\u2560{horizontal_line}\u2563')
          .format(**string_vars,
                  spaces = " " * 14))
    for day_num in range(1, 26):
        day = str(day_num).zfill(2)
        # print(globals())
        function = globals()["day_" + day]
        stop = print_day(day, default, function)
        if day_num != 25 and not stop:
            print("\u2560{horizontal_line}\u2563".format(**string_vars))
        else:
            print("\u255A{horizontal_line}\u255D".format(**string_vars))
            break


def print_day(day, default, func):
    """
    Prints out formatted result of both parts of each day

    :param day: Day number
    :param default: Use default filesystem
    :param func:
    :return:
    """
    print("\u2551 \u2022 Day: {day}{spaces}\u2551"
          .format(day = day,
                  spaces = " " * 22))
    try:
        if default:
            file = "Y19/assignments/" + day + ".txt."
        else:
            file = input("Enter full path to file:")
        parts = ("one", "two")
        generator = map(print_part, func(file), parts)
        if "#TODO" in list(generator):
            return True
    except FileNotFoundError:
        print("\u2560{spaces}\u25E6 Input file not specified{spaces}\u2551"
              .format(spaces = " " * 3))


def print_part(result, num):
    """
    Prints out result of day part

    :param result: Result value
    :param num: part number: One | Two
    """
    part_string = " \t\u25E6 Part " + num + ": " + str(result)
    print("\u2551 " + part_string + " " * (31 - len(part_string)) + "\u2551")
    return result
