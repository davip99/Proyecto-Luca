<<<<<<< HEAD
import csv
import os


def load_existing_ranks():
    
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






def create_game(existing_ranks):
    
    rank = 1
    while rank in existing_ranks:
        rank += 1
        
    # Solicitar al usuario que ingrese los valores para los campos
    name = input("Ingrese el nombre del juego: ")
    platform = input("Ingrese la plataforma del juego: ")
    year = input("Ingrese el año de lanzamiento del juego: ")
    genre = input("Ingrese el género del juego: ")
    publisher = input("Ingrese el editor del juego: ")
    na_sales = input("Ingrese las ventas en América del Norte: ")
    eu_sales = input("Ingrese las ventas en Europa: ")
    jp_sales = input("Ingrese las ventas en Japón: ")
    other_sales = input("Ingrese las ventas en otras regiones: ")
    global_sales = input("Ingrese las ventas globales: ")
    
    
    if not name:
        print("Error: El nombre del juego es obligatorio.")
        return False
    
    if year and not year.isdigit():
        print("Error: El año de lanzamiento debe ser un número entero.")
        return False
    
    
    game_created = True
    print(f"Juego '{name}' creado con éxito. Rango asignado automáticamente: {rank}")
    
    # Devolver el resultado como un booleano
    return game_created


existing_ranks = load_existing_ranks()
if create_game(existing_ranks):
    print("¡Juego creado con éxito!")
else:
    print("Error al crear el juego.")





=======
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
>>>>>>> bad641d1e57a53d92cdd9c4bb22e2c22c299115c
