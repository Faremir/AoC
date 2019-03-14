from collections import defaultdict


class Guard:
    def __init__(self, id):
        self.total_sleep_time = 0
        self.most_frequent_minute = 0
        self.minute_frequency = 0
        self.id = id

    def __repr__(self):
        return "#" + str(self.id) + " slept time:  " + str(self.total_sleep_time) + " \n\tmost frequented minut:  " + str(self.most_frequent_minute) + ":\n\t\t" + str(self.minute_frequency) + " minutes\n"


class Watch:
    def __init__(self, file = "input"):
        self.guard_dict = defaultdict(list)
        self.__parse__(file)
        self.guards_list = []

    def __parse__(self, file):
        input_list = []
        with open(file, "r") as input_file:
            for line in input_file.readlines():
                date, time, action = line[:-1].split(" ", 2)
                date, time = date[1:], time[:-1]
                input_list.append([(date, time), action])
        input_list.sort(key = lambda x: x[0])

        guard_id = ""
        sleep_time = []
        for (date, time), action in input_list:
            _, minutes = time.split(":")
            if "Guard" in action:
                guard_id = action[:-13]
            elif "falls" in action:
                sleep_time.append(int(minutes))
            else:
                sleep_time.append(int(minutes))
                self.guard_dict[guard_id].append(sleep_time)
                sleep_time = []

    def parse_guards(self):
        for guard, timestamps in self.guard_dict.items():
            most_frequented_sleep_time = defaultdict(int)
            new_guard_object = Guard(int(guard[7:]))
            minute = 0
            most = float('-inf')
            frequency = 0
            for (start, end) in timestamps:
                new_guard_object.total_sleep_time += (end - start)
                for i in range(start, end + 1):
                    most_frequented_sleep_time[i] += 1
                    if most_frequented_sleep_time[i] > most:
                        most = most_frequented_sleep_time[i]
                        minute = i
                        frequency = most
            new_guard_object.most_frequent_minute = minute
            new_guard_object.minute_frequency = frequency
            self.guards_list.append(new_guard_object)

    def comparator(self, comparator = None):
        maximum = float('-inf')
        guard = None
        for item in self.guards_list:
            comparable = item.total_sleep_time
            if comparator == "minute_frequency":
                comparable = item.minute_frequency
            if comparable > maximum:
                maximum = comparable
                guard = item
            print(item)

        return guard.most_frequent_minute * guard.id
