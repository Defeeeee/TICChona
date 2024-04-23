import os  # Importamos la libreria os para limpiar la pantalla
import random  # Utilizamos la libreria random para generar la posicion de los barcos
from string import \
    ascii_lowercase as abecedario  # Importamos el abecedario en minusculas para usar coordenadas en formato "X1"
from typing import List  # Importamos la libreria List para poder utilizar Listas

verticales: dict = {} # Creamos un diccionario vacio #defe 

for count, value in enumerate(abecedario):  # Creamos un diccionario que mapea cada letra a su posición en el abecedario
    verticales[value] = count

n = 0  # Inicializamos la variable n en 0

"""
Por: Manuel Pebe Pueyrredon, Borja Izurieta y Federico Diaz Nemeth

Descripción:
    Este código es una implementación del juego de batalla naval en Python.
    El juego se puede jugar en modo de un solo jugador o multijugador.
    En el modo de un solo jugador, los barcos se colocan al azar en el tablero.
    En el modo multijugador, cada jugador coloca sus propios barcos.
    Los jugadores ingresan las coordenadas de sus disparos y el juego termina cuando todos los barcos de un jugador han sido hundidos.

    Features no vistas en clase utilizadas en el código:

        Se utilizan funciones para organizar, (item 4.7 https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

        Se utilizan inline if's (https://stackoverflow.com/questions/11880430/how-to-write-inline-if-statement-for-print)

        Se utilizan estruturas try except para manejar errores (item 8.3 https://docs.python.org/3/tutorial/errors.html)

        Se utiliza la libreria os para limpiar la pantalla, en este caso ejecutando os.system("clear") al usar OSX (https://docs.python.org/3/library/os.html)

        Se utilizan tuplas para transformar las coordenadas en un formato valido (item 5.3 https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)

        Se utilizan metodos varios de la clase string como .isdigit() o .lower() para validar las coordenadas (https://docs.python.org/3/library/stdtypes.html#string-methods)
        
        Se utiliza enumerate para recorrer el abecedario y crear un diccionario con las letras y su posición (https://realpython.com/python-enumerate/)
        
        Se utilizan diccionarios para mapear las letras a sus posiciones en el abecedario (https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
"""


def get_coords(coor: str) -> tuple[int, int]:  # Función para obtener las coordenadas a partir de una cadena
    """
    Esta función toma una cadena de entrada que representa las coordenadas y la convierte en una tupla de enteros.
    Valida la entrada y genera un ValueError si la entrada no es válida.
    """
    if coor[0].lower() not in verticales:  # Verificamos que la primera parte de la coordenada sea una letra válida
        raise ValueError
    if not coor[1:].isdigit():  # Verificamos que la segunda parte de la coordenada sea un número
        raise ValueError
    return verticales[coor[0].lower()], int(coor[1:]) - 1  # Devolvemos la coordenada como una tupla de enteros


def crear_tablero(tablerosize: int) -> List[List[str]]:  # Función para crear un tablero de juego vacío
    """
    Esta función crea un tablero de juego vacío de un tamaño dado.
    El tablero es una lista de listas, con cada lista interna que representa una fila en el tablero.
    """
    lista: List[List[str]] = []  # Creamos una lista vacia
    for _ in range(tablerosize):  # Recorremos el rango de n
        lista.append(["_"] * tablerosize)  # Agregamos una lista de n elementos a la lista

    return lista  # Devolvemos la lista de tamaño n*n


def llenar_tablero(rand: bool, tabl: List[List[str]: int], cantidadbarcos: int,
                   n: int) -> None:  # Función para llenar el tablero de juego con barcos
    """
    Esta función llena el tablero de juego con barcos.
    En el modo de un solo jugador, los barcos se colocan al azar.
    En el modo multijugador, cada jugador ingresa las coordenadas de sus barcos.
    """
    if rand:  # Si estamos en modo de un solo jugador
        i: int = 0
        while i < cantidadbarcos:  # Recorremos la cantidad de barcos
            posX: int = random.randint(0, len(tabl) - 1)  # Generamos una posición aleatoria para el barco
            posY: int = random.randint(0, len(tabl) - 1)  # Generamos una posición aleatoria para el barco
            if coordenadas_validas(posX, posY, n):  # Verificamos que las coordenadas sean válidas
                if tabl[posX][posY] == "*":  # Si ya hay un barco en esa posición, continuamos con el siguiente ciclo
                    continue
                else:
                    tabl[posX][posY] = "*"  # Colocamos un barco en la posición generada
                    i += 1
    else:  # Si estamos en modo multijugador
        for _ in range(cantidadbarcos):  # Recorremos la cantidad de barcos
            coor = get_coords(input(
                "Ingrese las coordenadas del barco: "))  # Pedimos al jugador que ingrese las coordenadas del barco
            while not coordenadas_validas(coor[0], coor[1], n):  # Verificamos que las coordenadas sean válidas
                print("Coordenadas invalidas")
                coor = get_coords(input(
                    "Ingrese las coordenadas del barco: "))  # Si las coordenadas no son válidas, pedimos que las ingrese de nuevo
            tabl[coor[0]][coor[1]] = "*"  # Colocamos un barco en la posición ingresada


def coordenadas_validas(x: int, y: int, n: int) -> bool:  # Función para verificar si las coordenadas son válidas
    """
    Esta función verifica si las coordenadas dadas son válidas (es decir, dentro de los límites del tablero de juego).
    """
    return 0 <= x < n and 0 <= y < n  # Las coordenadas son válidas si están dentro de los límites del tablero


def disparar(tablero: List[List[str]], ataque: List[List[str]], coor: tuple) -> int:  # Función para disparar a un barco
    """
    Esta función implementa la lógica para disparar a un barco.
    """
    if tablero[coor[0]][coor[1]] == "*":  # Si hay un barco en la posición ingresada
        tablero[coor[0]][coor[1]] = "X"  # Marcamos el barco como hundido
        ataque[coor[0]][coor[1]] = "X"  # Marcamos el barco como hundido en el tablero de ataque
        return 1  # Devolvemos 1 para indicar que se hundió un barco
    elif tablero[coor[0]][coor[1]] == "X" or tablero[coor[0]][coor[1]] == "A":  # Si ya se disparó a esa posición
        print("Ya disparaste aca")  # Informamos al jugador que ya disparó a esa posición
        return 0  # Devolvemos 0 para indicar que no se hundió ningún barco
    else:  # Si no hay un barco en la posición ingresada
        ataque[coor[0]][coor[1]] = "A"  # Marcamos la posición como agua en el tablero de ataque
        return 0  # Devolvemos 0 para indicar que no se hundió ningún barco


def show_tablero(tabl: List[List[str]]) -> None:  # Función para mostrar el tablero de juego
    """
    Esta función imprime el estado actual del tablero de juego.
    """
    for fila in tabl:  # Recorremos cada fila del tablero
        print(fila)  # Imprimimos la fila


def single_player() -> None:  # Función para el modo de un solo jugador
    """
    Esta función implementa la lógica del juego para el modo de un solo jugador.
    Maneja los turnos, verifica si un disparo golpeó un barco y determina cuándo termina el juego.
    """
    try:
        n = int(input("Ingrese el tamaño del tablero: "))  # Solicita al jugador que ingrese el tamaño del tablero
        cantidadbarcos = int(
            input("Ingrese la cantidad de barcos: "))  # Solicita al jugador que ingrese la cantidad de barcos
        cantidaddisparos = input(
            "Ingrese la cantidad de disparos: ")  # Solicita al jugador que ingrese la cantidad de disparos
        if cantidaddisparos == "":  # Si el jugador no ingresa una cantidad de disparos
            cantidaddisparos = 100  # Establece la cantidad de disparos en 100
        else:
            cantidaddisparos = int(cantidaddisparos)  # Convierte la cantidad de disparos a un entero
        if cantidadbarcos > n ** 2:  # Si la cantidad de barcos es mayor que el tamaño del tablero
            raise ValueError  # Genera un error
        if n > 26:  # Si el tamaño del tablero es mayor que 26
            raise ValueError  # Genera un error
    except ValueError:
        print("Ingrese un numero valido")
        return

    while True:
        tablero = crear_tablero(n)  # Crea un tablero de juego
        tableroataque = crear_tablero(n)  # Crea un tablero de ataque
        llenar_tablero(True, tablero, cantidadbarcos, n)  # Llena el tablero de juego con barcos
        cantidaddisparada: int = 0  # Inicializa el contador de disparos
        count = 0  # Inicializa el contador de barcos hundidos

        while cantidaddisparada < cantidaddisparos:  # Mientras no se hayan realizado todos los disparos
            os.system("clear")  # Limpia la pantalla
            print("Tablero del oponente")  # Imprime el tablero del oponente
            show_tablero(tableroataque)  # Muestra el tablero de ataque
            try:
                coor = get_coords(input("Ingrese las coordenadas del barco: "))  # Solicita al jugador que ingrese las coordenadas del disparo
            except:
                print("Coordenadas invalidas")  # Informa al jugador que las coordenadas son inválidas
                continue  # Continúa con el siguiente ciclo del bucle

            if coordenadas_validas(coor[0], coor[1], n):  # Verifica si las coordenadas son válidas
                count += disparar(tablero, tableroataque,
                                  coor)  # Realiza un disparo y suma el resultado al contador de barcos hundidos
            else:
                print("Coordenadas invalidas")  # Informa al jugador que las coordenadas son inválidas
                continue  # Continúa con el siguiente ciclo del bucle
            cantidaddisparada += 1  # Incrementa el contador de disparos
            if cantidadbarcos - count == 0:  # Si todos los barcos han sido hundidos
                break  # Termina el juego

        os.system("clear")  # Limpia la pantalla
        show_tablero(tablero)  # Muestra el tablero de juego
        print(
            f"Disparos acertados: {count}\nDisparos fallidos {cantidaddisparada - count if not cantidaddisparos - count < 0 else 0}")  # Imprime el número de disparos acertados y fallidos
        input("Presione enter para continuar")  # Solicita al jugador que presione enter para continuar


def multi_player() -> None:
    """
    Esta función implementa la lógica del juego para el modo multijugador.
    Maneja los turnos, verifica si un disparo golpeó un barco y determina cuándo termina el juego.
    """
    try:
        n = int(input("Ingrese el tamaño del tablero: "))  # Solicita al jugador que ingrese el tamaño del tablero
        cantidadbarcos = int(
            input("Ingrese la cantidad de barcos: "))  # Solicita al jugador que ingrese la cantidad de barcos
        cantidaddisparos = int(
            input("Ingrese la cantidad de disparos: "))  # Solicita al jugador que ingrese la cantidad de disparos
        if cantidadbarcos > n ** 2:  # Si la cantidad de barcos es mayor que el tamaño del tablero
            raise ValueError  # Genera un error
        if n > 26:  # Si el tamaño del tablero es mayor que 26
            raise ValueError  # Genera un error
    except ValueError:
        print("Ingrese un numero valido")  # Informa al jugador que debe ingresar un número válido
        return

    turno: int = random.randint(1, 2)  # Determina aleatoriamente quién comienza el juego

    while True:
        os.system("clear")  # Limpia la pantalla
        tablero1 = crear_tablero(n)  # Crea el tablero del primer jugador
        tablero2 = crear_tablero(n)  # Crea el tablero del segundo jugador
        ataque1 = crear_tablero(n)  # Crea el tablero de ataque del primer jugador
        ataque2 = crear_tablero(n)  # Crea el tablero de ataque del segundo jugador
        print("Jugador 1")
        llenar_tablero(False, tablero1, cantidadbarcos, n)  # Llena el tablero del primer jugador con barcos
        os.system("clear")  # Limpia la pantalla
        print("Jugador 2")
        llenar_tablero(False, tablero2, cantidadbarcos, n)  # Llena el tablero del segundo jugador con barcos
        cantidaddisparada1: int = 0  # Inicializa el contador de disparos del primer jugador
        cantidaddisparada2: int = 0  # Inicializa el contador de disparos del segundo jugador
        count1 = 0  # Inicializa el contador de barcos hundidos del primer jugador
        count2 = 0  # Inicializa el contador de barcos hundidos del segundo jugador
        os.system("clear")  # Limpia la pantalla
        input("Presione enter para comenzar")  # Solicita a los jugadores que presionen enter para comenzar
        os.system("clear")  # Limpia la pantalla

        while cantidaddisparada1 < cantidaddisparos and cantidaddisparada2 < cantidaddisparos:  # Mientras no se hayan realizado todos los disparos
            if turno == 1:  # Si es el turno del primer jugador
                print("Turno del Jugador 1: ")
                print("Tu tablero")
                show_tablero(tablero1)  # Muestra el tablero del primer jugador
                print("Tablero del oponente")
                show_tablero(ataque1)  # Muestra el tablero de ataque del primer jugador
                coor = get_coords(input(
                    "Ingrese las coordenadas del barco: "))  # Solicita al primer jugador que ingrese las coordenadas del disparo
                if coordenadas_validas(coor[0], coor[1], n):  # Verifica si las coordenadas son válidas
                    count1 += disparar(tablero2, ataque1,
                                       coor)  # Realiza un disparo y suma el resultado al contador de barcos hundidos del primer jugador
                    turno = 1 if count1 else 2  # Cambia el turno al segundo jugador si el primer jugador no hundió un barco
                    cantidaddisparada1 += 1  # Incrementa el contador de disparos del primer jugador
                else:
                    print("Coordenadas invalidas")  # Informa al primer jugador que las coordenadas son inválidas
                    continue  # Continúa con el siguiente ciclo del bucle

            elif turno == 2:  # Si es el turno del segundo jugador
                print("Turno del Jugador 2: ")
                print("Tu tablero")
                show_tablero(tablero2)  # Muestra el tablero del segundo jugador
                print("Tablero del oponente")
                show_tablero(ataque2)  # Muestra el tablero de ataque del segundo jugador
                coor = get_coords(input(
                    "Ingrese las coordenadas del barco: "))  # Solicita al segundo jugador que ingrese las coordenadas del disparo
                if coordenadas_validas(coor[0], coor[1], n):  # Verifica si las coordenadas son válidas
                    count2 += disparar(tablero1, ataque2,
                                       coor)  # Realiza un disparo y suma el resultado al contador de barcos hundidos del segundo jugador
                    turno = 2 if count2 else 1  # Cambia el turno al primer jugador si el segundo jugador no hundió un barco
                    cantidaddisparada2 += 1  # Incrementa el contador de disparos del segundo jugador
                else:
                    print("Coordenadas invalidas")  # Informa al segundo jugador que las coordenadas son inválidas
                    continue  # Continúa con el siguiente ciclo del bucle

            if cantidadbarcos - count1 == 0 or cantidadbarcos - count2 == 0:  # Si todos los barcos de uno de los jugadores han sido hundidos
                break  # Termina el juego


def main() -> None:
    while True:  # Bucle infinito para mantener el juego en ejecución hasta que el usuario decida salir
        inp: str = input(
            "Desea disparar los barcos puestos random (R) o desea jugar de a dos(2P)?: ").upper()  # Solicita al usuario que elija el modo de juego
        if inp == "2P":  # Si el usuario elige el modo multijugador
            while True:  # Bucle infinito para mantener el modo multijugador en ejecución
                multi_player()  # Inicia el modo multijugador
        elif inp == "R":  # Si el usuario elige el modo de un solo jugador
            while True:  # Bucle infinito para mantener el modo de un solo jugador en ejecución
                single_player()  # Inicia el modo de un solo jugador
        else:  # Si el usuario no elige un modo de juego válido
            print("Opcion invalida")  # Informa al usuario que la opción es inválida
            continue  # Continúa con el siguiente ciclo del bucle, solicitando al usuario que elija un modo de juego


main()  # Inicia el juego
