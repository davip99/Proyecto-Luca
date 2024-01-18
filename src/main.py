def introducir_int(tetxo):
    """
    Introducir un numero entero y devolverlo

    Args:
        tetxo (str): Texto al pedir el numero

    Raises:
        ValueError: Valor introducido no es un numero entero (int)

    Returns:
        int: numero entero escrito
    """
    print(type(tetxo))
    try:
        numero = int(input(tetxo))
    except ValueError:
        raise ValueError
    else:
        return numero


def menu():
    """
    Funcion Menu. Muestra el menu y navega por el.
    """
    valor_minimo = 0
    valor_maximo = 1
    opcion = -1
    while opcion != 0:
        print("MENU:")
        print("[1] Crear Juego.")
        # Opciones
        print("[0] Salir")
        try:
            opcion = introducir_int("Introduce opcion: ")
        except ValueError:
            print("ERROR. Valor introducido no es una opcion\n")
        else:
            if opcion < valor_minimo or opcion > valor_maximo:
                print("ERROR. Opcion no existente\n")
            elif opcion == 0:
                print("Saliendo de la aplicacion\n")
            elif opcion == 1:
                print("Opcion 1: Crear Juego\n")
                # Funcion Crear juego


menu()
