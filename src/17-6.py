class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        size = len(graph)
        q = deque()
        visited = {}
        colors = [""] * size
        for i in range(size):
            if i in visited:
                continue
            visited[i] = True
            q.append(i)
            colors[i] = "red"
            while q:
                # 이번 라운드의 대기열에 있는 노드는 다음 노드와 다른 색상을 가져야 한다.
                for _ in range(len(q)):
                    curr_id = q.popleft()
                    curr_color = colors[curr_id]
                    for next_id in graph[curr_id]:
                        if next_id not in visited:
                            next_color = "green" if curr_color == "red" else "red"
                            q.append(next_id)
                            colors[next_id] = next_color
                            visited[next_id] = True
                        else:
                            if colors[next_id] == curr_color:
                                return False
        return True
