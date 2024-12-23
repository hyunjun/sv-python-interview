class Solution:
    def longestOnes(self, A: list[int], K: int) -> int:
        max_len = -1
        # 이중 포인트 정의
        left, right = 0, 0
        # 전환 수량(flip) 정의
        flip = 0
        for right, item in enumerate(A):
            if item == 0:
                flip += 1
            # 현재 0의 개수가 K를 초과하지 않는지 확인
            while flip > K:
                if A[left] == 0:
                    flip -= 1
                left += 1
            # 현재의 최대 길이 업데이트
            max_len = max(max_len, right - left + 1)
        return max_len
