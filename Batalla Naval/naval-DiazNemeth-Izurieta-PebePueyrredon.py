from os import system  # Importamos la funcion system de la libreria os para limpiar la consola
from typing import List  # Importamos la clase List de la libreria typing para poder definir listas
import random

n: int = 5  # Definimos el tamaño del tablero

cantidadbarcos: int = int(
    input("Ingrese la cantidad de barcos con la que quiere jugar "))  # Definimos la cantidad de barcos

cantidaddisparada: int = 0  # Definimos la cantidad de disparos

count: int = 0  # Definimos la cantidad de barcos hundidos

tablero: List[List[bool]] = []  # Definimos el tablero como una lista de listas de bools

tablero2: List[List[bool]] = []  # Definimos el tablero2 como una lista de listas de bools

tableroataque1: List[List[int]] = []  # Definimos el tableroataque1 como una lista de listas de ints

tableroataque2: List[List[int]] = []  # Definimos el tableroataque2 como una lista de listas de ints

cantidaddisparos: int = cantidadbarcos * 2  # Definimos la cantidad de disparos

for _ in range(n):
    tablero.append([False] * n)  # Agregamos una lista de n falsos (casilla vacia) a la lista tablero

opcion: str = input("Queres jugar multiplayer? (s/n) ").lower()  # pregunta si queres jugar multi o no

if opcion == "s":  # si la opcion es s, se ejecuta el siguiente codigo
    for _ in range(n):
        tablero2.append([False] * n)  # Agregamos una lista de n falsos (casilla vacia) a la lista tablero2

    for _ in range(n):
        tableroataque1.append([0] * n)  # el tablero de ataque 1 se llena de 0 en las casillas

    for _ in range(n):
        tableroataque2.append([0] * n)  # el tablero de ataque 2 se llena de 0 en las casillas

    print("Jugador 1")  # es el turno del J1 de elegir donde poner sus barcos / se loopea cantidadbarcos veces
    for _ in range(cantidadbarcos):
        coordenadaX: int = int(input("Ingrese la coordenada X "))
        coordenadaY: int = int(input("Ingrese la coordenada Y "))

        tablero[coordenadaX][coordenadaY] = True  # transforma las casillas elegidas en barcos
    system("clear")  # limpia la consola

    # Imprime el tablero con los barcos del J1
    for linea in tablero:
        for valor in linea:
            print("X" if valor else "O", end=" ")
        print()
    input("Presiona enter para confirmar")
    system("clear")

    print("Jugador 2")  # el turno del J2 de elegir la ubi de sus barcos / loop cantidadbarcos veces
    for _ in range(cantidadbarcos):
        coordenadaX: int = int(input("Ingrese la coordenada X "))
        coordenadaY: int = int(input("Ingrese la coordenada Y "))

        tablero2[coordenadaX][coordenadaY] = True  # transforma las casillas elegidas en barcos
    system("clear")  # limpia la consola

    # Imprime el tablero con los barcos del J2
    for linea in tablero2:
        for valor in linea:
            print("X" if valor else "O", end=" ")
        print()
    input("Presiona enter para confirmar")
    system("clear")

    # Se inician las variables de los jugadores en False, "sin ganar"
    jugador1: bool = False
    jugador2: bool = False

    count1: int = 0  # Lleva la cuenta de los disparos acertados J1
    count2: int = 0  # Lleva la cuenta de los disparos acertados J2

    cantidaddisparada1: int = 0  # Cuenta disparos de J1
    cantidaddisparada2: int = 0  # Cuenta disparos de J2

    while not (jugador1 or jugador2):  # No gano ninguno todavia
        system("clear")
        print("Jugador 1")
        coorX: int = int(input("Ingrese la coordenada X "))  # Pide coordenadas de disparo
        coorY: int = int(input("Ingrese la coordenada Y "))

        if tablero2[coorX][coorY]:  # Si la coor elegida es True
            print("Barco destruido")

            count1 += 1  # Suma un tiro acertado
            tablero2[coorX][coorY] = False  # Se borra el barco del tablero oponente
            tableroataque1[coorX][coorY] = 1  # Se instancia el barco como destruido en el tablero de ataque

            # Mostramos el tablero de ataque, X corresponde a barco destruido, 
            # O a casilla no atacada y A a casilla atacada pero sin barco (Agua)
            for linea in tableroataque1:
                for valor in linea:
                    print("X" if valor == 1 else "O" if valor == 0 else "A", end=" ")
                print()
            input("Presiona enter para continuar")

        else:
            print("Agua")

            tableroataque1[coorX][coorY] = 2

            for linea in tableroataque1:
                for valor in linea:
                    print("X" if valor == 1 else "O" if valor == 0 else "A", end=" ")
                print()

            input("Presiona enter para continuar")

        # Sumamos uno a la cantidad disparada por cada turno, se restan los disparos restantes y aclaramos cuantos barcos quedan por destruir
        cantidaddisparada1 += 1
        print(f"Te quedan {cantidaddisparos - cantidaddisparada1} disparos")
        print(f'Quedan {cantidadbarcos - count} barcos' if cantidadbarcos - count > 1 else "Queda un barco")

        if count1 == cantidadbarcos:  # Si los barcos acertados son iguales a los barcos totales, el jugador gana
            print("Ganaste, Jugador 1")
            jugador1 = True
            break

        system("clear")

        print("Jugador 2")
        coorX: int = int(input("Ingrese la coordenada X "))
        coorY: int = int(input("Ingrese la coordenada Y "))

        if tablero[coorX][coorY]:
            print("Barco destruido")

            count2 += 1
            tablero[coorX][coorY] = False
            tableroataque2[coorX][coorY] = 1

            for linea in tableroataque2:
                for valor in linea:
                    print("X" if valor == 1 else "O" if valor == 0 else "A", end=" ")
                print()

            input("Presiona enter para continuar")

        else:
            print("Agua")

            tableroataque2[coorX][coorY] = 2
            for linea in tableroataque2:
                for valor in linea:
                    print("X" if valor == 1 else "O" if valor == 0 else "A", end=" ")
                print()

            input("Presiona enter para continuar")

        cantidaddisparada2 += 1
        print(f"Te quedan {cantidaddisparos - cantidaddisparada2} disparos")
        print(f'Quedan {cantidadbarcos - count} barcos' if cantidadbarcos - count > 1 else "Queda un barco")

        if count2 == cantidadbarcos:
            print("Ganaste, Jugador 2")
            jugador2 = True
            break

elif opcion == "n":
    for _ in range(cantidadbarcos):
        tablero[random.randint(0, n - 1)][random.randint(0, n - 1)] = True  # Se generan barcos random en el tablero

    for _ in range(cantidaddisparos):
        coordenadaX: int = int(input("Ingrese la coordenada X "))
        coordenadaY: int = int(input("Ingrese la coordenada Y "))

        if tablero[coordenadaX][coordenadaY]:
            print("Barco destruido")
            count += 1
            tablero[coordenadaX][coordenadaY] = False
            input("Presiona enter para continuar")

        else:
            print("Agua")  # Imprimimos que no le pegaste
            input("Presiona enter para continuar")  # Imprimimos que no le pegaste

        cantidaddisparada += 1  # Aumentamos la cantidad disparada en 1
        print(
            f"Te quedan {cantidaddisparos - cantidaddisparada} disparos")  # Imprimimos la cantidad de disparos que quedan
        print(
            f'Quedan {cantidadbarcos - count} barcos' if cantidadbarcos - count > 1 else "Queda un barco")  # Imprimimos la cantidad de barcos que quedan

        if count == cantidadbarcos:  # Si la cantidad de barcos hundidos es igual a la cantidad de barcos
            print("Ganaste")  # Imprimimos que ganaste
            break

    for linea in tablero:  # Recorremos cada linea de la lista tablero
        for valor in linea:  # Recorremos cada valor de la lista
            print("X" if valor else "O", end=" ")  # Imprimimos X si es True y O si es False
        print()

    print(
        f"Disparos acertados {count}, disparos fallados {cantidaddisparada - count}")  # Imprimimos la cantidad de disparos acertados y fallados
