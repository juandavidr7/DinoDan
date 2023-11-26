import gi


gi.require_version("Gtk", "3.0")
gi.require_version("Gst", "1.0")

from gi.repository import Gtk, Gst, Gdk
from Configuration import VentanaConfig
from Multiplayer import VentanaMulti
from niveles import form_niveles

Gst.init(None)
class form(Gtk.Window):
    def __init__(self):
        super().__init__(title="Memory Dinosaur Game")
        self.set_default_size(300, 400)
        self.set_border_width(10)
       

     
        self.report_state = True
        self.music_state = True

        music_file = "back.mpga"
        self.player = Gst.ElementFactory.make("playbin", "player")
        self.player.set_property("uri", Gst.filename_to_uri(music_file))
        if not Gst.uri_protocol_is_valid(music_file):
            print("Error: El archivo de música no es válido")
        if self.player.get_state(Gst.CLOCK_TIME_NONE) == Gst.State.NULL:
            pass
        else:
            self.player.set_state(Gst.State.PLAYING)


         # Establecer la posición de la ventana en el centro
        self.set_position(Gtk.WindowPosition.CENTER)

        overlay = Gtk.Overlay()
        self.add(overlay)

        # El fondo
        fondo = Gtk.Image.new_from_file("img/fondo.jpeg")
        overlay.add_overlay(fondo)

        css_provider = Gtk.CssProvider()
        css_provider.load_from_data(b"""
            * {
                color: red;
            }
            .btn-jugar:hover {
                background-color: #2980b9;
            }
        """)

        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(
            Gdk.Screen.get_default(),
            css_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        # VBox principal
        vb = Gtk.VBox(spacing=10)
        overlay.add_overlay(vb)

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
