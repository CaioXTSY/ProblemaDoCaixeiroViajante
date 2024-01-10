class Converter:
    def __init__(self, file, length) -> None:
        self.length = length
        with open(file, 'r') as arquivo:
            self.lista = arquivo.read()

    def matrix_converter(self):
        grafo = [float(i) for i in self.lista.split()]
        grafo = [grafo[i:i + int(self.length)] for i in range(0, len(grafo), int(self.length))]
        return grafo

    def grafo(self):
        matriz_convertida = self.matrix_converter()
        grafo_dict = {}

        for i, linha in enumerate(matriz_convertida, start=1):
            grafo_dict[i] = linha

        return grafo_dict