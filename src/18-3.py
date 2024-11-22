def findCircleNum(self, M: List[List[int]]) -> int:
    def dfs(i, j):
        if M[i][j] == -1:  # 방문했다면
            return
        M[i][j] = -1
        for dir in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            next_i = i + dir[0]
            next_j = j + dir[1]
            if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n or M[next_i][next_j] != 1:
                continue
            dfs(next_i, next_j)

    m, n = len(M), len(M[0])
    cnt = 0
    for i in range(m):
        for j in range(n):
            if M[i][j] == 1:
                cnt += 1
                dfs(i, j)
    return cnt
