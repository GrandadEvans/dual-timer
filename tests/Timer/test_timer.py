#! /usr/bin/env python3
"""
Class responsible for testing the timer functionality
"""

import pytest
from ...src.timer.Timer import Timer

__author__ = "John Evans <john@grandadevans.com?"
__copyright__ = "Copyright 2015, John Evans"
__credits__ = ["John Evans <john@grandadevans.com>"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "John Evans"
__email__ = "john@grandadevans.com"
__status__ = "Development"

class TestTimer:

    def test_the_class_is_initialised_with_a_start_of_zero(self):
        timer = Timer()
        duration = timer.duration
        assert(duration == 0)