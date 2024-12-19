class Solution:
    def preorderTraversal(self, root):  # 전위 순회
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) \
    + self.preorderTraversal(root.right)
