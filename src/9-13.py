int maximum_depth(TreeNode * root) {
    if (!root) {
        return 0
        # 빈 노드의 경우 0을 반환한다.
    }
    int left_depth = maximum_depth(root -> left)
    int right_depth = maximum_depth(root -> right)
    return max(left_depth, right_depth) + 1
    # 루트 노드의 하위 트리의 깊이를 반환한다.
}
