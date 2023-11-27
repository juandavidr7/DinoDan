import gi
from gi.repository import Gtk, GLib
import random

gi.require_version("Gtk", "3.0")

class Form_dificil(Gtk.Window):

    def __init__(self, form_instance):
        super().__init__(title="Busca mi pareja")
        self.set_default_size(200, 350)
        self.set_border_width(10)

        self.form_instance = form_instance

        self.cartas_numeros = list(range(1, 9)) * 2
        self.cartas_seleccionadas = []
        self.intentos_exitosos = 0
        self.intentos_fallidos = 0

        # Establecer la posición de la ventana en el centro
        self.set_position(Gtk.WindowPosition.CENTER)
        

        vbox = Gtk.VBox(spacing=2)
        self.add(vbox)

        hbox1 = Gtk.Box(spacing=6)
        hbox2 = Gtk.Box(spacing=6)
        hbox3 = Gtk.Box(spacing=6)
        hbox4 = Gtk.Box(spacing=6)
        hbox5 = Gtk.Box(spacing=6)
        

        self.entry_numero_carta = Gtk.Entry()
        self.entry_numero_carta.set_text("")
        hbox5.pack_start(self.entry_numero_carta, True, True, 0)

        self.imagenes = []

        for i in range(16):
            imagen = Gtk.Image.new_from_file("img/0.jpeg")
            imagen.numero = self.cartas_numeros[i]

            if i < 4:
                hbox1.pack_start(imagen, True, True, 0)
            elif i>=4 and i<8:
                hbox2.pack_start(imagen, True, True, 0)
            elif i>=8 and i<12:
                hbox3.pack_start(imagen, True, True, 0)
            else:
                hbox4.pack_start(imagen, True, True, 0)

            self.imagenes.append(imagen)

        vbox.pack_start(hbox1, True, True, 0)
        vbox.pack_start(hbox2, True, True, 0)
        vbox.pack_start(hbox3, True, True, 0)
        vbox.pack_start(hbox4, True, True, 0)
        vbox.pack_start(hbox5, True, True, 0)

        lbl_imagen = Gtk.Label()
        lbl_imagen.set_text("Pulse en <<Iniciar Juego>> para comenzar")
        vbox.pack_start(lbl_imagen, True, True, 7)

        lbl_victoria = Gtk.Label()
        lbl_victoria.set_text("Completa todas las parejas posibles, en el menor tiempo posible")
        vbox.pack_start(lbl_victoria, True, True, 7)

        btn_iniciar_juego = Gtk.Button.new_with_label("Iniciar el juego")
        btn_iniciar_juego.connect("clicked", self.on_iniciar_juego, lbl_imagen)
        vbox.pack_start(btn_iniciar_juego, True, True, 0)

        btn_seleccionar = Gtk.Button.new_with_label("Seleccionar carta")
        btn_seleccionar.connect("clicked", self.on_seleccionar_clicked, lbl_imagen, lbl_victoria)
        vbox.pack_start(btn_seleccionar, True, True, 0)

        btn_volver = Gtk.Button.new_with_label("Volver")
        btn_volver.connect("clicked", self.on_cerrar_clicked)
        vbox.pack_start(btn_volver, True, True, 0)

        btn_cerrar = Gtk.Button.new_with_label("Cerrar")
        btn_cerrar.connect("clicked", self.on_close_clicked)
        vbox.pack_start(btn_cerrar, True, True, 0)

    def on_iniciar_juego(self, button, lbl_imagen):
        self.barajar_cartas()
        self.limpiar_cartas(lbl_imagen)
        self-iniciar_cronometro(self)
        self.cartas_seleccionadas = []
        self.intentos_exitosos = 0
        self.intentos_fallidos = 0
        
        lbl_imagen.set_text("Seleccione dos cartas: Intentos: 0")

    def on_seleccionar_clicked(self, button, lbl_imagen, lbl_victoria):
        numero_carta = int(self.entry_numero_carta.get_text())

        if 1 <= numero_carta <= 16:
            posicion_carta = numero_carta - 1
            carta_seleccionada = self.imagenes[posicion_carta]

            
            if carta_seleccionada not in self.cartas_seleccionadas:
                lbl_imagen.set_text(f"Carta seleccionada: {numero_carta}")
                carta_seleccionada.set_from_file(f"img/{(self.cartas_numeros[posicion_carta])}.jpeg")
                self.cartas_seleccionadas.append(carta_seleccionada)

                if len(self.cartas_seleccionadas) == 2:
                    self.validar_parejas(lbl_imagen, lbl_victoria)
                    self.ocultar_cartas_despues_delay(2)

                    if self.intentos_exitosos == 8:
                        lbl_victoria.set_text(f"¡Felicidades! Has encontrado todas las parejas en {self.intentos_exitosos} intentos exitosos, {self.intentos_fallidos} intentos fallidos, con un total de {self.intentos_exitosos + self.intentos_fallidos} intentos.")
                        self.entry_numero_carta.set_sensitive(False)
                        self.detener_cronometro(self)

            else:
                lbl_imagen.set_text("Número de carta no válido o ya seleccionada. Inténtalo de nuevo.")
                self.intentos_fallidos += 1


        else:
            lbl_imagen.set_text("Número de carta no válido. Inténtalo de nuevo.")

    def validar_parejas(self, lbl_imagen, lbl_victoria):
        print(self.cartas_seleccionadas)

        if self.cartas_seleccionadas[0].get_property("file") == self.cartas_seleccionadas[1].get_property("file"):
            lbl_imagen.set_text("¡Encontraste pareja!")
            self.cartas_seleccionadas[0].set_sensitive(False)  
            self.cartas_seleccionadas[1].set_sensitive(False)
            self.cartas_seleccionadas = []
            self.intentos_exitosos += 1

            
        else:
            lbl_imagen.set_text("¡No es pareja! Intenta con otra carta.")
            self.intentos_fallidos += 1

    def ocultar_cartas_despues_delay(self, delay):
        GLib.timeout_add(delay * 1000, self.ocultar_cartas)

    def ocultar_cartas(self):
        for imagen in self.cartas_seleccionadas:
            imagen.set_from_file("img/0.jpeg")
            imagen.set_sensitive(True)
        self.cartas_seleccionadas = []
        self.entry_numero_carta.set_text("")
       
    def iniciar_cronometro(self, widget):
        GLib.timeout_add(1000, self.actualizar_tiempo)

    def actualizar_tiempo(self):
        if self.avanzar_tiempo:
            self.tiempo_transcurrido += 1
            self.actualizar_etiqueta()
            return True
        else:
            return False
    
    def detener_cronometro(self, widget):
        self.avanzar_tiempo = False

    def actualizar_etiqueta(self):
        self.lbl_contador.set_text(f"Tiempo: {self.tiempo_transcurrido} segundos")


    def barajar_cartas(self):
        random.shuffle(self.cartas_numeros)
        print(self.cartas_numeros)

    def limpiar_cartas(self, lbl_imagen):
        for carta in self.imagenes:
            carta.set_from_file("img/0.jpeg")
            carta.set_sensitive(True)
        lbl_imagen.set_text(f"Seleccione dos cartas: Intentos: {self.intentos_exitosos + self.intentos_fallidos}")

    def on_close_clicked(self, but_cerrar):
        Gtk.main_quit()

    def on_cerrar_clicked(self, widget):
        # Destroy the current window
        self.destroy()

        # Show the form window using the stored reference
        self.form_instance.show_menu()


