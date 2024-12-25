class Solution:
    def findCircleNum(self, M: list[list[int]]) -> int:
        def bfs(i, j):
            q = deque()
            q.append((i, j))
            M[i][j] = -1  # 방문한 것으로 표시
            while q:
                currx, curry = q.popleft()
                for dirx, diry in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    nextx = currx + dirx
                    nexty = curry + diry
                    if nextx < 0 or nextx >= m or nexty < 0 \
                        or nexty >= n or M[nextx][nexty] != 1:
                        continue
                    M[nextx][nexty] = -1  # 방문한 것으로 표시
                    q.append((nextx, nexty))

        m, n = len(M), len(M[0])
        cnt = 0
        for i in range(m):
            for j in range(n):
                if M[i][j] == 1:
                    cnt += 1
                    bfs(i, j)
        return cnt
