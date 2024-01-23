import mysql.connector
from src.Juegos import Juegos

conexion = mysql.connector.connect(user='root',
                                   password='FF1CD5HgBggF6Gb3B-eb6452geEHeEE5',
                                   host='roundhouse.proxy.rlwy.net',
                                   database='railway',
                                   port='15049')


def listar_siglo20():
    """
    Funcion devuelve los juegos que sean del siglo 
    """
    lista_juegos = []
    # Establece conexion con la base de datos y prepara la query
    cursor = conexion.cursor()
    query = ("SELECT * FROM Juegos "
             "WHERE year < 2001")

    # Ejecuta la query y muestra por pantalla los elementos seleccionados
    cursor.execute(query)
    for id, rank, name, platform, year, genre, publisher, na_Sales, eu_sales, jp_sales, other_sales, global_sales in cursor:
        juego = Juegos(name, platform, year, genre, publisher, na_Sales,
                       eu_sales, jp_sales, other_sales, global_sales, rank)
        lista_juegos.append(juego)
    cursor.close()
    return lista_juegos
    

def listar_editores():
    """
    Funcion devuelve la lista de editores de juegos

    Returns:
        list: lista de editores
    """
    lista_editores = []
    cursor = conexion.cursor()
    query = ("SELECT distinct(publisher) FROM `Juegos` ORDER BY publisher;")
    cursor.execute(query)
    for editor in cursor:
        lista_editores.append(editor[0])
    cursor.close()
    return lista_editores


def listar_publisher(publisher):
    """
    Funcion devuelve la lista de juegos de un publisher especificado.

    Args:
        publisher (str): publisher que se desea buscar

    Returns:
        list: lista de los juegos del publisher especificado
    """
    lista_juegos = []
    cursor = conexion.cursor()
    query = (
        f"SELECT * FROM `Juegos` WHERE `publisher` = '{publisher}' ORDER BY name;")
    cursor.execute(query)
    for id, rank, name, platform, year, genre, publisher, na_Sales, eu_sales, jp_sales, other_sales, global_sales in cursor:
        juego = Juegos(name, platform, year, genre, publisher, na_Sales,
                       eu_sales, jp_sales, other_sales, global_sales, rank)
        lista_juegos.append(juego)
    cursor.close()
    return lista_juegos

def listar_top(lugar):
    """
    Funcion devuelve la lista de top ventas de juegos de un lugar.

    Args:
        lugar (str): Lugar deseado

    Returns:
        list: lista de top ventas de juegos del lugar especificado
    """
    lista_juegos = []
    # Establece conexion con la base de datos y prepara la query
    cursor = conexion.cursor()
    query = ("SELECT `rank`, name, platform, year, genre, publisher, {} FROM Juegos ORDER BY {} DESC LIMIT 5;".format(lugar, lugar))

    # Ejecuta la query y añade los valores a lista_juegos
    cursor.execute(query)
    for row in cursor:
        lista_juegos.append(row)

    # Cierra la conexion y devuelve lista_juegos
    cursor.close()
    return lista_juegos
