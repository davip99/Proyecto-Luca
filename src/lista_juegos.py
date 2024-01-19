import csv
from src.Juegos import Juegos

#RECORDADLE A JORGE QUE ESPABILE Y PIENSE DONDE METER ESTA BASURA
def val_per(a):
    try:
        return int(a)
    except ValueError:
        return "NA"

class Lista_Juegos:

    def __init__(self, csv_path):
        """
        Constructor de la clase Lista_jeugos.
        Genera dos atributos:
            lista_csv<Juegos>: Lista de los Juegos
            lista_rank<int>: Lista de los ranks escogidos

        Args:
            csv_path (str): string de la ruta del csv.
        """
        self.lista_csv, self.lista_rank, self.lista_names = Lista_Juegos.convert_csv_list(
            csv_path)

    def read_list(self):
        """
        Lee la lista de juegos.
        """
        # imprime 5 valores, cambiarlo al final
        for juego in self.lista_csv[:655]:
            print(juego)

    def exist(self, juego):
        """
        Comprueba si un juego especifico existe en la lista

        Args:
            juego (Juegos): Juego a comprobar.

        Returns:
            bool: True si existe el juego, False si no.
        """
        return juego.name in self.lista_names

    def genero(self):
        generos = []
        for juego in self.lista_csv[:10]:
            if not juego.genre in generos:
                generos.append(juego.genre)
        return generos

    def filter_genre(self, genero):
        for juego in self.lista_csv[:10]:
            if genero == juego.genre:
                print(juego)

    def check_duplicate_games(self, game):
        for existing_game in self.lista_csv:
            if game.name == existing_game.name:
                print("Juego duplicado")
                return True
        return False

    def add_game(self):
        new_game = Juegos.create_game()
        duplicado = self.check_duplicate_games(new_game)

        if not duplicado:
            rank = 1
            while rank in self.lista_rank:
                rank += 1
            try:
                new_game.rank = rank
                print(new_game)
                guardar = input("Quieres guardar el juego(Y/N): ")
                if guardar == "Y":
                    self.lista_csv.insert(rank - 1, new_game)
                    self.lista_rank.insert(rank - 1, rank)
                else:
                    print("Juego no guardado")
            except AttributeError:
                print("Juego no guardado")

    @staticmethod
    def convert_csv_list(csv_path):
        """
        Convertir de csv a lista.

        Args:
            csv_path (str): Direccion del csv.

        Returns:
            list: Lista de los jeugos del csv.
        """
        lista_csv = []
        lista_rank = []
        lista_names = []
        with open(csv_path, newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for fila in csv_reader:
                rank, name, platform, year, genre, publisher, na_Sales, eu_sales, jp_sales, other_sales, global_sales = fila
                juego = Juegos(name, platform, val_per(year), genre, publisher,
                               float(na_Sales), float(eu_sales), float(jp_sales), float(other_sales), float(global_sales), rank)
                lista_csv.append(juego)
                lista_rank.append(int(rank))
                lista_names.append(name)
        return lista_csv, lista_rank, lista_names
