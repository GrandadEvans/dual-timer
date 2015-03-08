#! /usr/bin/env python3
"""
Class responsible for testing the timer functionality
"""

import pytest
import time
from gi.repository import GLib

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

    def test_the_status_changes_when_we_start_the_timer(self):
        timer = Timer()
        timer.start_timer()
        status = timer.status
        assert(status.lower() == 'started')

    # def test_the_timer_runs_when_the_status_is_started(self):
    #     timer = Timer()
    #     timer.start_timer()
    #     GLib.timeout_add_seconds(1, 3, self.return_false)
    #     print(timer.duration)
    #     assert(timer.duration == 3)
    #
    # def return_false(self):
    #     return False

    def test_the_duration_updates_when_update_duration_is_called(self):
        timer = Timer()
        assert(timer.duration == 0)
        timer.update_duration()
        assert(timer.duration == 1)

    def test_the_duration_does_not_increment_if_the_status_isnt_started(self):
        timer = Timer()
        assert(timer.duration == 0)
        timer.update_duration()
        assert(timer.duration == 1)
        timer.status = "Paused"
        timer.update_duration()
        assert(timer.duration == 1)

    def test_the_duration_does_not_increment_if_the_status_is_stopped(self):
        timer = Timer()
        assert(timer.duration == 0)
        timer.update_duration()
        assert(timer.duration == 1)
        timer.status = "Stopped"
        timer.update_duration()
        assert(timer.duration == 1)

    def test_the_duration_increment_if_the_status_is_started(self):
        timer = Timer()
        assert(timer.duration == 0)
        timer.update_duration()
        assert(timer.duration == 1)
        timer.status = "Started"
        timer.update_duration()
        assert(timer.duration == 2)

    def test_the_duration_increment_if_the_status_is_restarted(self):
        timer = Timer()
        assert(timer.duration == 0)
        timer.update_duration()
        assert(timer.duration == 1)
        timer.status = "Re-started"
        timer.update_duration()
        assert(timer.duration == 2)

    def test_the_pause_timer_method_works(self):
        timer = Timer()
        timer.pause_timer()
        assert(timer.status == "Paused")

    def test_the_stop_timer_method_works(self):
        timer = Timer()
        timer.stop_timer()
        assert(timer.status == "Stopped")

    def test_the_restart_timer_method_works(self):
        timer = Timer()
        timer.restart_timer()
        assert(timer.status == "Re-started")