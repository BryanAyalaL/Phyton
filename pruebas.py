turno =0
jugadores=int(input("Ingrese los jugadores "))
while turno<10:
    
    jugador_actual=turno%jugadores
    print (jugador_actual)
    turno+=1


"""
def jugar_ruleta(ruleta, jugadores, turno=0):
    if not jugadores:
        print("No hay jugadores. Finalizando el juego.")
        return

    jugador = jugadores[turno % len(jugadores)]  # Selecciona el jugador actual
    print(f"\nTurno de {jugador['nombre']} - Saldo: {jugador['saldo']}")
    
    menu()
    if opcion(ruleta, jugadores, jugador):  # Si el jugador no salió, continúa el juego
        jugar_ruleta(ruleta, jugadores, turno + 1)  # Pasa al siguiente jugador
    else:
        if turno + 1 < len(jugadores):  # Si no es el último jugador, pasa al siguiente
            jugar_ruleta(ruleta, jugadores, turno + 1)
        else:
            print("Todos los jugadores han salido. Fin del juego.")
    
"""