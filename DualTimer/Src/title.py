from gi.repository import Gtk
from gi.repository import GLib
from gi.repository import Wnck


class WindowTitle(object):
    def __init__(self):
        self.title = None
        GLib.timeout_add(100, self.get_title)

    def get_title(self):
        try:
            Gtk.main_iteration()
            screen = Wnck.Screen.get_default()
            screen.force_update()
            active = screen.get_active_window()
            title = active.get_name()
            if self.title != title:
                self.title = title
                print(title)
        except AttributeError:
            pass
        return True


WindowTitle()
Gtk.main()
