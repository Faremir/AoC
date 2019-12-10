import math


def get_fuel_requirment(file) -> int:
    """
    Calculating the fuel requirement based on weight of multiple modules.

    :returns: Resulting sum
    """
    with open(file, "r") as input_file:
        requirments = [int(weight) // 3 - 2 for weight in input_file.readlines()]
    return sum(requirments)


def _module_req_mass_list_(weight_list):
    if not weight_list:
        return 0
    fuel_list = []
    for weight in weight_list:
        fuel_req = weight // 3 - 2
        if fuel_req > 0:
            fuel_list.append(fuel_req)
    return sum(fuel_list) + _module_req_mass_list_(fuel_list)


def _module_req_mass_nolist_(mass):
    weight = (mass // 3) - 2
    if weight <= 0:
        return 0
    return weight + _module_req_mass_nolist_(weight)


def get_fuel_req_rec_nolist(file):
    """
    Calculating the fuel requirement based on weight of multiple modules.
    List parsing

    :returns: Resulting sum
    """
    with open(file, "r") as input_file:
        sum = 0
        for weight in input_file.readlines():
            sum += _module_req_mass_nolist_(int(weight))
    return sum


def get_fuel_req_recursive_list(file) -> int:
    """
    Calculating the fuel requirement based on weight of multiple modules.
    List parsing

    :returns: Resulting sum
    """
    with open(file, "r") as input_file:
        requirments = [int(weight) for weight in input_file.readlines()]

    return _module_req_mass_list_(requirments)
