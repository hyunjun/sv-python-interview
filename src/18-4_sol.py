class Solution:
    def findCircleNum(self, M: list[list[int]]) -> int:
        # 부모 노드 찾기
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # 경로 압축
            return parent[x]

        # 두 집합 합치기
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1

        n = len(M)
        parent = list(range(n))  # 각 원소는 자기 자신을 부모로 초기화
        rank = [0] * n  # 각 집합의 랭크 초기화

        # M[i][j]가 1이면 i와 j가 연결되어 있음을 의미하므로 union 연산
        for i in range(n):
            for j in range(i + 1, n):  # 대칭이므로 i, j 쌍만 한 번씩 확인
                if M[i][j] == 1:
                    union(i, j)

        # 서로 다른 부모 노드의 수가 곧 서로 다른 집합(친구원)의 수
        count = sum(1 for i in range(n) if find(i) == i)
        return count
