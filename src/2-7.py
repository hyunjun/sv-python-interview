class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_ones = 0
        ones = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                ones += 1
            else:
                # 0으로 초기화한다.
                max_ones = max(max_ones, ones)
                ones = 0
        return max(max_ones, ones)
