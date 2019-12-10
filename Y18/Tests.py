from Y18.days import *


def day_01(file = ""):
    """
    Test: Day 1
    """
    print(D01.part_one(file))
    print(D01.part_two(file))


def day_02(file = ""):
    """
    Test: Day 2
    """
    boxes = D02.Boxes(file)
    checksum = boxes.get_correct_hash()
    print(checksum)
    difference = boxes.get_correct_boxes()
    print(difference)


def day_03(file = ""):
    """
    Test: Day 3
    """
    claims = D03.Claims(file)
    print(claims.get_overlapping_area())
    print(claims.get_not_overlapping())


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
    print(grid.parse_grid())


def day_12(file = ""):
    """
    Test: Day 12
    """
    zero = "#.#####.#.#.####.####.#.#...#.......##..##.#.#.#.###..#.....#.####..#.#######.#....####.#....##....#"
    garden = D12.Garden(zero, 20, False, "Y18/input")
    print("Part one: ", garden.aging())
    garden = D12.Garden(zero, 50000000000, False, "Y18/input")
    print("Part two: ", garden.aging())


def day_13(file = ""):
    """
    Test: Day 13
    """
    track = D13.Track("Y18/input")
    print(track.run_track())


def day_14(file = ""):
    """
    Test: Day 14
    """
    factory = D14.ChocolateChart("880751")
    print(factory)


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


pass


def day_19(file = ""):
    """
    Test: Day 19
    """
    pass


def day_20(file = ""):
    """
    Test: Day 20
    """
    pass


def day_21(file = ""):
    """
    Test: Day 21
    """
    pass


def day_22(file = ""):
    """
    Test: Day 22
    """
    pass


def day_23(file = ""):
    """
    Test: Day 23
    """
    pass


def day_24(file = ""):
    """
    Test: Day 24
    """
    pass



def testing(default, default_format = ".txt", file = ""):
    print("\u2560" + "\u2550" * 13 + " 2018 " + "\u2550" * 13 + "\u2551")

    days = {"01": day_01, "02": day_02, "03": day_03, "04": day_04, "05": day_05, "06": day_06, "07": day_07, "08": day_08, "09": day_09, "10": day_10, "11": day_11, "12": day_12, "13": day_13, "14": day_14, "15": day_15, "16": day_16, "17": day_17, "18": day_18, "19": day_19, "20": day_20, "21": day_21, "22": day_22, "23": day_23, "24": day_24}
    for day, func in days.items():
        print_day(day, default, func)


def print_day(day, default, func):
    """
    Prints out formatted result of both parts of each day :py:func:`day_01`

    :param day: Day number
    :param default: Use default filesystem
    :param func:
    :return:
    """
    print("\u2551 \u2022 Day: " + day + " " * 22 + "\u2551")
    try:
        if default:
            file = "Y18/assignments/" + day + ".txt."
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
