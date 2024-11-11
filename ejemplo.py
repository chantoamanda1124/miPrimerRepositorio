import time
import random

# Escribe tu código aquí

Mipuntaje = 0
Puntajepc = 0

while True:
    p1 = input("Que eliges: piedra, papel o tijera(en minusculas)").lower()
    if p1 =="piedra" or p1 == "papel" or p1 == "tijera":
        pc = random.randint(1, 3)
        if pc == 1:
            pc = "piedra"
        elif pc == 2:
            pc = "papel"
        else:
            pc = "tijera"
            
        print("¡Piedra, papel o tijera!")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("3")
        print("La pc a elegido: ", pc)
        
        if pc == p1:
            print('Empate')
        elif p1 == 'piedra' and pc == 'tijera':
            print('¡Ganaste!')
            Mipuntaje = Mipuntaje + 1
        elif p1 == 'papel' and pc == 'piedra':
            print('¡Ganaste!')
            Mipuntaje = Mipuntaje + 1
        elif p1 == 'tijera' and pc == 'papel':
            print('¡Ganaste!')
            Mipuntaje = Mipuntaje + 1
        else:
            print('¡Perdiste!')
            Puntajepc = Puntajepc + 1
        print('Puntajes: Jugador:', Mipuntaje, ', Computadora:', Puntajepc)
        
    else:
        print("¿Nunca has jugado al piedra papel o tijera?")