"""
#Integrantes:
1. Juan David Rincón, 202342032 - 3743
2. David Elian Taborda, 202341331 - 3743
3. Libardo Alejandro Quintero Gómez, 202342181 - 3743



Analisis del problema:


1.Se dispone de tres niveles de dificultad: Fácil (2x4), Medio (2x6), Difícil (4x4).
El nivel Fácil tiene un tablero de 2 filas y 4 columnas (8 cartas en total).
El nivel Medio tiene un tablero de 2 filas y 6 columnas (12 cartas en total).
El nivel Difícil tiene un tablero de 4 filas y 4 columnas (16 cartas en total).
2. La GUI debe incluir elementos como etiquetas, campos de entrada, botones y otras opciones necesarias.
3. Las imágenes deben cargarse de manera aleatoria en el tablero cada vez que se inicie el juego.
4. Debe existir una función para descubrir las imágenes y verificar si forman parejas. Si se encuentran parejas, se deben desactivar; de lo contrario, se vuelven a ocultar.
5. Al encontrar todas las parejas, se debe mostrar un mensaje indicando que el jugador ganó, junto con el número de intentos fallidos y totales.
6. Hay bonificaciones adicionales si se guardan los resultados en un archivo o si se agregan opciones extra al juego, como temporizador, niveles, tipos de imágenes, entre otros.

Pasos a seguir:

1. Planificación El juego: Diseñar una estructura para la lógica del juego y la interfaz gráfica.
2. Desarrollo de la lógica del juego: Crear funciones para cargar imágenes, manejar la lógica de descubrir parejas, contar intentos, determinar la victoria, etc.
3. Construcción de la interfaz gráfica: Utilizar Gtk u otra biblioteca para construir la interfaz con botones, etiquetas, campos de entrada y el tablero.
4. Integración de la lógica y la interfaz gráfica: Vincular las funciones del juego con los elementos de la interfaz gráfica para que se activen/desactiven las imágenes en respuesta a las acciones del jugador.
5. Pruebas y refinamiento: Probar el juego, corregir errores y mejorar la interfaz para una mejor experiencia de usuario.
6. Documentación y entrega: Preparar la documentación necesaria y entregar el proyecto con el código fuente y los archivos requeridos.

Consideraciones adicionales:

- Organización del código para que sea legible y modular.
- Utilizar funciones para tareas repetitivas o lógica compleja.
- Implementar un enfoque orientado a objetos si es adecuado para mejorar la estructura del código.
- Asegurarse de manejar excepciones y errores.
- Implementar el sistema de bonificaciones para obtener puntajes adicionales.

En resumen, el proyecto implica una combinación de lógica de programación, diseño de interfaz gráfica y manejo de eventos para crear un juego interactivo de búsqueda de parejas.

Pseudocodigo Facil.py
Procedimiento SeleccionarCarta(boton, lbl_imagen, lbl_victoria):
    // Obtener número de carta desde la entrada
    numero_carta = ConvertirAEntero(ObtenerTexto(self.entry_numero_carta))
    
    // Agregar el número de carta a la lista de posibles parejas
    AgregarALista(self.posibles_parejas, numero_carta)
    
    // Verificar si la carta ya ha sido encontrada
    Si numero_carta está en self.parejas_encontradas entonces:
        // Mostrar mensaje y sugerir otra carta
        EstablecerTexto(lbl_imagen, "Has seleccionado una carta ya encontrada\nIntenta con otra.")
        
    Sino:
        // Verificar que el número ingresado esté entre 1 y 8
        Si 1 <= numero_carta <= 8 entonces:
            // Obtener la posición de la carta seleccionada en la lista de imágenes
            posicion_carta = numero_carta - 1
            carta_seleccionada = ObtenerElementoEnPosicion(self.imagenes, posicion_carta)
            
            // Verificar si la carta ya ha sido seleccionada anteriormente
            Si carta_seleccionada no está en self.cartas_seleccionadas entonces:
                // Mostrar información sobre la carta seleccionada
                EstablecerTexto(lbl_imagen, "Carta seleccionada: " + ConvertirATexto(numero_carta))
                
                // Mostrar la imagen correspondiente a la carta seleccionada
                EstablecerImagenDesdeArchivo(carta_seleccionada, "img/" + ConvertirATexto(self.cartas_numeros[posicion_carta]) + ".jpg")
                
                // Agregar la carta seleccionada a la lista de cartas seleccionadas
                AgregarALista(self.cartas_seleccionadas, carta_seleccionada)
                
                // Verificar si se han seleccionado dos cartas
                Si LongitudDeLista(self.cartas_seleccionadas) == 2 entonces:
                    ValidarParejas(lbl_imagen, numero_carta)
                    OcultarCartasDespuesDelay(2)  // Cambiado a 1 segundo
                    
                    // Verificar si se han encontrado todas las parejas
                    Si self.intentos_exitosos == 4 entonces:
                        EstablecerTexto(lbl_victoria, "¡Felicidades! Has encontrado todas las parejas!")
                        EstablecerTexto(lbl_imagen, ConvertirATexto(self.intentos_exitosos) + " intentos exitosos \n" + ConvertirATexto(self.intentos_fallidos) + " intentos fallidos  \n" + ConvertirATexto(self.intentos_exitosos + self.intentos_fallidos) + " Total de intentos")
                        
                        // Habilitar el botón "Jugar de nuevo" y detener el cronómetro
                        HabilitarBoton(self.btn_iniciar_juego, Verdadero)
                        DetenerCronometro()
                        
                        // Ocultar la entrada para el número de carta
                        OcultarElemento(self.entry_numero_carta)
                        
                        // Verificar el estado del informe actual
                        current_report_state = ObtenerAtributo(self.form_instance, "current_report_state")
                        Imprimir(current_report_state)
                        
                        // Si el informe está activado, generar y guardar resultados
                        Si current_report_state es Verdadero entonces:
                            texto_resultados = GenerarTextoResultados()
                            Imprimir(texto_resultados)
                            
                            // Guardar los resultados en un archivo
                            AbrirYGuardarEnArchivo("resultados.txt", texto_resultados)
            Sino:
                EstablecerTexto(lbl_imagen, "Número de carta no válido o ya seleccionada. Inténtalo de nuevo.")
                Incrementar(self.intentos_fallidos, 1)
        Sino:
            EstablecerTexto(lbl_imagen, "Número de carta no válido. Inténtalo de nuevo.")Procedimiento IniciarJuego(boton, lbl_imagen, lbl_victoria):
    // Establecer el texto de la etiqueta de victoria
    EstablecerTexto(lbl_victoria, "Completa todas las parejas, en el menor tiempo posible")
    
    // Mostrar la entrada para el número de carta
    MostrarElemento(self.entry_numero_carta)
    
    // Deshabilitar el botón de iniciar juego
    EstablecerSensibilidad(self.btn_iniciar_juego, Falso)
    
    // Reiniciar el tiempo transcurrido y comenzar el cronómetro
    Establecer(self.tiempo_transcurrido, 0)
    IniciarCronometro(self)
    
    // Barajar las cartas
    BarajarCartas()
    
    // Limpiar las cartas en la interfaz gráfica
    LimpiarCartas(lbl_imagen)
    
    // Reiniciar variables de juego
    Establecer(self.cartas_seleccionadas, [])
    Establecer(self.intentos_exitosos, 0)
    Establecer(self.intentos_fallidos, 0)
    Establecer(self.avanzar_tiempo, Verdadero)
    
    // Establecer texto inicial en la etiqueta de imagen
    EstablecerTexto(lbl_imagen, "Seleccione dos cartas:")


Procedimiento SeleccionarCarta(boton, lbl_imagen, lbl_victoria):
    // Obtener número de carta desde la entrada
    numero_carta = ConvertirAEntero(ObtenerTexto(self.entry_numero_carta))
    
    // Agregar el número de carta a la lista de posibles parejas
    AgregarALista(self.posibles_parejas, numero_carta)
    
    // Verificar si la carta ya ha sido encontrada
    Si numero_carta está en self.parejas_encontradas entonces:
        // Mostrar mensaje y sugerir otra carta
        EstablecerTexto(lbl_imagen, "Has seleccionado una carta ya encontrada\nIntenta con otra.")
        
    Sino:
        // Verificar que el número ingresado esté entre 1 y 8
        Si 1 <= numero_carta <= 8 entonces:
            // Obtener la posición de la carta seleccionada en la lista de imágenes
            posicion_carta = numero_carta - 1
            carta_seleccionada = ObtenerElementoEnPosicion(self.imagenes, posicion_carta)
            
            // Verificar si la carta ya ha sido seleccionada anteriormente
            Si carta_seleccionada no está en self.cartas_seleccionadas entonces:
                // Mostrar información sobre la carta seleccionada
                EstablecerTexto(lbl_imagen, "Carta seleccionada: " + ConvertirATexto(numero_carta))
                
                // Mostrar la imagen correspondiente a la carta seleccionada
                EstablecerImagenDesdeArchivo(carta_seleccionada, "img/" + ConvertirATexto(self.cartas_numeros[posicion_carta]) + ".jpg")
                
                // Agregar la carta seleccionada a la lista de cartas seleccionadas
                AgregarALista(self.cartas_seleccionadas, carta_seleccionada)
                
                // Verificar si se han seleccionado dos cartas
                Si LongitudDeLista(self.cartas_seleccionadas) == 2 entonces:
                    ValidarParejas(lbl_imagen, numero_carta)
                    OcultarCartasDespuesDelay(2)  // Cambiado a 1 segundo
                    
                    // Verificar si se han encontrado todas las parejas
                    Si self.intentos_exitosos == 4 entonces:
                        EstablecerTexto(lbl_victoria, "¡Felicidades! Has encontrado todas las parejas!")
                        EstablecerTexto(lbl_imagen, ConvertirATexto(self.intentos_exitosos) + " intentos exitosos \n" + ConvertirATexto(self.intentos_fallidos) + " intentos fallidos  \n" + ConvertirATexto(self.intentos_exitosos + self.intentos_fallidos) + " Total de intentos")
                        
                        // Habilitar el botón "Jugar de nuevo" y detener el cronómetro
                        HabilitarBoton(self.btn_iniciar_juego, Verdadero)
                        DetenerCronometro()
                        
                        // Ocultar la entrada para el número de carta
                        OcultarElemento(self.entry_numero_carta)
                        
                        // Verificar el estado del informe actual
                        current_report_state = ObtenerAtributo(self.form_instance, "current_report_state")
                        Imprimir(current_report_state)
                        
                        // Si el informe está activado, generar y guardar resultados
                        Si current_report_state es Verdadero entonces:
                            texto_resultados = GenerarTextoResultados()
                            Imprimir(texto_resultados)
                            
                            // Guardar los resultados en un archivo
                            AbrirYGuardarEnArchivo("resultados.txt", texto_resultados)
            Sino:
                EstablecerTexto(lbl_imagen, "Número de carta no válido o ya seleccionada. Inténtalo de nuevo.")
                Incrementar(self.intentos_fallidos, 1)
        Sino:
            EstablecerTexto(lbl_imagen, "Número de carta no válido. Inténtalo de nuevo.")

Procedimiento BarajarCartas():
    Aleatorizar(self.cartas_numeros)
    Imprimir(self.cartas_numeros)

Procedimiento LimpiarCartas(lbl_imagen):
    Para cada carta en self.imagenes hacer:
        EstablecerImagen(carta, "img/0.jpg")
        Habilitar(carta)
    Fin Para
    EstablecerTexto(lbl_imagen, "Seleccione dos cartas:")

Procedimiento ValidarParejas(lbl_imagen, numero_carta):
    Imprimir(self.cartas_seleccionadas)

    Si self.cartas_seleccionadas[0].ObtenerPropiedad("file") == self.cartas_seleccionadas[1].ObtenerPropiedad("file") Entonces
        AgregarElemento(self.parejas_encontradas, self.posibles_parejas[0])
        AgregarElemento(self.parejas_encontradas, self.posibles_parejas[1])
        Imprimir(self.parejas_encontradas)
        EstablecerTexto(lbl_imagen, "¡Encontraste pareja!")
        Deshabilitar(self.cartas_seleccionadas[0])  // Deshabilita las cartas emparejadas
        Deshabilitar(self.cartas_seleccionadas[1])
        Limpiar(self.cartas_seleccionadas)
        Incrementar(self.intentos_exitosos)
        Limpiar(self.posibles_parejas)
    Sino
        EstablecerTexto(lbl_imagen, "¡No es pareja! Intenta con otra carta.")
        Incrementar(self.intentos_fallidos)
        Limpiar(self.posibles_parejas)
    Fin Si

Procedimiento OcultarCartasDespuesDelay(delay):
    AgregarTiempo(delay * 1000, OcultarCartas)

Procedimiento OcultarCartas():
    Para cada imagen en self.cartas_seleccionadas hacer:
        EstablecerImagen(imagen, "img/0.jpg")
        Habilitar(imagen)
    Fin Para
    Limpiar(self.cartas_seleccionadas)
    EstablecerTexto(self.entry_numero_carta, "")

Procedimiento IniciarCronometro(widget):
    Establecer(self.tiempo_transcurrido, 0)
    AgregarTiempo(1000, ActualizarTiempo)

Procedimiento ActualizarTiempo():
    Si self.avanzar_tiempo Entonces
        Incrementar(self.tiempo_transcurrido)
        ActualizarEtiqueta()
        Devolver Verdadero
    Sino
        Devolver Falso
    Fin Si

Procedimiento DetenerCronometro(widget):
    Establecer(self.avanzar_tiempo, Falso)

Procedimiento ActualizarEtiqueta():
    EstablecerTexto(self.lbl_contador, "Tiempo: " + ConvertirAString(self.tiempo_transcurrido - 1) + " segundos")

Procedimiento OnCerrarClicked(widget):
    Destruir(self)

    // Mostrar la ventana del formulario utilizando la referencia almacenada
    self.form_instance.MostrarMenu()

Procedimiento OnCloseClicked(but_cerrar):
    SalirGtk() 
    Pseudocodigo Medio.py
    Clase Form_medio:
    Atributos:
        tiempo_transcurrido = 0
        avanzar_tiempo = Falso
        cartas_numeros = []
        cartas_seleccionadas = []
        intentos_exitosos = 0
        intentos_fallidos = 0
        parejas_encontradas = []
        posibles_parejas = []

    Método _init_():
        // Inicialización de la ventana y contenedores
        ...

    Método on_iniciar_juego():
        Si self.entry_numero_carta es visible:
            OcultarElemento(self.entry_numero_carta)
        DeshabilitarBoton(self.btn_iniciar_juego)
        tiempo_transcurrido = 0
        iniciar_cronometro(self)
        barajar_cartas()
        limpiar_cartas(lbl_imagen)
        cartas_seleccionadas = []
        intentos_exitosos = 0
        intentos_fallidos = 0
        lbl_imagen = "Seleccione dos cartas:"

    Método on_seleccionar_clicked():
        numero_carta = ConvertirAEntero(ObtenerTexto(self.entry_numero_carta))
        AgregarALista(self.posibles_parejas, numero_carta)
        Si numero_carta está en self.parejas_encontradas:
            EstablecerTexto(lbl_imagen, "Has seleccionado una carta ya encontrada\nIntenta con otra.")
        Sino:
            Si 1 <= numero_carta <= 12:
                posicion_carta = numero_carta - 1
                carta_seleccionada = self.imagenes[posicion_carta]
                Si carta_seleccionada no está en self.parejas_encontradas:
                    Si carta_seleccionada no está en self.cartas_seleccionadas:
                        EstablecerTexto(lbl_imagen, f"Carta seleccionada: {numero_carta}")
                        EstablecerImagenDesdeArchivo(carta_seleccionada, f"img/{self.cartas_numeros[posicion_carta]}.jpg")
                        AgregarALista(self.cartas_seleccionadas, carta_seleccionada)
                        Si LongitudDeLista(self.cartas_seleccionadas) == 2:
                            ValidarParejas(lbl_imagen, lbl_victoria)
                            OcultarCartasDespuesDelay(2)
                            current_report_state = ObtenerAtributo(self.form_instance, "current_report_state")
                            Si self.intentos_exitosos == 6:
                                EstablecerTexto(lbl_victoria, "¡Felicidades! Has encontrado todas las parejas!")
                                EstablecerTexto(lbl_imagen, f"{self.intentos_exitosos} intentos exitosos \n{self.intentos_fallidos} intentos fallidos  \n{self.intentos_exitosos + self.intentos_fallidos} Total de intentos")
                                DeshabilitarElemento(self.entry_numero_carta)
                                DetenerCronometro(self)
                                OcultarElemento(self.entry_numero_carta)
                                Si current_report_state es Verdadero:
                                    texto_resultados = GenerarTextoResultados()
                                    Imprimir(texto_resultados)
                                    AbrirYGuardarEnArchivo("resultados.txt", texto_resultados)
                    Sino:
                        EstablecerTexto(lbl_imagen, "Número de carta no válido o ya seleccionada. Inténtalo de nuevo.")
                        Incrementar(self.intentos_fallidos, 1)
                Sino:
                    EstablecerTexto(lbl_imagen, "Número de carta no válido. Inténtalo de nuevo.")

    Método validar_parejas():
        Si LongitudDeLista(self.cartas_seleccionadas) == 2:
            Si self.cartas_seleccionadas[0].ObtenerPropiedad("file") == self.cartas_seleccionadas[1].ObtenerPropiedad("file"):
                AgregarElemento(self.parejas_encontradas, self.posibles_parejas[0])
                AgregarElemento(self.parejas_encontradas, self.posibles_parejas[1])
                Deshabilitar(self.cartas_seleccionadas[0])
                Deshabilitar(self.cartas_seleccionadas[1])
                Limpiar(self.cartas_seleccionadas)
                Incrementar(self.intentos_exitosos)
                Limpiar(self.posibles_parejas)
            Sino:
                Incrementar(self.intentos_fallidos)
                Limpiar(self.posibles_parejas)

    Método ocultar_cartas_despues_delay(delay):
        AgregarTiempo(delay * 1000, OcultarCartas)

    Método ocultar_cartas():
        Para cada imagen en self.cartas_seleccionadas hacer:
            EstablecerImagen(imagen, "img/0.jpg")
            Habilitar(imagen)
        Fin Para
        Limpiar(self.cartas_seleccionadas)
        EstablecerTexto(self.entry_numero_carta, "")

    Método iniciar_cronometro(widget):
        Establecer(self.tiempo_transcurrido, 0)
        AgregarTiempo(1000, ActualizarTiempo)

    Método actualizar_tiempo():
        Si self.avanzar_tiempo:
            Incrementar(self.tiempo_transcurrido)
            ActualizarEtiqueta()
            Devolver Verdadero
        Sino:
            Devolver Falso

    Método detener_cronometro(widget):
        Establecer(self.avanzar_tiempo, Falso)

    Método actualizar_etiqueta():
        EstablecerTexto(self.lbl_contador, "Tiempo: " + ConvertirAString(self.tiempo_transcurrido - 1) + " segundos")

    Método barajar_cartas():
        Aleatorizar(self.cartas_numeros)

    Método limpiar_cartas(lbl_imagen):
        Para cada carta en self.imagenes hacer:
            EstablecerImagen(carta, "img/0.jpg")
            Habilitar(carta)
        Fin Para
        EstablecerTexto(lbl_imagen, "Seleccione dos cartas:")

    Método on_close_clicked(but_cerrar):
        SalirGtk()

    Método on_cerrar_clicked(widget):
        Destruir(self)
        self.form_instance.MostrarMenu()

Procedimiento CrearInstanciaFormMedio():
    InstanciaFormMedio = Instanciar(Form_medio)  // Creación de la instancia de Form_medio
    Ejecutar(InstanciaFormMedio)  // Mostrar la interfaz gráfica de Form_medio

// Llamada al procedimiento para crear la instancia de Form_medio
CrearInstanciaFormMedio()
Pseudocodigos Dificil.py
Clase Form_dificil:
    Atributos:
        tiempo_transcurrido = 0
        avanzar_tiempo = Falso
        cartas_numeros = []
        cartas_seleccionadas = []
        intentos_exitosos = 0
        intentos_fallidos = 0
        parejas_encontradas = []
        posibles_parejas = []

    Método _init_():
        InicializarVentana()
        CrearContenedores()
        MostrarVentana()
        self.on_iniciar_juego(None, lbl_imagen, lbl_victoria)
        self.iniciar_cronometro(self)

    Método on_iniciar_juego():
        RestablecerValores()
        OcultarInputNumeroCarta()
        DeshabilitarBotonIniciarJuego()
        IniciarCronometro()
        BarajarCartas()
        LimpiarCartas()
        MostrarMensajeInicio()

    Método on_seleccionar_clicked():
        número_carta = ObtenerNumeroCarta()
        ValidarSeleccion(número_carta)
        Si LongitudDeLista(cartas_seleccionadas) == 2:
            VerificarParejas()
        Sino:
            MostrarMensajeError("Seleccione dos cartas válidas.")

    Método validar_parejas():
        Si CartasSonPareja():
            ActualizarIntentosExitosos()
            LimpiarListaPosiblesParejas()
        Sino:
            ActualizarIntentosFallidos()
            OcultarCartasDespuésDelay(2)
            LimpiarListaPosiblesParejas()

    Método iniciar_cronometro(widget):
        RetrasoCronometro(1000)
        Si avanzar_tiempo es Verdadero:
            ActualizarTiempo()

    Método actualizar_tiempo():
        Si avanzar_tiempo es Verdadero:
            IncrementarTiempo()
            ActualizarEtiqueta()
            Devolver Verdadero
        Sino:
            Devolver Falso

    Método detener_cronometro(widget):
        avanzar_tiempo = Falso

    Método actualizar_etiqueta():
        EstablecerTextoEtiquetaTiempo("Tiempo: " + ConvertirAString(tiempo_transcurrido - 1) + " segundos")

    Método limpiar_cartas():
        Para cada carta en self.imagenes hacer:
            EstablecerImagen(carta, "img/0.jpg")
            Habilitar(carta)
        Fin Para
        EstablecerTexto(lbl_imagen, f"Seleccione dos cartas: Intentos: {intentos_exitosos + intentos_fallidos}")

    Método on_close_clicked(but_cerrar):
        SalirGtk()

    Método on_cerrar_clicked(widget):
        Destruir(self)
        self.form_instance.MostrarMenu()

# Llamada a la función para crear la instancia de Form_dificil
CrearInstanciaFormDificil()

Procedimiento Retraso(delay):
    AgregarTiempo(delay * 1000, OcultarCartas)

Procedimiento RetrasoCronometro(tiempo):
    AgregarTiempo(tiempo, ActualizarTiempo)

Función CartasSonPareja():
    Si cartas_seleccionadas[0].ObtenerPropiedad("file") == cartas_seleccionadas[1].ObtenerPropiedad("file"):
        Devolver Verdadero
    Sino:
        Devolver Falso

Función ObtenerNumeroCarta():
    número_carta = ConvertirAEntero(ObtenerTexto(entry_numero_carta))
    Devolver número_carta

Función ValidarSeleccion(número_carta):
    Si 1 <= número_carta <= 16:
        posición_carta = número_carta - 1
        carta_seleccionada = imagenes[posición_carta]
        Si carta_seleccionada no está en cartas_seleccionadas:
            EstablecerTexto(lbl_imagen, f"Carta seleccionada: {número_carta}")
            EstablecerImagenDesdeArchivo(carta_seleccionada, f"img/{cartas_numeros[posición_carta]}.jpg")
            AgregarALista(cartas_seleccionadas, carta_seleccionada)
        Sino:
            MostrarMensajeError("Número de carta ya seleccionado. Inténtalo de nuevo.")
            Incrementar(intentos_fallidos, 1)
    Sino:
        MostrarMensajeError("Número de carta no válido. Inténtalo de nuevo.")
        Incrementar(intentos_fallidos, 1)

Función VerificarParejas():
    Si LongitudDeLista(cartas_seleccionadas) == 2:
        Si CartasSonPareja():
            validar_parejas()
        Sino:
            OcultarCartasDespuésDelay(2)

Función MostrarMensajeError(mensaje):
    EstablecerTexto(lbl_imagen, mensaje)

Función MostrarMensajeInicio():
    EstablecerTexto(lbl_imagen, "Seleccione dos cartas: Inicie el juego.")
Función ActualizarIntentosExitosos():
    Incrementar(intentos_exitosos)  # Incrementar el contador de intentos exitosos

Función ActualizarIntentosFallidos():
    Incrementar(intentos_fallidos)  # Incrementar el contador de intentos fallidos

Método OcultarCartasDespuésDelay(delay):
    Retraso(delay)  # Retrasar la ejecución de la función de ocultar cartas

Método OcultarCartas():
    Para cada imagen en cartas_seleccionadas hacer:
        EstablecerImagen(imagen, "img/0.jpg")  # Mostrar imagen de carta oculta
        Habilitar(imagen)  # Habilitar la carta
    Fin Para
    Limpiar(cartas_seleccionadas)  # Limpiar la lista de cartas seleccionadas
    EstablecerTexto(entry_numero_carta, "")  # Limpiar el campo de entrada del número de carta

Procedimiento CrearInstanciaFormDificil():
    InstanciaFormDificil = Instanciar(Form_dificil)  # Creación de la instancia de Form_dificil
    Ejecutar(InstanciaFormDificil)  # Mostrar la interfaz gráfica de Form_dificil

# Llamada al procedimiento para crear la instancia de Form_dificil
CrearInstanciaFormDificil()




Pseudocodigo Multiplayer.py
Clase VentanaMulti:
    Método __init__(self, form_instance):
        Crear ventana con título "Busca mi pareja" y tamaño 1200x800
        Configurar la posición de la ventana al centro
        Inicializar variables para el juego (tiempo, turnos, cartas, etc.)
        Crear contenedor Overlay y agregar imagen de fondo
        Crear cajas y contenedores para organizar la interfaz gráfica

        Crear elementos de interfaz: etiquetas, botones, entradas, etc.
        Vincular botones a sus funciones correspondientes
        Mostrar la ventana de juego

        Llamar al método on_iniciar_juego() para empezar el juego

    Método on_iniciar_juego(self, button, lbl_imagen, lbl_victoria):
        Configurar interfaz para un nuevo juego
        Barajar las cartas para ambos jugadores
        Limpiar las cartas de la interfaz
        Restablecer variables del juego
        Iniciar el cronómetro

    Método on_seleccionar_clicked(self, button, lbl_imagen, lbl_victoria, btn_seleccionar):
        Si turno es 1:
            Obtener número de carta ingresado por jugador uno
            Agregar el número a la lista de posibles parejas para jugador uno

            Si el número de carta ya ha sido encontrado:
                Mostrar mensaje: "Has seleccionado una carta ya encontrada. Intenta con otra."
            Sino:
                Si el número de carta está entre 1 y 8:
                    Obtener la posición de la carta seleccionada
                    Mostrar la carta seleccionada en la interfaz gráfica
                    Agregar la carta seleccionada a la lista de cartas seleccionadas para jugador uno

                    Si se han seleccionado dos cartas:
                        Validar si forman una pareja
                        Ocultar las cartas después de un breve retraso
                        Cambiar al turno del jugador dos
                        Actualizar mensaje en la interfaz

                Sino:
                    Mostrar mensaje: "Número de carta no válido. Inténtalo de nuevo."

        Sino:
            Obtener número de carta ingresado por jugador dos
            (Realizar acciones similares a las realizadas para el jugador uno pero aplicadas al jugador dos)

    Método barajar_cartas_ply1(self):
        Barajar aleatoriamente las cartas para el jugador 1

    Método barajar_cartas_ply2(self):
        Barajar aleatoriamente las cartas para el jugador 2

    Método limpiar_cartas(self):
        Restablecer todas las cartas de la interfaz a su estado inicial

    Método validar_parejas(self, lbl_imagen, numero_carta):
        Si es el turno del jugador uno:
            Si las cartas seleccionadas forman una pareja válida:
                Agregar las cartas a la lista de parejas encontradas para jugador uno
                Deshabilitar las cartas emparejadas en la interfaz
                Actualizar variables de juego (intentos, parejas, etc.)
                Limpiar las listas de cartas seleccionadas y posibles parejas

            Sino:
                Actualizar mensajes e incrementar intentos fallidos

        Sino:
            (Realizar acciones similares para validar las parejas del jugador dos)

    (Métodos restantes para controlar el cronómetro, actualización de etiquetas, cierre de ventana, etc.)
Método ocultar_cartas_despues_delay(self, delay):
        Programar un retardo para ocultar las cartas después de un tiempo determinado

    Método ocultar_cartas(self):
        Si es el turno del jugador dos:
            Ocultar las cartas seleccionadas por el jugador uno
            Limpiar la entrada de texto

        Sino:
            Ocultar las cartas seleccionadas por el jugador dos
            Limpiar la entrada de texto

    Método iniciar_cronometro(self, widget):
        Iniciar el cronómetro actualizando el tiempo cada segundo

    Método actualizar_tiempo(self):
        Si el juego está en curso:
            Incrementar el tiempo transcurrido
            Actualizar la etiqueta que muestra el tiempo transcurrido
            Continuar actualizando el tiempo

        Sino:
            Detener la actualización del tiempo

    Método detener_cronometro(self, widget):
        Detener el avance del tiempo

    Método actualizar_etiqueta(self):
        Actualizar la etiqueta que muestra el tiempo transcurrido

    Método on_cerrar_clicked(self, widget):
        Cerrar la ventana actual
        Mostrar la ventana del formulario principal

    Método on_close_clicked(self, but_cerrar):
        Salir (Gtk)


"""
