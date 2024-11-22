class Solution:
    def treeToDoublyList(self, root: "Node") -> "Node":
        if not root:
            return root

        res = []

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            res.append(node)
            inorder(node.right)

        inorder(root)

        for i in range(len(res) - 1):
            res[i].right = res[i + 1]
            res[i + 1].left = res[i]

        res[-1].right = res[0]
        res[0].left = res[-1]

        return res[0]
