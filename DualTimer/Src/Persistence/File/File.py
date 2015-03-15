#! /usr/bin/env python3
"""
Class responsible for all the all file manipulations
"""

import io
import os
from io import StringIO
import time
import datetime

# import Third party

# import local

__author__ = "John Evans <john@grandadevans.com?"
__copyright__ = "Copyright 2015, John Evans"
__credits__ = ["John Evans <john@grandadevans.com>"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "John Evans"
__email__ = "john@grandadevans.com"
__status__ = "Development"


class File:

    def __init__(self):
        self.base_dir = os.path.dirname(__file__) + '/../../../'
        self.file_object = None

    def create(self, file_path):
        f = open(file_path, 'a')
        self.file_object = f

    def write(self, file_path, data_to_write, mode="a"):
        f = open(file_path, mode)
        f.write(data_to_write)

    def update(self, file_path, data_to_add):
        f = open(file_path, 'a')
        f.write(data_to_add)

    def delete(self, file_path):
        f = os.remove(file_path)
