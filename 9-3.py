class Solution:
    def inorderTraversal(self, root):
        if not root:
            return []
        return
        self.inorderTraversal(root.left)
        + [root.val]
        + self.inorderTraversal(root.right)
