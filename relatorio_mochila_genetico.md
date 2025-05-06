# Problema da Mochila 0/1 com Algoritmo Genético

## 👥 Integrantes
- Leonardo (Leo) – Engenharia de Software, Católica SC

## 🎯 Objetivo
Resolver o problema da mochila 0/1 utilizando um algoritmo bio-inspirado (Algoritmo Genético), aplicando técnicas heurísticas para encontrar soluções próximas do ótimo em problemas complexos de otimização.

## 📦 Descrição do Problema

Dado:
- Um conjunto de `n` itens com:
  - Peso: `w[i]`
  - Valor: `v[i]`
- Uma mochila com capacidade máxima `W`

Objetivo:
- Escolher um subconjunto de itens que maximize o valor total, sem exceder o peso da mochila.

Exemplo usado:
```python
pesos = [2, 3, 4, 5]
valores = [3, 4, 5, 6]
capacidade = 5
```

---

## 🧬 Algoritmo Utilizado: Algoritmo Genético (GA)

### 🔹 Representação
- Cada indivíduo é um vetor binário (ex: `[1, 0, 1, 0]`)
- 1 indica que o item está incluído; 0, que está fora da mochila

### 🔹 Operadores Genéticos
- **Seleção:** Torneio (3 indivíduos aleatórios)
- **Crossover:** Ponto único
- **Mutação:** Troca de bits com taxa de 10%
- **Elitismo:** Mantém a melhor solução entre as gerações

### 🔹 Avaliação (Fitness)
- Soma dos valores dos itens incluídos
- Penalização: fitness = 0 se o peso ultrapassar a capacidade da mochila

---

## 🧪 Resultados

### 🧾 Parâmetros
- População: 50 indivíduos
- Gerações: 100
- Taxa de mutação: 0.1

### 🏆 Melhor Solução Encontrada
```python
Melhor solução: [1, 1, 0, 0]
Valor total: 7
Peso total: 5
```

---

## 🧠 Dificuldades e Aprendizados

### ❗ Dificuldades
- Encontrar um equilíbrio entre mutação e crossover
- Evitar que a população convirja muito cedo (diversidade genética)

### 📘 Aprendizados
- O Algoritmo Genético se mostrou eficiente mesmo com instâncias pequenas
- A penalização por peso excedente é essencial para manter soluções viáveis
- A abordagem pode ser escalada facilmente para problemas maiores

---

## 📌 Testes Futuros
- Executar o algoritmo com 1.000 e 10.000 itens para avaliar escalabilidade
- Comparar com outros algoritmos bio-inspirados como PSO, ACO e Cuckoo

---

## 🧾 Referências
- Goldberg, D. E. *Genetic Algorithms in Search, Optimization and Machine Learning*
- OpenAI / ChatGPT – auxílio na construção e revisão do código
