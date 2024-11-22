class Solution(object):
    def validTree(self, n, edges):
        lookup = collections.defaultdict(list)
        for edge in edges:  # 각 간선을 인접 리스트에 기록한다.
            lookup[edge[0]].append(edge[1])
            lookup[edge[1]].append(edge[0])
        visited = [False] * n  # 리스트의 모든 노드 방문 상태가 False로 설정한다.

        if not self.helper(0, -1, lookup, visited):
            return False

        for v in visited:  # 노드를 방문했는지 확인한다.
            if not v:
                return False

        return True

    def helper(self, curr, parent, lookup, visited):
        if visited[curr]:  # 노드를 방문한 경우 False를 반환한다.
            return False
        visited[curr] = True  # 현재 방문한 노드를 방문했음을 기록
        for i in lookup[curr]:  # 현재 노드의 다음 방문 노드를 확인한다
            if i != parent and not self.helper(i, curr, lookup, visited):
                return False

        return True
