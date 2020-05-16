from Y18.days import *


def day_01(file = ""):
    """
    Test: Day 1
    """
    yield D01.part_one(file)
    yield D01.part_two(file)


def day_02(file = ""):
    """
    Test: Day 2
    """
    boxes = D02.Boxes(file)
    yield boxes.get_correct_hash()
    yield boxes.get_correct_boxes()


def day_03(file = ""):
    """
    Test: Day 3
    """
    claims = D03.Claims(file)
    yield claims.get_overlapping_area()
    yield claims.get_not_overlapping()


def day_04(file = ""):
    """
    Test: Day 4
    """


def day_05(file = ""):
    """
    Test: Day 5
    """


def day_06(file = ""):
    """
    Test: Day 6
    """
    day_sixth = D06.Plane()
    day_sixth.get_finite_sizes()
    day_sixth.get_shared_size()
    day_sixth.print_grid()


def day_07(file = ""):
    """
    Test: Day 7
    """
    workers = 5
    graph = D07.TaskManager(workers)

    time_to_complete = graph.process_tasks()
    print("Order: ")
    for task in graph.completed_tasks:
        print(task.marking, end = " ")
    print("\n\ttime: " + str(time_to_complete) + " seconds")


def day_08(file = ""):
    """
    Test: Day 8
    """
    data = [int(data) for data in open(file).read().split(" ")]
    root, _ = D08.build_tree(data)
    print(D08.sum_tree_metadata(root))
    print(D08.sum_root_value(root))


def day_09(file = ""):
    """
    Test: Day 9
    """
    # noinspection PyUnusedLocal
    test_cases = {"10 players; last marble is worth 1618 points": "high score is 8317",
                  "13 players; last marble is worth 7999 points": "high score is 146373",
                  "17 players; last marble is worth 1104 points": "high score is 2764",
                  "21 players; last marble is worth 6111 points": "high score is 54718",
                  "30 players; last marble is worth 5807 points": "high score is 37305"}
    # noinspection PyUnusedLocal
    test_input = "405 players; last marble is worth 70953 points"


def day_10(file = ""):
    """
    Test: Day 10
    """
    pass


def day_11(file = ""):
    """
    Test: Day 11
    """
    grid = D11.Grid(8141)
    yield grid.parse_grid()


def day_12(file = ""):
    """
    Test: Day 12
    """
    zero = "#.#####.#.#.####.####.#.#...#.......##..##.#.#.#.###..#.....#.####..#.#######.#....####.#....##....#"
    garden = D12.Garden(zero, 20, False, "Y18/input")
    yield garden.aging()
    garden = D12.Garden(zero, 50000000000, False, "Y18/input")
    yield garden.aging()


def day_13(file = ""):
    """
    Test: Day 13
    """
    track = D13.Track("Y18/input")
    yield track.run_track()


def day_14(file = ""):
    """
    Test: Day 14
    """
    factory = D14.ChocolateChart("880751")
    yield factory.get_range()
    yield factory.get_recipes_count()


def day_15(file = ""):
    """
    Test: Day 15
    """
    # print("\nAfter 0 round:")
    game = D15.Game()
    print(game.prevent_dead_elves())


def day_16(file = ""):
    """
    Test: Day 16
    """
    neco = D16.InstructionsEffet('Y18\input')
    neco.run_instructions()
    print(neco)


def day_17(file = ""):
    """
    Test: Day 17
    """
    reservoir = D17.Reservoir('Y18/input')
    reservoir.flow()
    print(reservoir.calc_remaining_water())


def day_18(file = ""):
    """
    Test: Day 18
    """
    area = D18.Acres(50, "Y18/input")
    area.flow()
    print(area.result())


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
           '\u2551{spaces}2018{spaces}\u2551\n'
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
