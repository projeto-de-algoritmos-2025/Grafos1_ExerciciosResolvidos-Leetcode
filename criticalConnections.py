 from collections import defaultdict

class Solution:
    def criticalConnections(self, n, conexoes):
        grafo = defaultdict(list)
        for u, v in conexoes:
            grafo[u].append(v)
            grafo[v].append(u)

        descoberta = [-1] * n
        baixo = [-1] * n
        tempo = [0]
        resposta = []

        def dfs(no, pai):
            descoberta[no] = baixo[no] = tempo[0]
            tempo[0] += 1

            for vizinho in grafo[no]:
                if vizinho == pai:
                    continue
                if descoberta[vizinho] == -1:
                    dfs(vizinho, no)
                    baixo[no] = min(baixo[no], baixo[vizinho])
                    if baixo[vizinho] > descoberta[no]:
                        resposta.append([no, vizinho])
                else:
                    baixo[no] = min(baixo[no], descoberta[vizinho])

        dfs(0, -1)
        return resposta
