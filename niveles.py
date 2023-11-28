import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

from Facil import Form_facil
from Medio import Form_medio
from Dificil import Form_dificil

class form_niveles(Gtk.Window):
    def __init__(self, form_instance):
        super().__init__(title="Niveles de Juego")
        self.set_default_size(640, 800)
        

        self.form_instance = form_instance
        self.current_report_state = self.form_instance.report_state
        self.player_name = self.form_instance.player_name
        print("Estado del report", self.current_report_state)
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
        btn_facil = Gtk.Button.new_with_label("Nivel fácil")
        btn_facil.connect("clicked", self.nivel_facil)
        btn_facil.set_size_request(250, 100)
        btn_facil.get_style_context ().add_class(Gtk.STYLE_CLASS_DESTRUCTIVE_ACTION)
        buttons_container.pack_start(btn_facil, False, True, 0)
        

        # Button calcular valor
        btn_medio = Gtk.Button.new_with_label("Nivel Medio")
        btn_medio.connect("clicked", self.nivel_medio)
        btn_medio.set_size_request(250, 100)
        btn_medio.get_style_context ().add_class(Gtk.STYLE_CLASS_DESTRUCTIVE_ACTION)
        buttons_container.pack_start(btn_medio, False, True, 0)

        # Button totalizar
        btn_dificil = Gtk.Button.new_with_label("Nivel Dificil")
        btn_dificil.connect("clicked", self.nivel_dificil)
        btn_dificil.set_size_request(250, 100)
        btn_dificil.get_style_context ().add_class(Gtk.STYLE_CLASS_DESTRUCTIVE_ACTION)
        buttons_container.pack_start(btn_dificil, False, True, 0)

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

    def nivel_facil(self, widget):
        self.Ventana_facil = Form_facil(self)
        self.Ventana_facil.show_all()
        self.hide()

    def nivel_medio(self, widget):
       
        self.Ventana_medio = Form_medio(self)
        self.Ventana_medio.show_all()
        self.hide()

    def nivel_dificil(self, widget):
        self.Ventana_dificl = Form_dificil(self)
        self.Ventana_dificl.show_all()
        self.hide()

    def show_menu(self):
        self.show_all()

    def on_cerrar_clicked(self, widget):
        # Destroy the current window
        self.destroy()

        # Show the form window using the stored reference
        self.form_instance.show_menu()


