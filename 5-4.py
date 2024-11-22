import heapq
from typing import List


class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], K: int
    ) -> float:
        wq = sorted([(a / b, b) for (a, b) in zip(wage, quality)])
        res = float("inf")
        heap = []
        qSum = 0

        for avg, q in wq:
            qSum += q
            # 기본 우선순위 큐는 최소값 우선순위 큐이다.
            # 큐에서 제거되는 용역이 최소가 될 수 있도록 q를 음수의 값으로 바꾼다.
            heapq.heappush(heap, -q)
            if len(heap) > K:
                qSum += heapq.heappop(heap)
            if len(heap) == K:
                res = min(res, avg * qSum)

        return res
