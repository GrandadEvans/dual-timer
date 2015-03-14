#! /usr/bin/env python3
"""
Class to take care of the projects
"""

# import built in modules
import os
import json

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
        print(self.project_path)

    def create_project_directory(self):
        if os.path.isdir(self.project_path):
            raise Exception("Project already exists")
        os.mkdir(self.project_path)

    def create_project_info_file(self):
        return open(Config().paths()[
            "base"] + "stubs/Project/project.json", 'w')

    def create_the_project_info(self):
        fp = self.create_project_info_file()
        fp.write(json.dumps({
            "name": self.project_name,
            "start_date": None,
            "end_date": None,
            "end_date_type": None
        }))
