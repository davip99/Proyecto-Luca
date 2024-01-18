from lista_juegos import Lista_Juegos as lj

def control(action):

    lj.convert_csv_list()

    if action == 1:
        pass
        #create_game = lj.create_game()
        #lj.add_game(create_game)
    elif action == 2:
        lj.read_list()

control(2)
