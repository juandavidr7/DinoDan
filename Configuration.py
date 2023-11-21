import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class VentanaConfig(Gtk.Window):
    def __init__(self, form_instance):
        Gtk.Window.__init__(self, title="Nueva Partida")
        self.set_default_size(200, 100)

        # Store the reference to the form instance
        self.form_instance = form_instance

        # Crear un botón en la nueva ventana
        boton_nueva_ventana = Gtk.Button(label="Cerrar")
        boton_nueva_ventana.connect("clicked", self.on_cerrar_clicked)

        # Añadir el botón a la nueva ventana
        self.add(boton_nueva_ventana)

    def on_cerrar_clicked(self, widget):
        # Destroy the current window
        self.destroy()

        # Show the form window using the stored reference
        self.form_instance.show_menu()
