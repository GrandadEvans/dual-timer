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
        duration = Timer().duration
        assert(duration == 0)

    def test_we_are_returned_a_unique_id_for_new_timers(self):
        id = str(Timer().id)
        assert(len(id) == 36)

    def test_we_have_the_correct_timer_status_on_instantiation(self):
        status = Timer().status
        assert(status.lower() == 'not yet started')