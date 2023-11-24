import gi
from gi.repository import Gtk, GLib
import random

gi.require_version("Gtk", "3.0")

class Form_facil(Gtk.Window):
    def __init__(self, form_instance):
        super().__init__(title="Busca mi pareja")
        self.set_default_size(50, 50)
        self.set_border_width(1)
        # Establecer la posición de la ventana en el centro
        self.set_position(Gtk.WindowPosition.CENTER)
        self.tiempo_transcurrido = 0
        self.avanzar_tiempo = False
        self.form_instance = form_instance

        self.cartas_numeros = [1, 2, 3, 4, 1, 2, 3, 4]
        self.cartas_seleccionadas = []
        self.parejas_encontradas = []
        self.posibles_parejas = []

        vbox = Gtk.VBox(spacing=2)
        self.add(vbox)

        hbox1 = Gtk.Box(spacing=6)
        hbox2 = Gtk.Box(spacing=6)
        hbox3 = Gtk.Box(spacing=6)

        self.entry_numero_carta = Gtk.Entry()
        self.entry_numero_carta.set_text("")
        hbox3.pack_start(self.entry_numero_carta, True, True, 0)

        # Aquí comienza la creación de las imagenes 
        self.imagenes = []
        for i in range(8):
            # Asignación de cada uno de las imagenes a un espacio de la interfaz
            imagen = Gtk.Image.new_from_file("img/0.jpeg")
            imagen.numero = self.cartas_numeros[i]
            # Esto es pa que quede organizado bien bonito xd
            if i < 4:
                hbox1.pack_start(imagen, True, True, 0)
            else:
                hbox2.pack_start(imagen, True, True, 0)
            # Y acá se está creando un array, que me va guardar todas las imagenes en imagenes[]
            self.imagenes.append(imagen)

        # Todo esto es pura creación de botones, vinculación, asociación con las funciones
        vbox.pack_start(hbox1, True, True, 0)
        vbox.pack_start(hbox2, True, True, 0)
        vbox.pack_start(hbox3, True, True, 0)

        lbl_imagen = Gtk.Label()
        lbl_imagen.set_text("Pulse en <<Iniciar Juego>> para comenzar")
        vbox.pack_start(lbl_imagen, True, True, 7)
        
        lbl_victoria = Gtk.Label()
        lbl_victoria.set_text("Completa todas las parejas posibles, en el menor tiempo posible")
        vbox.pack_start(lbl_victoria, True, True, 7)

        self.lbl_contador = Gtk.Label(label="Tiempo: 0 segundos")
        vbox.pack_start(self.lbl_contador, True, True, 0)

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

    # Función para llamar a las funciones principales e inicie el juego
    def on_iniciar_juego(self, button, lbl_imagen):
        self.iniciar_cronometro(self)
        self.barajar_cartas()
        self.limpiar_cartas(lbl_imagen)
        self.cartas_seleccionadas = []
        self.intentos_exitosos = 0
        self.intentos_fallidos = 0
        self.avanzar_tiempo = True
        
        lbl_imagen.set_text("Seleccione dos cartas: Intentos: 0")
    # Esta es la función más perra, aquí se hacen varias cosas
    def on_seleccionar_clicked(self, button, lbl_imagen, lbl_victoria):
        numero_carta = int(self.entry_numero_carta.get_text())
        self.posibles_parejas.append(numero_carta)
        
        if numero_carta in self.parejas_encontradas:
            lbl_imagen.set_text("Has seleccionado una carta ya encontrada\nIntenta con otra.")
            # Verificar que el número ingresado en la "Entry" esté entre 1 y 8
        else:
            if 1 <= numero_carta <= 8:
                posicion_carta = numero_carta - 1
                carta_seleccionada = self.imagenes[posicion_carta]
                
                # Acá lo que hace es que va guardando temporalmente la carta seleccionada,
                # dentro de otro array de cartas seleccionadas para después hacer comparaciones
                if carta_seleccionada not in self.cartas_seleccionadas:
                    lbl_imagen.set_text(f"Carta seleccionada: {numero_carta}")
                    carta_seleccionada.set_from_file(f"img/{(self.cartas_numeros[posicion_carta])}.jpeg")
                    self.cartas_seleccionadas.append(carta_seleccionada)

                    if len(self.cartas_seleccionadas) == 2:
                        self.validar_parejas(lbl_imagen, numero_carta)
                        self.ocultar_cartas_despues_delay(2)  # Cambiado a 1 segundo
                        if self.intentos_exitosos == 4:
                                lbl_victoria.set_text(f"¡Felicidades! Has encontrado todas las parejas en {self.intentos_exitosos} intentos exitosos, {self.intentos_fallidos} intentos fallidos, con un total de {self.intentos_exitosos + self.intentos_fallidos} intentos.")
                                self.entry_numero_carta.set_sensitive(False)
                                self.detener_cronometro(self)
                        
                else:
                    lbl_imagen.set_text("Número de carta no válido o ya seleccionada. Inténtalo de nuevo.")
                    self.intentos_fallidos += 1
            else:
                lbl_imagen.set_text("Número de carta no válido. Inténtalo de nuevo.")

    # Esta funcion solo baraja las cartas, para que no salga siempre iguales xd
    def barajar_cartas(self):
        random.shuffle(self.cartas_numeros)
        print(self.cartas_numeros)

    # Esto es pa que no se vean las cartas como tal
    def limpiar_cartas(self, lbl_imagen):
        for carta in self.imagenes:
            carta.set_from_file("img/0.jpeg")
            carta.set_sensitive(True)
        lbl_imagen.set_text("Seleccione dos cartas:")

    # Acá se van a hacer las validaciones con los dos arrays creados previamente
    def validar_parejas(self, lbl_imagen, numero_carta):
        print(self.cartas_seleccionadas)
        
        
        if self.cartas_seleccionadas[0].get_property("file")== self.cartas_seleccionadas[1].get_property("file"):
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

    # Aca se define el tiempo que van a tardar en volverse a ocultar
    def ocultar_cartas_despues_delay(self, delay):
        GLib.timeout_add(delay * 1000, self.ocultar_cartas)

    # Esto es para que las cartas se vuelvan a ocultar, si no se encuentra que sean pareja
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

    def on_cerrar_clicked(self, widget):
        # Destroy the current window
        self.destroy()

        # Show the form window using the stored reference
        self.form_instance.show_menu()

    # Cerrar el programa
    def on_close_clicked(self, but_cerrar):
        Gtk.main_quit()