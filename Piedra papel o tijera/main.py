#Main
from juego import jugar_juego

def main():
    juegos_ganados_jugador = 0
    juegos_ganados_maquina = 0

    for juego_num in range(1, 6):
        resultado = jugar_juego(juego_num)
        if resultado == 'jugador':
            juegos_ganados_jugador += 1
        elif resultado == 'maquina':
            juegos_ganados_maquina += 1

    print(f"\nJuegos ganados por el jugador: {juegos_ganados_jugador}")
    print(f"Juegos ganados por la maquina: {juegos_ganados_maquina}")

# Ejecutar el programa
if __name__ == "__main__":
    main()
