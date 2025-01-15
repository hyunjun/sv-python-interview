class Solution:
    def findCircleNum(self, M: list[list[int]]) -> int:
        n = len(M)
        visited = [False] * n
        count = 0

        # Stack을 사용한 DFS 탐색
        for i in range(n):
            if not visited[i]:  # 아직 방문하지 않았다면 새로운 프로빈스를 발견한 것
                count += 1
                stack = [i]  # 스택 초기화, 시작 노드를 넣음
                visited[i] = True
                while stack:
                    curr = stack.pop()  # 스택에서 하나씩 꺼냄
                    for j in range(n):
                        if M[curr][j] == 1 and not visited[j]:
                            visited[j] = True
                            stack.append(j)  # 연결된 노드를 스택에 추가
        return count
