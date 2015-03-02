#! /usr/bin/python3

from Timer import Timer
from gi.repository import Gtk

class TutorialTextEditor:

    def on_window_destroy(self, widget, data=None):
        Gtk.main_quit()

    def button_timer_client_start(self, widget, data=None):
        self.client.start_timer()

    def button_timer_client_pause(self, widget, data=None):
        self.client.pause_timer()

    def button_timer_client_stop(self, widget, data=None):
        self.client.stop_timer()

    def button_timer_billable_start(self, widget, data=None):
        self.billable.start_timer()

    def button_timer_billable_pause(self, widget, data=None):
        self.billable.pause_timer()

    def button_timer_billable_stop(self, widget, data=None):
        self.billable.stop_timer()

    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("dual-timer.glade")

        self.window = builder.get_object("dual-timer-main-window")
        self.about_dialog = builder.get_object("about-window")

        builder.connect_signals(self)

        self.client = Timer("client", builder)
        self.billable = Timer("billable", builder)

    def on_gtk_about_activate(self, menuitem, data=None):
        print("help about selected")
        self.response = self.about_dialog.run()
        self.about_dialog.hide()

if __name__ == "__main__":
    editor = TutorialTextEditor()
    editor.window.show()
    Gtk.main()

