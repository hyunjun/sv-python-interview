class Solution:


def subarraySum(self, nums: List[int], K: int) -> int:
    table = defaultdict(int)
    res, presume = 0, 0
    table[0] = 1
    for i, num in enumerate(nums):
        presum += num
        if presum-K in table:  # 현재 추정-K가 딕셔너리에 있는 경우
            res += table[presum-K]
            # 현재까지의 합산 수를 업데이트한다.
            table[presum] += 1
    return res
