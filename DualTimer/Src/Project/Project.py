#! /usr/bin/env python3
"""
Class to take care of the projects
"""

# import built in modules

# import Third party

# import local
from DualTimer.Src.Persistence.File.File import File

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
