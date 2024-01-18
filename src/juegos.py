import Clase_LISTA
class Juegos:

    def __init__(self, rank, name, platform, year, genre, publisher, na_Sales, eu_sales, jp_sales, other_sales):
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


    def genero(a):
        """
        Muestra solo de los 17 primeros juegos, CAMBIAR AL FINAL POR FAVOOR :_(
        :return:
        """
        for juego in lista_juegos[:17]:
            if juego.genre == a:
                linea = Clase_LISTA.mi_lista[(lista_juegos.index(juego)) + 1].split(",")
                linea_formateada = " | ".join(linea)
                print(linea_formateada)


lista_juegos = []
for i in range(1, len(Clase_LISTA.mi_lista)):
    ref = Clase_LISTA.mi_lista[i].split(",")
    juegos = Juegos(ref[0], ref[1], ref[2], ref[3], ref[4], ref[5], ref[6], ref[7], ref[8], ref[9])
    lista_juegos.append(juegos)


"""
                                 PRUEBAS
Juegos.genero("Sports")
print("-------------------------------------------------")
Juegos.genero("Platform")
print("-------------------------------------------------")
Juegos.genero("Shooter")
print("-------------------------------------------------")
Juegos.genero("Puzzle")
print("-------------------------------------------------")
Juegos.genero("Action")
"""
