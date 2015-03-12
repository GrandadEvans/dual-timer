#! /usr/bin/env python3
"""
Class responsible for all the timer functionality
"""

import uuid
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


class Timer:

    def __init__(self):
        self.id = uuid.uuid4()
        self.duration = 0
        self.status = "Not Yet Started"
        self.entries = []

    def start_timer(self):
        print('in start_timer')
        self.status = "Started"
        new_entry = {
            "start": time.time(),
            "end": None,
            "duration": 0
        }
        self.entries.append(new_entry)

    def update_duration(self):
        if self.status.lower() == "paused" or self.status.lower() == "stopped":
            return False

        self.duration = int(self.duration) + 1
        return True

    def pause_timer(self):
        self.status = "Paused"
        index = self.get_current_entry_index()
        self.entries[index]["end"] = time.time()

    def stop_timer(self):
        self.status = "Stopped"

    def restart_timer(self):
        self.status = "Re-started"

    def get_short_format_duration_string(self):
        return str(datetime.timedelta(seconds=self.duration))

    def get_long_format_duration_string(self):
        short = self.get_short_format_duration_string()

        bits = short.split(':')
        h = str(self.add_zero(bits[0])) + 'h'
        m = str(self.add_zero(bits[1])) + 'm'

        return h + ' ' + m

    def add_zero(self, bit):
        if len(bit) == 1:
            return '0' + bit
        return bit

    def get_current_entry_index(self):
        index = len(self.entries)
        return index - 1

    def get_total_duration(self):
        total = 0
        for entry in self.entries:
            total += entry["duration"]
        return total

    def clear_entries(self):
        self.entries = []
