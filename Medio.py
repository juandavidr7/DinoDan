import gi
from gi.repository import Gtk, GLib
import random

gi.require_version("Gtk", "3.0")

class Form_medio(Gtk.Window):

    def __init__(self, form_instance):
        super().__init__(title="Busca mi pareja")
        self.set_default_size(640, 800)

        self.tiempo_transcurrido = 0
        self.avanzar_tiempo = False

        self.form_instance = form_instance
        self.player_name = self.form_instance.player_name

        self.cartas_numeros = list(range(1, 7)) * 2
        self.cartas_seleccionadas = []
        self.intentos_exitosos = 0
        self.intentos_fallidos = 0
        self.parejas_encontradas = []
        self.posibles_parejas = []

        # Establecer la posición de la ventana en el centro
        self.set_position(Gtk.WindowPosition.CENTER)


         # Crear un contenedor de tipo Overlay
        overlay = Gtk.Overlay()
        self.add(overlay)

        # Crear un widget de imagen y cargar la imagen de fondo
        image = Gtk.Image()
        image.set_from_file("img/fondo_medio.jpg")  # Reemplaza con la ruta de tu imagen
        overlay.add_overlay(image)

        vbox = Gtk.VBox(spacing=2)
        overlay.add_overlay(vbox)

        hbox1 = Gtk.Box(spacing=6)
        hbox2 = Gtk.Box(spacing=6)
        hbox3 = Gtk.Box(spacing=6)
        hbox4 = Gtk.Box(spacing=6)
        hbox5 = Gtk.Box(spacing=6)
        hbox6 = Gtk.Box(spacing=6)
        hbox7 = Gtk.Box(spacing=6)
        
        lbl_victoria = Gtk.Label()
        lbl_victoria.set_text("Completa todas las parejas, en el menor tiempo posible")
        lbl_victoria.get_style_context().add_class("titulo")
        vbox.pack_start(lbl_victoria, True, True, 7)
        

        self.entry_numero_carta = Gtk.Entry()
        self.entry_numero_carta.set_text("")
        hbox4.pack_start(self.entry_numero_carta, True, False, 0)

        self.imagenes = []

        for i in range(12):
            imagen = Gtk.Image.new_from_file("img/0.jpg")
            imagen.numero = self.cartas_numeros[i]

            if i < 4:
                hbox1.pack_start(imagen, True, True, 0)
            elif i>=4 and i<8:
                hbox2.pack_start(imagen, True, True, 0)
            else:
                hbox3.pack_start(imagen, True, True, 0)
           
            self.imagenes.append(imagen)

        vbox.pack_start(hbox1, True, True, 0)
        vbox.pack_start(hbox2, True, True, 0)
        vbox.pack_start(hbox3, True, True, 0)
        vbox.pack_start(hbox4, True, True, 0)
        vbox.pack_start(hbox5, True, True, 0)


        lbl_imagen = Gtk.Label()
        lbl_imagen.get_style_context ().add_class("informacion")
        hbox5.pack_start(lbl_imagen, True, True, 3)
        
        self.lbl_contador = Gtk.Label(label="Tiempo: 0 segundos")
        self.lbl_contador.get_style_context ().add_class("informacion")
        hbox5.pack_start(self.lbl_contador, True, True, 0)

        self.btn_iniciar_juego = Gtk.Button.new_with_label("Jugar de nuevo")
        self.btn_iniciar_juego.connect("clicked", self.on_iniciar_juego, lbl_imagen, lbl_victoria)
        self.btn_iniciar_juego.set_size_request(250, 100)
        self.btn_iniciar_juego.get_style_context ().add_class(Gtk.STYLE_CLASS_DESTRUCTIVE_ACTION)
        hbox6.pack_start(self.btn_iniciar_juego, False, True, 0)

        btn_seleccionar = Gtk.Button.new_with_label("Seleccionar carta")
        btn_seleccionar.connect("clicked", self.on_seleccionar_clicked, lbl_imagen, lbl_victoria)
        btn_seleccionar.set_size_request(250, 100)
        btn_seleccionar.get_style_context ().add_class(Gtk.STYLE_CLASS_DESTRUCTIVE_ACTION)
        hbox6.pack_start(btn_seleccionar, False, True, 0)

        btn_volver = Gtk.Button.new_with_label("Volver")
        btn_volver.connect("clicked", self.on_cerrar_clicked)
        btn_volver.set_size_request(250, 100)
        btn_volver.get_style_context ().add_class(Gtk.STYLE_CLASS_DESTRUCTIVE_ACTION)
        hbox7.pack_start(btn_volver, False, True, 0)

        btn_cerrar = Gtk.Button.new_with_label("Cerrar")
        btn_cerrar.connect("clicked", self.on_close_clicked)
        btn_cerrar.set_size_request(250, 100)
        btn_cerrar.get_style_context ().add_class(Gtk.STYLE_CLASS_DESTRUCTIVE_ACTION)
        hbox7.pack_start(btn_cerrar, False, True, 0)

        align_bottom = Gtk.Alignment.new(0.5, 0.5, 0, 0)
        align_bottom.add(hbox6)
        vbox.pack_start(align_bottom, False, False, 8)

        align_bottom2 = Gtk.Alignment.new(0.5, 1, 0, 0)
        align_bottom2.add(hbox7)
        vbox.pack_start(align_bottom2, False, False, 8)

        self.on_iniciar_juego(None, lbl_imagen, lbl_victoria)
        

    def on_iniciar_juego(self, button, lbl_imagen, lbl_victoria):
        lbl_victoria.set_text("Completa todas las parejas, en el menor tiempo posible")
        self.entry_numero_carta.show()
        self.btn_iniciar_juego.set_sensitive(False)
        self.tiempo_transcurrido = 0
        self.iniciar_cronometro(self)
        self.barajar_cartas()
        self.limpiar_cartas(lbl_imagen)
        self.cartas_seleccionadas = []
        self.intentos_exitosos = 0
        self.intentos_fallidos = 0
        lbl_imagen.set_text("Seleccione dos cartas:")
        self.avanzar_tiempo = True

    def on_seleccionar_clicked(self, button, lbl_imagen, lbl_victoria):
        numero_carta = int(self.entry_numero_carta.get_text())
        self.posibles_parejas.append(numero_carta)
        
        if numero_carta in self.parejas_encontradas:
            lbl_imagen.set_text("Has seleccionado una carta ya encontrada\nIntenta con otra.")
        else:

            if 1 <= numero_carta <= 12:
                posicion_carta = numero_carta - 1
                carta_seleccionada = self.imagenes[posicion_carta]

                if carta_seleccionada not in self.parejas_encontradas:
                    if carta_seleccionada not in self.cartas_seleccionadas:
                        lbl_imagen.set_text(f"Carta seleccionada: {numero_carta}")
                        carta_seleccionada.set_from_file(f"img/{(self.cartas_numeros[posicion_carta])}.jpg")
                        self.cartas_seleccionadas.append(carta_seleccionada)

                        if len(self.cartas_seleccionadas) == 2:
                            self.validar_parejas(lbl_imagen, lbl_victoria)
                            self.ocultar_cartas_despues_delay(2)
                            current_report_state = self.form_instance.current_report_state
                            if self.intentos_exitosos == 6:
                                lbl_victoria.set_text(f"¡Felicidades! Has encontrado todas las parejas!")
                                lbl_imagen.set_text(f"{self.intentos_exitosos} intentos exitosos \n{self.intentos_fallidos} intentos fallidos  \n{self.intentos_exitosos + self.intentos_fallidos} Total de intentos")
                                self.entry_numero_carta.set_sensitive(False)
                                self.detener_cronometro(self)
                                self.entry_numero_carta.hide()

                                print(current_report_state)
                                if current_report_state == True:
                                    text = f"""
    Resultados de la partida en nivel Medio, jugador {self.player_name}:
    Intentos totales: {self.intentos_exitosos + self.intentos_fallidos}
    Intentos fallidos: {self.intentos_fallidos}
    Intentos exitosos: {self.intentos_exitosos}
    Tiempo de solución: {self.tiempo_transcurrido} Segundos
                                        """
                                    print(text)
                                    with open("resultados.txt", "w") as archivo:
                                        archivo.write(text)


                    else:
                        lbl_imagen.set_text("Número de carta no válido o ya seleccionada. Inténtalo de nuevo.")
                        self.intentos_fallidos += 1

                else:
                    lbl_imagen.set_text("Esta pareja ya fue encontrada. Inténtalo de nuevo.")

            else:
                lbl_imagen.set_text("Número de carta no válido. Inténtalo de nuevo.")

    def validar_parejas(self, lbl_imagen, lbl_victoria):
        print(self.cartas_seleccionadas)

        if self.cartas_seleccionadas[0].get_property("file") == self.cartas_seleccionadas[1].get_property("file"):
            self.parejas_encontradas.append(self.posibles_parejas[0])
            self.parejas_encontradas.append(self.posibles_parejas[1])
            print(self.parejas_encontradas)
            lbl_imagen.set_text("¡Encontraste pareja!")
            self.cartas_seleccionadas[0].set_sensitive(False)  # Deshabilita las cartas emparejadas
            self.cartas_seleccionadas[1].set_sensitive(False)
            self.cartas_seleccionadas = []
            self.intentos_exitosos += 1
            self.posibles_parejas = []

            
        else:
            lbl_imagen.set_text("¡No es pareja! Intenta con otra carta.")
            self.intentos_fallidos += 1
            self.posibles_parejas = []

    def ocultar_cartas_despues_delay(self, delay):
        GLib.timeout_add(delay * 1000, self.ocultar_cartas)

    def ocultar_cartas(self):
        for imagen in self.cartas_seleccionadas:
            imagen.set_from_file("img/0.jpg")
            imagen.set_sensitive(True)
        self.cartas_seleccionadas = []
        self.entry_numero_carta.set_text("")

    def iniciar_cronometro(self, widget):
        self.tiempo_transcurrido = 0
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
        self.lbl_contador.set_text(f"Tiempo: {self.tiempo_transcurrido-1} segundos")


    def barajar_cartas(self):
        random.shuffle(self.cartas_numeros)
        print(self.cartas_numeros)

    def limpiar_cartas(self, lbl_imagen):
        for carta in self.imagenes:
            carta.set_from_file("img/0.jpg")
            carta.set_sensitive(True)
        lbl_imagen.set_text(f"Seleccione dos cartas: Intentos: {self.intentos_exitosos + self.intentos_fallidos}")

    def on_close_clicked(self, but_cerrar):
        Gtk.main_quit()
    
    def on_cerrar_clicked(self, widget):
        # Destroy the current window
        self.destroy()

        # Show the form window using the stored reference
        self.form_instance.show_menu()

