import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.lista_juegos import Lista_Juegos as lj
import src.juegos_pandas as jpandas
import src.util as util
from src.Juegos import Juegos
import bbdd

milista = lj("src/csv/vgsales.csv")


def mostrar_datos(lista_juegos, lugar_str):
    """
    Funcion muestra los juegos de un lugar

    Args:
        lista_juegos (list): lista de los jeugos
        lugar_str (str): lugar
    """
    for juego in lista_juegos:
            print(f"Rank: {juego[0]}")
            print(f"Nombre: {juego[1]}")
            print(f"Plataforma: {juego[2]}")
            print(f"Año: {juego[3]}")
            print(f"Género: {juego[4]}")
            print(f"Publisher: {juego[5]}")
            print(f"{lugar_str}: {juego[6]}")
            print("-" * 20)


def control(action):
    """
    Función de control:
        Recibe inputs desde el menú y se encarga de llamar a la función correspondiente
    """

    if action == 1:
        # Funcion Crear Juegos
        milista.add_game()

    elif action == 2:
        # Funcion Listar Juegos
        milista.read_list()

    elif action == 3:
        # Imprime los géneros registrados en la base
        select_genre = milista.genero()
        for i in select_genre:
            print(i, end=" ")
        # Funcion Listar Juegos por género
        genre = input("\nSelecciona un genero para filtrar: ")
        game_filter = milista.filter_genre(genre)
        for game in game_filter:
            print(game)

    elif action == 4:
        # Imprime los juegos publicados en el s. XX
        lista_juegos = bbdd.listar_siglo20()
        for juego in lista_juegos:
            print(juego)

    elif action == 5:
        # Listar editores
        lista_editores = bbdd.listar_editores()
        for editor in lista_editores:
            print("- " + editor)

    elif action == 6:
        # Listar juegos de Nintendo
        lista_juegos = bbdd.listar_publisher("Nintendo")
        for juego in lista_juegos:
            print(juego)

    elif action == 7:
        # Listar los 5 juegos mas vendidos en una region
        try:
            lugar = util.input_int("Elige una opcion: 1.NA, 2.EU, 3.JP, 4.GLOBAL ")
            if lugar == 1:
                lista_juegos = bbdd.listar_top(lugar='na_sales')
                lugar_str = 'Ventas NA'
                mostrar_datos(lista_juegos, lugar_str)
            elif lugar == 2:
                lista_juegos = bbdd.listar_top(lugar='eu_sales')
                lugar_str = 'Ventas EU'
                mostrar_datos(lista_juegos, lugar_str)
            elif lugar == 3:
                lista_juegos = bbdd.listar_top(lugar='jp_sales')
                lugar_str = 'Ventas JP'
                mostrar_datos(lista_juegos, lugar_str)
            elif lugar == 4:
                lista_juegos = bbdd.listar_top(lugar='global_sales')
                lugar_str = 'Ventas GLOBAL'
                mostrar_datos(lista_juegos, lugar_str)
            else:
                raise ValueError("Valor fuera de rango")
        except ValueError as e:
            print(e)
    
    elif action == 8:
        # Listar los 25 primeros juegos con pandas
        jpandas.csv_pandas()
    
    elif action == 9:
        try:
            nombre = util.input_obligatorio(
                "Introduce nombre del juego que deseas modificar: ")
            lista_juegos = bbdd.buscar_nombre(nombre)
            if len(lista_juegos) > 1:
                opcion = 0
                for juego in lista_juegos:
                    opcion += 1
                    print(f"opcion {opcion}")
                    print(juego)
                index = util.input_int(
                    "Existen varios juegos con el mismo nombre elige una opcion: ")
                if ((index) > len(lista_juegos)) and ((index) < len(lista_juegos)):
                    raise ValueError("Valor fuera de rango")
                else:
                    print(f"opcion {index}")
                    juego = lista_juegos[index-1]
            else:
                juego = lista_juegos[0]
                print(juego)
                
            print("Introduce el nuevo juego a modificar")
            new_juego = Juegos.new_game()
            print("Juego antiguo:")
            print(juego)
            print("Nuevo juego:")
            print(new_juego)
            confirmar = input("Desea guardarlo Y/N: ")
            if confirmar == "Y":
                print("Juego guardado")
                bbdd.actualizar(juego, new_juego)
            elif confirmar == "N":
                print("Juego no guardado")
            else:
                print("Opcion no valida")
                print("Juego no guardado")
        except ValueError as e:
            print(e)
        except IndexError:
            print("Juego no existente")

    elif action == 10:
        # Eliminar un juego de la bbdd
        try:
            juego = util.input_int("Introduce el rank del juego que quieres eliminar: ")
            if juego < 0:
                raise ValueError("Valor fuera de rango")
            else:
                bbdd.borrar_juego(juego)
        except ValueError as e:
            print(e)
        
    elif action == 11:
        # Listar juegos publicados en años pares
        lista_juegos = bbdd.filter_years_even()
        for juego in lista_juegos:
            print(juego)