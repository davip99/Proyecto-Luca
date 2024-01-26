import mysql.connector
from src.Juegos import Juegos
import configparser

config = configparser.ConfigParser()
config.read("src/csv/config.properties")

user = config.get("BBDD", "user")
password = config.get("BBDD", "password")
host = config.get("BBDD", "host")
database = config.get("BBDD", "database")
port = config.get("BBDD", "port")

conexion = mysql.connector.connect(
    user=user, password=password, host=host, database=database, port=port)


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


def borrar_juego(juegos):
    """
    Funcion borrar juego de la bbdd.

    Args:
        juego (int): Ranking del juego a borrar
    """
    try:
        cursor = conexion.cursor()
        query = ("SELECT * FROM Juegos WHERE `rank` = {};".format(juegos))
        cursor.execute(query)
        for id, rank, name, platform, year, genre, publisher, na_Sales, eu_sales, jp_sales, other_sales, global_sales in cursor:
            juego = Juegos(name, platform, year, genre, publisher, na_Sales,
                           eu_sales, jp_sales, other_sales, global_sales, rank, id)
        borrar = input(f'¿Quiere borrar el juego: {juego}? \nY/N:')
        if borrar == "Y":
            query = ("DELETE FROM Juegos WHERE `rank` = {};".format(juegos))
            cursor.execute(query)
            # conexion.commit() #Guarda los cambios en la bbdd
            print("Juego eliminado")
        else:
            print("Juego no eliminado")
    except Exception as e:
        print(f"Error al borrar el juego: {e}\nJuego no eliminado")
    finally:
        cursor.close()


def filter_years_even():
    """
    Funcion devuelve la lista de juegos publicados en años pares.

    Returns:
        list: lista de juegos publicados en años pares
    """
    lista_juegos = []
    cursor = conexion.cursor()

    try:
        # Utilizar parámetros de sustitución en lugar de formateo de cadena directo
        query = "SELECT * FROM Juegos WHERE year % 2 = 0"
        cursor.execute(query)

        for row in cursor:
            id, rank, name, platform, year, genre, publisher, na_Sales, eu_sales, jp_sales, other_sales, global_sales = row
            juego = Juegos(name, platform, year, genre, publisher, na_Sales,
                           eu_sales, jp_sales, other_sales, global_sales, rank)
            lista_juegos.append(juego)

    except Exception as e:
        print(f"Error al filtrar juegos: {e}")

    finally:
        cursor.close()

    return lista_juegos


def buscar_nombre(nombre):
    """
    Funcion devuelve la lista de juegos con el nombre especificado.

    Args:
        nombre (str): nombre que se desea buscar

    Returns:
        list: lista de los juegos del nombre especificado
    """
    lista_juegos = []
    cursor = conexion.cursor()
    query = (
        f"SELECT * FROM `Juegos` WHERE `name` = '{nombre}' ORDER BY Year;")
    cursor.execute(query)
    for id, rank, name, platform, year, genre, publisher, na_Sales, eu_sales, jp_sales, other_sales, global_sales in cursor:
        juego = Juegos(name, platform, year, genre, publisher, na_Sales,
                       eu_sales, jp_sales, other_sales, global_sales, rank, id)
        lista_juegos.append(juego)
    cursor.close()
    return lista_juegos


def actualizar(juego, new_juego):
    """
    Actualiza el juego con uno nuevo en la bbdd

    Args:
        juego (Juego): Juego antiguo
        new_juego (Juego): juego nuevo
    """
    cursor = conexion.cursor()
    query2 = f"UPDATE `Juegos` SET `name`='{new_juego.name}', `platform`='{new_juego.platform}', `year`={new_juego.year}, `genre`='{new_juego.genre}', `publisher`='{new_juego.publisher}', `na_Sales`={
        new_juego.na_Sales}, `eu_sales`={new_juego.eu_sales}, `jp_sales`={new_juego.jp_sales}, `other_sales`={new_juego.other_sales}, `global_sales`={new_juego.global_sales} WHERE id = {juego.id};"
    cursor.execute(query2)
    conexion.commit()
    cursor.close()


def juegos_media(lugar):
    """
    Recoge los juegos con media mas alta del lugar

    Args:
        lugar (str): lugar especificado

    Returns:
        list: lista de juegos
    """
    lista_juegos = []
    cursor = conexion.cursor()
    query = (f"SELECT `rank`, `name`, `platform`, `year`, `genre`, `publisher`, `{
             lugar}` FROM `Juegos` WHERE {lugar} > (SELECT AVG({lugar}) FROM `Juegos`) ORDER BY {lugar} desc;")
    cursor.execute(query)
    for row in cursor:
        lista_juegos.append(row)
    cursor.close()
    return lista_juegos
