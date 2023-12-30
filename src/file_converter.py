class converter:
    def __init__(self, file, length) -> None:
        self.length = length
        with open(file, 'r') as arquivo:
            self.lista = arquivo.read()
    
    def matrix_converter(self, matriz, dimension):
        grafo = [float(i) for i in matriz.split()]
        grafo = [grafo[i:i + int(dimension)] for i in range(0, len(grafo), int(dimension))]
        return grafo
    
    def grafo(self):
        return self.matrix_converter(self.lista, self.length)