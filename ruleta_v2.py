import random

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

def menu():
    print("\n------MENU DE APUESTAS------")
    print("1. Columna")
    print("2. Docena")
    print("3. Apuestas pares (rojo/negro)")
    print("0. Salir")

def jugar_ruleta(ruleta, jugadores, turno=0):
    if not jugadores:  # Si no hay jugadores
        print("No hay jugadores. Finalizando el juego.")
        return
    
    jugador = jugadores[turno % len(jugadores)]
    print(f"\nTurno de {jugador['nombre']} - Saldo: {jugador['saldo']}")
    menu()
    opcion = input("Selecciona el tipo de apuesta (0 para salir): ")
    
    if opcion == "0":
        print(f"{jugador['nombre']} ha decidido salir del juego.")
        jugadores.remove(jugador)
        if not jugadores:  # Si no quedan jugadores
            print("No hay más jugadores activos. Finalizando el juego.")
            return
    
    elif opcion == "1":
        print("Apuesta en columna")
        apostar_columna(ruleta, jugador)
    
    # Agrega lógica de las otras apuestas según la opción elegida
    
    jugar_ruleta(ruleta, jugadores, turno + 1)  # Llamada recursiva al siguiente turno

def apostar_columna(ruleta, jugador):
    columna_elegida = input("Selecciona una columna (1, 2, o 3): ")
    numero_ganador = random.choice([0, '00'] + list(range(1, 37)))
    color_ganador = ruleta[numero_ganador]
    print(f"Número ganador: {numero_ganador} (Color: {color_ganador})")

    if numero_ganador == 0 or numero_ganador == '00':
        print("El número ganador es 0 o 00, no hay ganadores en la columna.")
    elif (columna_elegida == "1" and numero_ganador % 3 == 1) or \
         (columna_elegida == "2" and numero_ganador % 3 == 2) or \
         (columna_elegida == "3" and numero_ganador % 3 == 0):
        print(f"¡{jugador['nombre']} gana la apuesta en la columna seleccionada!")
        jugador['saldo'] += 20  # Aumenta el saldo como ejemplo
    else:
        print(f"Lo siento, {jugador['nombre']} pierde la apuesta.")
        jugador['saldo'] -= 10  # Disminuye el saldo como ejemplo

def iniciar_juego():
    ruleta = crear_ruleta()
    jugadores = [{"nombre": "Jugador1", "saldo": 100}, {"nombre": "Jugador2", "saldo": 100}]
    print("Bienvenidos a la ruleta de Bryan's Casino")
    jugar_ruleta(ruleta, jugadores)

iniciar_juego()
