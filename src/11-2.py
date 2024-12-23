from collections import defaultdict


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        if node is None:
            return None
        # 큐를 선언한다.
        q = deque()
        q.append(node)
        # 해시 테이블을 사용하여 원래 노드와 새 노드 간의 대응 관계를 나타낸다.
        vis = defaultdict()
        vis[node] = Node(node.val)

        while q:
            front = q.popleft()  # 첫번째 원소를 꺼낸다.
            for child in front.neighbors:
                # 현재 노드는 방문되지 않았다면
                if child not in vis:
                    vis[child] = Node(child.val)
                    q.append(child)
                vis[front].neighbors.append(vis[child])
        return vis[node]
