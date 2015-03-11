#! /usr/bin/env python3
"""
Class responsible for all the timer functionality
"""

import uuid
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

class Timer:

    def __init__(self):
        self.id = uuid.uuid4()
        self.duration = 0
        self.status = "Not Yet Started"

    def start_timer(self):
        self.status = "Started"