#! /usr/bin/env python3
"""
Class to take care of the projects
"""

# import built in modules
import os
import json
import pprint

# import Third party

# import local
from DualTimer.Src.Persistence.File.File import File
from DualTimer.Src.Config.App import App as Config

__author__ = "John Evans <john@grandadevans.com?"
__copyright__ = "Copyright 2015, John Evans"
__credits__ = ["John Evans <john@grandadevans.com>"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "John Evans"
__email__ = "john@grandadevans.com"
__status__ = "Development"


class Project:

    def __init__(self, project_name):
        self.project_name = project_name
        self.project_path = Config().paths()["base"] + 'stubs/Project/'
        self.project_info_file = self.project_path + "project.json"
        self.project_details = {
            "name": self.project_name,
            "start_date": None,
            "end_date": None,
            "end_date_type": None,
            "contacts": [],
            "billing": {
                "billable": True,
                "billable_unit": "hours",
                "billable_rate": 0.00,
                "currency": "GBP"
            },
            "budget": {
                "unit": "hours",
                "value": 0
            }
        }
        self.pp = pprint.PrettyPrinter(indent=4)
        self.pp.pprint(self.project_path)

    def create_project_directory(self):
        if os.path.isdir(self.project_path):
            raise Exception("Project already exists")
        os.mkdir(self.project_path)

    def create_project_info_file(self):
        return open(Config().paths()[
            "base"] + "stubs/Project/project.json", 'w')

    def create_the_project_info(self):
        fp = self.create_project_info_file()
        fp.write(json.dumps(self.project_details))

    def delete_project(self):
        if os.path.isfile(self.project_info_file) is True:
            os.remove(self.project_info_file)
        if os.path.isdir(self.project_path) is True:
            os.removedirs(self.project_path)

    def update_project(self, details):
        # print(details)
        for item, value in details.items():
            # print("For loop:", item)
            self.change_dot_notation_to_stacked(item, value)

    def change_dot_notation_to_stacked(self, item, value):
        if "." in item:
            bits = item.split(".")
            self.project_details[bits[0]][bits[1]] = value
        else:
            self.project_details[item] = value
        self.create_the_project_info()

    def add_contact(self, contact):
        if str(contact).lower() not in self.project_details["contacts"]:
            self.project_details["contacts"].append(contact)
        self.create_the_project_info()

    def set_not_billable(self):
        self.project_details["billing"]["billable"] = False
        self.create_the_project_info()
