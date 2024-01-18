

csv = "src/csv/vgsales.csv"
lista_csv = []
class Lista_Juegos:
    def __init__(self, rank, name, platform, year, genre, publisher, na_sales, eu_sales, jp_sales, other_sales, global_sales):
        self.rank = rank
        self.name = name
        self.platform = platform
        self.year = year
        self.genre = genre
        self.publisher = publisher
        self.na_sales = na_sales
        self.eu_sales = eu_sales
        self.jp_sales = jp_sales
        self.other_sales = other_sales
        self.global_sales = global_sales

    @staticmethod
    def convert_csv_list():
        ''' Funcion convertir csv a lista
            Transforma el csv a una lista
            Devuelve la lista
        '''
        
        with open(csv, newline='', encoding='utf-8') as archivo_csv:

            for fila in archivo_csv:
                lista_csv.append(fila)
        
        return lista_csv


    def read_list():
        '''
        Funcion para leer la lista de juegos e imrimirlos por pantalla
        '''
        separador = ","
        # imprime 5 valores, cambiarlo al final
        for juego in lista_csv[:5]:
            linea = juego.split(separador)
            linea_formateada = " | ".join(linea)
            print(linea_formateada)
