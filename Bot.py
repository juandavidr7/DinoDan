import gi
from gi.repository import Gtk, GLib
import random

gi.require_version("Gtk", "3.0")

    # Esta es la función más perra, aquí se hacen varias cosas


class VentanaBot(Gtk.Window):
    def __init__(self, form_instance):
        super().__init__(title="Busca mi pareja")
        self.set_default_size(50, 50)
        self.set_border_width(1)
        # Establecer la posición de la ventana en el centro

        self.connect("show", self.StartGame)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.tiempo_transcurrido = 0
        self.avanzar_tiempo = False
        self.form_instance = form_instance

        self.cartas_numeros = [1, 2, 3, 4, 1, 2, 3, 4]
        self.turno = 1
        self.cartas_seleccionadas_ply1 = []
        self.parejas_encontradas_ply1 = []
        self.posibles_parejas_ply1 = []
        self.cartas_seleccionadas_ply2 = []
        self.parejas_encontradas_ply2 = []
        self.posibles_parejas_ply2 = []


        vbox = Gtk.VBox(spacing=2)
        self.add(vbox)

        MultHbox = Gtk.Box(spacing=2)

        vbox1 = Gtk.VBox(spacing=2)
        vbox2 = Gtk.VBox(spacing=2)
        

        hbox1 = Gtk.Box(spacing=6)
        hbox2 = Gtk.Box(spacing=6)
        hbox4 = Gtk.Box(spacing=6)
        hbox5 = Gtk.Box(spacing=6)
        hbox3 = Gtk.Box(spacing=6)

        self.entry_numero_carta = Gtk.Entry()
        self.entry_numero_carta.set_text("")
        hbox3.pack_start(self.entry_numero_carta, True, True, 0)

        # Aquí comienza la creación de las imagenes 
        self.imagenes = []
        self.imagenes2 = []
        for i in range(8):
            # Asignación de cada uno de las imagenes a un espacio de la interfaz
            imagen = Gtk.Image.new_from_file("img/0.jpg")
            imagen2 = Gtk.Image.new_from_file("img/0.jpg")
            imagen.numero = self.cartas_numeros[i]
            imagen2.numero = self.cartas_numeros[i]
            # Esto es pa que quede organizado bien bonito xd
            if i < 4:
                hbox1.pack_start(imagen, True, True, 0)
                hbox4.pack_start(imagen2, True, True, 0)
            else:
                hbox2.pack_start(imagen, True, True, 0)
                hbox5.pack_start(imagen2, True, True, 0)
            # Y acá se está creando un array, que me va guardar todas las imagenes en imagenes[]
            self.imagenes.append(imagen)
            self.imagenes2.append(imagen2)

        # Todo esto es pura creación de botones, vinculación, asociación con las funciones
        lbl_ply1 = Gtk.Label()
        lbl_ply1.set_text("Jugador 1")
        lbl_ply2= Gtk.Label()
        lbl_ply2.set_text("Jugador 2")
        vbox1.pack_start(lbl_ply1, True, True, 0)
        vbox2.pack_start(lbl_ply2, True, True, 0)
        
        vbox1.pack_start(hbox1, True, True, 0)
        vbox1.pack_start(hbox2, True, True, 0)
        vbox2.pack_start(hbox4, True, True, 0)
        vbox2.pack_start(hbox5, True, True, 0)
        MultHbox.pack_start(vbox1, True, True, 0)
        MultHbox.pack_start(vbox2, True, True, 0)
        vbox.pack_start(MultHbox, True, True, 0)
        vbox.pack_start(hbox3, True, True, 0)

        lbl_imagen = Gtk.Label()
        lbl_imagen.set_text("Pulse en <<Iniciar Juego>> para comenzar")
        vbox.pack_start(lbl_imagen, True, True, 7)

        self.lbl_turnos = Gtk.Label()
        self.lbl_turnos.set_text("")
        vbox.pack_start(self.lbl_turnos, True, True, 0)
        
        lbl_victoria = Gtk.Label()
        lbl_victoria.set_text("Completa todas las parejas posibles, en el menor tiempo posible")
        vbox.pack_start(lbl_victoria, True, True, 7)

        self.lbl_contador = Gtk.Label(label="Tiempo: 0 segundos")
        vbox.pack_start(self.lbl_contador, True, True, 0)

        btn_seleccionar = Gtk.Button.new_with_label("Seleccionar carta")
        btn_seleccionar.connect("clicked", self.on_seleccionar_clicked, lbl_imagen, lbl_victoria, btn_seleccionar)
        vbox.pack_start(btn_seleccionar, True, True, 0)

        btn_volver = Gtk.Button.new_with_label("Volver")
        btn_volver.connect("clicked", self.on_cerrar_clicked)
        vbox.pack_start(btn_volver, True, True, 0)
        
        btn_cerrar = Gtk.Button.new_with_label("Cerrar")
        btn_cerrar.connect("clicked", self.on_close_clicked)
        vbox.pack_start(btn_cerrar, True, True, 0)

    # Función para llamar a las funciones principales e inicie el juego
    
    def StartGame(self, widget):
        self.iniciar_cronometro(self)
        self.barajar_cartas()
        self.limpiar_cartas()
        self.lbl_turnos.set_text("Turno para el jugador uno")
        self.cartas_seleccionadas_ply1 = []
        self.cartas_seleccionadas_ply = []
        self.intentos_exitosos = 0
        self.intentos_exitosos2 = 0
        self.turno = 1
        self.intentos_fallidos = 0
        self.intentos_fallidos2 = 0
        self.avanzar_tiempo = True
        
    # Esta es la función más perra, aquí se hacen varias cosas
    def on_seleccionar_clicked(self, button, lbl_imagen, lbl_victoria, btn_seleccionar):
        if self.turno == 1:
            self.lbl_turnos.set_text("Turno para el jugador uno")
            numero_carta = int(self.entry_numero_carta.get_text())
            self.posibles_parejas_ply1.append(numero_carta)
            
            if numero_carta in self.parejas_encontradas_ply1:
                lbl_imagen.set_text("Has seleccionado una carta ya encontrada\nIntenta con otra.")
                # Verificar que el número ingresado en la "Entry" esté entre 1 y 8
            else:
                if 1 <= numero_carta <= 8:
                    posicion_carta = numero_carta - 1
                    carta_seleccionada = self.imagenes[posicion_carta]
                    
                    # Acá lo que hace es que va guardando temporalmente la carta seleccionada,
                    # dentro de otro array de cartas seleccionadas para después hacer comparaciones
                    if carta_seleccionada not in self.cartas_seleccionadas_ply1:
                        lbl_imagen.set_text(f"Carta seleccionada: {numero_carta}")
                        carta_seleccionada.set_from_file(f"img/{(self.cartas_numeros[posicion_carta])}.jpg")
                        self.cartas_seleccionadas_ply1.append(carta_seleccionada)

                        if len(self.cartas_seleccionadas_ply1) == 2:
                            
                            self.validar_parejas(lbl_imagen, numero_carta)
                            self.ocultar_cartas_despues_delay(2)  # Cambiado a 1 segundo
                            self.turno = 2
                            self.lbl_turnos.set_text("Turno para el jugador dos")
                            if self.intentos_exitosos == 4:
                                    lbl_victoria.set_text(f"¡Felicidades! Ha ganado el jugador 1 en {self.intentos_exitosos} intentos exitosos, {self.intentos_fallidos} intentos fallidos, con un total de {self.intentos_exitosos + self.intentos_fallidos} intentos.")
                                    self.lbl_turnos.set_text("Fin del juego")
                                    self.entry_numero_carta.set_sensitive(False)
                                    btn_seleccionar.set_sensitive(False)
                                    self.detener_cronometro(self)
                                    current_report_state = self.form_instance.report_state
                                    print(current_report_state)
                                    if current_report_state == True:
                                        text = f"""
    Resultados de la partida Multijugador:
    Ganador: Jugador 1
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
                    lbl_imagen.set_text("Número de carta no válido. Inténtalo de nuevo.")
        else:
            
            numero_carta = int(self.entry_numero_carta.get_text())
            self.posibles_parejas_ply2.append(numero_carta)
            
            if numero_carta in self.parejas_encontradas_ply2:
                lbl_imagen.set_text("Has seleccionado una carta ya encontrada\nIntenta con otra.")
                # Verificar que el número ingresado en la "Entry" esté entre 1 y 8
            else:
                if 1 <= numero_carta <= 8:
                    posicion_carta = numero_carta - 1
                    carta_seleccionada = self.imagenes2[posicion_carta]
                    
                    # Acá lo que hace es que va guardando temporalmente la carta seleccionada,
                    # dentro de otro array de cartas seleccionadas para después hacer comparaciones
                    if carta_seleccionada not in self.cartas_seleccionadas_ply2:
                        lbl_imagen.set_text(f"Carta seleccionada: {numero_carta}")
                        carta_seleccionada.set_from_file(f"img/{(self.cartas_numeros[posicion_carta])}.jpg")
                        self.cartas_seleccionadas_ply2.append(carta_seleccionada)

                        if len(self.cartas_seleccionadas_ply2) == 2:
                            
                            self.validar_parejas(lbl_imagen, numero_carta)
                            self.ocultar_cartas_despues_delay(2)  # Cambiado a 1 segundo
                            self.turno = 1
                            self.lbl_turnos.set_text("Turno para el jugador uno")
                            if self.intentos_exitosos2 == 4:
                                    lbl_victoria.set_text(f"¡Felicidades! Ha ganado el jugador 2 en {self.intentos_exitosos2} intentos exitosos, {self.intentos_fallidos2} intentos fallidos, con un total de {self.intentos_exitosos2 + self.intentos_fallidos2} intentos.")
                                    self.lbl_turnos.set_text("Fin del juego")
                                    
                                    self.entry_numero_carta.set_sensitive(False)
                                    btn_seleccionar.set_sensitive(False)
                                    self.detener_cronometro(self)
                                    current_report_state = self.form_instance.report_state
                                    print(current_report_state)
                                    if current_report_state == True:
                                        text = f"""
    Resultados de la partida en Multijugador:
    Ganador: Jugador 2
    Intentos totales: {self.intentos_exitosos2 + self.intentos_fallidos2}
    Intentos fallidos: {self.intentos_fallidos2}
    Intentos exitosos: {self.intentos_exitosos2}
    Tiempo de solución: {self.tiempo_transcurrido} Segundos
                                        """
                                        print(text)
                                        with open("resultados.txt", "w") as archivo:
                                            archivo.write(text)
                                    
                                    
                            
                    else:
                        lbl_imagen.set_text("Número de carta no válido o ya seleccionada. Inténtalo de nuevo.")
                        self.intentos_fallidos2 += 1
                else:
                    lbl_imagen.set_text("Número de carta no válido. Inténtalo de nuevo.")



    # Esta funcion solo baraja las cartas, para que no salga siempre iguales xd
    def barajar_cartas(self):
        random.shuffle(self.cartas_numeros)
        print(self.cartas_numeros)

    # Esto es pa que no se vean las cartas como tal
    def limpiar_cartas(self):
        for carta in self.imagenes:
            carta.set_from_file("img/0.jpg")
            carta.set_sensitive(True)
        for carta in self.imagenes2:
            carta.set_from_file("img/0.jpg")
            carta.set_sensitive(True)
        

    # Acá se van a hacer las validaciones con los dos arrays creados previamente
    def validar_parejas(self, lbl_imagen, numero_carta):
        print(self.cartas_seleccionadas_ply1)
        print(self.cartas_seleccionadas_ply2)
        if self.turno == 1:
            if self.cartas_seleccionadas_ply1[0].get_property("file")== self.cartas_seleccionadas_ply1[1].get_property("file"):
                self.parejas_encontradas_ply1.append(self.posibles_parejas_ply1[0])
                self.parejas_encontradas_ply1.append(self.posibles_parejas_ply1[1])
                print(self.parejas_encontradas_ply1)
                lbl_imagen.set_text("¡Encontraste pareja!")
                self.cartas_seleccionadas_ply1[0].set_sensitive(False)  # Deshabilita las cartas emparejadas
                self.cartas_seleccionadas_ply1[1].set_sensitive(False)
                self.cartas_seleccionadas_ply1 = []
                self.intentos_exitosos += 1
                self.posibles_parejas_ply1 = []
            else:
                lbl_imagen.set_text("¡No es pareja! Intenta con otra carta.")
                self.intentos_fallidos += 1
                self.posibles_parejas_ply1 = []
        else:
            if self.cartas_seleccionadas_ply2[0].get_property("file")== self.cartas_seleccionadas_ply2[1].get_property("file"):
                self.parejas_encontradas_ply2.append(self.posibles_parejas_ply2[0])
                self.parejas_encontradas_ply2.append(self.posibles_parejas_ply2[1])
                print(self.parejas_encontradas_ply2)
                lbl_imagen.set_text("¡Encontraste pareja!")
                self.cartas_seleccionadas_ply2[0].set_sensitive(False)  # Deshabilita las cartas emparejadas
                self.cartas_seleccionadas_ply2[1].set_sensitive(False)
                self.cartas_seleccionadas_ply2 = []
                self.intentos_exitosos2 += 1
                self.posibles_parejas_ply2 = []
            else:
                lbl_imagen.set_text("¡No es pareja! Intenta con otra carta.")
                self.intentos_fallidos2 += 1
                self.posibles_parejas_ply2 = []

    # Aca se define el tiempo que van a tardar en volverse a ocultar
    def ocultar_cartas_despues_delay(self, delay):
        GLib.timeout_add(delay * 1000, self.ocultar_cartas)

    # Esto es para que las cartas se vuelvan a ocultar, si no se encuentra que sean pareja
    def ocultar_cartas(self):
        if self.turno == 2:
            for imagen in self.cartas_seleccionadas_ply1:
                imagen.set_from_file("img/0.jpg")
                imagen.set_sensitive(True)
            self.cartas_seleccionadas_ply1 = []
            self.entry_numero_carta.set_text("")
        else:
            for imagen2 in self.cartas_seleccionadas_ply2:
                imagen2.set_from_file("img/0.jpg")
                imagen2.set_sensitive(True)
            self.cartas_seleccionadas_ply2 = []
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
