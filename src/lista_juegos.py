class lista:
    def __init__(self):
        self.items = []

    def agregar(self, item):
        self.items.append(item)

    def remover(self, item):
        self.items.remove(item)

    def obtener(self, index):
        return self.items[index]

    def tamano(self):
        return len(self.items)

def leer_csv_y_agregar_a_lista(file_name, lista):
    juegos = open(file_name, "r")
    juegos.readline()
    for row in juegos:
        values = row.strip().split(",")
        lista.agregar(values)
    juegos.close()

mi_lista = lista()
leer_csv_y_agregar_a_lista("C:/Users/jorge/Downloads/vgsales.csv", mi_lista)

print(mi_lista.obtener(0))
