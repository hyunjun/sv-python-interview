from treenode import TreeNode


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if root is None:
            return None

        # p/q의 노드를 찾고 현재 노드를 반환한다.
        if root is p or root is q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 왼쪽 및 오른쪽 하위 트리에서 반환된 노드가 비어 있지 않으면 현재 노드를 반환한다.
        if left and right:
            return root
        elif left:
            return left
        else:
            return right
