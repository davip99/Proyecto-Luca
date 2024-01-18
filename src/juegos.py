class Juegos:
    
    def __init__(self, rank, name, platform, year, genre, publisher, na_Sales, eu_sales, jp_sales, other_sales, global_sales):
        """
        Constructor de la clase Juegos

        Args:
            rank (int): Rango del videojuego.
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
        """
        Metodo para mostrar toda la informacion del objeto juego.

        Returns:
            str: Los datos de la clase en texto.
        """
        return f"Rank: {self.rank},\n Name: {self.name},\n Platform: {self.platform},\n Year: {self.year},\n Genre: {self.genre},\n Publisher: {self.publisher},\n NA_Sales: {self.na_Sales},\n EU_sales: {self.eu_sales},\n JP_sales: {self.jp_sales},\n Other_sales: {self.other_sales},\n Global_sales: {self.global_sales}\n"