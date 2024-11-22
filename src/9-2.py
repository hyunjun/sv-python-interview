class Solution:
    def preorderTraversal(self, root):  # 전위순회
        stack = []
        sol = []
        curr = root
        while stack or curr:
            if curr:
                sol.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()
        return sol
