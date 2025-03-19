import random

def lanzar_dado():
    return random.randint(1, 6)

def jugar_turno(jugador):
    print(f"Turno de {jugador}")
    resultado = lanzar_dado()
    print(f"{jugador} lanzó un {resultado}")
    return resultado

def determinar_ganador(jugador1, jugador2):
    puntaje1 = jugar_turno(jugador1)
    puntaje2 = jugar_turno(jugador2)

    if puntaje1 > puntaje2:
        print(f"¡{jugador1} gana!")
    elif puntaje1 < puntaje2:
        print(f"¡{jugador2} gana!")
    else:
        print("¡Fue un Empate!")

# Juego
determinar_ganador("Jugador 1", "Jugador 2")