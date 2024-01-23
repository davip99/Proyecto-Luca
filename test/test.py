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
        print("\nElemento concreto existe\n")

    def test_check_duplicate(self):
        game_to_check = game("Super Mario Bros.","NES","1985","Platform","Nintendo",29.08,3.58,6.81,0.77,40.24, "2")
        self.assertTrue(self.lista_juegos.check_duplicate_games(game_to_check))
        print("\nJuego duplicado\n")

    def test_check_csv(self):
        csv = "src/csv/vgsales.csv"
        self.assertTrue(self.lista_juegos.verificar_csv(csv))
        lista_csv, lista_rank, lista_names = self.lista_juegos.convert_csv_list(csv)

        # Verifica si todas las listas son instancias de la clase list
        self.assertIsInstance(lista_csv, list)
        self.assertIsInstance(lista_rank, list)
        self.assertIsInstance(lista_names, list)
        print("\nTodas las listas son instancias de la clase list\n")
    
    def test_filtro_genero(self):
        genero = "Platform"
        salida_esperada = game("Super Mario Bros.","NES","1985","Platform","Nintendo",29.08,3.58,6.81,0.77,40.24, "2")
        filtro = self.lista_juegos.filter_genre(genero)
        for f in filtro:
            if f.genre in salida_esperada.genre:
                print(f)
        self.assertTrue(f.genre == salida_esperada.genre)
        print(f"\nGénero esperado: {genero}, Género mostrado: {f.genre}\n")
        
    def test_type(self):
        rango = len(self.lista_juegos.lista_csv)
        for i in range(rango):
            genero = self.lista_juegos.lista_csv[i].genre
            nombre = self.lista_juegos.lista_csv[i].name
            year = self.lista_juegos.lista_csv[i].year
            ventas = self.lista_juegos.lista_csv[i].na_Sales
            self.assertTrue(isinstance(genero, str) and isinstance(nombre, str) and (isinstance(year, str) or isinstance(year, int)) and isinstance(ventas, float))
        print(f"\nLos tipos de las variables corresponden con lo esperado\n")

    def test_primer_elemento(self):
        game_to_check = game("Wii Sports","Wii","2006","Sports","Nintendo",41.49,29.02,3.77,8.46,82.74, "1")
        self.assertTrue(str(self.lista_juegos.lista_csv[0]) == str(game_to_check))
        print("\nPrimer elemento existe\n")

    def test_game_atribute_null(self):
        self.assertIsInstance(game.create_game("a","Wii","2006","Sports","Nintendo",41.49,29.02,3.77,8.46,82.74), game)
        self.assertNotIsInstance(game.create_game(" ","Wii","2006","Sports","Nintendo",41.49,29.02,3.77,8.46,82.74), game)
        print("\nError al introducir un juego con atributos null\n")

    def test_juegos_siglo20(self):
        listado = src.bbdd.listar_siglo20()
        for juego in listado:
            self.assertTrue(juego.year < 2001)
        print("\nLos juegos mostrados son previos al s. XXI\n")

    def test_suma_juegos_nintendo(self):
        cursor = src.bbdd.conexion.cursor()
        query = src.bbdd.listar_publisher('Nintendo')
        total_nintendo = len(query)
        query2 = ("select count(publisher), platform from Juegos where publisher = 'Nintendo' group by platform;")
        cursor.execute(query2)
        total_plataforma = 0
        for count, b in cursor:
            total_plataforma += count
        self.assertEqual(total_nintendo, total_plataforma)
        print("\nLa suma de los juegos de Nintendo es igual a los juegos de sus plataformas\n")

    def test_juegos_publisher(self):
        listado = src.bbdd.listar_publisher("Prueba123")
        self.assertTrue(len(listado)==0)
        print("\nNo se devuelven datos de publishers desconocidos\n")

    def test_top_sales(self):
        listado = src.bbdd.listar_top("na_sales")
        test = True
        na_sales_max = listado[0][6]
        for fila in listado:
            if fila[6] > na_sales_max:
                test = False
            na_sales_max = fila[6]
        self.assertTrue(test)

        """
        def test_provisional(self):
        b = src.lista_juegos.Lista_Juegos.convert_csv_list("src/csv/vgsales.csv")
        valores_ventas = []
        for juego in b[0]:
                valores_ventas.append(juego.na_Sales)
        a = src.bbdd.listar_top('na_sales')
        top_na_sales = []
        for juego in a:
            top_na_sales.append(juego[6])
        valores_ventas = sorted(valores_ventas, reverse=True)
        #print(valores_ventas[:5])
        #print(top_na_sales)
        self.assertTrue(top_na_sales == valores_ventas[:5])
        """

if __name__ == '__main__':
    unittest.main()
