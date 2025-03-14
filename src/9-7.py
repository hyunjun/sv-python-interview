from queue import Queue
from treenode import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        result = []
        if root is None:
            return []

        # Python 큐 사용
        q = Queue()
        # add the root
        q.put(root)

        while not q.empty():
            # 큐에 있는 노드 수를 탐색한다.
            temp = []
            for i in range(q.qsize()):
                # 첫 번째 값을 가져온다
                node = q.get()
                temp.append(node.val)
                if node.left is not None:
                    q.put(node.left)
                if node.right is not None:
                    q.put(node.right)
            result.append(temp)

        return result
