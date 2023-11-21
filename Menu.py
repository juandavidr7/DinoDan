import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from Configuration import VentanaConfig
from Multiplayer import VentanaMulti
from niveles import form_niveles

class form(Gtk.Window):
    def __init__(self):
        super().__init__(title="Memory Dinosaur Game")
        self.set_default_size(300, 400)
        self.set_border_width(10)
        vb = Gtk.VBox(spacing=2)
        self.add(vb)

        hbox1 = Gtk.Box(spacing=6)
        hbox2 = Gtk.Box(spacing=6)
        hbox3 = Gtk.Box(spacing=6)

        # Label fila
        lbl_fila = Gtk.Label()
        lbl_fila.set_text("Dinosaur Memory Game")
        vb.pack_start(lbl_fila, True, True, 0)

        # Button cargar valor
        btn_jugar = Gtk.Button.new_with_label("Niveles")
        btn_jugar.connect("clicked", self.cargar_juego)
        hbox1.pack_start(btn_jugar, True, True, 0)

        # Button calcular valor
        btn_configuracion = Gtk.Button.new_with_label("Configuracion")
        btn_configuracion.connect("clicked", self.cargar_configuracion)
        hbox2.pack_start(btn_configuracion, True, True, 0)

        # Button totalizar
        btn_multijugador = Gtk.Button.new_with_label("Multijugador")
        btn_multijugador.connect("clicked", self.jugar_multijugador)
        hbox3.pack_start(btn_multijugador, True, True, 0)

        # Se cargan los hbox al vbox
        vb.pack_start(hbox1, True, True, 0)
        vb.pack_start(hbox2, True, True, 0)
        vb.pack_start(hbox3, True, True, 0)

        # Create an attribute to hold the reference to VentanaConfig
        self.Ventana_Config = None

    def cargar_juego(self, widget):
        self.Ventana_main = form_niveles(self)
        self.Ventana_main.show_all()
        self.hide()

    def cargar_configuracion(self, widget):
       
        self.Ventana_Config = VentanaConfig(self)
        self.Ventana_Config.show_all()
        self.hide()

    def jugar_multijugador(self, widget):
        self.Ventana_multi = VentanaMulti(self)
        self.Ventana_multi.show_all()
        self.hide()

    def show_menu(self):
        self.show_all()


win = form()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
