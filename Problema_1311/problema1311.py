from collections import deque, defaultdict

class Solution(object):
    def watchedVideosByFriends(self, videosAssistidos, amigos, id, nivel):
        """
        :type videosAssistidos: List[List[str]]
        :type amigos: List[List[int]]
        :type id: int
        :type nivel: int
        :rtype: List[str]
        """
        visitado = set()
        fila = deque()
        fila.append((id, 0))
        visitado.add(id)
        pessoasNivel = []

        while fila:
            pessoa, dist = fila.popleft()
            if dist == nivel:
                pessoasNivel.append(pessoa)
            elif dist < nivel:
                for amigo in amigos[pessoa]:
                    if amigo not in visitado:
                        visitado.add(amigo)
                        fila.append((amigo, dist + 1))

        frequencia = defaultdict(int)
        for pessoa in pessoasNivel:
            for video in videosAssistidos[pessoa]:
                frequencia[video] += 1

        resultado = sorted(frequencia.items(), key=lambda x: (x[1], x[0]))
        return [video for video, _ in resultado]

