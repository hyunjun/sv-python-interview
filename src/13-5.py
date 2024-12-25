class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        # 두 개의 해시 테이블 정의
        p_counter = Counter(p)
        s_counter = Counter()

        # 최종 결과
        ans = []
        np = len(p)
        ns = len(s)
        # 슬라이딩 윈도우를 활용한다.
        left = 0
        for i in range(ns):  # 오른쪽 포인터 이동 반복문
            s_counter[s[i]] += 1
            # 문자열 길이가 대상 문자열 길이와 같은 경우
            if i - left + 1 == np:
                # 두 해시 테이블이 동일하면 시작 주소를 ans에 푸시한다.
                if s_counter == p_counter:
                    ans.append(left)
                # 현재 문자가 하나만 있는 경우 해당 문자를 Counter에서 삭제해야 한다.
                if s_counter[s[left]] == 1:
                    del s_counter[s[left]]
                else:
                    s_counter[s[left]] -= 1
                # 왼쪽 포인터 이동
                left += 1

        return ans
