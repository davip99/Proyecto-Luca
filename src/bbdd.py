import mysql.connector
from Juegos import Juegos

conexion = mysql.connector.connect(user='root',
                                   password='FF1CD5HgBggF6Gb3B-eb6452geEHeEE5',
                                   host='roundhouse.proxy.rlwy.net',
                                   database='railway',
                                   port='15049')


def filtro_siglo20():
    # Establece conexion con la base de datos y prepara la query
    cursor = conexion.cursor()
    query = ("SELECT name, platform, year, genre, publisher, na_sales, eu_sales, jp_sales, other_sales, global_sales FROM Juegos "
             "WHERE year < 2001")

    #Ejecuta la query y muestra por pantalla los elementos seleccionados
    cursor.execute(query)
    for (name, platform, year, genre, publisher, na_sales, eu_sales, jp_sales, other_sales, global_sales) in cursor:
        print("Name: {}\n Platform: {}\n Year: {}\n Genre: {}\n Publlisher: {}\n NA_sales: {}\n EU_sales: {}\n JP_sales: {}\n Other_sales: {}\n Global_sales: {}\n".format(name, platform, year, genre, publisher, na_sales, eu_sales, jp_sales, other_sales, global_sales))
    return "Name: {}\n Platform: {}\n Year: {}\n Genre: {}\n Publlisher: {}\n NA_sales: {}\n EU_sales: {}\n JP_sales: {}\n Other_sales: {}\n Global_sales: {}\n".format(name, platform, year, genre, publisher, na_sales, eu_sales, jp_sales, other_sales, global_sales)

    # Cierra la conexion
    cursor.close()
    conexion.close()


def listar_editores():
    lista_editores = []
    cursor = conexion.cursor()
    query = ("SELECT distinct(publisher) FROM `Juegos` ORDER BY publisher;")
    cursor.execute(query)
    for editor in cursor:
        lista_editores.append(editor[0])
    cursor.close()
    return lista_editores


def listar_juegos_nintendo():
    lista_jeugos = []
    cursor = conexion.cursor()
    query = ("SELECT * FROM `Juegos` WHERE `publisher` = 'Nintendo' ORDER BY name;")
    cursor.execute(query)
    for id, rank, name, platform, year, genre, publisher, na_Sales, eu_sales, jp_sales, other_sales, global_sales in cursor:
        juego = Juegos(name, platform, year, genre, publisher, na_Sales,
                       eu_sales, jp_sales, other_sales, global_sales, rank)
        lista_jeugos.append(juego)
    cursor.close()
    return lista_jeugos
