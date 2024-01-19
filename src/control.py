from lista_juegos import Lista_Juegos as lj

milista = lj("src/csv/vgsales.csv")


def control(action):

    if action == 1:
        milista.add_game()

    elif action == 2:
        milista.read_list()

    elif action == 3:
        select_genre = milista.genero()
        for i in select_genre:
            print(i, end=" ")
        genre = input("\nSelecciona un genero para filtrar: ")
        milista.filter_genre(genre)
