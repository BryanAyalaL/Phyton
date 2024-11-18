import random

def crear_ruleta():
    """
    Función para crear la ruleta del casino, asignando colores a cada número según el patrón
    tradicional de la ruleta de casino americana. La ruleta tiene 38 espacios numerados 
    del 0 al 36 y un '00', con cada número asignado a un color:
    - El 0 y el '00' son verdes.
    - Los números del 1 al 36 alternan entre rojo y negro, en bloques de 9 números cada uno.

    Retorna:
        dict: Un diccionario `ruleta` donde cada clave es un número de la ruleta (0, 1-36, '00') 
              y su valor es el color asignado ("Verde", "rojo", "negro").
    """
    
    # Inicializamos un diccionario vacío para almacenar los números y sus colores
    ruleta = {}

    # Asignamos el color verde al 0 y al '00'
    ruleta[0] = "Verde"
    ruleta['00'] = "Verde"

    # `x` alterna entre 0 y 1 para ayudar a definir el patrón de color en cada bloque de 9 números
    x = 0
    # `j` recorrerá los números del 1 al 36 y `i` marca los límites de cada bloque de 9 números
    j = 1

    # Dividimos la ruleta en cuatro bloques de 9 números y asignamos el color a cada número en el bloque
    for i in range(1, 38, 9):
        # Cambiamos el valor de `x` para alternar el patrón de color en cada bloque
        x ^= 1

        # Para los bloques donde x == 1, los números pares son rojos y los impares negros
        while j < i and x == 1:
            if j % 2 == 0:
                ruleta[j] = "rojo"
            else:
                ruleta[j] = "negro"
            #print(f"numero: {j} es de color: {ruleta[j]}")
            j += 1

        # Para los bloques donde x == 0, los números pares son negros y los impares rojos
        while j <= i and x == 0:
            if j % 2 == 0:
                ruleta[j] = "negro"
            else:
                ruleta[j] = "rojo"
            #print(f"numero: {j} es de color: {ruleta[j]}")
            j += 1
    return ruleta

def menu():
    print("------MENU DE APUESTAS------")
    print("Selecciona el tipo de apuesta que deseas realizar:")
    print("1. Columna - Todos los números en una línea")
    print("   - Pago: 2:1")
    print()
    print("2. Docena - Todos los números de la docena")
    print("   - Pago: 2:1")
    print()
    print("3. Apuestas pares - Apuesta al negro o rojo")
    print("   - Pago: 1:1")
    print()
    print("4. Un Número - Apuesta a un número específico (ejemplo: 24)")
    print("   - Pago: 35:1")
    print()
    print("5. Dos Números - Apuesta a dos números adyacentes (ejemplo: 20 y 10)")
    print("   - Pago: 17:1")
    print()
    print("6. Tres Números - Apuesta a tres números en fila (ejemplo: 1, 2 y 3)")
    print("   - Pago: 11:1")
    print()
    print("7. Cuatro Números - Apuesta a cuatro números en cuadro (ejemplo: 4, 5, 6 y 7)")
    print("   - Pago: 8:1")
    print()
    print("8. Cinco Números - Apuesta a cinco números específicos (ejemplo: 1, 2, 3, 4 y 5)")
    print("   - Pago: 6:1")
    print()
    print("9. Seis Números - Apuesta a seis números consecutivos (ejemplo: 1 a 6)")
    print("   - Pago: 5:1")
    print()
    print("0. Salir")

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
    elif (columna_elegida == "1" and numero_ganador % 3 == 1) or \
       (columna_elegida == "2" and numero_ganador % 3 == 2) or \
       (columna_elegida == "3" and numero_ganador % 3 == 0):
        ganancia = apuesta * 2
        jugador["saldo"] += ganancia
        print(f"¡Felicidades {jugador['nombre']}! Ganaste {ganancia}. Nuevo saldo: {jugador['saldo']}")
    else:
        jugador["saldo"] -= apuesta
        print(f"Lo siento, {jugador['nombre']}, perdiste la apuesta. Nuevo saldo: {jugador['saldo']}")


# Ejemplo de ejecución
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

