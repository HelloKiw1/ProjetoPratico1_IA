# grafo_1: Grafo simples
grafo_1 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

    #     A
    #    / \
    #   B   C
    #  / \   \
    # D   E   F
    #      \
    #       F


# grafo_2: Grafo com cSiclo
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
    'C': ['E', 'F'],
    'D': ['F'],
    'E': ['D'],
    'F': [],
    #'G': []
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