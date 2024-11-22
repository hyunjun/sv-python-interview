class Solution:
    def subarraySum(self, nums: List[int], K: int) -> int:
        if K < 0:
            return 0
        j, sum, ans = 0, 0, 0
        for i, num in enumerate(nums):
            sum += num  # 오른쪽 포인터를 이동
            while sum > K:  # 현재 합계가 K보다 큰 경우 왼쪽 포인터를 계속 이동한다.
                sum -= nums[j]
                j += 1
            if sum == K:
                ans += 1  # 배열의 합이 K와 같으면 결과에 1을 더한다.
        return ans
