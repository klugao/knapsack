import random

# Dados do problema
pesos = [2, 3, 4, 5]
valores = [3, 4, 5, 6]
capacidade = 5
tamanho_populacao = 50
geracoes = 100
taxa_mutacao = 0.1

n_itens = len(pesos)

def gerar_individuo():
    return [random.randint(0, 1) for _ in range(n_itens)]

def avaliar(individuo):
    peso_total = sum([gene * pesos[i] for i, gene in enumerate(individuo)])
    valor_total = sum([gene * valores[i] for i, gene in enumerate(individuo)])
    if peso_total > capacidade:
        return 0
    return valor_total

def selecao_torneio(populacao):
    competidores = random.sample(populacao, 3)
    return max(competidores, key=avaliar)

def crossover(pai1, pai2):
    ponto = random.randint(1, n_itens - 1)
    filho1 = pai1[:ponto] + pai2[ponto:]
    filho2 = pai2[:ponto] + pai1[ponto:]
    return filho1, filho2

def mutar(individuo):
    return [1 - gene if random.random() < taxa_mutacao else gene for gene in individuo]

def algoritmo_genetico():
    populacao = [gerar_individuo() for _ in range(tamanho_populacao)]
    melhor_solucao = max(populacao, key=avaliar)

    for _ in range(geracoes):
        nova_populacao = []

        while len(nova_populacao) < tamanho_populacao:
            pai1 = selecao_torneio(populacao)
            pai2 = selecao_torneio(populacao)
            filho1, filho2 = crossover(pai1, pai2)
            nova_populacao.append(mutar(filho1))
            nova_populacao.append(mutar(filho2))

        populacao = nova_populacao
        melhor_na_geracao = max(populacao, key=avaliar)
        if avaliar(melhor_na_geracao) > avaliar(melhor_solucao):
            melhor_solucao = melhor_na_geracao

    return melhor_solucao, avaliar(melhor_solucao)

solucao, valor = algoritmo_genetico()
print("Melhor solução encontrada:", solucao)
print("Valor total:", valor)
print("Peso total:", sum([solucao[i] * pesos[i] for i in range(n_itens)]))
