csv = "../src/csv/vgsales.csv"

lista_csv = []


class Lista_Juegos:

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

        return lista_csv


mi_lista = Lista_Juegos.convert_csv_list()
