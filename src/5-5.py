import heapq


class Solution:
    def isPossible(self, nums: list[int]) -> bool:
        heaps = {}
        # 우선순위 큐의 원소를 미리 정의
        for n in range(nums[0] - 1, nums[-1] + 1):
            heaps[n] = []

        for n in nums:
            if heaps[n - 1]:
                # 현재 값보다 1이 작은 우선순위 큐를 pop하고 동시에 길이 1을 추가한다.
                length = heapq.heappop(heaps[n - 1]) + 1
            else:
                length = 1
            # 현재 값에 해당하는 값과 길이를 우선순위 큐에 삽입한다.
            heapq.heappush(heaps[n], length)

        for n in nums:
            if heaps[n] and heaps[n][0] < 3:
                return False
        return True
