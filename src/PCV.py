from itertools import permutations


def calcular_distancia(caminho, grafo):
    distancia_total = 0
    for i in range(len(caminho) - 1):
        distancia_total += grafo[caminho[i]][caminho[i + 1]]
    distancia_total += grafo[caminho[-1]][caminho[0]]
    return distancia_total

def resolver_tsp(grafo):
    num_cidades = len(grafo)
    melhor_caminho = None
    melhor_distancia = float('inf')

    cidades = list(range(num_cidades))
    todas_permutacoes = permutations(cidades)

    for caminho in todas_permutacoes:
        distancia_atual = calcular_distancia(caminho, grafo)
        if distancia_atual < melhor_distancia:
            melhor_distancia = distancia_atual
            melhor_caminho = caminho

    return [melhor_caminho, melhor_distancia]