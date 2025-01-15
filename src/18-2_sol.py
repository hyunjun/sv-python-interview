from collections import deque


class Solution:
    def findCircleNum(self, M: list[list[int]]) -> int:
        n = len(M)
        visited = [False] * n
        count = 0

        # BFS로 연결된 노드들 탐색
        for i in range(n):
            if not visited[i]:  # 아직 방문하지 않았다면 새로운 친구원을 발견한 것
                count += 1
                queue = deque([i])  # 큐 초기화, 시작 노드를 넣음
                visited[i] = True
                while queue:
                    curr = queue.popleft()  # 큐에서 하나씩 꺼냄
                    for j in range(n):
                        if M[curr][j] == 1 and not visited[j]:
                            visited[j] = True
                            queue.append(j)  # 연결된 노드를 큐에 추가
        return count
