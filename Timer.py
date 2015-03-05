import sys
import time
import datetime
import inspect
from gi.repository import GLib

class Timer:

    def __init__(self, name, builder):

        # The label
        self.status_label = builder.get_object(name + "-timer-label")
        # self.dock_status_label = builder.get_object(name + "-timer-dock_label")

        # The counter that is updated
        self.status_counter = builder.get_object(name + "-timer-status")
        self.dock_status_counter = builder.get_object(name + "-timer-dock-status")

        # The status
        self.status = "No actions yet"

        # create an empty list of entries
        self.entries = []

        self.started_status = "Started"
        self.paused_status = "Paused"
        self.stopped_status = "Stopped"
        self.restarted_status = "Re-Started"

        # Update the text
        # self.timer()
        self.total_diff = 0

        # Reset the counter
        self.reset_counter()

    def calculate_total_diff(self):
        # print("calculate_total_diff:", inspect.currentframe().f_lineno)
        total_diff = 0
        if len(self.entries) == 0:
            # print("no entries:", inspect.currentframe().f_lineno)
            self.total_diff = 0 + self.calculate_current_diff()
        else:
            # print("Printing entries at:", inspect.currentframe().f_lineno)
            # print(self.entries)
            for entry in self.entries:
                # print(total_diff, ' + ', entry[2], '(', inspect.currentframe().f_lineno, ')')
                total_diff += entry[2]

            if self.status == self.paused_status or self.status == self.stopped_status:
                # print("Status is paused:", inspect.currentframe().f_lineno)
                self.total_diff = total_diff
            else:
                # print("Status is NOT paused:", inspect.currentframe().f_lineno)
                self.total_diff = total_diff + self.calculate_current_diff()

    def calculate_current_diff(self):
        i = int(int(time.time()) - self.time_started)
        # print("calculate_current_diff:", i, '(', inspect.currentframe().f_lineno, ')')
        return i

    def updateText(self):
        # print("updateText:", inspect.currentframe().f_lineno)
        time_string = self.format_time_string()
        time_string_for_dock = self.format_time_string_for_dock()
        # print(time_string)
        self.status_counter.set_text(time_string)
        self.dock_status_counter.set_text(time_string_for_dock)
        # print(inspect.currentframe().f_lineno)
        self.status_label.set_text(self.status)
        # self.dock_status_label.set_text(self.status)
        # print(inspect.currentframe().f_lineno)

    def reset_counter(self):
        # print("reset_counter:", inspect.currentframe().f_lineno)
        # print("Resetting the queue")
        self.time_started = time.time()
        # print("time started reset to:", self.time_started)

    def start_timer(self):
        # print("start_timer:", inspect.currentframe().f_lineno)
        # print("Start button clicked")
        if self.status == self.started_status or self.status == self.restarted_status:
            # print("Status is started or re-started", inspect.currentframe().f_lineno)
            return True

        elif self.status != self.stopped_status:
            # print("status is not stopped ie it's paused:", self.status, inspect.currentframe().f_lineno)
            self.initialise_fresh_timer_entry()
            # print(inspect.currentframe().f_lineno)
            self.status = self.started_status
            # print(inspect.currentframe().f_lineno)

    def pause_timer(self):
        # print("\n\n")
        # print("pause_timer:", self.status)
        # print("\n\n")
        if self.status == self.started_status:
            self.add_to_entries()
            self.status = self.paused_status
            # print("Status changed to paused")
            self.updateText()
        elif self.status == self.paused_status:
            self.status = self.restarted_status
            # print("Status changed to Re-Started")
            self.initialise_fresh_timer_entry()

    def stop_timer(self):
        # print("\n\n")
        # print("stop_timer:", self.status)
        # print("\n\n")
        if self.status == self.started_status or self.status == self.paused_status:
            if self.status == self.started_status:
                self.add_to_entries()
            self.status = self.stopped_status
            # print("Status changed to stopped")
            self.updateText()

    def initialise_fresh_timer_entry(self):
        # print("initialise_fresh_timer_entry:", inspect.currentframe().f_lineno)
        self.reset_counter()
        # print(inspect.currentframe().f_lineno)
        # print("reached here")
        GLib.timeout_add_seconds(priority=1, interval=1, function=self.update_timer)

    def update_timer(self):
        # print("update_timer:", inspect.currentframe().f_lineno)
        self.calculate_total_diff()
        self.updateText()
        if self.status == self.paused_status or self.status == self.stopped_status:
            # print("status is paused or stopped so returning false")
            return False

        # print("Returning true to timeout_add_seconds", inspect.currentframe().f_lineno)
        return True

    def add_to_entries(self):
        # print("add_to_entries")
        start = self.time_started
        finish = int(time.time())
        diff = int(finish - start)
        self.entries.append([start, finish, diff])

    def format_time_string(self):
        # print("format_time_string:", inspect.currentframe().f_lineno)
        self.calculate_total_diff()
        # print("Total diff:", self.total_diff, inspect.currentframe().f_lineno)

        time_list = str(datetime.timedelta(seconds=self.total_diff)).split(':')
        # print(time_list)
        time_string = time_list[0] + "h "  + time_list[1] + "m " + time_list[2] + "s"
        # print("Time string:", time_string, inspect.currentframe().f_lineno)
        return time_string

    def format_time_string_for_dock(self):
        # print("format_time_string:", inspect.currentframe().f_lineno)
        self.calculate_total_diff()
        # print("Total diff:", self.total_diff, inspect.currentframe().f_lineno)

        return str(datetime.timedelta(seconds=self.total_diff))
        # time_list = str(datetime.timedelta(seconds=self.total_diff)).split(':')
        # print(time_list)
        # time_string = time_list[0] + ":"  + time_list[1] + ":" + time_list[2] + "s"
        # print("Time string:", time_string, inspect.currentframe().f_lineno)
        # return time_string
