import unittest
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from src.lista_juegos import Lista_Juegos as lj
from src.Juegos import Juegos as game

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
        genero = "Shooter"
        filtro = self.lista_juegos.filter_genre(genero).genre
        self.assertTrue(genero == filtro)
        print(f"Género esperado: {genero}, Género mostrado: {filtro}")
        
    def test_type(self):
        for i in range(70):
            genero = self.lista_juegos.lista_csv[i].genre
            nombre = self.lista_juegos.lista_csv[i].name
            year = self.lista_juegos.lista_csv[i].year
            ventas = self.lista_juegos.lista_csv[i].na_Sales
            self.assertTrue(isinstance(genero, str) and isinstance(nombre, str) and isinstance(year, int) and isinstance(ventas, float))
        print(f"Los tipos de las variables corresponden con lo esperado")
if __name__ == '__main__':
    unittest.main() 
