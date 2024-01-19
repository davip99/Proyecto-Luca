import unittest
from lista_juegos import Lista_Juegos as lj

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
        self.elemento_concreto = ['2,Super Mario Bros.,NES,1985,Platform,Nintendo,29.08,3.58,6.81,0.77,40.24']
        
    #Despues de cada test
    def tearDown(self):
        print("-- Destruyendo el contexto del test")
        del(self.elemento_concreto)        
    
        
    def test_tonto(self):
        self.assertTrue(True)

    def test_elemento_concreto(self):
        print("Prueba existe un elemento concreto")
        lj.convert_csv_list()
        r = lj.read_list()
        self.assertIn(self.elemento_concreto, r)