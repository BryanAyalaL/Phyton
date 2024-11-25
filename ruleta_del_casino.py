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

# Función para mostrar el menú (sin cambios)
def menu():
    print("\n------MENU DE APUESTAS------")
    print("1. Columna - Todos los números en una línea (Pago: 2:1)")
    print("2. Docena - Todos los números de la docena (Pago: 2:1)")
    print("3. Apuestas pares - Apuesta al negro o rojo (Pago: 1:1)")
    print("4. Un Número - Apuesta a un número específico (Pago: 35:1)")
    print("5. Dos Números - Apuesta a dos números adyacentes (Pago: 17:1)")
    print("6. Tres Números - Apuesta a tres números en fila (Pago: 11:1)")
    print("7. Cuatro Números - Apuesta a cuatro números en cuadro (Pago: 8:1)")
    print("8. Cinco Números - Apuesta a cinco números específicos (Pago: 6:1)")
    print("9. Seis Números - Apuesta a seis números consecutivos (Pago: 5:1)")
    print("0. Salir")

def opcion (ruleta,jugadores_activos,jugador):

    while True:
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
            return True
        elif opcion == "5":
            return True
        elif opcion == "6":
            return True
        elif opcion == "7":
            return True
        elif opcion == "8":
            return True
        elif opcion == "9":
            return True
        else:
            print("Opción inválida. Por favor, selecciona un número del 0 al 9.")
def verificar_cantidad_apostar(jugador):
    while True:
        try:
            cantidad = int(input(f"{jugador['nombre']}, ingresa la cantidad a apostar: "))
            if cantidad <= 0:
                print(f"{jugador['nombre']}, la cantidad debe ser mayor a 0.")
            elif cantidad > jugador["saldo"]:
                print(f"{jugador['nombre']}, no puedes apostar más de tu saldo disponible ({jugador['saldo']}).")
            else:
                return cantidad  # Cantidad válida, salir del bucle
        except ValueError:
            print("Por favor, ingresa un número válido.")


def verificar_saldo(jugador, jugadores_activos):
    """
    Verifica si el jugador tiene saldo suficiente. Si no, lo elimina del juego.
    """
    if jugador["saldo"] <= 0:
        print(f"{jugador['nombre']} no tiene saldo suficiente y ha salido del juego.")
        jugadores_activos.remove(jugador)
        return False
    return True

# Pedir la elección de columna al usuario
def pedir_numero(valores_permitidos):
    numero_elegido = input(f"Selecciona un número de {valores_permitidos}: ")
    if numero_elegido.isdigit() and int(numero_elegido) in valores_permitidos:
        return int(numero_elegido)
    else:
        print(f"Selección inválida. Por favor elige un número de {valores_permitidos}.")
        return pedir_numero(valores_permitidos)

# Función para apostar en la columna
def apostar_columna(ruleta,jugador):
    print("\nHas seleccionado: Columna - Todos los números en una línea")
    print("Elige una columna para apostar:")
    print("1. Columna 1 (1, 4, 7, ..., 34)")
    print("2. Columna 2 (2, 5, 8, ..., 35)")
    print("3. Columna 3 (3, 6, 9, ..., 36)")

    # Pedir la elección de columna al usuario
    columna_elegida = pedir_numero([1, 2, 3])
    apuesta=verificar_cantidad_apostar(jugador)

    # Generar un número aleatorio entre 0, '00' y 1 a 36 para simular el giro de la ruleta
    numero_ganador = random.choice([0, '00'] + list(range(1, 37)))
    color_ganador = ruleta[numero_ganador]
    print(f"Número ganador: {numero_ganador} (Color: {color_ganador})")

    # Determinar si el número ganador está en la columna elegida
    if numero_ganador == 0 or numero_ganador == '00':
        print("El número ganador es 0 o 00, lo que significa que no hay ganadores en la columna.")
        jugador["saldo"] -= apuesta
        print(f"Lo siento, {jugador['nombre']}, perdiste la apuesta. Nuevo saldo: {jugador['saldo']}")
    elif (columna_elegida == 1 and numero_ganador % 3 == 1) or \
       (columna_elegida == 2 and numero_ganador % 3 == 2) or \
       (columna_elegida == 3 and numero_ganador % 3 == 0):
        ganancia = apuesta * 2
        jugador["saldo"] += ganancia
        print(f"¡Felicidades {jugador['nombre']}! Ganaste {ganancia}. Nuevo saldo: {jugador['saldo']}")
    else:
        jugador["saldo"] -= apuesta
        print(f"Lo siento, {jugador['nombre']}, perdiste la apuesta. Nuevo saldo: {jugador['saldo']}")

# Función para apostar en una docena
def apostar_docena(ruleta,jugador):
    print("\nHas seleccionado: docena - grupos de doce")
    print("Elige una docena para apostar:")
    print("1. Docena 1 (1 al 12)")
    print("2. Docena 2 (13 al 24)")
    print("3. Docena 3 (25 al 36)")

    # Pedir la elección de columna al usuario
    docena_elegida = pedir_numero([1, 2, 3])
    apuesta=verificar_cantidad_apostar(jugador)

    # Generar un número aleatorio entre 0, '00' y 1 a 36 para simular el giro de la ruleta
    numero_ganador = random.choice([0, '00'] + list(range(1, 37)))
    color_ganador = ruleta[numero_ganador]
    print(f"Número ganador: {numero_ganador} (Color: {color_ganador})")

    # Determinar si el número ganador está en la columna elegida
    if numero_ganador == 0 or numero_ganador == '00':
        print("El número ganador es 0 o 00, lo que significa que no hay ganadores en la docena.")
        jugador["saldo"] -= apuesta
        print(f"Lo siento, {jugador['nombre']}, perdiste la apuesta. Nuevo saldo: {jugador['saldo']}")
    elif (docena_elegida == 1 and numero_ganador <13) or \
       (docena_elegida == 2 and 12<numero_ganador<25 ) or \
       (docena_elegida == 3 and 24<numero_ganador<37):
        ganancia = apuesta * 2
        jugador["saldo"] += ganancia
        print(f"¡Felicidades {jugador['nombre']}! Ganaste {ganancia}. Nuevo saldo: {jugador['saldo']}")
    else:
        jugador["saldo"] -= apuesta
        print(f"Lo siento, {jugador['nombre']}, perdiste la apuesta. Nuevo saldo: {jugador['saldo']}")

# Funcion para validar el color
def verificar_color(ruleta):
    color_usuario = input("Elige un color (rojo o negro): ").lower()
    if color_usuario in ruleta.values():
        return color_usuario  # Devuelve el color válido
    else:
        print("Error, datos no válidos. Intenta de nuevo.")
        verificar_color(ruleta)    

# Funcion para aapostar en pares 
def apostar_color(ruleta, jugador):
    print("\nHas seleccionado: color - rojo o negro")
    color_usuario=verificar_color(ruleta)
    apuesta=verificar_cantidad_apostar(jugador)

    # Generar un número aleatorio entre 0, '00' y 1 a 36 para simular el giro de la ruleta
    numero_ganador = random.choice([0, '00'] + list(range(1, 37)))
    color_ganador = ruleta[numero_ganador]
    print(f"Número ganador: {numero_ganador} (Color: {color_ganador})")

    if color_ganador==color_usuario:
        ganancia = apuesta
        jugador["saldo"] += ganancia
        print(f"¡Felicidades {jugador['nombre']}! Ganaste {ganancia}. Nuevo saldo: {jugador['saldo']}")
    else:
        jugador["saldo"] -= apuesta
        print(f"Lo siento, {jugador['nombre']}, perdiste la apuesta. Nuevo saldo: {jugador['saldo']}")

def jugar_ruleta(ruleta, jugadores):
    turno = 0
    jugadores_activos = jugadores.copy()  # Copia para evitar modificar la lista original

    while jugadores_activos:
        jugador = jugadores_activos[turno % len(jugadores_activos)]

        if not verificar_saldo(jugador, jugadores_activos):
            if not jugadores_activos:
                print("Todos los jugadores han salido. Fin del juego.")
                break
            turno -= 1
            continue

        print(f"\nTurno de {jugador['nombre']} - Saldo: {jugador['saldo']}")
        menu()
        resultado = opcion(ruleta, jugadores_activos, jugador)
        
        if not resultado:
            print(f"{jugador['nombre']} ha salido voluntariamente del juego.")
            jugadores_activos.remove(jugador)
            if not jugadores_activos:
                print("Todos los jugadores han salido. Fin del juego.")
                break
            turno -= 1
        turno += 1


# Ejemplo de uso
if __name__ == "__main__":
    ruleta = crear_ruleta()
    jugadores = [{"nombre": "Jugador1", "saldo": 100}, {"nombre": "Jugador2", "saldo": 100}]
    print("Bienvenidos a la ruleta de Bryan's Casino")
    jugar_ruleta(ruleta, jugadores)

