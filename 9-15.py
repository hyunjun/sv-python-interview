class Codec:
    def dfs(self, s):
        first = s.pop(0)
        if first == "#":
            return None
        root = TreeNode(int(first))
        root.left = self.dfs(s)
        root.right = self.dfs(s)
        return root

    def serialize(self, root):
        if root is None:
            return "#,"
        return (
            str(root.val) + "," + self.serialize(root.left) +
            self.serialize(root.right)
        )

    def deserialize(self, data):
        s = data.split(",")
        root = self.dfs(s)
        return root
