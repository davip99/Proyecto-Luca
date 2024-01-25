import util as util
import control as ct


def menu_grafico():
    """
    Funcion imprime por consola el menu.
    """
    print("\n")
    print("MENU:")
    print("[1] Crear Juego.")
    print("[2] Listar Juegos.(Con listas)")
    print("[3] Listar Juegos por generos.(Con listas)")
    print("[4] Listar Juegos del s. XX.(Con BBDD)")
    print("[5] Listar editores. (Con BBDD)")
    print("[6] Listar juegos de Nintendo. (Con BBDD)")
    print("[7] Listar los 5 juegos mas vendidos en cada region. (Con BBDD)")
    print("[8] Listar los 25 juegos usando pandas")
    print("[9] Actualizar Juego (Con BBDD)")
    print("[10] Borrar un juego de la base de datos")
    print("[11] Listar los juegos publicados en años pares")
    print("---")
    print("[0] Salir")


def menu():
    """
    Funcion Menu. Muestra el menu y navega por el.
    """
    valor_minimo = 0
    valor_maximo = 11
    opcion = -1
    while opcion != 0:
        menu_grafico()
        try:
            opcion = util.input_int("Introduce opcion: ")
            if opcion < valor_minimo or opcion > valor_maximo:
                raise ValueError
        except ValueError:
            print("El valor introducido no es una opcion\n")
        else:
            if opcion == 0:
                print("Saliendo de la aplicacion\n")
            elif opcion == 1:
                print("Opcion 1: Crear Juego\n")
                # Funcion Crear Juegos
                ct.control(1)
            elif opcion == 2:
                print("Opcion 2: Listar Juegos\n")
                # Funcion Listar Juegos
                ct.control(2)
            elif opcion == 3:
                print("Opcion 3: Listar Juegos por genero\n")
                # Funcion Listar Juegos por género
                ct.control(3)
            elif opcion == 4:
                print("Opcion 4: Listar Juegos previos al s. XX\n")
                # Funcion Listar Juegos por anio
                ct.control(4)
            elif opcion == 5:
                print("Opcion 5: Listar editores.\n")
                # Funcion Listar editores
                ct.control(5)
            elif opcion == 6:
                print("Opcion 6: Listar juegos de Nintendo.\n")
                # Funcion Listar juegos de Nintendo
                ct.control(6)
            elif opcion == 7:
                print("Opcion 7: Listar los 5 juegos mas vendidos en cada region.\n")
                # Funcion Listar 5 juegos mas vendidos de cada region
                ct.control(7)
            elif opcion == 8:
                print("Opcion 8 Listar los 25 juegos usando pandas\n")
                # Funcion listar juegos pandas
                ct.control(8)
            elif opcion == 9:
                print("[9] Actualizar juego\n")
                # Funcion listar juegos pandas
                ct.control(9)
            elif opcion == 10:
                print("Opcion 10: Borrar un juego de la base de datos\n")
                # Funcion borrar juego
                ct.control(10)
            elif opcion == 11:
                print("Opcion 11: Listar los juegos publicados en años pares\n")
                # Funcion listar juegos de años pares
                ct.control(11)
