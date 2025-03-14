from treenode import TreeNode


def maximum_depth(root: TreeNode) -> int:
    # 빈 노드의 경우 0을 반환한다.
    if not root:
        return 0
    left_depth = maximum_depth(root.left)
    right_depth = maximum_depth(root.right)
    # 루트 노드의 하위 트리의 깊이를 반환한다.
    return max(left_depth, right_depth) + 1

