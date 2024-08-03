import random
import os

def mostrar ():
    print("\t\t\tJUEGO DE PIERDRA PAPEL O TIJERAS\nselecciones PIEDRA PAPEL O TIJERAS\n")
def juego():
    while True:
        mostrar()

        opciones = ["piedra", "papel", "tijeras"]
        jugador1 = input("Elija su opcion: ")
        
        jugador2 = random.choice(opciones)
        punto = vod(jugador1,jugador2)
        print(f"el jugador 1 eligio:{jugador1}\n y el jugador 2 eligio: {jugador2}")
        if punto == 1:
            print("VICTORIA DEL JUGADOR 1!!!")
        elif punto == 2:
            print("VICTORIA DEL JUGADOR 2!!!")
        else:
            print("EMPATE")
        val = menu()
        if val == 0:
            limpiar_pantalla()
            break
        limpiar_pantalla()

def vod (j1,j2):
    if j1 == j2:
        return 0
    elif j1.lower() == "piedra":
        if j2.lower() == "tijeras":
            return 1
        else:
            return 2
    elif j1.lower() == "papel":
        if j2.lower() == "piedra":
            return 1
        else:
            return 2
    else:
        if j2.lower() == "papel":
            return 1
        else:
            return 2

def menu():
    print("¿Desea volver a jugar?")
    opcion = ""
    while opcion.lower() != "si" and opcion.lower() != "no":
        opcion = input("")
        if opcion.lower() != "si" and opcion.lower() != "no":
            print("Opción no válida")
    if opcion.lower() == "si":
        return 1
    else:
        return 0
    
    


def limpiar_pantalla():
    if os.name == 'posix':  # Para sistemas tipo Unix (Linux, macOS)
        os.system('clear')
    elif os.name == 'nt':  # Para Windows
        os.system('cls')

# Luego, puedes llamar a la función limpiar_pantalla() cuando quieras limpiar la pantalla



    
           
juego()


