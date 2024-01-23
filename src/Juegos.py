import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
import src.util as util


class Juegos:

    def __init__(self, name, platform, year, genre, publisher, na_Sales, eu_sales, jp_sales, other_sales, global_sales, rank=0):
        """
        Constructor de la clase Juegos.

        Args:
            name (str): Nombre del videojuego.
            platform (str): Plataforma del videojuego.
            year (int): Año de salida del videojuego.
            genre (str): Genero del videojuego.
            publisher (str): Publisher del videojuego.
            na_Sales (float): Ventas en Norte America del videojuego.
            eu_sales (float): Ventas en Europa del videojuego.
            jp_sales (flaot): Ventas en Japon del videojuego.
            other_sales (float): Venta en otros lugares del videojuego.
            global_sales (float): Ventas globales del videojuego.
            rank (int, optional): Ventas globales del videojuego. Por defecto es 0.
        """
        self.name = name
        self.platform = platform
        self.year = year
        self.genre = genre
        self.publisher = publisher
        self.na_Sales = na_Sales
        self.eu_sales = eu_sales
        self.jp_sales = jp_sales
        self.other_sales = other_sales
        self.global_sales = global_sales
        self.rank = rank

    def __str__(self):
        """
        Metodo para retornar el objeto y sus atributos como una cadena de texto.

        Returns:
            str: Texto con los atributos del objeto juego.
        """
        texto = f"Rank: {self.rank}\n Name: {self.name}\n Platform: {self.platform}\n Year: {self.year}\n Genre: {self.genre}\n Publisher: {self.publisher}\n NA_Sales: {self.na_Sales}\n EU_sales: {self.eu_sales}\n JP_sales: {self.jp_sales}\n Other_sales: {self.other_sales}\n Global_sales: {self.global_sales}\n"
        return texto

    @staticmethod
    def new_game():
        try:
            name = util.input_obligatorio("Ingrese el nombre del juego: ")
            platform = util.input_obligatorio(
                "Ingrese la plataforma del juego: ")
            year = util.input_int("Ingrese el año de lanzamiento del juego: ")
            genre = util.input_obligatorio("Ingrese el género del juego: ")
            publisher = util.input_obligatorio("Ingrese el editor del juego: ")
            na_Sales = util.input_float(
                "Ingrese las ventas en América del Norte: ")
            eu_sales = util.input_float("Ingrese las ventas en Europa: ")
            jp_sales = util.input_float("Ingrese las ventas en Japón: ")
            other_sales = util.input_float(
                "Ingrese las ventas en otras regiones: ")
            global_sales = util.input_float("Ingrese las ventas globales: ")

        except ValueError as e:
            print(str(e))
        else:
            juego = Juegos.create_game(name, platform, year, genre, publisher,
                                       na_Sales, eu_sales, jp_sales, other_sales, global_sales)
            return juego

    @staticmethod
    def create_game(name, platform, year, genre, publisher,
                    na_Sales, eu_sales, jp_sales, other_sales, global_sales):
        """
        Crear un juego pidiendo los campos por consola.

        Returns:
            Juego: Objeto juego creado a partir de los valoes introducidos.
        """
        try:
            check = util.datos_vacios(name, platform, year, genre, publisher)
        except ValueError as e:
            print(str(e))
        else:
            juego = Juegos(name, platform, int(year), genre, publisher,
                           na_Sales, eu_sales, jp_sales, other_sales, global_sales)
            print(f"Juego '{juego.name}' creado con éxito")
            return juego
