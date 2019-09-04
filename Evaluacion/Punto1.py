'''Duvan Latorre - Esteban Torres'''
from random import randint, uniform, random
def ra():
    a = randint(1,6)
    return a

players = []

def basico():
    i = 0
    while (i <= jg):
        players.append()
        i = i + 1
        print("Jugador ", i, ": Presione una tecla para jugar")
        key = input()
        p1 = 

def tablero():
    print(":::::Menú:::::")
    print("1. Nivel básico (Tablero de 20 posiciones)")
    print("2. Nivel intermedio (Tablero de 30 posiciones)")
    print("3. Nivel avanzado (Tablero de 50 posiciones)")
    print("Escoja el nivel de juego: ")
    nvl = int(input())
    if (nvl == 1):
        print("Nivel Basico")

    elif(nvl == 2):
        print("Nivel Intermedio")
    elif(nvl == 3):
        print("Nivel Avanzado")
    else:
        print("Digite una opción valida.")
        tablero()
    

print("::::Bienvenido a carrera numérica::::")
print("Digite la cantidad de jugadores: ")
jg = int(input())

if (jg < 2 ):
    print("El limite de jugadores es de 2 a 4.")
elif (jg > 4):
    print("El limite de jugadores es de 2 a 4.")
else:
    print(":::Carrera Numérica:::")
    tablero()