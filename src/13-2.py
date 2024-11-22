class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s += "@"
        # Counter를 정의한다.
        dict_t = collections.Counter(t)
        # T의 왼쪽 포인터, 오른쪽 포인터 및 figures를 정의한다.
        l, r, figures = 0, 0, len(dict_t.keys())
        res = [0, len(s) + 1]  # 길이 정의
        while r < len(s):
            if figures == 0:  # 이 조건시 충족시 T의 모든 문자열의 포함된 것이다.
                if r - l < res[1] - res[0]:  # 길이 업데이트
                    res = [l, r]
                if s[l] in dict_t:  # 왼쪽 포인터가 가리키는 문자가 사전에 있는 경우
                    dict_t[s[l]] += 1
                    # 해당 문자 수가 이미 0보다 큰 경우 새 문자가 추가되었음을 의미한다.
                    if dict_t[s[l]] > 0:
                        figures += 1
                l += 1  # 왼쪽 포인터 이동
            else:
                if s[r] in dict_t:  # 오른쪽 포인터가 가리키는 문자가 사전에 있는 경우
                    dict_t[s[r]] -= 1  # 숫자를 1씩 줄이다.
                    # 해당 문자의 개수가 0이면 현재 문자가 문자열에서 제거된다는 의미이다.
                    if dict_t[s[r]] == 0:
                        figures -= 1
                r += 1  # 오른쪽 포인터 이동
        # 결과 반환
        if res == [0, len(s) + 1]:
            return ""
        else:
            return s[res[0]: res[1]]
