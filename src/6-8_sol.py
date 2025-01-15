from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], K: int) -> int:
        table = defaultdict(int)
        res, presum = 0, 0
        table[0] = 1  # 누적 합이 K와 같은 부분 배열을 초기 상태부터 처리하기 위해 0을 추가

        for num in nums:
            presum += num  # 현재까지의 누적 합
            if presum - K in table:  # 현재 누적 합 - K가 딕셔너리에 있는 경우
                res += table[presum - K]  # 해당 경우의 개수를 결과에 추가
            table[presum] += 1  # 현재 누적 합을 딕셔너리에 업데이트

        return res
