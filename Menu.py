import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk, Gdk
from Configuration import VentanaConfig
from Multiplayer import VentanaMulti
from niveles import form_niveles

 

class Form(Gtk.Window):
    def __init__(self):
        super().__init__(title="Memory Dinosaur Game")
        self.set_default_size(640, 800)
        self.set_resizable(False)

        # Crear un contenedor de tipo Overlay
        overlay = Gtk.Overlay()
        self.add(overlay)

        # Crear un widget de imagen y cargar la imagen de fondo
        image = Gtk.Image()
        image.set_from_file("img/fondo.jpg")  # Reemplaza con la ruta de tu imagen
        overlay.add_overlay(image)

        # Establecer la posición de la ventana en el centro
        self.set_position(Gtk.WindowPosition.CENTER)

        # VBox principal
        vb = Gtk.VBox(spacing=10)
        overlay.add_overlay(vb)

        # VBox para botones
        buttons_container = Gtk.VBox(spacing=6)

        # Button cargar valor
        btn_jugar = Gtk.Button.new_with_label("Niveles")
        btn_jugar.connect("clicked", self.cargar_juego)
        btn_jugar.set_size_request(250, 100)
        btn_jugar.set_name("btn-menu")
        btn_jugar.get_style_context ().add_class(Gtk.STYLE_CLASS_DESTRUCTIVE_ACTION)
        buttons_container.pack_start(btn_jugar, False, True, 0)
        

        # Button calcular valor
        btn_configuracion = Gtk.Button.new_with_label("Configuracion")
        btn_configuracion.connect("clicked", self.cargar_configuracion)
        btn_configuracion.set_name("btn_configuracion")
        btn_configuracion.set_size_request(250, 100)
        btn_configuracion.set_name("btn-menu")
        btn_configuracion.get_style_context ().add_class(Gtk.STYLE_CLASS_DESTRUCTIVE_ACTION)
        buttons_container.pack_start(btn_configuracion, False, True, 0)

        # Button totalizar
        btn_multijugador = Gtk.Button.new_with_label("Multijugador")
        btn_multijugador.connect("clicked", self.jugar_multijugador)
        btn_multijugador.set_name("btn_multijugador")
        btn_multijugador.set_size_request(250, 100)
        btn_multijugador.set_name("btn-menu")
        btn_multijugador.get_style_context ().add_class(Gtk.STYLE_CLASS_DESTRUCTIVE_ACTION)
        buttons_container.pack_start(btn_multijugador, False, True, 0)

        # Añadir margen hacia abajo a la caja de botones
        buttons_container.set_margin_top(420)  # Ajusta el valor según tus preferencias

        # Crear un contenedor para centrar los botones en la parte inferior
        align_bottom = Gtk.Alignment.new(0.5, 1, 0, 0)
        align_bottom.add(buttons_container)
        vb.pack_start(align_bottom, False, False, 0)

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
# Cargar el archivo de estilo CSS

style_provider = Gtk.CssProvider()
style_provider.load_from_path('estilos.css')
Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(),style_provider,Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

win = Form()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()