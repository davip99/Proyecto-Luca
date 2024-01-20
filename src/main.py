import util as util
from lista_juegos import Lista_Juegos
import control as ct


def menu():
    """
    Funcion Menu. Muestra el menu y navega por el.
    """
    valor_minimo = 0
    valor_maximo = 3
    opcion = -1
    while opcion != 0:
        print("MENU:")
        print("[1] Crear Juego.")
        print("[2] Listar Juegos.")
        print("[3] Listar Juegos por generos.")
        print("---")
        print("[0] Salir")
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


if __name__ == '__main__':
    menu()
