from lista_juegos import Lista_Juegos as lj

def control(action):
    milista = lj("src/csv/vgsales.csv")
    if action == 1:
        pass
        #create_game = lj.create_game()
        #lj.add_game(create_game)
    elif action == 2:
        milista.read_list()
    elif action == 3:
        select_genre = milista.genero()
        for i in select_genre:
            print(i, end=" ")
        genre = input("\nSelecciona un genero para filtrar: ")
        milista.filter_genre(genre)

control(3)
    

