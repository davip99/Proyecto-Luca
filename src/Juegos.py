
class Juegos:

    def __init__(self, name, platform, year, genre, publisher, na_Sales, eu_sales, jp_sales, other_sales, global_sales, rank=0):
        """
        Constructor de la clase Juegos

        Args:
            name (str): Nombre del videojuego.
            platform (str): Plataforma del videojuego
            year (int): Año de salida del videojuego
            genre (str): Genero del videojuego
            publisher (str): Publisher del videojuego
            na_Sales (float): Ventas en Norte America del videojuego
            eu_sales (float): Ventas en Europa del videojuego
            jp_sales (flaot): Ventas en Japon del videojuego
            other_sales (float): Venta en otros lugares del videojuego
            global_sales (float): Ventas globales del videojuego
            rank (int, optional): Ventas globales del videojuego. Por defecto es 0.
        """
        self.rank = rank
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

    def __str__(self):
        return f"Rank: {self.rank}\n Name: {self.name}\n Platform: {self.platform}\n Year: {self.year}\n Genre: {self.genre}\n Publisher: {self.publisher}\n NA_Sales: {self.na_Sales}\n EU_sales: {self.eu_sales}\n JP_sales: {self.jp_sales}\n Other_sales: {self.other_sales}\n Global_sales: {self.global_sales}\n"

    @staticmethod
    def create_game():
        """
        Crear un juego pidiendo los campos por consola

        Returns:
            Juego: Objeto Juego creado a partir  de los valoes
        """
        try:
            name = input_obligatorio("Ingrese el nombre del juego: ")
            platform = input_obligatorio("Ingrese la plataforma del juego: ")
            year = input_int("Ingrese el año de lanzamiento del juego: ")
            genre = input_obligatorio("Ingrese el género del juego: ")
            publisher = input_obligatorio("Ingrese el editor del juego: ")
            na_Sales = input_float("Ingrese las ventas en América del Norte: ")
            eu_sales = input_float("Ingrese las ventas en Europa: ")
            jp_sales = input_float("Ingrese las ventas en Japón: ")
            other_sales = input_float("Ingrese las ventas en otras regiones: ")
            global_sales = input_float("Ingrese las ventas globales: ")
        except ValueError as e:
            print(str(e))
        else:
            print(f"Juego '{name}' creado con éxito")
            return Juegos(name, platform, int(year), genre, publisher, na_Sales, eu_sales, jp_sales, other_sales, global_sales)


# Organizar mas tarde

def input_obligatorio(texto):
    valor = input(texto)
    if len(valor.strip()) <= 0:
        raise ValueError("Valor incorrecto, Este campo es obligatorio.")
    return valor

def input_int(texto):
    try:
        num_int = int(input(texto))
    except ValueError:
        raise ValueError("Valor incorrecto, se necesita un numero entero.")
    else:
        return num_int


def input_float(texto):
    try:
        num_float = float(input(texto))
    except ValueError:
        raise ValueError(
            "Valor no correcto, se necesita un numero entero o decimal.")
    else:
        return num_float
