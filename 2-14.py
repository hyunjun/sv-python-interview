class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False
        ls = s.split("e")
        if len(ls) == 1:  # e가 없으면 모든 문자열을 판단한다.
            return self.decide_num(ls[0])
        elif len(ls) == 2:  # e가 있으면, 두 부분으로 나누어서 판단한다.
            return self.decide_num(ls[0]) and self.decide_pow(ls[1])
        else:
            return False

    def decide_num(self, s):
        if not s:
            return False
        if s[0] in ["+", "-"]:
            s = s[1:]
        ls = s.split(".")
        if len(ls) == 1:  # 소수점이 없으면 그대로 숫자인지 판단한다.
            return ls[0].isnumeric()
        elif len(ls) == 2:  # 소수점이 있다면, 소수점 앞뒤로 판단한다.
            if not ls[0] and ls[1].isnumeric():  # 소수점 앞이 공백인 경우
                return True
            elif not ls[1] and ls[0].isnumeric():  # 소수점 뒤가 공백인 경우
                return True
            else:
                return (
                    ls[0].isnumeric() and ls[1].isnumeric()
                )  # 소수점 앞, 뒤 모두 유효한 숫자라면 반환

    def decide_pow(self, s):  # 거듭제곱 부분은 “부호 + 숫자”형태만 가능, 소수점은 사용 불가
        if not s:
            return False
        if s[0] in ["+", "-"]:
            s = s[1:]
        return s.isnumeric()
