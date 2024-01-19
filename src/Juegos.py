
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
        return f"Rank: {self.rank},\n Name: {self.name},\n Platform: {self.platform},\n Year: {self.year},\n Genre: {self.genre},\n Publisher: {self.publisher},\n NA_Sales: {self.na_Sales},\n EU_sales: {self.eu_sales},\n JP_sales: {self.jp_sales},\n Other_sales: {self.other_sales},\n Global_sales: {self.global_sales}\n"

    @staticmethod
    def create_game():
        """
        Crear un juego pidiendo los campos por consola

        Returns:
            Juego: Objeto Juego creado a partir  de los valoes
        """
        name = input("Ingrese el nombre del juego: ")
        platform = input("Ingrese la plataforma del juego: ")
        year = input("Ingrese el año de lanzamiento del juego: ")
        genre = input("Ingrese el género del juego: ")
        publisher = input("Ingrese el editor del juego: ")
        na_Sales = float(input("Ingrese las ventas en América del Norte: "))
        eu_sales = float(input("Ingrese las ventas en Europa: "))
        jp_sales = float(input("Ingrese las ventas en Japón: "))
        other_sales = float(input("Ingrese las ventas en otras regiones: "))
        global_sales = float(input("Ingrese las ventas globales: "))

        if not name:
            print("Error: El nombre del juego es obligatorio.")
            return False

        if not platform:
            print("Error: La plataforma del juego es obligatorio.")
            return False
        
        if not genre:
            print("Error: El género del juego es obligatorio.")
            return False

        if year and not year.isdigit():
            print("Error: El año de lanzamiento debe ser un número entero.")
            return False

        try:
            na_Sales = float(na_Sales)
        except ValueError:
            print("Error: Todos los valores en ventas deben ser números.")
            return False

        try:
            eu_sales = float(eu_sales)
        except ValueError:
            print("Error: Todos los valores en ventas deben ser números.")
            return False

        try:
            jp_sales = float(jp_sales)
        except ValueError:
            print("Error: Todos los valores en ventas deben ser números.")
            return False

        try:
            other_sales = float(other_sales)
        except ValueError:
            print("Error: Todos los valores en ventas deben ser números.")
            return False

        try:
            global_sales = float(global_sales)
        except ValueError:
            print("Error: Todos los valores en ventas deben ser números.")
            return False

        game_created = True
        print(f"Juego '{name}' creado con éxito")

        # Devolver el resultado como un booleano
        return Juegos(name, platform, int(year), genre, publisher, na_Sales, eu_sales, jp_sales, other_sales, global_sales)
