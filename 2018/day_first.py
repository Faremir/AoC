def part_one(file):
    result = 0
    with open(file, "r") as input_file:
        for line in input_file.readlines():
        result += int(line)
    return result

def part_two():
    file = "day 1.txt"
    input_field = []
    result = 0
    results_list = [0]
    with open(file, "r") as input_file:
        for line in input_file.readlines():
            input_field.append(int(line))
    while True:
        for i in input_field:
            result += i
            if result in results_list:
                return result
            results_list.append(result)


