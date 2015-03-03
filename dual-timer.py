#! /usr/bin/python3

from Timer import Timer
from Project import Project
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

    def new_project_window_create_project(self, widget, data=None):
        print("New Project button clicked (but nothing done about it")

        self.project = Project({
            "name": self.new_project_window_name_input.get_text(),
            "path": self.new_project_window_directory_input.get_filename(),
            "start_date": self.new_project_window_start_date_input.get_date(),
            "finish_date": self.new_project_window_finish_date_input.get_date(),
            "finish_date_type": self.new_project_window_finish_date_type_input.get_active()
        })
        print("Project information file created")
        self.new_project_window.hide()
        self.project_choice_window.hide()
        self.project_choice_button.set_label(self.project.project_info['project_name'])


    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("dual-timer.glade")

        self.window = builder.get_object("dual-timer-main-window")
        self.about_dialog = builder.get_object("about-window")
        self.new_project_window = builder.get_object("new-project-window")
        self.project_choice_button = builder.get_object("project-choice-button")
        self.project_choice_window = builder.get_object("project-choice-window")
        self.new_project_window_name_input = builder.get_object("new-project-window-name-input")
        self.new_project_window_directory_input = builder.get_object("new-project-window-directory-input")
        self.new_project_window_start_date_input = builder.get_object("new-project-window-start-date-input")
        self.new_project_window_finish_date_input = builder.get_object("new-project-window-finish-date-input")
        self.new_project_window_finish_date_type_input = builder.get_object("new-project-window-finish-date-type-input")

        builder.connect_signals(self)

        self.client = Timer("client", builder)
        self.billable = Timer("billable", builder)

    def on_gtk_about_activate(self, menuitem, data=None):
        print("help about selected")
        self.response = self.about_dialog.run()
        self.about_dialog.hide()

    def new_project_window_show(self, widget, data=None):
        print("Showing new project window")
        self.response = self.new_project_window.show()

    def project_choice_window_show(self, widget, data=None):
        print("Showing the project choice window")
        self.response = self.project_choice_window.show()


if __name__ == "__main__":
    editor = TutorialTextEditor()
    editor.window.show()
    Gtk.main()

