class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        left = 0
        right = x
        value = -1
        while left <= right:
            mid = (left + right) // 2
            if mid * mid > x:
                value = mid
                right = mid - 1
            else:
                left = mid + 1
        if value * value > x:
            return value - 1
        return value
