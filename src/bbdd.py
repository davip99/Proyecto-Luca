import mysql.connector

conexion = mysql.connector.connect(user='root',
    password='FF1CD5HgBggF6Gb3B-eb6452geEHeEE5',
    host='roundhouse.proxy.rlwy.net',
    database='railway',
    port='15049')

cursor = conexion.cursor()

nombre = 'railway'
cursor.execute("USE {}".format(nombre))


def filtro_siglo20(cursor):
    query = ("SELECT name, platform, year, genre, publisher FROM Juegos "
             "WHERE year < 2001")
    cursor.execute(query)
    for (name, platform, year, genre, publisher) in cursor:
        print("{}, {}, {}, {}, {}".format(name, platform, year, genre, publisher))

    cursor.close()
    conexion.close()

filtro_siglo20(cursor)



