# Union Find
class Solution:
    def findCircleNum (self, M: list[list[int]]) -> int:
        m, n = len(M), len(M[0])
        roots = [-1]*m*n
        total_cnt = 0
        for x in range(m):
            for y in range(n):
                if M[x][y] == 1:
                    total_cnt += 1

        def find_roots(x, y):
            idx = x*n+y
            while roots[idx] != -1:
                idx = roots[idx]
            return idx

        for x in range(m):
            for y in range(n):
                if M[x][y] == 1:
                    # 이웃 노드를 확인한다.
                    for dirx, diry in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        nextx = x+dirx
                        nexty = y+diry
                        if nextx < 0 or nextx >= m or nexty < 0 or nexty >= n or M[nextx][nexty] != 1:
                            continue
                        curr_root = find_roots(x, y)
                        next_root = find_roots(nextx, nexty)
                        if curr_root != next_root:
                            roots[next_root] = curr_root
                            total_cnt -= 1
        return total_cnt
