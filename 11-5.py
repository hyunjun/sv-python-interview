class Solution(object):
    def validTree(self, n, edges):
        if len(edges) != n - 1:  # Check number of edges.
            return False

        # 인접 리스트 초기화
        neighbors = collections.defaultdict(list)
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)

        # BFS를 사용하여 유효한 트리인지 확인한다.
        visited = {}
        q = collections.deque([0])
        while q:
            curr = q.popleft()
            for node in neighbors[curr]:
                if node not in visited:
                    visited[node] = True
                    q.append(node)
                else:
                    return False

        return len(visited) == n
