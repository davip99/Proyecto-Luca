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
        print("El juego existe")

    def test_check_duplicate(self):
        game_to_check = game("Super Mario Bros.","NES","1985","Platform","Nintendo",29.08,3.58,6.81,0.77,40.24, "2")
        self.assertTrue(self.lista_juegos.check_duplicate_games(game_to_check))

if __name__ == '__main__':
    unittest.main() 