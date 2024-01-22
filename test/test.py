import unittest
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.lista_juegos import Lista_Juegos as lj
from src.Juegos import Juegos as game
import src.bbdd

class PruebaTestFixture(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("-- Al inicio del sistema de test")
        
    @classmethod
    def tearDownClass(cls):        
        print("-- Al final del sistema de test")
        
    #Antes de cada test
    def setUp(self):
        print("-- Preparando el contexto del text")
        csv_path = "src/csv/vgsales.csv"
        self.lista_juegos = lj(csv_path)
        
    #Despues de cada test
    def tearDown(self):
        print("-- Destruyendo el contexto del test") 
        del(self.lista_juegos)      
    
    def test_elemento_concreto(self):
        game_to_check = game("Super Mario Bros.","NES","1985","Platform","Nintendo",29.08,3.58,6.81,0.77,40.24, "2")
        self.assertTrue(self.lista_juegos.exist(game_to_check))

    def test_check_duplicate(self):
        game_to_check = game("Super Mario Bros.","NES","1985","Platform","Nintendo",29.08,3.58,6.81,0.77,40.24, "2")
        self.assertTrue(self.lista_juegos.check_duplicate_games(game_to_check))

    def test_check_csv(self):
        csv = "src/csv/vgsales.csv"
        self.assertTrue(self.lista_juegos.verificar_csv(csv))
        lista_csv, lista_rank, lista_names = self.lista_juegos.convert_csv_list(csv)

        # Verifica si todas las listas son instancias de la clase list
        self.assertIsInstance(lista_csv, list)
        self.assertIsInstance(lista_rank, list)
        self.assertIsInstance(lista_names, list)
    
    def test_filtro_genero(self):
        genero = "Platform"
        salida_esperada = game("Super Mario Bros.","NES","1985","Platform","Nintendo",29.08,3.58,6.81,0.77,40.24, "2")
        filtro = self.lista_juegos.filter_genre(genero)
        for f in filtro:
            if f.genre in salida_esperada.genre:
                print(f)
        self.assertTrue(f.genre == salida_esperada.genre)
        print(f"Género esperado: {genero}, Género mostrado: {f.genre}")
        
    def test_type(self):
        for i in range(70):
            genero = self.lista_juegos.lista_csv[i].genre
            nombre = self.lista_juegos.lista_csv[i].name
            year = self.lista_juegos.lista_csv[i].year
            ventas = self.lista_juegos.lista_csv[i].na_Sales
            self.assertTrue(isinstance(genero, str) and isinstance(nombre, str) and isinstance(year, int) and isinstance(ventas, float))
        print(f"Los tipos de las variables corresponden con lo esperado")

    def test_primer_elemento(self):
        game_to_check = game("Wii Sports","Wii","2006","Sports","Nintendo",41.49,29.02,3.77,8.46,82.74, "1")
        self.assertTrue(str(self.lista_juegos.lista_csv[0]) == str(game_to_check))

    def test_game_atribute_null(self):
        self.assertIsInstance(game.create_game("a","Wii","2006","Sports","Nintendo",41.49,29.02,3.77,8.46,82.74), game)
        self.assertNotIsInstance(game.create_game(" ","Wii","2006","Sports","Nintendo",41.49,29.02,3.77,8.46,82.74), game)

    def test_juegos_siglo20(self):
        self.assertTrue(int(src.bbdd.filtro_siglo20().split("\n")[2].split()[1]) < 2001)

if __name__ == '__main__':
    unittest.main() 
