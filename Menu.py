import gi


gi.require_version("Gtk", "3.0")
gi.require_version("Gst", "1.0")

<<<<<<< HEAD
from gi.repository import Gtk, Gdk
=======
from gi.repository import Gtk, Gst, Gdk
>>>>>>> 03eb6c54a8e2df08987cd7b77feff647c553e22b
from Configuration import VentanaConfig
from Multiplayer import VentanaMulti
from niveles import form_niveles

<<<<<<< HEAD
 

class Form(Gtk.Window):
    def __init__(self):
        super().__init__(title="Memory Dinosaur Game")
        self.set_default_size(640, 800)
        self.set_resizable(False)
=======
Gst.init(None)
class form(Gtk.Window):
    def __init__(self):
        super().__init__(title="Memory Dinosaur Game")
        self.set_default_size(300, 400)
        self.set_border_width(10)
       

     
        self.report_state = True
        self.music_state = True

        music_file = "videoplayback.m4a"
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
>>>>>>> 03eb6c54a8e2df08987cd7b77feff647c553e22b

        # Crear un contenedor de tipo Overlay
        overlay = Gtk.Overlay()
        self.add(overlay)

<<<<<<< HEAD
        # Crear un widget de imagen y cargar la imagen de fondo
        image = Gtk.Image()
        image.set_from_file("img/fondo.jpg")  # Reemplaza con la ruta de tu imagen
        overlay.add_overlay(image)
=======
        # El fondo
        fondo = Gtk.Image.new_from_file("img/fondo.jpeg")
        overlay.add_overlay(fondo)
>>>>>>> 03eb6c54a8e2df08987cd7b77feff647c553e22b

        # Establecer la posición de la ventana en el centro
        self.set_position(Gtk.WindowPosition.CENTER)

        # VBox principal
        vb = Gtk.VBox(spacing=10)
        overlay.add_overlay(vb)

<<<<<<< HEAD
        # VBox para botones
        buttons_container = Gtk.VBox(spacing=6)
=======
        self.add(vb)

        hbox1 = Gtk.Box(spacing=6)
        hbox2 = Gtk.Box(spacing=6)
        hbox3 = Gtk.Box(spacing=6)

      
        # Label fila
        lbl_fila = Gtk.Label()
        lbl_fila.set_text("Dinosaur Memory Game")
        vb.pack_start(lbl_fila, True, True, 0)
>>>>>>> 03eb6c54a8e2df08987cd7b77feff647c553e22b

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

<<<<<<< HEAD
style_provider = Gtk.CssProvider()
style_provider.load_from_path('estilos.css')
Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(),style_provider,Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

win = Form()
=======
    


    


win = form()
>>>>>>> 03eb6c54a8e2df08987cd7b77feff647c553e22b
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()