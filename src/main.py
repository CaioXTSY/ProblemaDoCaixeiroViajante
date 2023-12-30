import file_converter
import PCV

file = file_converter.converter(input('File name: '), input('Dimension: '))
retorno = PCV.resolver_tsp(file.grafo())

print(retorno)
