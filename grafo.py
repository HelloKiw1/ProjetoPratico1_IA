# grafo_1: Grafo simples
grafo_1 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

    #     A
    #    / \
    #   B   C
    #  / \   \
    # D   E   F
    #      \
    #       F


# grafo_2: Grafo com ciclo
grafo_2 = { 
    'A': ['B'],
    'B': ['C'],
    'C': ['D', 'A'],
    'D': ['E'],
    'E': []
}

# A → B → C → D → E
# ↑         ↓
# └─────────┘


# grafo_3: Grafo com múltiplos caminhos
grafo_3 = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}

    #     A
    #    / \
    #   B   C
    #   |  / \
    #   D-E   |
    #    \   /
    #      F


# grafo_4: Grafo disconexo
grafo_4 = {
    'A': ['B'],
    'B': [],
    'C': ['D'],
    'D': []
}

# A → B    C → D


# grafo_5: Árvore binária
grafo_5 = {
    '1': ['2', '3'],
    '2': ['4', '5'],
    '3': ['6', '7'],
    '4': [],
    '5': ['8', '9'],
    '6': [],
    '7': [],
    '8': [],
    '9': []
}
    #     1
    #    / \
    #   2   3
    #  / \   \
    # 4   5   6
    #      / \
    #     8   9
