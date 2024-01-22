
import sys
from pathlib import Path
import bbdd
sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.lista_juegos import Lista_Juegos as lj

milista = lj("src/csv/vgsales.csv")

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
        lugar = int(input("Elige una opcion: 1.NA, 2.EU, 3.JP, 4.GLOBAL "))
        if lugar == 1:
            lista_juegos = bbdd.listar_top(lugar='na_sales')
            lugar_str = 'Ventas NA'
        elif lugar == 2:
            lista_juegos = bbdd.listar_top(lugar='eu_sales')
            lugar_str = 'Ventas EU'
        elif lugar == 3:
            lista_juegos = bbdd.listar_top(lugar='jp_sales')
            lugar_str = 'Ventas JP'
        elif lugar == 4:
            lista_juegos = bbdd.listar_top(lugar='global_sales')
            lugar_str = 'Ventas GLOBAL'
            
        for juego in lista_juegos:
            print(f"Rank: {juego[0]}")
            print(f"Nombre: {juego[1]}")
            print(f"Plataforma: {juego[2]}")
            print(f"Año: {juego[3]}")
            print(f"Género: {juego[4]}")
            print(f"Publisher: {juego[5]}")
            print(f"{lugar_str}: {juego[6]}")
            print("-" * 20)
