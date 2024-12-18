from collections import deque


class Solution:
    def shortestSubarray(self, A: list[int], K: int) -> int:
        q = deque()
        q.append((-1, 0))  # 1단계
        min_size = float("inf")
        cumsum = 0

        for j in range(len(A)):
            # 큐의 앞부터 스캔
            cumsum = cumsum + A[j]
            while q and cumsum - q[0][1] >= K:
                min_size = min(min_size, j - q[0][0])
                q.popleft()

            # 해당 누적합을 유지하면서 현재 누적을 삽입한다.
            # 뒤쪽이 더 큰 원소여야 하고 q는 오름차순이 되어야 한다.
            while q and q[-1][1] >= cumsum:  # 예시의 3단계 부분
                q.pop()  # 가장 마지막에 있는 수가 cumsum보다 크면 가장 뒤 숫자를 뺀다.
            q.append((j, cumsum))

        return -1 if min_size == float("inf") else min_size


if __name__ == "__main__":
    object = Solution()
    result = object.shortestSubarray([84, -37, 32, 40, 95], 167)
    assert result == 3
    result = object.shortestSubarray([2, -1, 2], 3)
    assert result == 3
    result = object.shortestSubarray([1, 2], 4)
    assert result == -1
    print("pass all shortestSubarray tests")
