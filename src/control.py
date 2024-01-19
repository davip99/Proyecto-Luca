import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.lista_juegos import Lista_Juegos as lj

milista = lj("src/csv/vgsales.csv")


def control(action):
    """
    Función de control:
         Recibe inputs desde el menú y se encarga de llamar a la función correspondiente
         """

    if action == 1:
        milista.add_game()

    elif action == 2:
        milista.read_list()

    elif action == 3:
        """
        Imprime los géneros registrados en la base
        """
        select_genre = milista.genero()
        for i in select_genre:
            print(i, end=" ")
        """
        Función filtrar por género
        """
        genre = input("\nSelecciona un genero para filtrar: ")
        milista.filter_genre(genre)

    """elif action == 4:
            milista.filter_century20()"""
