import matplotlib.pyplot as plt
import networkx as nx

def desenhar_grafo(grafo_dict, titulo="Visualização em Camadas"):
    G = nx.DiGraph(grafo_dict)  

    try:
        pos = nx.nx_pydot.graphviz_layout(G, prog="dot")
    except:
        pos = nx.spring_layout(G, seed=42)

    plt.figure(figsize=(8, 6))
    nx.draw(
        G, pos,
        with_labels=True,
        node_color="#B0D6F2",
        node_size=1400,
        font_size=12,
        font_weight="bold",
        arrows=True,
        edge_color="#333333"
    )
    plt.title(titulo, fontsize=14)
    plt.show()
