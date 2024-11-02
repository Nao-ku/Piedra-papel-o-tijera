#Juego
from ronda import jugar_ronda

def jugar_juego(juego_num):
    print(f"\nJuego #{juego_num}")
    rondas_ganadas_jugador = 0
    rondas_ganadas_maquina = 0

    for ronda_num in range(1, 4):
        resultado = jugar_ronda(ronda_num)
        if resultado == 'jugador':
            rondas_ganadas_jugador += 1
        elif resultado == 'maquina':
            rondas_ganadas_maquina += 1

    if rondas_ganadas_jugador > rondas_ganadas_maquina:
        return 'jugador'
    elif rondas_ganadas_maquina > rondas_ganadas_jugador:
        return 'maquina'
    else:
        return 'empate'