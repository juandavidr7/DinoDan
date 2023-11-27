import gi
from gi.repository import Gtk, GLib
import random

gi.require_version("Gtk", "3.0")

    # Esta es la función más perra, aquí se hacen varias cosas


class VentanaMulti(Gtk.Window):
    def __init__(self, form_instance):
        super().__init__(title="Busca mi pareja")
        self.set_default_size(50, 50)
        self.set_border_width(1)
        
