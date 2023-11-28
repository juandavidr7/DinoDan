import gi


gi.require_version("Gtk", "3.0")
gi.require_version("Gst", "1.0")

from gi.repository import Gtk, Gst, Gdk
from Configuration import VentanaConfig
from niveles import form_niveles
from MultiSel import form_multi

Gst.init(None)
class Form(Gtk.Window):
    def __init__(self):
        super().__init__(title="Memory Dinosaur Game")
        self.set_default_size(640, 800)
        self.set_resizable(False)

     
        self.report_state = True
        self.music_state = True
        self.player_name = True

        music_file = "videoplayback.m4a"
        self.player = Gst.ElementFactory.make("playbin", "player")
        self.player.set_property("uri", Gst.filename_to_uri(music_file))
        if not Gst.uri_protocol_is_valid(music_file):
            print("Error: El archivo de música no es válido")
        if self.player.get_state(Gst.CLOCK_TIME_NONE) == Gst.State.NULL:
            pass
        else:
            self.player.set_state(Gst.State.PLAYING)

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

        self.NameLabelPly1 = Gtk.Label()
        self.NameLabelPly1.set_text("Bienvenido Jugador 1")
        rgba = Gdk.RGBA(1, 1, 1, 1) 
        self.NameLabelPly1.override_color(Gtk.StateFlags.NORMAL, rgba)
        Grid = Gtk.Grid()
        Grid.attach(self.NameLabelPly1, 0, 0, 1, 1)
        vb.pack_start(Grid, False, False, 0)
        # VBox para botones
        buttons_container = Gtk.VBox(spacing=6)

        # Button cargar valor
        btn_nombre = Gtk.Button.new_with_label("Nombre Jugador1")
        btn_nombre.connect("clicked", self.cargar_nombre)
        btn_nombre.set_size_request(250, 50)
        btn_nombre.set_name("btn-menu")
        btn_nombre.get_style_context ().add_class(Gtk.STYLE_CLASS_DESTRUCTIVE_ACTION)
        buttons_container.pack_start(btn_nombre, False, True, 0)

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
        buttons_container.set_margin_top(200)  # Ajusta el valor según tus preferencias

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
        self.Ventana_multi = form_multi(self)
        self.Ventana_multi.show_all()
        self.hide()

    def cargar_nombre(self, widget):
        self.Ventana_nombre = FormName(self)
        self.Ventana_nombre.show_all()

    def show_menu(self):
        self.show_all()
# Cargar el archivo de estilo CSS
class FormName(Gtk.Window):
    def __init__(self1, form):
        super().__init__(title="Ingresa tu nombre")
        self1.set_default_size(200, 200)
        self1.set_resizable(False)
        vb = Gtk.VBox()
        self1.add(vb)

        self1.form_instance = form


        lbl_name = Gtk.Label()
        lbl_name.set_text("Ingresa tu nombre de jugador:")

        input_name = Gtk.Entry()
        input_name.set_placeholder_text("Tu nombre...")

        button_name = Gtk.Button()
        button_name.set_label("Aceptar")
        button_name.connect("clicked", self1.guardar_nombre, input_name)
        button_name.set_size_request(150, 50)
        button_name.set_name("btn-menu")
        button_name.get_style_context ().add_class(Gtk.STYLE_CLASS_DESTRUCTIVE_ACTION)

        vb.pack_start(lbl_name, True, True, 0)
        vb.pack_start(input_name, True, True, 0)
        vb.pack_start(button_name, True, True, 0)

    def guardar_nombre(self1, widget, input_name):
        self1.form_instance.player_name = input_name.get_text()
        self1.form_instance.NameLabelPly1.set_text(f"Bienvenido {self1.form_instance.player_name}")
        self1.hide()

            

            

style_provider = Gtk.CssProvider()
style_provider.load_from_path('estilos.css')
Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(),style_provider,Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

win = Form()

win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
