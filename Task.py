import os

class Task:

    def __init__(self):
        self.name = ""
        self.file = ""
        self.project = ""
        self.task_time = 0

    def increase_task_time(self, new_time):
        self.task_time += new_time

    def get_task_time(self):
        return self.task_time

    def set_name(self, name):
        self.name = name

    def set_file(self, file):
        self.file = file

    def set_project(self, project):
        self.project = project

    def get_task_filename(self):
        return os.path.abspath(self.default_save_directory + "/" + self.project + "/" + self.name + ".json")

    def open_file(self):
        return os.open(self.get_task_filename(), "w")

