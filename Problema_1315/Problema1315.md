# [1315. Sum of Nodes with Even-Valued Grandparent](https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/description/)

Dada a **raiz** de uma árvore binária, retorne a soma dos valores dos nós que possuem um **avô de valor par**. Se não existirem nós com **avô de valor par**, retorne **0**.

Um **avô** de um nó é o pai do seu pai (se existir).

## Exemplo 1:
![Grafo exemplo 1](https://github.com/projeto-de-algoritmos-2025/Grafos1_ExerciciosResolvidos-Leetcode/blob/main/Problema_1315/img/exemplo1.png)<br>
*Grafo exemplo 1* <br>
**Entrada: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]**
**Saída: 18**

#### Explicação:
Os nós vermelhos são os nós com avô de valor par. Os nós azuis são os avós de valor par.

## Exemplo 2:
![Grafo exemplo 2](https://github.com/projeto-de-algoritmos-2025/Grafos1_ExerciciosResolvidos-Leetcode/blob/main/Problema_1315/img/exemplo2.png)<br>
*Grafo exemplo 2* <br>
**Entrada: root = [1]**
**Saída: 0**

## Restrições:
- O número de nós na árvore está no intervalo **[1, 10^4]**.
- **1 <= Node.val <= 100**.

# Solução
![Problema 1315](https://github.com/projeto-de-algoritmos-2025/Grafos1_ExerciciosResolvidos-Leetcode/blob/main/Problema_1315/img/SumNodes.png) <br>
*Problema 1315 aceitação*

[Solução](https://github.com/projeto-de-algoritmos-2025/Grafos1_ExerciciosResolvidos-Leetcode/blob/main/Problema_1315/problema1315.py)