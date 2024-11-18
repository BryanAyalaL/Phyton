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
            print("Has seleccionado: Docena - Todos los números de la docena")
            # Agrega la lógica específica para esta apuesta
        elif opcion == "3":
            print("Has seleccionado: Apuestas pares - Apuesta al negro o rojo")
            # Agrega la lógica específica para esta apuesta
        elif opcion == "4":
            print("Has seleccionado: Un Número - Apuesta a un número específico")
            # Agrega la lógica específica para esta apuesta
        elif opcion == "5":
            print("Has seleccionado: Dos Números - Apuesta a dos números adyacentes")
            # Agrega la lógica específica para esta apuesta
        elif opcion == "6":
            print("Has seleccionado: Tres Números - Apuesta a tres números en fila")
            # Agrega la lógica específica para esta apuesta
        elif opcion == "7":
            print("Has seleccionado: Cuatro Números - Apuesta a cuatro números en cuadro")
            # Agrega la lógica específica para esta apuesta
        elif opcion == "8":
            print("Has seleccionado: Cinco Números - Apuesta a cinco números específicos")
            # Agrega la lógica específica para esta apuesta
        elif opcion == "9":
            print("Has seleccionado: Seis Números - Apuesta a seis números consecutivos")
            # Agrega la lógica específica para esta apuesta
        else:
            print("Opción inválida. Por favor, selecciona un número del 0 al 9.")

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
    apuesta = float(input(f"{jugador['nombre']}, ingresa la cantidad a apostar: "))

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

def jugar_ruleta(ruleta, jugadores):
    turno = 0
    jugadores_activos = jugadores.copy()  # Copia para evitar modificar la lista original

    while jugadores_activos:
        jugador = jugadores_activos[turno % len(jugadores_activos)]

        print(f"\nTurno de {jugador['nombre']} - Saldo: {jugador['saldo']}")
        
        menu()
        resultado = opcion(ruleta, jugadores_activos, jugador)
        
        if not resultado:
            print(f"{jugador['nombre']} ha sido eliminado del juego.")
            jugadores_activos.remove(jugador)
            if not jugadores_activos:
                print("Todos los jugadores han salido. Fin del juego.")
                break
            else:
                turno -= 1  # Ajusta el turno ya que se eliminó un jugador
        
        turno += 1

# Ejemplo de uso
if __name__ == "__main__":
    ruleta = crear_ruleta()
    jugadores = [{"nombre": "Jugador1", "saldo": 100}, {"nombre": "Jugador2", "saldo": 100}]
    print("Bienvenidos a la ruleta de Bryan's Casino")
    jugar_ruleta(ruleta, jugadores)

