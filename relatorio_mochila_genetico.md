# Relatório: Solução para o Problema da Mochila com Algoritmo Genético

Equipe: Eduardo Klug, Leonardo Rocha, Mateus de Faria, Mateus Mautone e Renan Iomes.

## Objetivo

O objetivo deste trabalho foi implementar uma solução para o Problema da Mochila 0/1 utilizando um Algoritmo Genético (GA). O algoritmo foi adaptado para maximizar o valor de itens selecionados, sem exceder a capacidade da mochila, utilizando técnicas de evolução genética: seleção, crossover, e mutação.

## Descrição do Problema da Mochila 0/1

O Problema da Mochila 0/1 é um problema clássico de otimização, no qual:

- Um conjunto de **n itens** está disponível, cada item tem:
  - Um **peso** `w[i]`
  - Um **valor** `v[i]`
- Há uma **mochila** com **capacidade limitada** `W`.
- O objetivo é selecionar um subconjunto de itens de forma que:
  - O **valor total** dos itens seja **máximo**.
  - O **peso total** dos itens selecionados não ultrapasse a **capacidade** da mochila.

## Algoritmo Genético Implementado

### Componentes do Algoritmo

1. **Representação dos Indivíduos**:
   - Cada indivíduo é representado por um vetor binário, onde cada bit indica se um item foi incluído (1) ou não (0).
   
2. **Função de Avaliação**:
   - A função de avaliação calcula o valor total de um indivíduo, penalizando soluções que excedem a capacidade da mochila.
   
3. **Seleção**:
   - A seleção é feita por **torneio** entre 3 indivíduos aleatórios da população. O vencedor é o indivíduo com o maior valor total, sem exceder a capacidade.

4. **Crossover (Recombinação)**:
   - O crossover é realizado por **ponto único**, onde os genes dos pais são combinados para gerar dois filhos.

5. **Mutação**:
   - A mutação altera aleatoriamente genes de um indivíduo com uma taxa de mutação pré-definida, com o objetivo de explorar novas soluções.

### Parâmetros do Algoritmo
- **Tamanho da População**: 50
- **Número de Gerações**: 100
- **Taxa de Mutação**: 0.1
- **Penalização de Soluções Inválidas**: Controlada por variável booleana `penalizar_solucoes_invalidas`

### Funcionamento da Penalização
- **Se `penalizar_solucoes_invalidas` for `True`**: Soluções que excedem a capacidade da mochila são penalizadas, atribuindo valor 0 a elas.
- **Se `penalizar_solucoes_invalidas` for `False`**: Soluções inválidas são descartadas sem penalização explícita, permitindo que o algoritmo tente encontrar outras soluções viáveis.

## Testes Realizados

### Instância Testada
- **Número de Itens**: 10
- **Pesos e Valores**: Conjunto aleatório de pesos e valores para 10 itens.
- **Capacidade da Mochila**: 50

### Resultados dos Testes

1. **Com `penalizar_solucoes_invalidas = True`**:
   - As soluções inválidas (com peso maior que a capacidade) foram penalizadas com valor 0.
   - O algoritmo conseguiu encontrar uma solução viável que maximizou o valor dentro da capacidade da mochila.

2. **Com `penalizar_solucoes_invalidas = False`**:
   - As soluções inválidas (com peso acima da capacidade) não foram penalizadas e, portanto, o algoritmo permitiu soluções que ultrapassaram a capacidade da mochila.
   - Como esperado, algumas dessas soluções excederam a capacidade da mochila, mas o valor total foi maior.

## Conclusão

O algoritmo genético foi eficaz para encontrar uma solução otimizada para o problema da mochila 0/1. A penalização de soluções inválidas com `penalizar_solucoes_invalidas = True` ajudou a evitar soluções inviáveis. Quando a penalização foi desativada (`False`), o algoritmo buscou soluções mais arriscadas, mas não garantiu que todas as soluções estivessem dentro dos limites da capacidade da mochila.

O próximo passo seria realizar ajustes finos, como a aumento da taxa de mutação e a melhora da inicialização da população para garantir uma convergência mais rápida e melhor desempenho em instâncias maiores (como 1000 ou 10000 itens).

## Código Fonte

O código do algoritmo genético utilizado para resolver o problema da mochila 0/1 está disponível no arquivo `algoritmo_genetico_mochila.py`, que contém a implementação do algoritmo, funções de avaliação, mutação, crossover e controle da penalização de soluções inválidas.