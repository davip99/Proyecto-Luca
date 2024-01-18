from Juegos import Juegos
import csv
import os


class Lista_Juegos:
    def __init__(self, csv_path):
        """
        Constructor de la clase Lista_jeugos.

        Args:
            csv_path (str): string de la ruta del csv.
        """
        self.lista_csv, self.lista_rank = Lista_Juegos.convert_csv_list(csv_path)

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
        with open(csv_path, newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for fila in csv_reader:
                rank, name, platform, year, genre, publisher, na_Sales, eu_sales, jp_sales, other_sales, global_sales = fila
                juego = Juegos(rank, name, platform, year, genre, publisher, na_Sales, eu_sales, jp_sales, other_sales, global_sales)
                lista_csv.append(juego)
                lista_rank.append(rank)
        return lista_csv, lista_rank

    def read_list(self):
        """
        Lee la lista de juegos.
        """
        # imprime 5 valores, cambiarlo al final
        for juego in self.lista_csv[:655]:
            print(juego)

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

    def load_existing_ranks():
        #Cambiar para no volver a leer los rangos
        # Construir la ruta completa al archivo CSV
        #csv_file_path = 'C:\\Users\\carma\\Visual Studio Code\\Proyecto\\Proyecto-Luca\\src\\csv\\vgsales.csv'
        script_directory = os.path.dirname(os.path.abspath(__file__))
        os.chdir(script_directory)
        
        csv_folder = 'csv'  # Ruta relativa desde el directorio actual del script
        csv_file_name = 'vgsales.csv'
        csv_file_path = os.path.join(csv_folder, csv_file_name)

        # Función para cargar la lista de rangos desde un archivo CSV
        existing_ranks = []
        with open(csv_file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                try:
                    rank = int(row[0])  
                    existing_ranks.append(rank)
                except ValueError:
                    pass  # Ignoramos las filas que no contienen números en la primera columna
        return existing_ranks

    def add_game(self):
        #implementar lista rangos
        new_game = Juegos.create_game()
        Lista_Juegos.load_existing_ranks()
        rank = 1
        while rank in Lista_Juegos.load_existing_ranks():
            rank +=1
        new_game.rank = rank
        print(new_game)
        guardar = input("Quieres guardar el juego(Y/N): ")
        if guardar == "Y":
            self.lista_csv.insert(rank-1, new_game)
        else:
            print("Juego no guardado")
        return self.lista_csv

