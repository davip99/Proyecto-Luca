from Juegos import Juegos
import csv


class Lista_Juegos:
    def __init__(self, csv_path):
        self.lista_csv = Lista_Juegos.convert_csv_list(csv_path)

    @staticmethod
    def convert_csv_list(csv_path):
        ''' Funcion convertir csv a lista
            Transforma el csv a una lista
            Devuelve la lista
        '''
        lista_csv = []
        with open(csv_path, newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for fila in csv_reader:
                rank, name, platform, year, genre, publisher, na_Sales, eu_sales, jp_sales, other_sales, global_sales = fila
                juego = Juegos(rank, name, platform, year, genre, publisher, na_Sales, eu_sales, jp_sales, other_sales, global_sales)
                lista_csv.append(juego)
        return lista_csv

    def read_list(self):
        '''
        Funcion para leer la lista de juegos e imrimirlos por pantalla
        '''
        # imprime 5 valores, cambiarlo al final
        for juego in self.lista_csv[:10]:
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