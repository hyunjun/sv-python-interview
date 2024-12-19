class Solution:
    def inorderTraversal(self, root):
        stack = []
        sol = []
        curr = root
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                sol.append(curr.val)
                curr = curr.right
        return sol
