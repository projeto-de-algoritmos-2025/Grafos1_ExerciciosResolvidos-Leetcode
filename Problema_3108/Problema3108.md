# [3108. Minimum Cost Walk in Weighted Graph](https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/description/)

Existe um grafo não direcionado ponderado com **n** vértices rotulados de **0** a **n - 1**.

Você recebe um inteiro **n** e um array **edges**, onde **edges[i] = [ui, vi, wi]** indica que há uma aresta entre os vértices **ui** e **vi** com peso **wi**.

Um passeio em um grafo é uma sequência de vértices e arestas. O passeio começa e termina em um vértice, e cada aresta conecta o vértice que vem antes dela ao vértice que vem depois. É importante destacar que um passeio pode visitar a mesma aresta ou vértice múltiplas vezes.

O custo de um passeio que começa no nó **u** e termina no nó **v** é definido como o **AND** bit a bit dos pesos das arestas percorridas durante o passeio. Em outras palavras, se a sequência de pesos das arestas encontradas durante o passeio for **w0, w1, w2, ..., wk**, então o custo é calculado como **w0 & w1 & w2 & ... & wk**, onde **&** denota o operador **AND** bit a bit.

Você também recebe um array 2D **query**, onde **query[i] = [si, ti]**. Para cada consulta, você deve encontrar o menor custo de um passeio que começa no vértice **si** e termina no vértice **ti**. Se não existir tal passeio, a resposta é **-1**.

Retorne o array **answer**, onde **answer[i]** representa o **menor** custo do passeio para a **i-ésima** consulta.

## Exemplo 1:
**Entrada:  
n = 5; <br>
edges = [[0,1,7],[1,3,7],[1,2,1]]; <br>
query = [[0,3],[3,4]]**

**Saída: [1,-1]**

#### Explicação:
![Grafo exemplo 1](https://github.com/projeto-de-algoritmos-2025/Grafos1_ExerciciosResolvidos-Leetcode/blob/main/Problema_3108/img/explicacao1.png)<br>
*Grafo exemplo 1* <br>
Para obter o custo **1** na primeira consulta **(0 → 3)**, podemos seguir o caminho:
**0 → 1** (peso 7), **1 → 2** (peso 1), **2 → 1** (peso 1), **1 → 3** (peso 7).
O cálculo do custo é: **7 & 1 & 1 & 7 = 1**.

Na segunda consulta (**3 → 4**), não existe nenhum passeio possível entre os nós 3 e 4, então a resposta é **-1**.

## Exemplo 2:

**Entrada: 
n = 3; <br>
edges = [[0,2,7],[0,1,15],[1,2,6],[1,2,1]]; <br>
query = [[1,2]]**

**Saída: [0]**

#### Explicação: 
![Grafo exemplo 2](https://github.com/projeto-de-algoritmos-2025/Grafos1_ExerciciosResolvidos-Leetcode/blob/main/Problema_3108/img/explicacao2.png)<br>
*Grafo exemplo 2* <br>
Para obter o custo 0 na consulta **(1 → 2)**, podemos seguir o caminho:
**1 → 2** (peso 1), **2 → 1** (peso 6), **1 → 2** (peso 1).

## Restrições:
- 2 <= n <= 10^5
- 0 <= edges.length <= 105
- edges[i].length == 3
- 0 <= ui, vi <= n - 1
- ui != vi
- 0 <= wi <= 10^5
- 1 <= query.length <= 10^5
- query[i].length == 2
- 0 <= si, ti <= n - 1
- si != ti


# Solução
![Problema 3108](https://github.com/projeto-de-algoritmos-2025/Grafos1_ExerciciosResolvidos-Leetcode/blob/main/Problema_3108/img/MinCost.png) <br>
*Problema 3108 aceitação*

[Solução](https://github.com/projeto-de-algoritmos-2025/Grafos1_ExerciciosResolvidos-Leetcode/blob/main/Problema_3108/problema3108.py)