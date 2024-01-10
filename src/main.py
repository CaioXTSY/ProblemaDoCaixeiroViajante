import file_converter
import PCV

file = file_converter.Converter(input('File name: '), input('Dimension: ')).grafo()
#retorno = PCV.resolver_tsp(file)

print(file)