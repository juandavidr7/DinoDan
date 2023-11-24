import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

class Cronometro(Gtk.Window):
    def __init__(self):
        super().__init__(title="Cronómetro")
        self.tiempo_transcurrido = 0
        self.avanzar_tiempo = False

        self.etiqueta = Gtk.Label(label="Tiempo: 0 segundos")
        self.boton_iniciar = Gtk.Button(label="Iniciar")
        self.boton_detener = Gtk.Button(label="Detener")
        self.boton_reiniciar = Gtk.Button(label="Reiniciar")

        self.boton_iniciar.connect("clicked", self.iniciar_cronometro)
        self.boton_detener.connect("clicked", self.detener_cronometro)
        self.boton_reiniciar.connect("clicked", self.reiniciar_cronometro)

        self.agregar_componentes()

    def agregar_componentes(self):
        caja = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        caja.pack_start(self.etiqueta, True, True, 0)
        caja.pack_start(self.boton_iniciar, True, True, 0)
        caja.pack_start(self.boton_detener, True, True, 0)
        caja.pack_start(self.boton_reiniciar, True, True, 0)

        self.add(caja)

    def iniciar_cronometro(self, widget):
        GLib.timeout_add(1000, self.actualizar_tiempo)
        self.avanzar_tiempo = True

    def detener_cronometro(self, widget):
        self.avanzar_tiempo = False

    def reiniciar_cronometro(self, widget):
        self.tiempo_transcurrido = 0
        self.actualizar_etiqueta()

    def actualizar_tiempo(self):
        if self.avanzar_tiempo:
            self.tiempo_transcurrido += 1
            self.actualizar_etiqueta()
            return True
        else:
            return False
            
         

    def actualizar_etiqueta(self):
        self.etiqueta.set_text(f"Tiempo: {self.tiempo_transcurrido} segundos")

if __name__ == "__main__":
    ventana = Cronometro()
    ventana.connect("destroy", Gtk.main_quit)
    ventana.show_all()
    Gtk.main()
