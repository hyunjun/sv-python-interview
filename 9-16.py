class Solution:
    def maxPathSum(self, root: "TreeNode") -> int:
        best_sum = -float("inf")  # 최대경로합 기록 변수

        def maxPath(v: "vertex"):  # 보조 함수 정의
            nonlocal best_sum  # 최대 경로 합을 추적하는 변수
            if v is None:  # 노드가 None인 경우
                return 0

            L = maxPath(v.left)  # 왼쪽 자식에 대해 재귀
            R = maxPath(v.right)  # 오른쪽 자식에 대해 재귀

            # 하위 트리 합계로 최대 경로합을 업데이트한다.
            best_sum = max(best_sum, v.val + L + R)

            # 자식 트리 중 더 큰 경로합을 반환한다.
            return max(0, v.val + L, v.val + R)

        maxPath(root)
        return best_sum
