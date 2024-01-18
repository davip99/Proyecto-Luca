csv = "src/csv/vgsales.csv"

class Lista_Juegos:

    def convert_csv_list(csv):
        ''' Funcion convertir csv a lista
            Transforma el csv a una lista
            Devuelve la lista
        '''
        lista_csv = []

        with open(csv, newline='', encoding='utf-8') as archivo_csv:
            
            for fila in archivo_csv:
                lista_csv.append(fila)
        
        return lista_csv

