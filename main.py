from busca_profundidade import busca_profundidade
from apoio_visual import desenhar_grafo
import grafo  

# Dicionário associando opções a grafos
opcoes_grafos = {
    "1": ("Grafo Simples", grafo.grafo_1),
    "2": ("Grafo com Ciclo", grafo.grafo_2),
    "3": ("Grafo com Múltiplos Caminhos", grafo.grafo_3),
    "4": ("Grafo Disconexo", grafo.grafo_4),
}

# Menu para seleção do grafo
print("Escolha o grafo a ser utilizado:")
for chave, (nome, _) in opcoes_grafos.items():
    print(f"{chave}. {nome}")

escolha = input("Digite o número do grafo desejado: ").strip()

if escolha not in opcoes_grafos:
    print("❌ Opção inválida. Encerrando programa.")
    exit()

nome_grafo, grafo = opcoes_grafos[escolha]
print(f"✅ Você selecionou: {nome_grafo}")

desenhar_grafo(grafo, titulo=nome_grafo)

# Entrada do usuário
print("Nós disponíveis:", list(grafo.keys()))
inicio = input("Digite o nó inicial: ").strip().upper()
objetivo = input("Digite o nó objetivo: ").strip().upper()

if inicio not in grafo or objetivo not in grafo:
    print("❌ Nós inválidos.")
else:
    caminho = busca_profundidade(grafo, inicio, objetivo)
    if caminho:
        print(f'✅ Caminho de {inicio} até {objetivo}: {caminho}')
    else:
        print(f'⚠️ Nenhum caminho encontrado de {inicio} até {objetivo}.')
# Mostra visualmente o grafo
desenhar_grafo(grafo, titulo=nome_grafo)
