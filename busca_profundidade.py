def busca_profundidade(grafo, inicio, objetivo, caminho=None, visitados=None):
    if caminho is None:
        caminho = []
    if visitados is None:
        visitados = set()

    caminho.append(inicio)
    visitados.add(inicio)

    if inicio == objetivo:
        return caminho

    for vizinho in grafo[inicio]:
        if vizinho not in visitados:
            resultado = busca_profundidade(grafo, vizinho, objetivo, caminho.copy(), visitados.copy())
            if resultado:
                return resultado
    print(f"❌ Tentativa mal sucedida: {caminho}")
    print(f'')
    return None
