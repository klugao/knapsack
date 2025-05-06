import random
import importlib

# Escolha qual instância testar: "instancia_10_itens", "instancia_1000_itens" ou "instancia_10000_itens"
INSTANCIA_ATUAL = "instancia_10000_itens"

# Importar a instância escolhida
dados = importlib.import_module(INSTANCIA_ATUAL)
pesos = dados.pesos
valores = dados.valores
capacidade = dados.capacidade

# Parâmetros do Algoritmo Genético
tamanho_populacao = 50
geracoes = 100
taxa_mutacao = 0.1
penalizar_solucoes_invalidas = True  # Variável booleana para penalizar ou não

n_itens = len(pesos)

# Função para gerar um indivíduo (solução)
def gerar_individuo():
    return [random.randint(0, 1) for _ in range(n_itens)]

# Função para avaliar um indivíduo
def avaliar(individuo):
    peso_total = sum([gene * pesos[i] for i, gene in enumerate(individuo)])
    valor_total = sum([gene * valores[i] for i, gene in enumerate(individuo)])

    # Penalizar ou não dependendo da variável booleana
    if peso_total > capacidade:
        if penalizar_solucoes_invalidas:
            return 0  # Penalizar com valor 0
        else:
            return valor_total  # Apenas descartar a solução sem penalizar
    return valor_total

# Seleção por torneio (3 indivíduos aleatórios)
def selecao_torneio(populacao):
    competidores = random.sample(populacao, 3)
    return max(competidores, key=avaliar)

# Crossover (ponto único)
def crossover(pai1, pai2):
    ponto = random.randint(1, n_itens - 1)
    filho1 = pai1[:ponto] + pai2[ponto:]
    filho2 = pai2[:ponto] + pai1[ponto:]
    return filho1, filho2

# Mutação
def mutar(individuo):
    return [1 - gene if random.random() < taxa_mutacao else gene for gene in individuo]

# Algoritmo Genético principal
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

# Executar o algoritmo e exibir os resultados
solucao, valor = algoritmo_genetico()
peso_final = sum([solucao[i] * pesos[i] for i in range(n_itens)])

print("\n📦 Algoritmo Genético - Problema da Mochila")
print(f"🔹 Instância usada: {INSTANCIA_ATUAL} ({n_itens} itens)")
print(f"🎯 Melhor solução encontrada: {solucao}")
print(f"💰 Valor total: {valor}")
print(f"⚖️ Peso total: {peso_final} (Capacidade: {capacidade})")