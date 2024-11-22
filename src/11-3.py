class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        table = {}

        def dfs(node):
            if not node:  # 노드가 비어 있으면 반환
                return node
            elif node.val in table:  # 노드가 이미 해시테이블에 있으면 반환
                return table[node.val]
            else:
                ans = Node(node.val)  # 새 노드 만들기
                table[node.val] = ans  # 대응 관계를 구축하여 해시 테이블에 저장
                for n in node.neighbors:  # 현재 노드의 이웃을 탐색한다.
                    ans.neighbors.append(dfs(n))
                return ans

        return dfs(node)
