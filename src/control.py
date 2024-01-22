
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
        bbdd.filtro_siglo20()

    elif action == 5:
        # Listar editores
        lista_editores = bbdd.listar_editores()
        for editor in lista_editores:
            print("- " + editor)

    elif action == 6:
        # Funcion Listar juegos de Nintendo
        lista_juegos = bbdd.listar_juegos_nintendo()
        for juego in lista_juegos:
            print(juego)
