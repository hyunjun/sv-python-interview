class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        self.target = target

        for i in range(1, len(num) + 1):
            if i == 1 or (i > 1 and num[0] != "0"):
                self.dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res)
        return res

    def dfs(self, num, fstr, fval, flast, res):
        # fstr은 현재 표현식이다.
        # fval은 현재 표현식의 값이다.
        # flast는 마지막으로 연산된 숫자 또는 피연산자의 값이다.
        # 예를 들어, fstr=2+3이면 flast=3이고, fstr=2-3이면 flast=-3이고, fstr=2+3*4이면 flast=3*4=12이다

        if not num:
            if fval == self.target:
                res.append(fstr)
            return

        for i in range(1, len(num) + 1):
            val = num[:i]
            if i == 1 or (i > 1 and num[0] != "0"):
                self.dfs(num[i:], fstr + "+" + val,
                         fval + int(val), int(val), res)
                self.dfs(num[i:], fstr + "-" + val,
                         fval - int(val), -int(val), res)
                self.dfs(num[i:], fstr + '*' + val, fval-flast +
                         flast*int(val), flast*int(val), res)
