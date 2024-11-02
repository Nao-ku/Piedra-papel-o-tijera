#funciones Piedra Papel o tijeras
import random

def jugar_ronda(ronda_num):
    print(f"Ronda #{ronda_num}")
    opciones = ['piedra', 'papel', 'tijera']
    jugador = input("Elige piedra, papel o tijera: ")
    maquina = random.choice(opciones)
    print(f"Computadora elige: {maquina}")

    if jugador == maquina:
        return 'empate'
    elif (jugador == 'piedra' and maquina == 'tijera') or \
        (jugador == 'papel' and maquina == 'piedra') or \
        (jugador == 'tijera' and maquina == 'papel'):
        return 'jugador'
    else:
        return 'computadora'
