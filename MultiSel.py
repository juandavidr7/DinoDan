import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

from Multiplayer import VentanaMulti
from Bot import VentanaBot


class form_multi(Gtk.Window):
    def __init__(self, form_instance):
        super().__init__(title="Selección de jugabilidad")
        self.set_default_size(640, 800)
        

        self.form_instance = form_instance
        self.report_state = self.form_instance.report_state

        # Establecer la posición de la ventana en el centro
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)
        

        # Crear un contenedor de tipo Overlay
        overlay = Gtk.Overlay()
        self.add(overlay)

        # Crear un widget de imagen y cargar la imagen de fondo
        image = Gtk.Image()
        image.set_from_file("img/fondo1.jpg")  # Reemplaza con la ruta de tu imagen
        overlay.add_overlay(image)

        vb = Gtk.VBox(spacing=2)
        overlay.add_overlay(vb)

        # VBox para botones
        buttons_container = Gtk.VBox(spacing=6)


        # Button cargar valor
        btn_player = Gtk.Button.new_with_label("Contra jugador")
        btn_player.connect("clicked", self.MultiplayerS)
        btn_player.set_size_request(250, 100)
        btn_player.set_name("btn-niveles")
        btn_player.get_style_context ().add_class(Gtk.STYLE_CLASS_DESTRUCTIVE_ACTION)
        buttons_container.pack_start(btn_player, False, True, 0)
        

        # Button calcular valor
        btn_bot = Gtk.Button.new_with_label("Contra la máquina")
        btn_bot.connect("clicked", self.BotS)
        btn_bot.set_size_request(250, 100)
        btn_bot.set_name("btn-niveles")
        btn_bot.get_style_context ().add_class(Gtk.STYLE_CLASS_DESTRUCTIVE_ACTION)
        buttons_container.pack_start(btn_bot, False, True, 0)

        # Button totalizar
     

        btn_volver = Gtk.Button.new_with_label("Volver")
        btn_volver.connect("clicked", self.on_cerrar_clicked)
        btn_volver.set_size_request(90, 50)
        btn_volver.set_name("btn-niveles")
        btn_volver.get_style_context ().add_class("btn-niveles")
        buttons_container.pack_start(btn_volver, False, True, 9)

        # Añadir margen hacia abajo a la caja de botones
        buttons_container.set_margin_top(400)  # Ajusta el valor según tus preferencias

        # Crear un contenedor para centrar los botones en la parte inferior
        align_bottom = Gtk.Alignment.new(0.5, 1, 0, 0)
        align_bottom.add(buttons_container)
        vb.pack_start(align_bottom, False, False, 0)

        # Create an attribute to hold the reference to VentanaConfig
        self.Ventana_Config = None

    def MultiplayerS(self, widget):
        self.Ventana_Multi = VentanaMulti(self)
        self.Ventana_Multi.show_all()
        self.hide()

    def BotS(self, widget):
        self.Ventana_Bot = VentanaBot(self)
        self.Ventana_Bot.show_all()
        self.hide()

    def show_menu(self):
        self.show_all()

    def on_cerrar_clicked(self, widget):
        # Destroy the current window
        self.destroy()

        # Show the form window using the stored reference
        self.form_instance.show_menu()

