class lista:
    def __init__(self):
        self.items = []

    def agregar(self, item):
        self.items.append(item)

    def remover(self, item):
        self.items.remove(item)
        
    def tamano(self):
        return len(self.items)

def leer_csv_y_agregar_a_lista(archivo, lista):
    juegos = open(archivo, "r")
    juegos.readline()
    for fila in juegos:
        juego = fila.strip().split(",")
        lista.agregar(juego)
    juegos.close()

mi_lista = lista()
leer_csv_y_agregar_a_lista("C:/Users/jorge/Downloads/vgsales.csv", mi_lista)

