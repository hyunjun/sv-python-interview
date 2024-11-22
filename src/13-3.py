class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) ->
    List[List[int]]:
        ans = []
        i = j = 0

        while i < len(A) and j < len(B):
            # A[i]가 B[j]와 교차하는지 확인
            # lo - 교차구간의 시작점
            # hi—교차구간 끝점
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            if lo <= hi:
                ans.append([lo, hi])

            # 끝점이 더 작은 구간의 배열의 다음 포인트로 이동한다..
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return ans
