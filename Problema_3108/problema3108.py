from collections import defaultdict

class Solution(object):
    def minimumCost(self, n, edges, query):
        """
        :type n: int
        :type edges: List[List[int]]
        :type query: List[List[int]]
        :rtype: List[int]
        """

        class DSU(object):
            def __init__(self, n):
                self.parent = list(range(n))
            
            def find(self, u):
                if self.parent[u] != u:
                    self.parent[u] = self.find(self.parent[u])
                return self.parent[u]
            
            def union(self, u, v):
                pu, pv = self.find(u), self.find(v)
                if pu != pv:
                    self.parent[pu] = pv

        # Inicializa a estrutura de união-find
        dsu = DSU(n)

        # Agrupa os vértices conectados
        for u, v, w in edges:
            dsu.union(u, v)

        # Identifica os componentes conectados
        components = defaultdict(list)
        for i in range(n):
            root = dsu.find(i)
            components[root].append(i)

        # Armazena a quantidade de arestas e o menor peso por componente
        comp_edge_count = defaultdict(int)
        comp_min_weight = {}

        for u, v, w in edges:
            root = dsu.find(u)
            comp_edge_count[root] += 1
            if root in comp_min_weight:
                comp_min_weight[root] = min(comp_min_weight[root], w)
            else:
                comp_min_weight[root] = w

        # Processa as queries
        result = []
        for u, v in query:
            if dsu.find(u) != dsu.find(v):
                result.append(-1)
                continue

            root = dsu.find(u)

            # Caso o componente tenha só um nó
            if len(components[root]) == 1:
                result.append(0 if u == v else -1)
            else:
                if comp_edge_count[root] >= len(components[root]):
                    result.append(0)
                else:
                    result.append(comp_min_weight[root])

        return result