class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # 길이가 n+1인 목록을 정의한다.
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1
        for i in range(2, n + 1, 1):
            # 현재 위치의 이전 번호를 가져온다.
            first = int(s[i - 1: i])
            second = int(s[i - 2: i])
            if first >= 1 and first <= 9:
                dp[i] += dp[i - 1]
            if second >= 10 and second <= 26:
                dp[i] += dp[i - 2]
        return dp[n]
