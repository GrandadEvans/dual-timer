import io
import os
import json

class Project:

    def __init__(self, project):

        print(project)
        self.project_name = project["name"]
        self.project_path = project["path"]
        self.project_start_date = project["start_date"]
        self.project_finish_date = project["finish_date"]
        self.project_finish_date_type = self.convert_estimate_type(project["finish_date_type"])

        self.project_info = {
            "project_name": self.project_name,
            "project_dir":  self.project_path,
            "project_start_date": self.project_start_date,
            "project_finish_date": self.project_finish_date,
            "project_finish_date_type": self.project_finish_date_type
        }

        self.create_template()

    def convert_estimate_type(self, active):
        if active:
            return "Estimated"
        return "Actual"

    def create_template(self):
        self.create_project_directory()
        self.create_project_info_file()

    def create_project_info_file(self):
        path = self.project_path + "/project-info.json"

        print(path)
        print(self.project_info)

        f = io.open(path, "w")
        json.dump(self.project_info, f, True, True, True, True, None, 1, (',', ': '))

    def create_project_directory(self):
        if not os.path.exists(self.project_path):
            os.makedirs(self.project_path)

    def set_project_name(self, project_name):
        self.project_name = project_name

    def set_project_path(self, project_path):
        self.create_project_directory(project_path)
        self.project_path = project_path

    def set_project_start_date(self, start_date):
        self.project_start_date = start_date

    def set_project_finish_date(self, finish_date):
        self.project_finish_date = finish_date

    def set_project_finish_date_type(self, finish_date_type):
        self.project_finish_date_type = finish_date_type

