import random

# Función para crear la ruleta (sin cambios)
def crear_ruleta():
    ruleta = {}
    ruleta[0] = "Verde"
    ruleta['00'] = "Verde"
    x = 0
    j = 1
    for i in range(1, 38, 9):
        x ^= 1
        while j < i and x == 1:
            ruleta[j] = "rojo" if j % 2 == 0 else "negro"
            j += 1
        while j <= i and x == 0:
            ruleta[j] = "negro" if j % 2 == 0 else "rojo"
            j += 1
    return ruleta

def girar_ruleta(ruleta):
    numero_ganador = random.choice([0, "00"] + list(range(1, 37)))
    return numero_ganador, ruleta[numero_ganador]

# Mostrar resultado del juego
def mostrar_resultado(jugador, resultado, apuesta, ganancia=0):
    if resultado:
        jugador["saldo"] += ganancia
        print(f"\n\u2714 \u001b[32m\u2714 \u001b[0m¡Felicidades {jugador['nombre']}! Ganaste {ganancia}. Nuevo saldo: {jugador['saldo']}\n")
    else:
        jugador["saldo"] -= apuesta
        print(f"\u2718 Lo siento, {jugador['nombre']}, perdiste la apuesta. Nuevo saldo: {jugador['saldo']}\n")

# Verificar cantidad válida para apostar
def verificar_cantidad_apostar(jugador):
    while True:
        try:
            apuesta = int(input(f"{jugador['nombre']}, ¿cuánto deseas apostar? (Saldo: {jugador['saldo']}): "))
            if 0 < apuesta <= jugador['saldo']:
                return apuesta
            else:
                print("Cantidad no válida. Debe ser mayor que cero y menor o igual a tu saldo disponible.")
        except ValueError:
            print("Por favor ingresa un número válido.")

# Pedir opción válida
def pedir_opcion(prompt, valores_permitidos):
    while True:
        try:
            opcion = int(input(prompt))
            if opcion in valores_permitidos:
                return opcion
            else:
                print(f"Opción inválida. Por favor selecciona entre {valores_permitidos}.")
        except ValueError:
            print("Entrada no válida. Por favor ingresa un número.")

def opcion (ruleta,jugadores_activos,jugador):
    while True:
        print("\n------MENU DE APUESTAS------")
        print("1. Columna - Todos los números en una línea (Pago: 2:1)")
        print("2. Docena - Todos los números de la docena (Pago: 2:1)")
        print("3. Color - Apuesta al negro o rojo (Pago: 1:1)")
        print("4. Un Número - Apuesta a un número específico (Pago: 35:1)")
        print("5. Dos Números - Apuesta a dos números adyacentes (Pago: 17:1)")
        print("6. Tres Números - Apuesta a tres números en fila (Pago: 11:1)")
        print("7. Cuatro Números - Apuesta a cuatro números en cuadro (Pago: 8:1)")
        print("8. Cinco Números - Apuesta a cinco números específicos (Pago: 6:1)")
        print("9. Seis Números - Apuesta a seis números consecutivos (Pago: 5:1)")
        print("0. Salir")
        opcion = input("Selecciona el tipo de apuesta (0 para salir): ")
        if opcion == "0":
            return False
        elif opcion == "1":
            print("Apuesta en columna")
            apostar_columna(ruleta,jugador)
            return True
        elif opcion == "2":
            print("Apuesta en docena")
            apostar_docena(ruleta,jugador)
            return True
        elif opcion == "3":
            print("Apuesta en color")
            apostar_color(ruleta, jugador)
            return True
        elif opcion == "4":
            print("Apuesta un numero")
            apostar_numeros(ruleta, jugador, 1, 35)
            return True
        elif opcion == "5":
            print("Apuesta dos numeros")
            apostar_numeros(ruleta, jugador, 2, 17)
            return True
        elif opcion == "6":
            print("Apuesta tres numeros")
            apostar_numeros(ruleta, jugador, 3, 11)
            return True
        elif opcion == "7":
            print("Apuesta cuatro numeros")
            apostar_numeros(ruleta, jugador, 4, 8)
            return True
        elif opcion == "8":
            print("Apuesta ucinco numeros")
            apostar_numeros(ruleta, jugador, 5, 6)
            return True
        elif opcion == "9":
            print("Apuesta seis numeros")
            apostar_numeros(ruleta, jugador, 6, 5)
            return True
        else:
            print("Opción inválida. Por favor, selecciona un número del 0 al 9.")

#verifica el saldo del jugador
def verificar_saldo(jugador, jugadores_activos):
    """
    Verifica si el jugador tiene saldo suficiente. Si no, lo elimina del juego.
    """
    if jugador["saldo"] <= 0:
        print(f"{jugador['nombre']} no tiene saldo suficiente y ha salido del juego.")
        jugadores_activos.remove(jugador)
        return False
    return True

# Función para apostar en la columna
def apostar_columna(ruleta,jugador):
    print("\nHas seleccionado: Columna - Todos los números en una línea")
    print("Elige una columna para apostar:")
    print("1. Columna 1 (1, 4, 7, ..., 34)")
    print("2. Columna 2 (2, 5, 8, ..., 35)")
    print("3. Columna 3 (3, 6, 9, ..., 36)")
    columna = pedir_opcion("Selecciona una columna para apostar: ", [1, 2, 3])
    apuesta = verificar_cantidad_apostar(jugador)
    numero_ganador, color_ganador = girar_ruleta(ruleta)
    print(f"\u00a1La ruleta gira! Resultado: {numero_ganador} ({color_ganador})")

    if numero_ganador != "00" and numero_ganador != 0 and (numero_ganador - 1) % 3 + 1 == columna:
        mostrar_resultado(jugador, True, apuesta, ganancia=apuesta * 2)
    else:
        mostrar_resultado(jugador, False, apuesta)

# Función para apostar en una docena
def apostar_docena(ruleta,jugador):
    print("\nHas seleccionado: docena - grupos de doce")
    print("Elige una docena para apostar:")
    print("1. Docena 1 (1 al 12)")
    print("2. Docena 2 (13 al 24)")
    print("3. Docena 3 (25 al 36)")

    docena = pedir_opcion("Selecciona una docena para apostar: ", [1, 2, 3])
    apuesta = verificar_cantidad_apostar(jugador)
    numero_ganador, color_ganador = girar_ruleta(ruleta)
    print(f"\u00a1La ruleta gira! Resultado: {numero_ganador} ({color_ganador})")

    if numero_ganador != "00" and numero_ganador != 0:  # Ignoramos 0 y 00
        # Determinar el rango de la docena seleccionada
        if (docena == 1 and 1 <= numero_ganador <= 12) or \
           (docena == 2 and 13 <= numero_ganador <= 24) or \
           (docena == 3 and 25 <= numero_ganador <= 36):
            mostrar_resultado(jugador, True, apuesta, ganancia=apuesta * 2)  # Pago 2:1
            return

    # Si no acierta
    mostrar_resultado(jugador, False, apuesta)

# Función para aapostar en color 
def apostar_color(ruleta, jugador):
    print("1: Rojo, 2: Negro")
    colores = {1: "rojo", 2: "negro"}
    eleccion = pedir_opcion("Elige un color para apostar: ", [1, 2])
    apuesta = verificar_cantidad_apostar(jugador)
    numero_ganador, color_ganador = girar_ruleta(ruleta)
    print(f"\u00a1La ruleta gira! Resultado: {numero_ganador} ({color_ganador})")

    if color_ganador == colores[eleccion]:
        mostrar_resultado(jugador, True, apuesta, ganancia=apuesta)
    else:
        mostrar_resultado(jugador, False, apuesta)

# Apuestas por columna
def verificar_numeros_usuario(numeros, cantidad):
    if len(numeros) != cantidad:
        return False
    for n in numeros:
        if not n.isdigit() or (n != '00' and (int(n) < 0 or int(n) > 36)):
            return False
    return True

def apostar_numeros(ruleta, jugador, cantidad, multiplicador):
    print(f"\nHas seleccionado: Apostar en {cantidad} números")
    print(f"Ingresa {cantidad} números separados por comas (Ejemplo: 1,2,3)")

    while True:
        entrada = input("Números seleccionados: ")
        numeros_usuario = entrada.replace(" ", "").split(",")

        # Si el jugador ingresa solo un número, permitirlo
        if cantidad == 1 and len(numeros_usuario) == 1 and verificar_numeros_usuario(numeros_usuario, 1):
            break
        # Si el jugador ingresa más de un número, validar la cantidad
        elif verificar_numeros_usuario(numeros_usuario, cantidad):
            break
        else:
            print(f"Entrada inválida. Por favor, selecciona exactamente {cantidad} números entre 0, 00 y 36.")

    apuesta = verificar_cantidad_apostar(jugador)
    numero_ganador, color_ganador = girar_ruleta(ruleta)
    print(f"\u00a1La ruleta gira! Resultado: {numero_ganador} ({color_ganador})")

    if str(numero_ganador) in numeros_usuario:
        ganancia = apuesta * multiplicador
        mostrar_resultado(jugador, True, apuesta, ganancia)
    else:
        mostrar_resultado(jugador, False, apuesta)

# Juego principal
def juego():
    ruleta = crear_ruleta()
    jugadores_activos = []
    num_jugadores = int(input("\u00bfCuántos jugadores participarán? "))
    while num_jugadores <= 0:
        print("Número de jugadores inválido. Debe ser mayor que cero.")
        num_jugadores = int(input("\u00bfCuántos jugadores participarán? "))


    for i in range(num_jugadores):
        nombre = input(f"Ingresa el nombre del jugador {i + 1}: ")
        saldo = int(input(f"Ingresa el saldo inicial para {nombre}: "))
        jugadores_activos.append({"nombre": nombre, "saldo": saldo})

    print("\n\u00a1Comienza el juego!\n")

    while jugadores_activos:
        for jugador in jugadores_activos[:]:
            print(f"\nTurno de {jugador['nombre']} (Saldo: {jugador['saldo']})")
            if not opcion(ruleta, jugadores_activos, jugador):
                print(f"\nGracias por jugar, {jugador['nombre']}!")
                jugadores_activos.remove(jugador)

            if jugador["saldo"] <= 0:
                print(f"{jugador['nombre']} se ha quedado sin saldo y ha sido eliminado del juego.")
                jugadores_activos.remove(jugador)

    print("\n\u00a1El juego ha terminado! Gracias por participar.")

# Ejecutar el juego
if __name__ == "__main__":
    juego()