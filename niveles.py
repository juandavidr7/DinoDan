import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

from Facil import Form_facil
from Medio import Form_medio
from Dificil import Form_dificil

class form_niveles(Gtk.Window):
    def __init__(self, form_instance):
        super().__init__(title="Niveles de Juego")
        self.set_default_size(300, 400)
        self.set_border_width(10)
        vb = Gtk.VBox(spacing=2)
        self.add(vb)

        self.form_instance = form_instance
        self.current_report_state = self.form_instance.report_state
        print("Estado del report", self.current_report_state)
        # Establecer la posición de la ventana en el centro
        self.set_position(Gtk.WindowPosition.CENTER)

        hbox1 = Gtk.Box(spacing=6)
        hbox2 = Gtk.Box(spacing=6)
        hbox3 = Gtk.Box(spacing=6)

        # Label fila
        lbl_fila = Gtk.Label()
        lbl_fila.set_text("Niveles de Juego")
        vb.pack_start(lbl_fila, True, True, 0)

        # Button cargar valor
        btn_facil = Gtk.Button.new_with_label("Nivel fácil")
        btn_facil.connect("clicked", self.nivel_facil)
        hbox1.pack_start(btn_facil, True, True, 0)

        # Button calcular valor
        btn_medio = Gtk.Button.new_with_label("Nivel Medio")
        btn_medio.connect("clicked", self.nivel_medio)
        hbox2.pack_start(btn_medio, True, True, 0)

        # Button totalizar
        btn_dificil = Gtk.Button.new_with_label("Nivel Dificil")
        btn_dificil.connect("clicked", self.nivel_dificil)
        hbox3.pack_start(btn_dificil, True, True, 0)

        # Se cargan los hbox al vbox
        vb.pack_start(hbox1, True, True, 0)
        vb.pack_start(hbox2, True, True, 0)
        vb.pack_start(hbox3, True, True, 0)

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




