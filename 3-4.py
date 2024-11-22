from collections import deque


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stk = deque()
        for i, ch in enumerate(s):
            if ch == "(":
                stk.append(i)

            elif ch == ")":
                # 이전 것이 (이면 스택에서 꺼낸다.
                if stk and s[stk[-1]] == "(":
                    stk.pop()
                else:
                    stk.append(i)

        res = ""

        # 이제 스택에 남은 것은 중복된 괄호이므로 삭제해야 한다.
        for i in range(len(s)):
            if stk and i == stk[0]:  # 중복된 괄호가 있고 종류가 같다면
                stk.popleft()  # 가장 앞의 원소가 삭제된다.
            else:
                res += s[i]

        return res


if __name__ == "__main__":
    object = Solution()
    s1 = "lee(t(c)o)de)"
    print(
        "origin string {} --> final string {}".format(
            s1, object.minRemoveToMakeValid(s1)
        )
    )

    s2 = "a)b(c)d"
    print(
        "origin string {} --> final string {}".format(
            s2, object.minRemoveToMakeValid(s2)
        )
    )
