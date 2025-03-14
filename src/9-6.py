from treenode import TreeNode


class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        curr = root
        stack = []
        s = []

        while True:
            if curr is not None:
                s.append(curr.val)  # 출력값에 부모 노드값을 가장 먼저 넣는다.
                # 스택에 현잿값을 넣어, 아래의 elif 문에서 왼쪽 노드를 탐색하게끔 한다.
                stack.append(curr)
                curr = curr.right  # 오른쪽으로 일단 현잿값으로 지정하고 다시 루프문으로 들어간다.
            elif stack:  # 현잿값이 없고, Stack에는 값이 있다면,
                curr = stack.pop(-1)  # stack.pop()과 동일하게 작동하며 현잿값은 다시 현재 노드
                curr = curr.left  # 왼쪽 자식 노드로 이동한다.
            else:  # 현재 노드 또는 스택에 노드가 없다면 정지한다.
                break

        return s[::-1]  # 마지막에 뒤집어 출력한다.
