import string
from collections import defaultdict


class Worker:
    def __init__(self):
        self.currently_working = False


class Task:
    def __init__(self):
        self.marking = ""
        self.prerequisites = []
        self.time_needed = 0
        self.time_worked = 0
        self.working_on = False
        self.worker = None
        self.is_completed = False


class TaskManager:
    def __init__(self, count_of_workers = 1, file = "input"):
        self.tasks = self.__parse__(file)
        self.workers = [Worker() for _ in range(count_of_workers)]
        self.completed_tasks = []

    def create_tasks(self, marking, tasks):
        tasks[marking].marking = marking
        tasks[marking].time_needed = string.ascii_uppercase.index(marking) + 61

    def __parse__(self, file):
        tasks = defaultdict(Task)
        with open(file) as input_file:
            for line in input_file.readlines():
                nodes = line.split(" ")
                self.create_tasks(nodes[7], tasks)
                self.create_tasks(nodes[1], tasks)
                tasks[nodes[7]].prerequisites.append(tasks[nodes[1]])
        tasks = sorted(tasks.items())
        return [task[1] for task in tasks]

    def is_dequeued(self, needed_to_process):
        return True if [x for x in needed_to_process if x not in self.completed_tasks] else False

    def process_opened_tasks(self, task):
        worker = next((wr for wr in self.workers if not wr.currently_working), None)
        if not self.is_dequeued(task.prerequisites) and worker:
            worker.currently_working = True
            task.working_on = True
            task.worker = worker
            task.time_worked = 1

    def set_task_completion(self):
        for task in self.tasks:
            if task.time_worked == task.time_needed:
                task.working_on = False
                task.is_completed = True
                self.completed_tasks.append(task)
                task.worker.currently_working = False
                self.tasks.remove(task)

    def process_tasks(self):
        time_to_complete = 0
        original_length = len(self.tasks)
        while len(self.completed_tasks) != original_length:
            for task in self.tasks:
                if task.working_on:
                    task.time_worked += 1
                else:
                    self.process_opened_tasks(task)
            time_to_complete += 1
            self.set_task_completion()
        return time_to_complete
