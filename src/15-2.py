class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        sum = 0
        for num in nums:
            sum += num
        first = self.dfs(nums, 0, len(nums) - 1)
        second = sum - first
        return first >= second

    def dfs(self, nums: list[int], s: int, e: int) -> int:
        if s > e:
            return 0
        start = nums[s] + min(self.dfs(nums, s + 1, e - 1), self.dfs(nums, s + 2, e))
        end = nums[e] + min(self.dfs(nums, s + 1, e - 1), self.dfs(nums, s, e - 2))
        return max(start, end)
