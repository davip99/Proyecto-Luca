import mysql.connector
from Juegos import Juegos

conexion = mysql.connector.connect(
    user='root',
    password='FF1CD5HgBggF6Gb3B-eb6452geEHeEE5',
    host='roundhouse.proxy.rlwy.net',
    database='railway',
    port='15049'
)

def listar_siglo20():
    lista_juegos = []
    # Establece conexion con la base de datos y prepara la query
    cursor = conexion.cursor()
    query = ("SELECT * FROM Juegos "
             "WHERE year < 2001;")

    # Ejecuta la query y añade los valores a lista_juegos
    cursor.execute(query)
    for  id, rank, name, platform, year, genre, publisher, na_Sales, eu_sales, jp_sales, other_sales, global_sales in cursor:
        juego = Juegos(name, platform, year, genre, publisher, na_Sales, eu_sales, jp_sales, other_sales, global_sales, rank)
        lista_juegos.append(juego)

    # Cierra la conexion y devuelve lista_juegos
    cursor.close()
    return lista_juegos

   
    
    conexion.close()

def listar_editores():
    lista_editores = []
    # Establece conexion con la base de datos y prepara la query
    cursor = conexion.cursor()
    query = ("SELECT distinct(publisher) FROM `Juegos` ORDER BY publisher;")

    # Ejecuta la query y añade los valores a lista_editores
    cursor.execute(query)
    for editor in cursor:
        lista_editores.append(editor[0])

    # Cierra la conexion y devuelve lista_editores
    cursor.close()
    return lista_editores

def listar_juegos_nintendo():
    lista_juegos = []
    # Establece conexion con la base de datos y prepara la query
    cursor = conexion.cursor()
    query = ("SELECT * FROM `Juegos` WHERE `publisher` = 'Nintendo' ORDER BY `rank`;")

    # Ejecuta la query y añade los valores a lista_juegos
    cursor.execute(query)
    for  id, rank, name, platform, year, genre, publisher, na_Sales, eu_sales, jp_sales, other_sales, global_sales in cursor:
        juego = Juegos(name, platform, year, genre, publisher, na_Sales, eu_sales, jp_sales, other_sales, global_sales, rank)
        lista_juegos.append(juego)

    # Cierra la conexion y devuelve lista_juegos
    cursor.close()
    return lista_juegos

def listar_top(lugar):
    lista_juegos = []
    # Establece conexion con la base de datos y prepara la query
    cursor = conexion.cursor()
    query = ("SELECT `rank`, name, platform, year, genre, publisher, {} FROM Juegos ORDER BY {} DESC LIMIT 5;".format(lugar, lugar))
    
    # Ejecuta la query y añade los valores a lista_juegos
    cursor.execute(query)
    for  row in cursor:
        lista_juegos.append(row)

    # Cierra la conexion y devuelve lista_juegos
    cursor.close()
    return lista_juegos
